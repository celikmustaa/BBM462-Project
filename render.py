import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# creating the dataset
data = {'1':0.024014, '2':0.023145, '4098':0.000006, '3':0.022759, '4':0.022669, '5':0.021325, '6':0.021248, '7':0.020338, '8':0.019469, '9':0.019136, '10':0.018833, '11':0.017911, '12':0.016685, '13':0.016572, '14':0.015745, '15':0.016465, '16':0.015240, '17':0.014663, '18':0.014407, '19':0.014032, '20':0.013693, '21':0.013509, '22':0.013116, '23':0.012486, '24':0.012176, '25':0.011808, '26':0.011944, '27':0.011302, '28':0.010618, '29':0.010231, '30':0.009517, '31':0.009755, '32':0.009422, '33':0.009071, '34':0.009137, '35':0.008726, '36':0.008322, '37':0.008453, '38':0.008506, '39':0.007763, '40':0.007780, '8232':0.000006, '41':0.007269, '42':0.007489, '43':0.007328, '44':0.007150, '45':0.006983, '46':0.006722, '47':0.006763, '48':0.006323, '49':0.006180, '50':0.006109, '51':0.005788, '52':0.005740, '53':0.005544, '54':0.005746, '55':0.005318, '56':0.005062, '57':0.004961, '58':0.004878, '59':0.004925, '60':0.005122, '61':0.004628, '62':0.004794, '63':0.004372, '64':0.004426, '65':0.004217, '66':0.004051, '4162':0.000006, '67':0.003938, '68':0.003747, '69':0.003783, '70':0.003539, '71':0.003581, '72':0.003759, '4168':0.000006, '73':0.003569, '74':0.003379, '75':0.003420, '76':0.003391, '77':0.003426, '78':0.003099, '79':0.003254, '80':0.002879, '81':0.002956, '82':0.003135, '83':0.002802, '84':0.002766, '85':0.002843, '86':0.002849, '87':0.002867, '88':0.002707, '89':0.002445, '90':0.002576, '91':0.002385, '92':0.002409, '93':0.002272, '94':0.002510, '95':0.002248, '96':0.002219, '97':0.002106, '98':0.002100, '99':0.001886, '8291':0.000006, '100':0.002034, '101':0.002022, '102':0.002130, '103':0.002100, '104':0.001921, '105':0.001838, '106':0.002005, '107':0.001880, '108':0.001868, '109':0.001743, '110':0.001648, '111':0.001719, '112':0.001868, '113':0.001660, '4209':0.000006, '114':0.001529, '115':0.001541, '116':0.001689, '117':0.001683, '118':0.001570, '119':0.001570, '120':0.001285, '121':0.001636, '122':0.001493, '123':0.001279, '124':0.001648, '125':0.001440, '126':0.001434, '127':0.001303, '128':0.001338, '129':0.001267, '130':0.001172, '131':0.001267, '132':0.001202, '133':0.001190, '134':0.001231, '135':0.001059, '136':0.001208, '137':0.001255, '138':0.001237, '139':0.001172, '140':0.000922, '141':0.000970, '142':0.001047, '4238':0.000006, '143':0.001202, '144':0.001017, '145':0.001190, '146':0.001035, '147':0.001029, '148':0.001005, '4244':0.000006, '149':0.001124, '150':0.000892, '151':0.000934, '152':0.000904, '153':0.000916, '154':0.000714, '155':0.001023, '156':0.000732, '157':0.000761, '158':0.000946, '159':0.000857, '160':0.000987, '161':0.000827, '162':0.000815, '163':0.000767, '164':0.000910, '165':0.000761, '166':0.000708, '4262':0.000006, '167':0.000761, '168':0.000785, '169':0.000696, '170':0.000660, '4266':0.000006, '171':0.000761, '172':0.000613, '173':0.000732, '174':0.000767, '175':0.000773, '176':0.000714, '177':0.000684, '178':0.000714, '179':0.000696, '180':0.000678, '181':0.000809, '182':0.000589, '183':0.000666, '184':0.000732, '185':0.000595, '4281':0.000006, '186':0.000529, '187':0.000672, '188':0.000565, '189':0.000529, '8381':0.000006, '190':0.000553, '191':0.000648, '192':0.000589, '193':0.000529, '194':0.000607, '4290':0.000006, '195':0.000506, '196':0.000482, '197':0.000529, '198':0.000553, '20678':0.000006, '199':0.000577, '200':0.000476, '201':0.000458, '202':0.000506, '203':0.000500, '204':0.000631, '4300':0.000006, '205':0.000577, '206':0.000440, '207':0.000541, '208':0.000452, '209':0.000494, '210':0.000553, '211':0.000494, '212':0.000464, '213':0.000404, '214':0.000434, '215':0.000381, '216':0.000523, '217':0.000369, '218':0.000470, '219':0.000428, '220':0.000452, '221':0.000428, '222':0.000428, '223':0.000399, '224':0.000399, '225':0.000428, '226':0.000327, '227':0.000321, '228':0.000440, '229':0.000339, '230':0.000375, '231':0.000381, '232':0.000393, '233':0.000410, '234':0.000303, '235':0.000315, '236':0.000351, '237':0.000351, '238':0.000476, '239':0.000333, '4335':0.000006, '240':0.000339, '241':0.000399, '242':0.000375, '243':0.000297, '244':0.000369, '245':0.000220, '246':0.000351, '247':0.000369, '248':0.000291, '249':0.000232, '250':0.000327, '251':0.000357, '252':0.000357, '253':0.000375, '254':0.000369, '255':0.000321, '256':0.000256, '8448':0.000006, '257':0.000256, '258':0.000297, '259':0.000286, '260':0.000268, '4356':0.000006, '261':0.000327, '262':0.000303, '263':0.000262, '264':0.000244, '265':0.000375, '266':0.000309, '267':0.000286, '268':0.000268, '269':0.000291, '270':0.000256, '271':0.000226, '272':0.000226, '273':0.000226, '274':0.000226, '275':0.000321, '276':0.000250, '277':0.000274, '278':0.000333, '279':0.000256, '4375':0.000006, '280':0.000214, '281':0.000232, '282':0.000286, '283':0.000268, '284':0.000190, '285':0.000202, '4381':0.000006, '286':0.000268, '287':0.000232, '288':0.000220, '289':0.000184, '290':0.000244, '291':0.000268, '292':0.000196, '293':0.000250, '294':0.000220, '295':0.000262, '296':0.000208, '297':0.000226, '298':0.000208, '299':0.000244, '300':0.000208, '301':0.000202, '302':0.000167, '303':0.000178, '304':0.000208, '305':0.000214, '306':0.000291, '307':0.000178, '308':0.000214, '309':0.000196, '310':0.000167, '311':0.000208, '312':0.000184, '313':0.000190, '4409':0.000006, '314':0.000173, '315':0.000196, '316':0.000178, '317':0.000161, '318':0.000244, '319':0.000155, '320':0.000178, '321':0.000178, '322':0.000190, '4418':0.000006, '323':0.000107, '324':0.000143, '325':0.000143, '326':0.000149, '327':0.000220, '328':0.000167, '329':0.000161, '330':0.000220, '331':0.000178, '332':0.000184, '333':0.000173, '4429':0.000006, '334':0.000202, '335':0.000149, '336':0.000196, '337':0.000125, '338':0.000119, '339':0.000178, '340':0.000131, '341':0.000149, '342':0.000137, '343':0.000107, '344':0.000161, '345':0.000119, '346':0.000101, '347':0.000113, '348':0.000143, '349':0.000155, '350':0.000173, '351':0.000173, '352':0.000095, '353':0.000125, '354':0.000119, '355':0.000149, '356':0.000119, '357':0.000131, '358':0.000143, '359':0.000178, '360':0.000178, '4456':0.000006, '361':0.000107, '362':0.000125, '363':0.000143, '364':0.000119, '365':0.000125, '366':0.000155, '367':0.000137, '368':0.000167, '369':0.000101, '370':0.000113, '371':0.000149, '372':0.000119, '373':0.000119, '374':0.000143, '375':0.000089, '376':0.000071, '377':0.000095, '378':0.000149, '379':0.000083, '380':0.000089, '381':0.000161, '382':0.000113, '383':0.000137, '384':0.000119, '385':0.000077, '386':0.000131, '387':0.000113, '388':0.000095, '389':0.000149, '390':0.000113, '391':0.000107, '392':0.000059, '393':0.000077, '394':0.000113, '395':0.000113, '4491':0.000006, '396':0.000095, '397':0.000131, '398':0.000095, '399':0.000083, '400':0.000107, '401':0.000137, '402':0.000125, '403':0.000131, '404':0.000113, '405':0.000077, '406':0.000137, '407':0.000095, '408':0.000113, '409':0.000095, '410':0.000113, '411':0.000101, '412':0.000077, '413':0.000083, '414':0.000089, '415':0.000095, '4511':0.000006, '416':0.000065, '417':0.000113, '418':0.000048, '419':0.000071, '420':0.000113, '421':0.000077, '422':0.000101, '423':0.000101, '424':0.000071, '425':0.000107, '426':0.000059, '427':0.000089, '428':0.000054, '429':0.000065, '430':0.000083, '431':0.000089, '432':0.000089, '433':0.000059, '4529':0.000006, '434':0.000071, '4530':0.000006, '435':0.000089, '436':0.000083, '437':0.000089, '438':0.000107, '439':0.000054, '440':0.000107, '441':0.000077, '442':0.000065, '443':0.000065, '444':0.000107, '445':0.000131, '446':0.000024, '447':0.000059, '448':0.000071, '449':0.000101, '450':0.000071, '451':0.000059, '452':0.000054, '453':0.000089, '4549':0.000006, '454':0.000095, '455':0.000048, '456':0.000083, '457':0.000119, '458':0.000101, '459':0.000101, '460':0.000077, '461':0.000107, '462':0.000089, '463':0.000048, '464':0.000054, '465':0.000077, '466':0.000042, '467':0.000077, '468':0.000030, '469':0.000077, '470':0.000083, '471':0.000048, '472':0.000095, '473':0.000059, '474':0.000065, '475':0.000077, '476':0.000059, '477':0.000071, '478':0.000083, '479':0.000059, '480':0.000095, '481':0.000083, '482':0.000071, '483':0.000101, '484':0.000054, '4580':0.000006, '485':0.000065, '4581':0.000006, '486':0.000059, '487':0.000065, '488':0.000030, '489':0.000065, '490':0.000071, '491':0.000054, '492':0.000036, '493':0.000054, '494':0.000065, '495':0.000030, '496':0.000048, '497':0.000054, '498':0.000054, '499':0.000042, '500':0.000059, '501':0.000054, '502':0.000030, '503':0.000059, '504':0.000059, '505':0.000042, '506':0.000071, '4602':0.000012, '507':0.000071, '508':0.000054, '4604':0.000006, '509':0.000042, '510':0.000083, '511':0.000048, '512':0.000054, '513':0.000048, '514':0.000065, '515':0.000048, '516':0.000071, '517':0.000036, '518':0.000018, '519':0.000071, '520':0.000054, '521':0.000024, '522':0.000059, '523':0.000054, '524':0.000030, '525':0.000048, '526':0.000018, '527':0.000071, '528':0.000054, '529':0.000054, '530':0.000077, '531':0.000065, '532':0.000083, '533':0.000042, '534':0.000042, '535':0.000048, '536':0.000054, '537':0.000065, '538':0.000065, '539':0.000054, '540':0.000018, '541':0.000048, '542':0.000059, '543':0.000054, '544':0.000024, '545':0.000030, '546':0.000036, '547':0.000054, '548':0.000030, '549':0.000059, '550':0.000036, '551':0.000054, '552':0.000054, '553':0.000030, '554':0.000042, '555':0.000065, '556':0.000030, '557':0.000065, '558':0.000024, '559':0.000048, '560':0.000036, '561':0.000071, '562':0.000030, '563':0.000048, '564':0.000065, '565':0.000036, '566':0.000036, '567':0.000077, '568':0.000059, '569':0.000006, '570':0.000071, '571':0.000089, '572':0.000006, '573':0.000059, '574':0.000054, '575':0.000059, '576':0.000042, '577':0.000048, '578':0.000012, '579':0.000071, '580':0.000065, '581':0.000030, '582':0.000048, '583':0.000024, '584':0.000048, '585':0.000024, '586':0.000036, '587':0.000024, '588':0.000036, '589':0.000024, '590':0.000036, '591':0.000059, '592':0.000036, '4688':0.000006, '593':0.000030, '594':0.000030, '595':0.000089, '596':0.000024, '597':0.000036, '598':0.000024, '599':0.000036, '600':0.000042, '4696':0.000006, '601':0.000030, '602':0.000054, '603':0.000048, '604':0.000030, '4700':0.000006, '605':0.000036, '606':0.000012, '607':0.000036, '608':0.000054, '609':0.000042, '610':0.000030, '611':0.000012, '612':0.000018, '613':0.000012, '614':0.000042, '615':0.000030, '616':0.000012, '617':0.000018, '618':0.000030, '619':0.000036, '620':0.000054, '621':0.000006, '622':0.000048, '623':0.000030, '624':0.000030, '625':0.000030, '626':0.000024, '627':0.000024, '628':0.000036, '629':0.000024, '630':0.000030, '4726':0.000006, '631':0.000036, '632':0.000006, '633':0.000036, '634':0.000030, '635':0.000024, '636':0.000042, '4732':0.000006, '637':0.000065, '638':0.000006, '639':0.000024, '640':0.000042, '641':0.000036, '642':0.000018, '643':0.000036, '644':0.000030, '645':0.000036, '646':0.000077, '647':0.000006, '648':0.000006, '649':0.000024, '650':0.000036, '651':0.000048, '652':0.000024, '653':0.000018, '654':0.000018, '655':0.000006, '656':0.000024, '657':0.000012, '658':0.000036, '659':0.000036, '660':0.000018, '661':0.000036, '662':0.000018, '4759':0.000006, '663':0.000054, '664':0.000030, '665':0.000030, '666':0.000012, '667':0.000006, '668':0.000036, '669':0.000006, '670':0.000030, '671':0.000030, '672':0.000048, '673':0.000018, '674':0.000059, '675':0.000018, '676':0.000030, '677':0.000030, '678':0.000036, '679':0.000030, '680':0.000036, '8872':0.000006, '681':0.000036, '682':0.000036, '683':0.000036, '684':0.000018, '685':0.000006, '4782':0.000006, '686':0.000030, '687':0.000024, '688':0.000048, '689':0.000030, '690':0.000018, '691':0.000030, '692':0.000024, '693':0.000036, '694':0.000024, '695':0.000018, '696':0.000018, '697':0.000012, '698':0.000030, '699':0.000024, '700':0.000012, '701':0.000036, '702':0.000030, '703':0.000024, '704':0.000024, '705':0.000030, '706':0.000018, '707':0.000071, '708':0.000018, '709':0.000006, '711':0.000024, '712':0.000030, '713':0.000012, '714':0.000018, '715':0.000024, '716':0.000012, '717':0.000024, '718':0.000012, '719':0.000036, '720':0.000012, '721':0.000024, '722':0.000042, '723':0.000018, '724':0.000036, '4820':0.000006, '725':0.000012, '726':0.000030, '727':0.000024, '728':0.000012, '729':0.000006, '731':0.000018, '733':0.000036, '734':0.000030, '735':0.000036, '736':0.000018, '737':0.000024, '738':0.000024, '739':0.000030, '740':0.000006, '741':0.000048, '742':0.000018, '743':0.000024, '4840':0.000006, '744':0.000030, '745':0.000018, '746':0.000042, '747':0.000012, '4843':0.000006, '748':0.000018, '749':0.000024, '750':0.000012, '751':0.000018, '752':0.000024, '753':0.000012, '754':0.000036, '755':0.000018, '756':0.000018, '757':0.000024, '758':0.000012, '759':0.000036, '4857':0.000006, '761':0.000006, '762':0.000036, '763':0.000012, '764':0.000012, '765':0.000024, '766':0.000012, '767':0.000024, '769':0.000012, '770':0.000012, '4866':0.000006, '771':0.000030, '772':0.000024, '773':0.000012, '774':0.000006, '775':0.000024, '776':0.000012, '777':0.000012, '778':0.000024, '779':0.000012, '780':0.000024, '781':0.000012, '782':0.000030, '783':0.000036, '784':0.000018, '785':0.000012, '786':0.000018, '787':0.000012, '788':0.000012, '789':0.000012, '790':0.000012, '791':0.000024, '792':0.000024, '793':0.000012, '794':0.000012, '795':0.000018, '796':0.000006, '797':0.000012, '798':0.000012, '4895':0.000006, '799':0.000012, '800':0.000018, '801':0.000012, '802':0.000036, '803':0.000012, '804':0.000018, '805':0.000012, '806':0.000018, '807':0.000012, '808':0.000024, '809':0.000012, '810':0.000018, '811':0.000036, '812':0.000018, '813':0.000018, '4909':0.000006, '814':0.000018, '4910':0.000006, '815':0.000018, '816':0.000018, '817':0.000018, '818':0.000024, '819':0.000030, '4915':0.000006, '820':0.000024, '821':0.000030, '822':0.000018, '823':0.000018, '824':0.000012, '825':0.000012, '826':0.000012, '827':0.000012, '828':0.000012, '829':0.000018, '830':0.000024, '831':0.000006, '832':0.000030, '833':0.000006, '835':0.000012, '836':0.000006, '837':0.000012, '4933':0.000006, '838':0.000024, '839':0.000012, '840':0.000042, '841':0.000018, '4938':0.000006, '843':0.000036, '844':0.000012, '9037':0.000006, '845':0.000012, '846':0.000012, '847':0.000012, '848':0.000006, '849':0.000006, '9042':0.000006, '850':0.000012, '4946':0.000006, '851':0.000024, '852':0.000024, '853':0.000012, '13141':0.000006, '854':0.000024, '855':0.000018, '857':0.000006, '858':0.000024, '859':0.000012, '860':0.000006, '861':0.000018, '9053':0.000006, '862':0.000012, '863':0.000042, '864':0.000006, '865':0.000006, '866':0.000030, '13154':0.000006, '867':0.000006, '868':0.000030, '869':0.000018, '870':0.000024, '871':0.000012, '872':0.000012, '873':0.000018, '874':0.000018, '875':0.000018, '876':0.000012, '877':0.000018, '878':0.000012, '879':0.000036, '880':0.000006, '881':0.000006, '882':0.000006, '883':0.000024, '884':0.000012, '4980':0.000006, '885':0.000006, '886':0.000030, '887':0.000012, '888':0.000012, '889':0.000012, '890':0.000012, '891':0.000012, '892':0.000018, '893':0.000012, '894':0.000006, '895':0.000012, '896':0.000006, '897':0.000012, '898':0.000018, '899':0.000006, '900':0.000012, '901':0.000012, '902':0.000018, '4998':0.000006, '903':0.000006, '904':0.000006, '906':0.000006, '5003':0.000006, '907':0.000006, '908':0.000006, '909':0.000012, '910':0.000030, '911':0.000006, '912':0.000006, '913':0.000006, '914':0.000006, '915':0.000030, '916':0.000006, '917':0.000024, '918':0.000006, '919':0.000006, '920':0.000018, '921':0.000030, '922':0.000006, '923':0.000012, '924':0.000006, '925':0.000006, '926':0.000006, '927':0.000006, '928':0.000006, '929':0.000012, '930':0.000018, '931':0.000012, '932':0.000006, '933':0.000006, '934':0.000012, '935':0.000006, '936':0.000018, '937':0.000012, '938':0.000018, '939':0.000012, '940':0.000012, '941':0.000024, '942':0.000018, '943':0.000006, '945':0.000012, '947':0.000006, '948':0.000018, '950':0.000006, '952':0.000018, '953':0.000006, '954':0.000006, '955':0.000006, '956':0.000018, '957':0.000006, '958':0.000006, '959':0.000012, '961':0.000012, '962':0.000006, '963':0.000012, '964':0.000024, '9156':0.000006, '965':0.000006, '967':0.000006, '969':0.000018, '970':0.000006, '5067':0.000006, '972':0.000006, '973':0.000006, '974':0.000006, '975':0.000012, '977':0.000012, '978':0.000012, '979':0.000006, '980':0.000024, '981':0.000006, '983':0.000012, '984':0.000018, '985':0.000006, '986':0.000006, '987':0.000024, '988':0.000012, '989':0.000006, '990':0.000006, '991':0.000030, '992':0.000006, '993':0.000012, '994':0.000006, '995':0.000024, '996':0.000006, '5093':0.000006, '997':0.000006, '998':0.000006, '999':0.000018, '1000':0.000012, '1001':0.000006, '1002':0.000012, '1003':0.000012, '1004':0.000006, '1007':0.000006, '5104':0.000006, '1010':0.000018, '1011':0.000006, '1012':0.000006, '1015':0.000018, '1016':0.000006, '1017':0.000042, '1018':0.000012, '1019':0.000024, '1020':0.000012, '1021':0.000006, '1022':0.000006, '1023':0.000006, '1026':0.000024, '1028':0.000012, '1032':0.000018, '1033':0.000006, '1034':0.000006, '1035':0.000012, '1036':0.000012, '1038':0.000012, '1040':0.000018, '1043':0.000024, '1044':0.000012, '1045':0.000018, '1046':0.000012, '1047':0.000006, '1049':0.000012, '1050':0.000012, '1051':0.000012, '1052':0.000006, '1054':0.000012, '1056':0.000012, '1057':0.000018, '1058':0.000006, '1059':0.000006, '1060':0.000012, '1062':0.000024, '1063':0.000024, '1064':0.000006, '1065':0.000006, '1066':0.000018, '1067':0.000018, '1068':0.000006, '1069':0.000018, '1070':0.000006, '1071':0.000006, '1072':0.000018, '1073':0.000006, '1075':0.000012, '1076':0.000006, '1077':0.000012, '1081':0.000006, '1082':0.000018, '1083':0.000012, '1084':0.000024, '1085':0.000006, '1087':0.000006, '9280':0.000006, '1088':0.000006, '1089':0.000018, '1090':0.000012, '1091':0.000012, '1092':0.000018, '1095':0.000006, '1099':0.000006, '1100':0.000018, '1102':0.000024, '1104':0.000012, '1105':0.000006, '1106':0.000006, '1107':0.000012, '1109':0.000012, '1110':0.000018, '1111':0.000024, '1112':0.000006, '1114':0.000006, '1115':0.000006, '1116':0.000006, '1120':0.000018, '1121':0.000006, '9316':0.000006, '1126':0.000006, '1127':0.000006, '1129':0.000012, '1131':0.000012, '1133':0.000006, '1135':0.000012, '1136':0.000012, '1137':0.000012, '1139':0.000012, '1141':0.000012, '1142':0.000012, '1143':0.000006, '5239':0.000006, '1144':0.000012, '1145':0.000012, '1147':0.000012, '1148':0.000018, '1151':0.000012, '1153':0.000018, '1155':0.000018, '1158':0.000006, '1159':0.000006, '1160':0.000006, '1161':0.000012, '1162':0.000018, '1163':0.000012, '1164':0.000006, '1165':0.000006, '1166':0.000012, '1168':0.000006, '1171':0.000018, '1172':0.000012, '1174':0.000006, '1175':0.000006, '1176':0.000012, '1177':0.000012, '1178':0.000006, '1179':0.000006, '1183':0.000006, '1184':0.000006, '1185':0.000006, '1186':0.000006, '1187':0.000018, '1188':0.000006, '5287':0.000006, '1193':0.000006, '1194':0.000006, '1198':0.000006, '1199':0.000018, '1200':0.000012, '1201':0.000006, '1202':0.000024, '1203':0.000006, '1207':0.000012, '1210':0.000006, '1211':0.000018, '1214':0.000012, '5311':0.000012, '1217':0.000012, '1220':0.000006, '1221':0.000006, '1222':0.000006, '1224':0.000012, '1226':0.000024, '1227':0.000006, '1228':0.000006, '1229':0.000018, '1231':0.000006, '1232':0.000006, '1234':0.000024, '1235':0.000012, '1237':0.000012, '5335':0.000006, '1239':0.000006, '1240':0.000006, '29912':0.000006, '1243':0.000012, '1244':0.000012, '1245':0.000006, '1246':0.000012, '1247':0.000012, '1248':0.000012, '1249':0.000006, '1250':0.000006, '1253':0.000006, '1254':0.000006, '1256':0.000006, '1257':0.000012, '1259':0.000006, '1265':0.000012, '1267':0.000006, '1273':0.000006, '1274':0.000006, '1275':0.000012, '1277':0.000006, '1278':0.000012, '1279':0.000006, '1280':0.000006, '1281':0.000012, '1282':0.000006, '1283':0.000006, '1284':0.000018, '1287':0.000012, '1288':0.000006, '1291':0.000012, '1292':0.000018, '1293':0.000006, '1295':0.000012, '5391':0.000006, '1296':0.000006, '1297':0.000006, '1300':0.000006, '1303':0.000006, '1305':0.000006, '1306':0.000006, '1308':0.000006, '1310':0.000006, '1311':0.000006, '5407':0.000006, '1313':0.000012, '1314':0.000006, '1316':0.000012, '1317':0.000006, '1319':0.000006, '1321':0.000006, '1322':0.000006, '1323':0.000006, '1325':0.000024, '1330':0.000006, '1333':0.000006, '1335':0.000006, '5432':0.000006, '1336':0.000006, '1338':0.000018, '1341':0.000006, '1343':0.000006, '1344':0.000006, '1345':0.000006, '1347':0.000006, '1348':0.000006, '1349':0.000012, '1351':0.000006, '1352':0.000012, '1353':0.000006, '1355':0.000006, '1356':0.000018, '1361':0.000006, '1362':0.000006, '1363':0.000006, '5462':0.000006, '1367':0.000006, '1369':0.000018, '1373':0.000006, '1374':0.000012, '1375':0.000006, '1377':0.000006, '1379':0.000006, '1380':0.000006, '1385':0.000006, '1388':0.000006, '1389':0.000006, '1390':0.000006, '1391':0.000012, '1394':0.000006, '1396':0.000024, '1397':0.000006, '1398':0.000006, '1400':0.000006, '5497':0.000006, '1402':0.000006, '1403':0.000012, '1406':0.000006, '1410':0.000006, '1412':0.000006, '1413':0.000006, '1414':0.000006, '1415':0.000006, '1417':0.000006, '1418':0.000012, '1420':0.000006, '1422':0.000006, '1424':0.000006, '1425':0.000006, '1426':0.000012, '1431':0.000024, '1432':0.000006, '1433':0.000018, '1435':0.000006, '1436':0.000006, '1438':0.000012, '1439':0.000006, '1440':0.000006, '1441':0.000006, '1442':0.000006, '5539':0.000006, '1443':0.000006, '1446':0.000006, '1448':0.000006, '1450':0.000006, '1457':0.000006, '1459':0.000006, '1464':0.000006, '1466':0.000012, '1467':0.000012, '1470':0.000006, '1476':0.000006, '1477':0.000006, '1480':0.000006, '1481':0.000006, '1484':0.000006, '1485':0.000006, '1489':0.000006, '1490':0.000006, '1492':0.000006, '1496':0.000006, '1500':0.000006, '1502':0.000006, '1503':0.000012, '1504':0.000006, '5601':0.000006, '1507':0.000006, '1509':0.000006, '1513':0.000012, '1520':0.000006, '1528':0.000006, '1529':0.000006, '1532':0.000012, '1536':0.000006, '1537':0.000012, '1540':0.000006, '1544':0.000006, '1545':0.000006, '1548':0.000012, '1549':0.000006, '1550':0.000012, '1551':0.000006, '1553':0.000006, '1554':0.000006, '1555':0.000012, '1556':0.000006, '5653':0.000006, '1558':0.000018, '1559':0.000012, '1560':0.000006, '1562':0.000012, '1567':0.000006, '1571':0.000006, '5668':0.000006, '1573':0.000012, '1576':0.000012, '1577':0.000006, '1578':0.000006, '1579':0.000006, '1580':0.000006, '1581':0.000012, '1584':0.000006, '1586':0.000006, '1587':0.000006, '1589':0.000006, '1591':0.000012, '1594':0.000006, '1596':0.000006, '1598':0.000012, '1600':0.000006, '1604':0.000006, '1608':0.000006, '1610':0.000018, '1612':0.000006, '1613':0.000006, '1618':0.000006, '5719':0.000006, '13917':0.000006, '1632':0.000006, '1633':0.000006, '1636':0.000006, '1639':0.000006, '1641':0.000006, '1645':0.000006, '1649':0.000006, '1651':0.000012, '1655':0.000006, '1658':0.000006, '1660':0.000024, '5759':0.000006, '1664':0.000006, '1667':0.000012, '1671':0.000006, '1672':0.000006, '1673':0.000006, '5772':0.000006, '1677':0.000006, '1680':0.000006, '1682':0.000006, '1684':0.000012, '1686':0.000006, '1687':0.000012, '1693':0.000006, '1695':0.000006, '1696':0.000006, '1698':0.000006, '1700':0.000006, '1703':0.000006, '1706':0.000012, '1709':0.000012, '1714':0.000006, '1719':0.000006, '1720':0.000006, '1726':0.000006, '1729':0.000006, '1732':0.000006, '1733':0.000006, '1735':0.000006, '1736':0.000006, '5833':0.000006, '1743':0.000006, '1747':0.000012, '1749':0.000006, '1751':0.000006, '1753':0.000012, '1756':0.000012, '1759':0.000006, '1760':0.000006, '1765':0.000006, '1769':0.000006, '1770':0.000006, '5870':0.000006, '1775':0.000006, '9969':0.000006, '1779':0.000006, '1780':0.000006, '1781':0.000006, '1782':0.000012, '1785':0.000012, '1793':0.000006, '1797':0.000006, '1799':0.000006, '1800':0.000006, '1802':0.000006, '5898':0.000006, '1808':0.000006, '1811':0.000006, '1813':0.000006, '1814':0.000006, '1816':0.000006, '1818':0.000006, '5915':0.000006, '30499':0.000006, '1828':0.000018, '5924':0.000006, '1829':0.000006, '1833':0.000006, '1835':0.000006, '5931':0.000006, '1837':0.000006, '1845':0.000012, '1847':0.000006, '1850':0.000006, '1853':0.000006, '1855':0.000006, '1856':0.000006, '1861':0.000006, '1867':0.000006, '1870':0.000006, '1872':0.000006, '1875':0.000012, '1878':0.000006, '1886':0.000006, '1890':0.000006, '1896':0.000006, '1898':0.000006, '1904':0.000006, '1908':0.000006, '1911':0.000006, '10106':0.000006, '1916':0.000006, '1925':0.000006, '1927':0.000006, '1932':0.000006, '1936':0.000006, '1945':0.000006, '6047':0.000006, '1951':0.000006, '1954':0.000012, '10146':0.000006, '1957':0.000006, '1960':0.000006, '1963':0.000006, '18349':0.000006, '1966':0.000006, '1974':0.000012, '1979':0.000006, '1981':0.000006, '1984':0.000006, '1986':0.000006, '1990':0.000006, '1992':0.000006, '1995':0.000006, '1999':0.000012, '2000':0.000006, '2001':0.000012, '2012':0.000006, '2014':0.000006, '2022':0.000006, '2025':0.000006, '2026':0.000006, '2032':0.000006, '2043':0.000006, '2051':0.000006, '2056':0.000012, '2058':0.000006, '2064':0.000006, '2069':0.000006, '2070':0.000006, '2078':0.000006, '2083':0.000006, '2084':0.000006, '2087':0.000006, '2091':0.000012, '2108':0.000006, '2111':0.000006, '2112':0.000012, '2113':0.000006, '2117':0.000012, '2119':0.000006, '2121':0.000006, '2122':0.000006, '2124':0.000006, '2125':0.000006, '14416':0.000006, '2131':0.000006, '2132':0.000012, '2134':0.000006, '2138':0.000006, '2141':0.000012, '2142':0.000006, '2144':0.000006, '2148':0.000006, '2150':0.000006, '2154':0.000006, '2160':0.000006, '2166':0.000006, '6263':0.000006, '2169':0.000006, '10367':0.000006, '2176':0.000006, '2177':0.000012, '2178':0.000006, '2179':0.000006, '2182':0.000006, '2185':0.000006, '6283':0.000006, '2188':0.000006, '22675':0.000006, '2198':0.000006, '2201':0.000006, '2205':0.000006, '2208':0.000006, '2212':0.000006, '2213':0.000006, '2214':0.000006, '2215':0.000006, '2218':0.000012, '2229':0.000006, '2231':0.000006, '2238':0.000018, '2244':0.000006, '2250':0.000006, '2251':0.000006, '2256':0.000006, '2258':0.000006, '2262':0.000006, '2282':0.000006, '2283':0.000012, '2285':0.000006, '2317':0.000006, '2320':0.000012, '2329':0.000006, '2332':0.000006, '2334':0.000006, '2335':0.000006, '2336':0.000012, '2337':0.000012, '2342':0.000006, '2354':0.000012, '2359':0.000006, '2367':0.000006, '2369':0.000006, '6468':0.000006, '18761':0.000006, '2378':0.000006, '14669':0.000006, '2382':0.000006, '6484':0.000006, '31064':0.000006, '2395':0.000006, '2415':0.000006, '2417':0.000006, '2419':0.000006, '2422':0.000006, '2428':0.000006, '2431':0.000006, '2434':0.000006, '6531':0.000006, '6535':0.000006, '2441':0.000006, '6550':0.000006, '2457':0.000006, '6554':0.000006, '2468':0.000006, '6570':0.000006, '2476':0.000006, '6572':0.000012, '2477':0.000006, '2478':0.000006, '2489':0.000006, '2491':0.000012, '2504':0.000006, '2505':0.000006, '2506':0.000006, '2510':0.000006, '2511':0.000006, '35279':0.000006, '2517':0.000006, '2531':0.000006, '2533':0.000006, '2538':0.000006, '2544':0.000006, '6647':0.000006, '6664':0.000006, '2573':0.000006, '2576':0.000006, '2585':0.000006, '2589':0.000006, '2591':0.000006, '2592':0.000006, '2608':0.000006, '2611':0.000012, '2636':0.000006, '2646':0.000012, '6743':0.000006, '2660':0.000006, '2667':0.000006, '2671':0.000006, '2675':0.000012, '2694':0.000006, '2700':0.000006, '2714':0.000012, '2725':0.000006, '10920':0.000006, '2731':0.000006, '2741':0.000006, '2742':0.000006, '10934':0.000006, '2746':0.000006, '2763':0.000006, '2784':0.000006, '2785':0.000006, '2800':0.000006, '2813':0.000006, '6919':0.000006, '2828':0.000006, '2836':0.000006, '2840':0.000006, '2847':0.000006, '2852':0.000006, '6957':0.000006, '2861':0.000006, '2867':0.000006, '7009':0.000006, '2942':0.000006, '2943':0.000006, '2951':0.000006, '2957':0.000006, '2958':0.000006, '2959':0.000006, '2968':0.000006, '2979':0.000006, '2981':0.000006, '2992':0.000006, '2996':0.000006, '3001':0.000006, '3002':0.000006, '11199':0.000006, '3017':0.000006, '3044':0.000006, '3048':0.000006, '3051':0.000006, '3057':0.000006, '3082':0.000006, '3097':0.000006, '3102':0.000006, '3103':0.000006, '3114':0.000006, '3121':0.000006, '3125':0.000006, '3136':0.000006, '3137':0.000006, '3145':0.000006, '3154':0.000006, '3155':0.000006, '3168':0.000006, '3190':0.000006, '3226':0.000006, '3237':0.000006, '3248':0.000006, '7348':0.000006, '3255':0.000006, '3262':0.000006, '3268':0.000006, '3293':0.000006, '7405':0.000006, '7410':0.000006, '3323':0.000006, '3329':0.000006, '3348':0.000006, '3368':0.000012, '3370':0.000006, '3386':0.000006, '3387':0.000006, '11602':0.000006, '3418':0.000006, '3421':0.000006, '3426':0.000006, '3437':0.000006, '3442':0.000006, '3466':0.000006, '3471':0.000006, '3473':0.000006, '3475':0.000006, '7603':0.000006, '7613':0.000006, '3536':0.000006, '3576':0.000006, '7676':0.000006, '3581':0.000006, '3590':0.000006, '3632':0.000006, '3635':0.000006, '3644':0.000006, '3664':0.000006, '7766':0.000006, '3680':0.000006, '3691':0.000006, '3697':0.000006, '3699':0.000006, '3704':0.000006, '3731':0.000006, '3732':0.000006, '3741':0.000006, '7855':0.000006, '3776':0.000006, '3777':0.000006, '3788':0.000006, '11990':0.000006, '7897':0.000006, '3810':0.000006, '3815':0.000006, '3827':0.000006, '7931':0.000006, '3850':0.000006, '3860':0.000006, '3905':0.000006, '3908':0.000006, '3917':0.000006, '3973':0.000006, '3975':0.000006, '4037':0.000006, '4058':0.000006, '4062':0.000006, '12265':0.000006, '8187':0.000006}

courses = list(data.keys())
values = list(data.values())


for i in range(0, len(courses)):
    courses[i] = int(courses[i])


fig = plt.figure(figsize=(40,13))

# creating the bar plot
plt.bar(courses, values, color='red',
        width=5.0)

plt.xticks([])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.title("Degree Distribution of LargeTwitch Network")
plt.show()