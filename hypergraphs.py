# Hypergraphs in python
import hypernetx as hnx
import matplotlib.pyplot as plt

# Definir os nós e hiper-arestas do hiper-grafo
nodes = {'designConcept', 'excitation', 'icCode', 'ipCode', 'voltageRegulModel', 'cableInletPos', 'location',
         'sensorStatorAct', 'sensorBearingAct', 'spaceHeaterAct', 'voltageRegulModel', 'tboxStator/material',
         'sensorStatorAct', 'sensorStator', 'sensorBearing', 'sensorBearingAct', 'spaceHeater', 'spaceHeaterAct',
         'sensorBearing.class', 'sensorBearing.qty', 'sensorBearing.type', 'sensorStator.class', 'sensorStator.type'}

hyperedges = {'E0': {'sensorStatorAct', 'sensorBearingAct', 'spaceHeaterAct', 'voltageRegulModel', 'tboxStator/material'},
              'E1': {'designConcept', 'excitation', 'icCode', 'ipCode'}, 
              'E2': {'location', 'cableInletPos', 'voltageRegulModel'},
              'E3': {'sensorStatorAct', 'sensorStator'},
              'E4': {'sensorBearing', 'sensorBearingAct'},
              'E5': {'spaceHeater', 'spaceHeaterAct'},
              'E6': {'sensorBearing', 'sensorBearing.class', 'sensorBearing.qty'},
              'E7': {'sensorStator', 'sensorStator.qty', 'sensorStator.class'},
              'E8': {'sensorBearing.class', 'sensorBearing.type', 'sensorStator.class', 'sensorStator.type'}}

nodes = { '/sensorStator/class', '/spaceHeaterAct', '/excitation', '/frameSize', '/sensorBearing/type', '/tboxStator/cableInletPos', '/tboxStator/material', '/sensorBearingAct', '/icCode', '/tboxStator/voltageRegulModel', '/spaceHeater', '/sensorBearing', '/statorWound/packageStator/length', '/ipCode', '/tboxStator/location', '/sensorStator/type', '/imCode/disc', '/imCode/imCode', '/sensorBearing/class', '/imCode/flange', '/imCode', '/designConcept', '/statorWound/packageStator/codeLength', '/sensorStatorAct', '/sensorStator', }

edges_ORC6511 = { 'HE1': {'/sensorBearingAct', '/sensorStatorAct', '/spaceHeaterAct'}, 'HE2': {'/designConcept'}, 'HE3': {'/sensorBearing', '/sensorBearingAct'}, 'HE4': {'/tboxStator/material', '/tboxStator/voltageRegulModel'}, 'HE5': {'/sensorStator', '/sensorStatorAct'}, 'HE6': {'/tboxStator/voltageRegulModel'}, 'HE7': {'/frameSize', '/imCode', '/imCode/disc', '/imCode/flange', '/imCode/imCode'}, 'HE8': {'/sensorBearing/class', '/sensorBearing/type', '/sensorStator/class', '/sensorStator/type'}, 'HE9': {'/tboxStator/cableInletPos', '/tboxStator/location'}, 'HE10': {'/excitation', '/icCode', '/ipCode'}, 'HE11': {'/statorWound/packageStator/codeLength', '/statorWound/packageStator/length'}, 'HE12': {'/spaceHeater', '/spaceHeaterAct'}} 

nodes = { '/sensorStator/class', '/spaceHeaterAct', '/excitation', '/frameSize', '/sensorBearing/type', '/tboxStator/cableInletPos', '/tboxStator/material', '/sensorBearingAct', '/icCode', '/tboxStator/voltageRegulModel', '/spaceHeater', '/sensorBearing', '/statorWound/packageStator/length', '/ipCode', '/tboxStator/location', '/sensorStator/type', '/imCode/disc', '/imCode/imCode', '/sensorBearing/class', '/imCode/flange', '/imCode', '/designConcept', '/statorWound/packageStator/codeLength', '/sensorStatorAct', '/sensorStator', }

edges_ORC6511 = { 'HE1': {'/sensorBearingAct', '/sensorStatorAct', '/spaceHeaterAct'}, 'HE2': {'/designConcept'}, 'HE3': {'/sensorBearing', '/sensorBearingAct'}, 'HE4': {'/tboxStator/material', '/tboxStator/voltageRegulModel'}, 'HE5': {'/sensorStator', '/sensorStatorAct'}, 'HE6': {'/tboxStator/voltageRegulModel'}, 'HE7': {'/frameSize', '/imCode', '/imCode/disc', '/imCode/flange', '/imCode/imCode'}, 'HE8': {'/sensorBearing/class', '/sensorBearing/type', '/sensorStator/class', '/sensorStator/type'}, 'HE9': {'/tboxStator/cableInletPos', '/tboxStator/location'}, 'HE10': {'/excitation', '/icCode', '/ipCode'}, 'HE11': {'/statorWound/packageStator/codeLength', '/statorWound/packageStator/length'}, 'HE12': {'/spaceHeater', '/spaceHeaterAct'}} 

nodes = { '/motherboard/secCpu/0/model', '/motherboard/efficiency', '/motherboard/cpu/clockRate', '/motherboard/cpu/model', '/motherboard/secCpu/1/cache', '/operatingSystem/model', '/motherboard/secCpu/0/clockRate', '/motherboard/secCpu/1/clockRate', '/motherboard/secCpu/1/model', '/efficiency', '/motherboard/cpu/cache', '/motherboard/secCpu/0/cache', }
edges_PC_tbl = { 'HE1': {'/efficiency', '/motherboard/efficiency'}, 'HE2': {'/motherboard/cpu/clockRate', '/motherboard/secCpu/0/clockRate', '/motherboard/secCpu/1/clockRate'}, 'HE3': {'/motherboard/cpu/cache', '/motherboard/cpu/clockRate', '/motherboard/cpu/model', '/motherboard/secCpu/0/cache', '/motherboard/secCpu/0/clockRate', '/motherboard/secCpu/0/model', '/motherboard/secCpu/1/cache', '/motherboard/secCpu/1/clockRate', '/motherboard/secCpu/1/model'}, 'HE4': {'/motherboard/efficiency', '/motherboard/secCpu/0/clockRate'}, 'HE5': {'/motherboard/cpu/clockRate', '/motherboard/cpu/model', '/motherboard/secCpu/0/clockRate', '/motherboard/secCpu/0/model', '/motherboard/secCpu/1/clockRate', '/motherboard/secCpu/1/model'}, 'HE6': {'/motherboard/cpu/model', '/operatingSystem/model'}, 'HE7': {'/motherboard/cpu/cache', '/motherboard/cpu/model', '/motherboard/secCpu/0/cache', '/motherboard/secCpu/0/model', '/motherboard/secCpu/1/cache', '/motherboard/secCpu/1/model'}} 

nodes = { '/motherboard/secCpu/0/model', '/motherboard/efficiency', '/motherboard/cpu/clockRate', '/motherboard/cpu/model', '/operatingSystem/model', '/motherboard/secCpu/1/cache', '/motherboard/secCpu/0/clockRate', '/motherboard/secCpu/1/clockRate', '/motherboard/secCpu/1/model', '/efficiency', '/motherboard/cpu/cache', '/motherboard/secCpu/0/cache', }
edges_PC = { 'HE1': {'/motherboard/cpu/model', '/motherboard/secCpu/0/model', '/motherboard/secCpu/1/model'}, 'HE2': {'/efficiency', '/motherboard/efficiency'}, 'HE3': {'/motherboard/cpu/clockRate', '/motherboard/secCpu/0/clockRate', '/motherboard/secCpu/1/clockRate'}, 'HE4': {'/motherboard/efficiency', '/motherboard/secCpu/0/clockRate'}, 'HE5': {'/motherboard/cpu/clockRate', '/motherboard/cpu/model', '/motherboard/secCpu/0/clockRate', '/motherboard/secCpu/0/model', '/motherboard/secCpu/1/clockRate', '/motherboard/secCpu/1/model'}, 'HE6': {'/motherboard/cpu/model', '/operatingSystem/model'}, 'HE7': {'/motherboard/cpu/cache', '/motherboard/cpu/model', '/motherboard/secCpu/0/cache', '/motherboard/secCpu/0/model', '/motherboard/secCpu/1/cache', '/motherboard/secCpu/1/model'}} 

nodes = { '/workaround/enumerated/powerFactor', '/designed/endshBrngSetNend/endsh/ext/fitDiam', '/basicParameters/phaseNumber', '/accessories/thermosensorStator/sensorClass', '/accessories/thermosensorBrngSize', '/accessories/thermosensorBrng/qtyPerApplication', '/designed/endshBrngSetDend/endshProtLid', '/designed/platesAndLabels/ratingPlate/ratingPlateData/completeAct', '/painting/gloss', '/accessories/thermosensorBrng/sensorClass', '/workaround/enumerated/ratedPower', '/designed/endshBrngSetNend/brng/angularContact', '/designed/tboxStatorSet/tbox/rawMat', '/designed/endshBrngSetNend/thermosensor/thermosensor/wireConfiguration', '/designed/flywheelHousing/dim/extDiam', '/designed/avrSet/avr/certUkca', '/designed/endshBrngSetDend/thermosensor/thermosensor/sensorClass', '/designed/avrSet', '/commercial/productLine', '/designed/shaft/flywheel', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certUkca', '/designed/endshBrngSetNend/brng/type', '/commercial/transportAndBilling/currentType', '/designed/endshBrngSetDend/thermosensorAct', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certUl', '/commercial/locationCableInletNDE', '/accessories/thermosensorBrng/qty', '/designed/endshBrngSetDend/brng/lubricant', '/designed/endshBrngSetNend/brng/operatingTemp', '/designed/endshBrngSetNend/endshProtLid/fixHole/qty', '/designed/platesAndLabels/ratingPlate/ratingPlateData/language', '/designed/statorMainWound/packageStator/statorMainLamination/externalDiameter', '/designed/avrSetAct', '/commercial/transportAndBilling/productClass', '/designed/statorMainWound/winding/phaseNumber', '/commercial/regionOfOperation', '/designed/platesAndLabels/ratingPlate/ratingPlate/material', '/designed/endshBrngSetDend/brngQty', '/designed/avrSet/avr/certCe', '/designed/tboxStatorSetAct', '/designed/endshBrngSetNend/endsh/brng/diam', '/mounting/shaftendDend/type', '/designed/endshBrngSetDend/endshProtLid/fixHole/qty', '/workaround/numberTranslation/spaceHeaterPhase', '/basicParameters/noise/standard', '/designed/endshBrngSetNend/brng/shieldingOrSealing', '/designed/endshBrngSetNend/thermosensor/thermosensor/type', '/basicParameters/vibration/level', '/designed/endshDendAct', '/accessories/thermosensorStator/qty', '/designed/flywheelHousingSupport', '/designed/statorMainWound/packageStator/externalDiameter', '/designed/tboxStatorSet/designConcept', '/designed/shaft/rotorMain/diam', '/designed/thermosensorStator/thermosensor/type', '/designed/thermosensorStator/thermosensor/sensorClass', '/designed/endshBrngSetDend/brng/intDiam', '/certification/certUkca', '/mounting/feet', '/operationAndCondition/coupling', '/designed/frameSize', '/accessories/thermosensorStatorSize', '/designed/tboxStatorSet/frameSize', '/designed/painting/colorCode', '/designed/endshBrngSetNend/brngQty', '/designed/endshBrngSetDend/thermosensorSize', '/designed/endshBrngSetNend/brng/intDiam', '/designed/endshBrngSetNend/brng/series', '/designed/endshBrngSetDend/thermosensor', '/designed/endshBrngSetNend/endsh/protLid/fixHolePosDiam', '/designed/endshBrngSetDend/frameSize', '/designed/tboxStatorSet/tbox/accessoriesRailReady', '/designed/endshBrngSetNend/endshProtLid', '/designed/shaft/brngDend', '/accessories/thermosensorStator/wireConfiguration', '/designed/flywheelAndHousing_gap', '/designed/flywheelHousingSupport/stator/fitDiam', '/designed/endshBrngSetDend/thermosensor/qty', '/designed/shaft/rotorMain/length', '/workaround/enumerated/temperatureRiseInput', '/designed/endshBrngSetNend/thermosensor/thermosensor/sensorClass', '/designed/flywheelHousing/rearFix/fixHoleQty', '/designed/flywheel', '/designed/frameFoot/length', '/designed/endshBrngSetNend/designConcept', '/designed/endshBrngSetDend/brng/shieldingOrSealing', '/basicParameters/ratedVoltageInput', '/designed/endshBrngSetNend/brng/lubricant', '/designed/endshBrngSetDend/brng/intClearance', '/designed/platesAndLabels/ratingPlate/ratingPlateData/complete', '/designed/endshBrngSetNend/thermosensorAct', '/designed/painting/gloss', '/designed/endshBrngSetDend/side', '/ambient/atmosCorrosCat', '/designed/rotorMainWound/rotorPackage/length', '/designed/flywheelHousingAct', '/basicParameters/noise/grade', '/designed/rotorMainWound/polesNumber', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certCe', '/designed/endshBrngSetDend/brng/extDiam', '/designed/endshBrngSetDend/endsh/protLid/fixHoleQty', '/mounting/locationCableInlet', '/designed/flywheelAct', '/certification/areaType', '/designed/tboxStatorSet/tbox/standard', '/designed/thermosensorStatorSize', '/designed/shaft/brngDend/diam', '/designed/avrSet/installationLocal', '/designed/endshBrngSetDend/brng/type', '/designed/statorMainWound/packageStator/length', '/designed/spaceHeaterSet/connectionElectricVoltage', '/designed/platesAndLabels/ratingPlate/ratingPlateData/type', '/designed/endshBrngSetNend/frameSize', '/designed/spaceHeaterAct', '/basicParameters/codeIP', '/designed/rawMatFixingElements', '/operationAndCondition/overspeedTime', '/designed/frameFoot/width', '/designed/endshBrngSetDend/endshProtLid/fixHole/posDiam', '/basicParameters/ratedPower', '/designed/endshBrngSetDend/endsh/protLid/fixHolePosDiam', '/operationAndCondition/overspeedMax', '/basicParameters/rotationSpeedRated', '/mounting/brng/endshBrngQty', '/accessories/thermosensorBrngAct', '/designed/endshBrngSetNend/thermosensor', '/certification/classifiedArea', '/designed/endshBrngSetNend/thermosensor/thermosensor', '/designed/manualOperation/language', '/designed/endshBrngSetDend/endsh/brng/diam', '/painting/paintingPlan', '/designed/frameAct', '/designed/endshBrngSetNend/endsh/protLid/fixHoleQty', '/designed/spaceHeaterSet', '/designed/manualOperation', '/designed/flywheelHousingSupport/dim/fixHolePosDiam', '/designed/endshBrngSetNend/brng/intClearance', '/designed/shaft/brngNend/diam', '/designed/designConcept', '/workaround/enumerated/overspeedTime', '/designed/endshBrngSetDend/brng/operatingTemp', '/designed/endshBrngSetDend/thermosensor/thermosensor/wireConfiguration', '/designed/tboxStatorSet', '/basicParameters/frameSize', '/certification/certTuv', '/commercial/applicationCode', '/designed/endshBrngSetNend/endshProtLid/fixHole/posDiam', '/designed/statorMainWound/packageStator/statorMainLamination/frameSupport', '/certification/certUl', '/mounting/flangeAct', '/designed/endshBrngSetDend/thermosensor/thermosensor/type', '/operationAndCondition/pulleysAndBelts', '/designed/flywheelHousingSupport/dim/fixHoleQty', '/designed/endshBrngSetNend/brngType', '/designed/frame', '/designed/statorMainWound/packageStator/fixType', '/accessories/thermosensorBrng/wireConfiguration', '/designed/fanDend/hub/intDiam', '/basicParameters/ratedPowerInput', '/painting/colorCode', '/certification/certCe', '/designed/endshBrngSetDend/brngType', '/basicParameters/standard', '/designed/shaft/fanIntDend/diam', '/basicParameters/temperatureRiseInput', '/designed/flywheelHousing/rearFix/fixHolePosDiam', '/designed/platesAndLabels/material', '/designed/flywheelHousing/rearFix/fitDiam', '/designed/endshBrngSetDend/brng/series', '/accessories/thermosensorBrng/type', '/designed/rotorMainWound/winding/phaseNumber', '/designed/avrSet/avr/certUl', '/designed/frameFoot', '/designed/endshBrngSetNend/thermosensorSize', '/accessories/thermosensorStatorAct', '/basicParameters/ratedFrequencyInput', '/designed/endshBrngSetNend/thermosensor/qty', '/designed/endshBrngSetDend/brng/angularContact', '/workaround/enumerated/spaceHeaterConnectionVoltage', '/designed/rotorMainWound/rotorPackage/internalDiameter', '/designed/avrSet/avr/model', '/designed/platesAndLabels/language', '/accessories/thermosensorStator', '/designed/thermosensorStatorAct', '/workaround/enumerated/ratedPowerInput', '/designed/endshBrngSetNend/side', '/designed/endshBrngSetDend/designConcept', '/basicParameters/vibration/standard', '/accessories/thermosensorBrng', '/operationAndCondition/powerFactor', '/designed/flywheelHousingSupport/dim/fitDiam', '/workaround/enumerated/overspeed', '/mounting/locationTbox', '/designed/thermosensorStator/thermosensor/wireConfiguration', '/designed/frameFootAct', '/designed/endshBrngSetNend/brng/extDiam', '/designed/thermosensorStator', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certTuv', '/accessories/thermosensorStator/qtyPerApplication', '/mounting/feetAct', '/designed/manualOperationAct', '/mounting/flange', '/designed/flywheelHousing', '/operationAndCondition/overspeed', '/designed/endshBrngSetDend', '/commercial/transportAndBilling/rotorType', '/designed/flywheel/ext/diam', '/accessories/thermosensorStator/type', }

edges_WENnovo = { 'HE1': {'/designed/endshBrngSetDend/thermosensor', '/designed/tboxStatorSet/tbox/accessoriesRailReady'}, 'HE2': {'/operationAndCondition/overspeed', '/operationAndCondition/overspeedMax'}, 'HE3': {'/accessories/thermosensorBrng/sensorClass', '/designed/endshBrngSetDend/thermosensor/thermosensor/sensorClass'}, 'HE4': {'/designed/flywheel', '/designed/flywheelAct'}, 'HE5': {'/designed/rotorMainWound/rotorPackage/length', '/designed/shaft/rotorMain/length'}, 'HE6': {'/designed/designConcept', '/designed/endshBrngSetNend/designConcept'}, 'HE7': {'/designed/endshBrngSetDend/brng/extDiam', '/designed/endshBrngSetDend/endsh/brng/diam', '/designed/endshBrngSetNend/brng/extDiam', '/designed/endshBrngSetNend/endsh/brng/diam'}, 'HE8': {'/basicParameters/ratedPower', '/workaround/enumerated/ratedPower'}, 'HE9': {'/designed/spaceHeaterSet', '/workaround/numberTranslation/spaceHeaterPhase'}, 'HE10': {'/basicParameters/ratedPowerInput', '/workaround/enumerated/ratedPowerInput'}, 'HE11': {'/designed/statorMainWound/packageStator/externalDiameter', '/designed/statorMainWound/packageStator/statorMainLamination/externalDiameter'}, 'HE12': {'/accessories/thermosensorStator', '/designed/thermosensorStator'}, 'HE13': {'/designed/rotorMainWound/rotorPackage/internalDiameter', '/designed/shaft/rotorMain/diam'}, 'HE14': {'/accessories/thermosensorBrng', '/designed/endshBrngSetNend/thermosensor/thermosensor'}, 'HE15': {'/designed/manualOperation', '/designed/manualOperationAct'}, 'HE16': {'/designed/thermosensorStator', '/designed/thermosensorStatorSize'}, 'HE17': {'/designed/rotorMainWound/rotorPackage/length', '/designed/statorMainWound/packageStator/length'}, 'HE18': {'/designed/frameFoot/length', '/designed/frameFoot/width'}, 'HE19': {'/basicParameters/temperatureRiseInput', '/workaround/enumerated/temperatureRiseInput'}, 'HE20': {'/designed/tboxStatorSet', '/designed/tboxStatorSetAct'}, 'HE21': {'/designed/endshBrngSetDend', '/designed/shaft/brngDend'}, 'HE22': {'/designed/endshBrngSetDend/brng/intClearance', '/designed/endshBrngSetDend/brng/lubricant', '/designed/endshBrngSetDend/brng/series', '/designed/endshBrngSetDend/brng/shieldingOrSealing', '/designed/endshBrngSetDend/brngType', '/designed/endshBrngSetNend/brng/intClearance', '/designed/endshBrngSetNend/brng/lubricant', '/designed/endshBrngSetNend/brng/series', '/designed/endshBrngSetNend/brng/shieldingOrSealing', '/designed/endshBrngSetNend/brngType'}, 'HE23': {'/designed/manualOperation'}, 'HE24': {'/basicParameters/noise/standard'}, 'HE25': {'/ambient/atmosCorrosCat', '/basicParameters/codeIP'}, 'HE26': {'/designed/endshBrngSetDend/brng/angularContact', '/designed/endshBrngSetDend/brng/type', '/designed/endshBrngSetNend/brng/angularContact', '/designed/endshBrngSetNend/brng/type'}, 'HE27': {'/certification/areaType', '/certification/classifiedArea'}, 'HE28': {'/designed/spaceHeaterAct', '/designed/spaceHeaterSet'}, 'HE29': {'/designed/endshBrngSetDend/endsh/protLid/fixHolePosDiam', '/designed/endshBrngSetDend/endshProtLid/fixHole/posDiam', '/designed/endshBrngSetNend/endsh/protLid/fixHolePosDiam', '/designed/endshBrngSetNend/endshProtLid/fixHole/posDiam'}, 'HE30': {'/mounting/feet', '/mounting/feetAct'}, 'HE31': {'/designed/designConcept', '/mounting/locationTbox'}, 'HE32': {'/designed/flywheelHousingSupport/stator/fitDiam', '/designed/statorMainWound/packageStator/externalDiameter'}, 'HE33': {'/certification/certCe', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certCe'}, 'HE34': {'/accessories/thermosensorBrng/type', '/accessories/thermosensorStator/type'}, 'HE35': {'/designed/tboxStatorSet', '/mounting/locationCableInlet'}, 'HE36': {'/designed/spaceHeaterSet', '/designed/tboxStatorSet/tbox/accessoriesRailReady'}, 'HE37': {'/designed/endshBrngSetDend/designConcept', '/designed/endshBrngSetDend/frameSize', '/designed/endshBrngSetDend/side', '/designed/endshBrngSetNend/designConcept', '/designed/endshBrngSetNend/frameSize', '/designed/endshBrngSetNend/side'}, 'HE38': {'/accessories/thermosensorBrng/qtyPerApplication', '/designed/endshBrngSetDend/brngQty', '/designed/endshBrngSetDend/thermosensor/qty'}, 'HE39': {'/designed/platesAndLabels/ratingPlate/ratingPlateData/complete', '/designed/platesAndLabels/ratingPlate/ratingPlateData/completeAct'}, 'HE40': {'/certification/certUl', '/designed/avrSet/avr/certUl'}, 'HE41': {'/designed/endshBrngSetNend/endsh/ext/fitDiam', '/designed/statorMainWound/packageStator/externalDiameter'}, 'HE42': {'/designed/rawMatFixingElements', '/painting/paintingPlan'}, 'HE43': {'/designed/flywheelHousingSupport'}, 'HE44': {'/designed/designConcept'}, 'HE45': {'/designed/endshBrngSetDend/thermosensor', '/designed/endshBrngSetDend/thermosensorSize', '/designed/endshBrngSetNend/thermosensor', '/designed/endshBrngSetNend/thermosensorSize'}, 'HE46': {'/designed/painting/colorCode', '/painting/colorCode'}, 'HE47': {'/accessories/thermosensorStator/sensorClass', '/designed/thermosensorStator/thermosensor/sensorClass'}, 'HE48': {'/accessories/thermosensorStator/type', '/designed/thermosensorStator/thermosensor/type'}, 'HE49': {'/designed/spaceHeaterSet', '/workaround/enumerated/spaceHeaterConnectionVoltage'}, 'HE50': {'/basicParameters/standard', '/designed/tboxStatorSet/tbox/standard'}, 'HE51': {'/accessories/thermosensorBrng/qty', '/designed/endshBrngSetDend/thermosensor/qty', '/designed/endshBrngSetNend/thermosensor/qty'}, 'HE52': {'/accessories/thermosensorStator', '/accessories/thermosensorStatorAct'}, 'HE53': {'/accessories/thermosensorBrng/sensorClass', '/accessories/thermosensorStator/sensorClass'}, 'HE54': {'/designed/designConcept', '/designed/tboxStatorSet', '/mounting/locationCableInlet', '/mounting/locationTbox'}, 'HE55': {'/commercial/applicationCode'}, 'HE56': {'/commercial/productLine'}, 'HE57': {'/designed/endshBrngSetNend/frameSize', '/designed/frameSize'}, 'HE58': {'/designed/platesAndLabels/language', '/designed/platesAndLabels/ratingPlate/ratingPlateData/language'}, 'HE59': {'/basicParameters/ratedFrequencyInput', '/basicParameters/rotationSpeedRated', '/designed/rotorMainWound/polesNumber'}, 'HE60': {'/commercial/locationCableInletNDE', '/designed/tboxStatorSetAct'}, 'HE61': {'/designed/flywheel', '/designed/shaft/flywheel'}, 'HE62': {'/designed/designConcept', '/designed/endshBrngSetDend/designConcept'}, 'HE63': {'/designed/endshBrngSetDend', '/designed/endshDendAct'}, 'HE64': {'/accessories/thermosensorBrng/wireConfiguration', '/designed/endshBrngSetDend/thermosensor/thermosensor/wireConfiguration'}, 'HE65': {'/basicParameters/phaseNumber', '/designed/rotorMainWound/winding/phaseNumber'}, 'HE66': {'/certification/certTuv', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certTuv'}, 'HE67': {'/designed/endshBrngSetDend/thermosensor', '/designed/endshBrngSetDend/thermosensorAct', '/designed/endshBrngSetNend/thermosensor', '/designed/endshBrngSetNend/thermosensorAct'}, 'HE68': {'/designed/endshBrngSetDend/brng/intDiam', '/designed/shaft/brngDend/diam'}, 'HE69': {'/designed/frame', '/designed/frameAct'}, 'HE70': {'/mounting/flange', '/mounting/flangeAct'}, 'HE71': {'/designed/flywheelHousing/rearFix/fixHoleQty', '/designed/flywheelHousingSupport/dim/fixHoleQty'}, 'HE72': {'/commercial/transportAndBilling/currentType', '/commercial/transportAndBilling/productClass', '/commercial/transportAndBilling/rotorType'}, 'HE73': {'/designed/endshBrngSetDend/frameSize', '/designed/frameSize'}, 'HE74': {'/designed/flywheelAndHousing_gap'}, 'HE75': {'/designed/designConcept', '/designed/frameSize'}, 'HE76': {'/designed/tboxStatorSet/tbox/accessoriesRailReady', '/designed/thermosensorStator'}, 'HE77': {'/accessories/thermosensorBrngAct', '/accessories/thermosensorStatorAct'}, 'HE78': {'/designed/flywheelHousing', '/designed/flywheelHousingAct'}, 'HE79': {'/designed/spaceHeaterSet/connectionElectricVoltage', '/workaround/enumerated/spaceHeaterConnectionVoltage'}, 'HE80': {'/accessories/thermosensorStator', '/accessories/thermosensorStatorSize'}, 'HE81': {'/accessories/thermosensorBrng/wireConfiguration', '/designed/endshBrngSetNend/thermosensor/thermosensor/wireConfiguration'}, 'HE82': {'/designed/endshBrngSetDend/endsh/protLid/fixHoleQty', '/designed/endshBrngSetDend/endshProtLid/fixHole/qty', '/designed/endshBrngSetNend/endsh/protLid/fixHoleQty', '/designed/endshBrngSetNend/endshProtLid/fixHole/qty'}, 'HE83': {'/accessories/thermosensorStator/wireConfiguration', '/designed/thermosensorStator/thermosensor/wireConfiguration'}, 'HE84': {'/basicParameters/noise/grade'}, 'HE85': {'/basicParameters/vibration/level'}, 'HE86': {'/accessories/thermosensorBrng', '/accessories/thermosensorBrngAct'}, 'HE87': {'/designed/endshBrngSetNend/side'}, 'HE88': {'/designed/avrSet/avr/model', '/designed/avrSet/installationLocal', '/designed/designConcept', '/designed/frameSize', '/designed/tboxStatorSet/tbox/rawMat'}, 'HE89': {'/designed/designConcept', '/designed/tboxStatorSet/designConcept'}, 'HE90': {'/accessories/thermosensorBrng/type', '/designed/endshBrngSetNend/thermosensor/thermosensor/type'}, 'HE91': {'/accessories/thermosensorBrng/sensorClass', '/designed/endshBrngSetNend/thermosensor/thermosensor/sensorClass'}, 'HE92': {'/designed/flywheelHousing/rearFix/fixHolePosDiam', '/designed/flywheelHousingSupport/dim/fixHolePosDiam'}, 'HE93': {'/designed/flywheel/ext/diam', '/designed/flywheelAndHousing_gap', '/designed/flywheelHousing/dim/extDiam'}, 'HE94': {'/designed/endshBrngSetDend/thermosensor/thermosensor/type', '/designed/endshBrngSetNend/thermosensor/thermosensor/type', '/designed/thermosensorStator/thermosensor/type'}, 'HE95': {'/designed/thermosensorStator', '/designed/thermosensorStatorAct'}, 'HE96': {'/designed/endshBrngSetDend/side'}, 'HE97': {'/mounting/locationCableInlet'}, 'HE98': {'/designed/endshBrngSetNend/brng/intDiam', '/designed/shaft/brngNend/diam'}, 'HE99': {'/accessories/thermosensorStator/qty', '/accessories/thermosensorStator/qtyPerApplication', '/basicParameters/phaseNumber'}, 'HE100': {'/accessories/thermosensorBrng', '/accessories/thermosensorBrngSize'}, 'HE101': {'/operationAndCondition/overspeedTime', '/workaround/enumerated/overspeedTime'}, 'HE102': {'/basicParameters/phaseNumber', '/designed/statorMainWound/winding/phaseNumber'}, 'HE103': {'/operationAndCondition/coupling', '/operationAndCondition/pulleysAndBelts'}, 'HE104': {'/basicParameters/frameSize', '/designed/frameSize'}, 'HE105': {'/designed/avrSet', '/designed/avrSetAct'}, 'HE106': {'/basicParameters/ratedFrequencyInput', '/basicParameters/ratedVoltageInput', '/basicParameters/standard', '/designed/manualOperation/language', '/designed/platesAndLabels/language', '/designed/platesAndLabels/ratingPlate/ratingPlateData/language', '/designed/platesAndLabels/ratingPlate/ratingPlateData/type'}, 'HE107': {'/designed/frameFoot', '/designed/frameFootAct'}, 'HE108': {'/designed/endshBrngSetDend/brng/operatingTemp', '/designed/endshBrngSetNend/brng/operatingTemp'}, 'HE109': {'/certification/certUkca', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certUkca'}, 'HE110': {'/designed/flywheelHousing/rearFix/fitDiam', '/designed/flywheelHousingSupport/dim/fitDiam'}, 'HE111': {'/designed/endshBrngSetDend/thermosensor/qty', '/designed/endshBrngSetDend/thermosensor/thermosensor/type', '/designed/endshBrngSetDend/thermosensor/thermosensor/wireConfiguration', '/designed/endshBrngSetNend/thermosensor/qty', '/designed/endshBrngSetNend/thermosensor/thermosensor/type', '/designed/endshBrngSetNend/thermosensor/thermosensor/wireConfiguration'}, 'HE112': {'/operationAndCondition/powerFactor', '/workaround/enumerated/powerFactor'}, 'HE113': {'/commercial/regionOfOperation'}, 'HE114': {'/designed/painting/gloss', '/painting/gloss'}, 'HE115': {'/designed/platesAndLabels/material', '/designed/platesAndLabels/ratingPlate/ratingPlate/material'}, 'HE116': {'/designed/endshBrngSetDend/endshProtLid', '/designed/endshBrngSetDend/side', '/designed/endshBrngSetNend/endshProtLid', '/designed/endshBrngSetNend/side'}, 'HE117': {'/designed/endshBrngSetDend', '/mounting/brng/endshBrngQty'}, 'HE118': {'/designed/fanDend/hub/intDiam', '/designed/shaft/fanIntDend/diam'}, 'HE119': {'/basicParameters/vibration/standard'}, 'HE120': {'/certification/certCe', '/designed/avrSet/avr/certCe'}, 'HE121': {'/certification/certUkca', '/designed/avrSet/avr/certUkca'}, 'HE122': {'/accessories/thermosensorBrng/qty', '/designed/endshBrngSetDend', '/designed/endshBrngSetNend/thermosensor/qty'}, 'HE123': {'/designed/flywheel', '/mounting/shaftendDend/type'}, 'HE124': {'/ambient/atmosCorrosCat'}, 'HE125': {'/designed/endshBrngSetDend/thermosensor/thermosensor/sensorClass', '/designed/endshBrngSetDend/thermosensor/thermosensor/wireConfiguration', '/designed/endshBrngSetNend/thermosensor/thermosensor/sensorClass', '/designed/endshBrngSetNend/thermosensor/thermosensor/wireConfiguration', '/designed/thermosensorStator/thermosensor/sensorClass', '/designed/thermosensorStator/thermosensor/wireConfiguration'}, 'HE126': {'/designed/endshBrngSetNend/thermosensor', '/designed/tboxStatorSet/tbox/accessoriesRailReady'}, 'HE127': {'/operationAndCondition/overspeed', '/workaround/enumerated/overspeed'}, 'HE128': {'/designed/endshBrngSetDend/designConcept', '/designed/endshBrngSetNend/designConcept'}, 'HE129': {'/accessories/thermosensorBrng/qtyPerApplication', '/designed/endshBrngSetNend/brngQty', '/designed/endshBrngSetNend/thermosensor/qty'}, 'HE130': {'/certification/certUl', '/designed/platesAndLabels/ratingPlate/ratingPlateData/certUl'}, 'HE131': {'/accessories/thermosensorBrng', '/designed/endshBrngSetDend', '/designed/endshBrngSetDend/thermosensor'}, 'HE132': {'/designed/painting/colorCode', '/designed/painting/gloss'}, 'HE133': {'/accessories/thermosensorBrng/type', '/designed/endshBrngSetDend/thermosensor/thermosensor/type'}, 'HE134': {'/designed/frameSize', '/designed/tboxStatorSet/frameSize'}, 'HE135': {'/designed/statorMainWound/packageStator/fixType', '/designed/statorMainWound/packageStator/statorMainLamination/frameSupport'}} 


nodes2 = {'a', 'b', 'c', 'd'}
hyperedges2 = {'HE1': {'a','b', 'c'}, 'HE2': {'b', 'c', 'd'}}

# Criar o hiper-grafo
H = hnx.Hypergraph(edges_WENnovo)

# Plotar o hiper-grafo
hnx.draw(H, with_node_labels=True)

plt.show()