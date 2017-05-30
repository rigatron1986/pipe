import os
import json
from xml.dom.minidom import Document, parse

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import pymel.core as pm


def writeAnim(objects=pm.selected(), filepath='C:/temp/anim.xml'):
    doc = Document()
    root = doc.createElement('Data')
    doc.appendChild(root)

    for obj in objects:
        obj_shotname = obj.name()
        obj_longname = obj.longName()

        xml_obj = doc.createElement('object')
        xml_obj.setAttribute('id', obj_longname)
        root.appendChild(xml_obj)

        channels = obj.listConnections(type='animCurve', connections=True, s=1, d=0)

        for i, channel in enumerate(channels):
            channel = channel[1]
            split_name = obj_shotname
            xml_channel_name = (channels[i][0].name().split(split_name + '.')[1])
            xml_channel = doc.createElement(xml_channel_name)
            xml_channel.setAttribute('type', 'keyed')
            xml_obj.appendChild(xml_channel)

            keys = pm.animation.keyframe(channel, q=True)
            values = pm.animation.keyframe(channel, q=True, valueChange=True)
            breakdown = pm.animation.keyframe(channel, q=True, breakdown=True)
            inTangentType = pm.animation.keyTangent(channel, q=True, inTangentType=True)
            outTangentType = pm.animation.keyTangent(channel, q=True, outTangentType=True)
            lock = pm.animation.keyTangent(channel, q=True, lock=True)
            weightLock = pm.animation.keyTangent(channel, q=True, weightLock=True)
            inAngle = pm.animation.keyTangent(channel, q=True, inAngle=True)
            outAngle = pm.animation.keyTangent(channel, q=True, outAngle=True)
            inWeight = pm.animation.keyTangent(channel, q=True, inWeight=True)
            outWeight = pm.animation.keyTangent(channel, q=True, outWeight=True)
            weightedTangents = pm.animation.keyTangent(channel, q=True, weightedTangents=True)[0]

            preIn = channel.preInfinity.get()
            postIn = channel.postInfinity.get()

            xml_infi = doc.createElement('infinity')
            xml_infi.setAttribute('preInfinity', json.dumps(preIn))
            xml_infi.setAttribute('postInfinity', json.dumps(postIn))
            xml_infi.setAttribute('weightedTangents', json.dumps(weightedTangents))
            xml_channel.appendChild(xml_infi)

            for i, key in enumerate(keys):
                xml_key = doc.createElement('key')
                xml_channel.appendChild(xml_key)

                bd = 0
                for bd_item in breakdown:
                    if bd_item == key:
                        bd = 1

                xml_key.setAttribute('key', json.dumps(keys[i]))
                xml_key.setAttribute('value', json.dumps(values[i]))
                xml_key.setAttribute('breakdown', json.dumps(bd))
                xml_key.setAttribute('inTangentType', json.dumps(inTangentType[i]))
                xml_key.setAttribute('outTangentType', json.dumps(outTangentType[i]))
                xml_key.setAttribute('lock', json.dumps(lock[i]))
                xml_key.setAttribute('weightLock', json.dumps(weightLock[i]))
                xml_key.setAttribute('inAngle', json.dumps(inAngle[i]))
                xml_key.setAttribute('outAngle', json.dumps(outAngle[i]))
                xml_key.setAttribute('inWeight', json.dumps(inWeight[i]))
                xml_key.setAttribute('outWeight', json.dumps(outWeight[i]))

        static_chans = pm.listAnimatable(obj)
        for static_chan in static_chans:
            testit = pm.keyframe(static_chan, q=True)
            connected = pm.listConnections(static_chan, destination=False, source=True)
            if testit or connected:
                continue

            try:
                xml_channel = doc.createElement(static_chan.name().split(obj_shotname + '.')[1])
            except IndexError:
                logger.warning('Could not export attribute {0}'.format(static_chan.name()))
                continue
            xml_channel.setAttribute('type', 'static')
            xml_channel.setAttribute('value', json.dumps(static_chan.get()))
            xml_obj.appendChild(xml_channel)

    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    with open(filepath, 'w') as f:
        f.write(doc.toprettyxml(indent='	', encoding='utf-8'))


def readAnim(filepath='C:/temp/anim.xml', objects=pm.selected()):
    if not os.path.exists(filepath):
        return [False, 'invalid filepath']
    doc = parse(filepath)
    for obj in objects:
        obj_shotname = obj.name()
        obj_longname = obj.longName()
        all_xml_objs = doc.getElementsByTagName('object')

        xml_obj = None
        for i in all_xml_objs:
            if i.getAttribute('id') == obj_longname:
                xml_obj = i
        if not xml_obj:
            logger.warning('Anim data not found for {0}'.format(obj_shotname))
            continue
        xml_channels = xml_obj.childNodes

        for xml_channel in xml_channels:
            if hasattr(xml_channel, 'getAttribute'):
                if xml_channel.getAttribute('type') == 'static':
                    value = json.loads(xml_channel.getAttribute('value'))
                    try:
                        cur_attr = eval('obj.' + xml_channel.tagName)
                    except AttributeError, e:
                        logger.warning('skipping for {0} as attribute was not found'.format(cur_attr))
                        continue
                    connected = pm.listConnections(cur_attr, destination=False, source=True);
                    if not connected and not cur_attr.isLocked():
                        cur_attr.set(value)
                elif xml_channel.getAttribute('type') == 'keyed':
                    xml_keys = []
                    for each in xml_channel.childNodes:
                        if hasattr(each, 'tagName'):
                            if each.tagName == 'key':
                                xml_keys.append(each)
                            elif each.tagName == 'infinity':
                                preI = json.loads(each.getAttribute('preInfinity'))
                                postI = json.loads(each.getAttribute('postInfinity'))
                                weightedTangents = json.loads(each.getAttribute('weightedTangents'))

                    try:
                        cur_attr = eval('obj.' + xml_channel.tagName)
                    except:
                        logger.warning(
                            'skipping for {0}.{1} as attribute was not found'.format(obj_shotname, xml_channel.tagName))
                        continue

                    for xml_key in xml_keys:

                        if not hasattr(xml_key, 'getAttribute'):
                            continue

                        time = json.loads(xml_key.getAttribute('key'))
                        value = json.loads(xml_key.getAttribute('value'))
                        breakdown = json.loads(xml_key.getAttribute('breakdown'))
                        tanLock = json.loads(xml_key.getAttribute('lock'))
                        weightLock = json.loads(xml_key.getAttribute('weightLock'))
                        inType = json.loads(xml_key.getAttribute('inTangentType'))
                        outType = json.loads(xml_key.getAttribute('outTangentType'))
                        tan1 = json.loads(xml_key.getAttribute('inAngle'))
                        tan2 = json.loads(xml_key.getAttribute('outAngle'))
                        weight1 = json.loads(xml_key.getAttribute('inWeight'))
                        weight2 = json.loads(xml_key.getAttribute('outWeight'))

                        cur_attr = eval('obj.' + xml_channel.tagName)
                        res = pm.setKeyframe(cur_attr, time=time, value=value, bd=breakdown)
                        if weightedTangents:
                            pm.keyTangent(cur_attr, weightedTangents=True, edit=True)
                        try:
                            pm.keyTangent(cur_attr, lock=tanLock, time=time)
                        except Exception, e:
                            logger.warning(e)

                        if weightedTangents:
                            pm.keyTangent(cur_attr, time=time, weightLock=weightLock)
                        if (inType != 'fixed' and outType != 'fixed'):
                            pm.keyTangent(cur_attr, e=1, a=1, time=time, itt=inType, ott=outType)
                        if (inType == 'fixed' and outType != 'fixed'):
                            pm.keyTangent(cur_attr, e=1, a=1, time=time, inAngle=tan1, inWeight=weight1, itt=inType,
                                          ott=outType)
                        if (inType == 'fixed' and outType == 'fixed'):
                            pm.keyTangent(cur_attr, e=1, a=1, time=time, inAngle=tan1, inWeight=weight1, outAngle=tan2,
                                          outWeight=weight2, itt=inType, ott=outType)

                        pm.setInfinity(cur_attr, poi=postI, pri=preI)


'''
import pymel.core as pm
import animexporter as animexporter
reload(animexporter)
animexporter.readAnim(filepath='C:/temp/anim.xml',objects=pm.selected())

animexporter.writeAnim(objects = pm.selected(),filepath='C:/temp/anim.xml')
'''
