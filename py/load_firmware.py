#!/usr/bin/env python

# Load firmware onto the Digital Bitbox.
#
# The Digital Bitbox must be in bootloader mode to use this script:
#   1- Unlock the bootloader using send_command.py to send '{"bootloader":"unlock"}'
#   2- Hold the touch button 3 seconds to permit unlocking.
#   3- Replug the device, and briefly touch the touch button within 3 seconds.
#      The LED will flash a few times quickly when entering bootloader mode.
#
# Firmware signatures are valid for deterministically built firware releases (refer to the github readme for building).
# Invalid firmware cannot be run.
#
# After loading new firmware, re-lock the bootloader using send_command.py to send '{"bootloader":"lock"}'


import sys
import binascii
from dbb_utils import *


if len(sys.argv) is not 3:
    print('\n\nUsage:\n\tpython load_firmware.py firmware_name.bin firmware_version\n\n')
    sys.exit()
else:
    fn = sys.argv[1]
    version = sys.argv[2]


# Private key signatures (order is important)
if 'signed' in fn:
    print('\n\nPlease load the unsigned firmware binfile. Signatures are added within this script.\n\n')
    sys.exit()
elif '2.0.0' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '302731115cafd4eb0d25747e604fe2a45f541c5e238dd5e946a34d608be104575b781b06f6b629e9debdfa1fe9cd27615fb0613bd90ccc527f5c9b838459c36e'
        '20b6aa64e7f1dfce652cf69966abdda71a76560011159620d6704036ee96705e019e5bc8de2ddfa1656879744611b6909568f07deec7cfc6b6a967431b9ce81a'
        'f82b0f23ebf8cfec971150580343327801a6a4f4a30473929ff681e9791f79bb5d645157378acdeaa1fdce6f3fea418829a04a2c6c5a4c27b3707b77a134f5d2'
        '4c9b22dbc81d5765b6d9bc008777dae96df90162b54b7802699f4d197d8eb28c27323bcf218b0f2437f9fdd1e1f06ccfabca6a26605115c131fb5bbd9195a11e'
        )
elif '2.1.1' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '713b243546825f155bc6527d27dd53331c963def45249fcce07079b13b95264f43889ac3a895621925d0a014fea9dc06fac25472c679ace3604a22e9b8a0bbd7'
        'e47e909617f401064b579665961e0535c9618ea525e0dd325623834e451e1bb63eec6fd7ea3d259d42ca776bac992d86933e89b589c04322d253a18080122c9f'
        '5d080a6cbbdceed080c13721bdd093eb3ad60881abf8b03146e28086e8f9b40f0a3921f0796079f196527cc037fe7451a426815f9c85043e0776e85975492b3a'
        'ca225002e2cf45d5580187d6564ab4f664a480867fa6f767a999c065a829e3c5599f21c06a26b473f9b303e2aca245ea899f67b7b156935b384ccfabc1069669'
        )
elif '2.2.2' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        'ab62cdc84efe891dac91f5632fcfe57115cf4fc6769f0a1cddb5268294dac38371207c616d7ac123bb075d042c8e0ee3f2e036ac200348156baf831ad5d2d1af'
        'f7d757c994a1c422fd4cb7adf589360231979dd1f1bb5dcd3fa28bc80eeb66882c7977df66d4f97e7761094f3f6f9748cd6f2c77eb22799212d154d2307031db'
        '170a6d1e5d511aa07d588d72e18481d3286dc583b12f2d22a7a35ee4a5d955d66f1aa76979305ff8ed002744a851159436e87645e3b021dd69231b9f57a033bf'
        'd293e93c78128fd6a4996961c34273c044cb120dd1c9a50d6b1db01577fd2a7a2644ec2ddb9e96f814082b5abc193da0e43c23e61eed6baa631a7f6ff67d3b77'
        )
elif '2.2.3' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        'a62edd2d91e565c4c3aeaace17943c097938ae7b30f8338b8937239dae55d6ba33b8dbc29a17d444bbccc6ca7a00cb717387a7bcb7688aaa0ad69d8ede143555'
        'ece868577966cad79be858908db5a5f2e780ae0d5b0f6d197a677fc9a66e70a075c948ba11562533407c4f66401bb03454df99349569f13ba534fb2877b1a671'
        '45c3964e3e720c9e78388ba8555275377448b564c55a3689cc0f0312be362e25273dc7f96f491a910707185718ceb3372ada9924eba8ced8fb42ab6f7ba416c1'
        '5aacc1ab96f4bf67bd423c855686fd8385ac874bcc2195c8d3df36a43b3dc7ab7d5ae5d938d4b275e308642c9e1d083e9d0ceeec9915c823073a766e0fde996b'
        )
elif '3.0.0' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '82bab51c67dbb4ac5ee46686cc10b485aa0868cf577c6a58e9706a156f9e0a5e0fb0032af50ae8b60a5a9e90c0814c0ab05a643ac28eb068524e1ad18683a395'
        'b12cd81632caf0e1a5dd51bd33172f11ef8fe14fa17c49c4a60146225fea629922509e23fafe53b3dcf4b8865a7b87187b557bbdb2aea3eef77ca8ec3e9b4658'
        '2fb4e401896eb81e53a7d8e659c118f721e8e4fd127b3243b135054e1111ad067d088c028517cc8515d8c43c44dd8865288eb04f1756021233e42ac99462daa2'
        '8f4a6af6123f33b222212eed67c21904e947c8967b72cf2a6ec77a69bebae93e5d145065fac7bd1d53929ffeb0275a5e7df1b856c02b0f58e8d2f594d2be5b3e'
        )
elif '4.0.0' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '0104628d9c67537a8ef79bff375afacf78c35fad647a090f05d45811e23c4a96539a9f9b3ca465f5af9e6691e518d816fa8e73c67896625be68de2621d22b5e8'
        '091d6e389ed384bcaf5d7ba16a8af1a34bd48084b911a5685f41ff3340cb11616cc1d06f8c558fac31c38afb95f1c30e42bd9da204002ba757b9d97263301676'
        '0f06409c24dc497d60524bb1275394de5df57981b485622d341e209d99b3e13854b21d7459abd0e3872011765b53e211069bc6b0438e18a4bed774ca2ac82048'
        '9dc82dae4bb7e6093e888e4dcdfebee068af79f255c5d78b9eb1118a752491740023aea8924944f213fb5733a62a82d8d5a2706ea163cecf83df8aac0711cdf1'
        )
elif '4.0.1' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        'f89c9481d32e49e3dd3770d881d711e048964657e1532efba759fbfd067ef60f39568e8411766d47932d87da2c9ce33e53eabcc4b1ddd230506658084ba5544a'
        '0416cf3aad238a30d94ce4884ac9e3e350f807402f6b6dd204e8ba5a8cad5d0179e6c7f1503d665c3be41dcc437eb68dd0d956f11f5c6d5ff4d45892b0f7179a'
        'fb22728ed783fef1cac48e5ebd1160a503baec0076adf963088717d48ba0d31a7f01445382196f66b71ee08e2c504a4e7d7a7972464aa3c27eb61668303ff643'
        '2d4983c0628424a63f9aa37acaf1faedb1b3ca69dd176161115ba6caf18b96c417322c4509325ff2d0945bcb95233db8da35804eb4f80fbfa20588d85b205794'
        )
elif '5.0.0' in version:
   sig = (
       '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
       '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
       '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
       'fb8f3f271869872b9fd7ee7985cb65434f8c2b24e0cc95b23d2e35ac94b10f44394889d44398498586f18a09ecb6ec1a0bd2c760a1e14288151cc0f96cbb99b2'
       '44acefdafb734091f9ea4bda8165cc9aac2c9ceb0e5cd33b8b1d0761c980dedd4e02a88510ab1eb6ace128dc32f64c926118289e4b1a54f62b55ef1b754a201c'
       '6ca3f4264c85db8b2f8f24ecf38efee60ad4117e5a293fc01adf7f1c445d896323fb9ecd386074b0bcbd9d120c88f09f3c801adcba9171a5553e68e5deb8e1cb'
       '8774a39d8d9ba34c1f47209f869bd9ea7806f3b584e5fcbc5531fc6a31b2b79c519d9c1b14b07db72d390a633dc4e55494b13e66be49c09cf2032aff7a6a5f7f'
       )
elif '6.0.0' in version:
   sig = (
       '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
       '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
       '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
       '76edbb3aec7bb595d93114cefb9062808790e631ccf7727a434c5865c71199fc0b6680a1cb6de8eb747d122a6232de475a2c6034cb11121e28a4de4987c9789f'
       '5608619e65c633ab6dac32c5fd4365591afbbd3890be66940b428f183e4fa4d56a81a18599ddc305c2285bf054283e57aa96bb2bf927c74dea41a39d0af20dff'
       '9678367ce39d3acec4d2d1de6518ab85bf06870d027e0501e292f6bc759dd2bc60b564f3d8ad5e3768fb23f3cef2ca839781f50781e42aa47fcd969eb79201d5'
       '95d75b7b6820317b33e007b46ded2984638d7321bcfe230b581cb638bc38592e6391b1ceeb2cddaa4ed5cfe19cd50c87031ad0f7cb93e9c375501730f15986ad'
       )
elif '6.0.1' in version:
  sig = (
      '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
      '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
      '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
      'a31ce24e6b9127a09b10d6869139f6a5846d1b93cdb3855907534d2f701eb19d306fb3a99519148ef8a6b2bf5e6f588b11753b6ad1ff6f29a48cc7ee470ebfe3'
      '8271ecedc4a7968be0d935f68a54e4e85cb1792193033039114c541c4d8ea83c3e0419e2b9aac90376a803074f362673845716824da4d52694a87aa364560afc'
      '28417cbfaecbbe6f3329d89192348cbb4674d15c8457944f675ea85df13d40f44630ec92629b7a422d0b152fe8dd028932a1cf389d7d108becb60af3504605e9'
      '11dcc79225db4be8bf8e3fae2689665c52151fefa3be183e6945d87e104c9e4d74a732e55f6705c5b9448689c571f66d015149445acaf54ddc3a96cf360bfcd6'
      )
elif '6.0.2' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        'f32c81811d9fcee78b011a74d29d96068afd6366ef79f6599054e0ba46f3d5517b8ad38c34d0117bfb137cc29b3b390555b8c0eaa13c8ff18ec8d82dd07c3e1d'
        'b53c45cc28c03f6e678e5ee68c533cdea1dcd66193578f03310c86f85a6a1d87541a9d430df36351d253a1c8eae6017ccff535ee678a5806b2c55534ca59eec5'
        'dd3a96de0e274da0431e98c0a40968c61be64eb5af7c8a73cefdc5b321e771f54a7d1cd7b20c68e16c087a31aaf703c398e761b92f619bceab7e8a49c4368edd'
        '41a0e5d3a09d79f83cb17c00faf06425f1f230a30379951f3bd96aac0740b93e188819a388f46c629a60d52f1721be35a7f7bff55a4a1b476f6d5a11029ab10f'
      )
elif '6.0.3' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '5932861985f702f1103173ae772ae9aed4db74a23ca9ba590827856466fd89c300ff0b910b3badfd7ffb46f4a84375f81cc8632d3496e7b8950fb907c40969fe'
        'dd0539315a7e3aa7743142d95aa4ae2c3dfa477aba40f8f53d724f25083ebc126a807d13e4eb6332184bc775a368f4d46aebc21d781cc7e697b1b3cf76f3b03e'
        'b7c2108d404de7b40c30d772cd668f361a8174369e5c33add1dfebd3e1bc222f296d1dda936ac6b4ff6e66d48e0d8df58bc99f5119079b5008a41e63203df6d2'
        'af85433087dbb3501aa7148bc9ee8209943070ab110d99512a843c2df753ffda45c4e0a40609d252d8cc53e56f866faf4895067d45f39ca4f91ab6559a1c02c7'
        )
elif '6.0.4' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '94a319fa4e208a3703615ab1a1d5b91c0c60fa06ce11cf1f3b95715231ce05c266fb7b92ffda64e7781152048ba5f24350eb886d2bb2ad203aa268584e531a9b'
        'a8f80f6d85a8d2f88d552a6543949f949eccd360449b0a81f8065c38a3aa163d67c6254078114f85d910062fc8e51c20e461a1c4219c6911dfb2d5242b39c739'
        '30f12c64b516380ab1adaceb4f3f4008b003ce6c3d0f51cfe4509990b568c9c5252748099a95d0b2127ccb7b3c92c9b19fc32a26df100761fe0aacb52233afb7'
        '34f59a71d7d46c22439700804cf02898f7e9c592f8c3c3c533da234e04201be2112dd33c0574eb1befeda3ea70d6a5c4690bcbc7ea02a38fd67427f8ceab1d4f'
        )
elif '6.1.0' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '50c1a2b8ca106dbab2acd4eec2193af35dbd1890af199b2dba091eb1ce65c96a3d0058e104626f1a060bb59c00c74699b3656e2885557d2baec8bb17967b25ec'
        'c514ed71d60486469e0b47afe93aafbc6f0b91818e98baa770692a3897be56f36eb82ea139e263bac8760192d97a39d3b48f61ac00c02d36f96d0aedb6168c85'
        '77da95464c5647fd8f88a4a37400959f7bfce19dcf288efb1ea2396b84499b7b1e43fb184ba3df3e41a3e1433bf563b8e3a7b6fc825b81695399351ea3e3ee66'
        '97b7b7861e929237c638690edc363ed8db1c85831e15114aaf1f103b97af7e3061fb85503f50104f3d36489e5e0b8b0313d750c114bd2eb80df9a3a0d02e12cc'
        )
elif '6.1.1' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '1e2e802701edf7b0ccc0e9e50e3d6afbbca9325df46005bd815d30dc7a9cd2607221cf0f93b76b81506a7cf5d79d35d4c67db84b52cb19a379dd83aa07f482d5'
        '7abdfbb497d9f23aa00b3c186fea27c1d791909d1937ce42e5dd5c4abcf62af863ce9e2b4fac914e5b4f96642631c7adae2bcfce53a0aab894ebf5496010968a'
        '29b381102cab0cb104dd57353630c1d0544808d15d3bf5810a7619ead8a00548294308fb63abbca048439fb9df2de412696544d940fafec819fc176b73beff73'
        '1b8c4505b246469cfa083e18c8fc039b203d8b97927658676058e57757a4ca750cbb442f30964f5ab1372b1a577d311707376e43325e117a4eedcbe85d0048c6'
        )
elif '7.0.0' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '80aa3c367bab0266aa6770d1b1d6980e30c0fd18e07258dab7af60676045a5e13bd4679cf9cd6831286811f7d2173e62c7f5f37419d9cdf87013520aec4ec642'
        '8ce42a69f03ea71af4f07841d5f9d417630d90ac9e5112a7f45f23801389e5812cc3dfb037e9866481ccceb203c2143a2e85286a9db1c4e5822d1b5b7d461495'
        '91cec9da81c9b45e03ddb9813c0d3c4e229fc0d12cbca42c00a29914021c62544e917cf979bbac5bb5fac310fb4f0165599d32d004ef5d26795566c2f12fae0c'
        'bf3b1e65840b842887bac9d7d48a3787eb32af1532bb16dd5d92357d0ea5ef374b2c68328f27ecee95b2b0bb34ed9bb9705761b36cfe93a550b8543260a2dd5c'
        )
elif '7.0.1' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        'e34772e2462db37425712aadb3d9d1059ec3a55375fe1d1a37e20d0069dc7b1765b1ca52da3c230f5c2a4325a7fa14c1f9ec55ebd364ba86443c2b7a13b74596'
        '7c3d40d7dec84451866c829cff10a10401ecaa4e9a4d33ffa5425a099bd9df2355059b962a0beeec667bada36de2484b42f98b86fbd507f392405217f5941c3f'
        '134eb617521a203b21a4495c06006c07cbdad2681f10169b6bee66e37cf798a801095c19918cbcc0403d626e47b1936286fa8566c4923da4933a1e035a8a9d23'
        'f3b26d44eee48de2d9e99fcdcd158fe33ac6a484e65267ac5e025369115828e724f8e30e784e2b7d5eaf60094e931e9a3c410d0890f280240c069d55e59776e6'
        )
elif '7.0.3' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        'f82d494b09415bde6426f154bbf28e0c13cdb07d3daad39d7954e677201696a47ca2a962915179ea059c56ceaf1523ed79ca3c90fce5ddee797c72fad023bb91'
        '51801755415b60d353d2e2e8711fa68f94f3840bb0b33791593f87238795075c36861763e03eb5e5ad3dae3c18386325d38cba9286b5104779daad99eb5628b0'
        'bffdbb174cfb15e20f3f730f32faf3132c22fd0ea99ffd2c534e2a7e8aa87c1c06b53f9fe419f022a77d17a9d4137dac071284bcc27d3c760d774ce97f1a285c'
        '25e5b0e14728b0617ae6a268c0a003663aa7c3adf583ee019af26953aea649f224d08f4043e4f8d7f799fda586c2ff5fa732663b0388ef6571124603b787b426'
        )
elif '7.0.4' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        'ff41ee436366c2dafd056dd61cc04d9e21c51303ac87851cc972637aa5668f195d56b4faff404e5d1d2d1bf0ee51c1cc4c19f74456e41869b01f317c33592e80'
        '979e20029fb848bd201fd849bd35c80fd3d4351b2eb4a525639e3a2123689cad1b9c681bd06db95717137b7778fa86b3c3d376028bfdb70fe2778dd12a42233b'
        '122f5ee27e9c3ca7cdf890969d9b3e8501674931b30f92a54dd1e05d37ffe3403771fc83855b9983273e17610d0804abf64a292160e32ba6940542e4618645e7'
        '2a03863b997fa79f890aa5e4ba6a75b3b5c7570fb37f9b27afa2f4df831deeb52a3176c5badf335aac8809ceb8427a01558e061860fe5892c7219697655b913f'
        )
elif '7.1.0' in version:
  sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '79ab2031396658f7604516646fb697501aa9486d2413555089fc9b41f51684362c7309daeaa045da90e7286316b78354cc9455c84903cfe49f704cf0726080be'
        '72371c5bfeef998ec5fd013b5a5f46bbad7e293fbb2a42c5f3beb0b07f0a67c839ef3fa80bab8464b02933dfe453ed12228a34ef82a7debe27673abe77d796e4'
        'f935e1384a2bfe963e827e76fa3c91e0f837b8c49587fee248766038bb3c9d1f1e816d3dd0d3c0a9528e617dfa970aa0ffda83e76e98c7b694ed64f0fbd0b5ba'
        'dbf5472cb263f632e5026de17a49a1401862b2f4602d4ad685657bfb0d119a434f0d86e8e904899a39154db67f77af264434382f7eddedea5f3eac5b0309a8cb'
        )
elif 'debug' in version:
    sig = (
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        )
else:
    print('\n\nError: invalid firmware version ({}). Use the form \'vX.X.X\'\n\n'.format(version))
    sys.exit()


def printFirmwareHash(filename):
    with open(filename, "rb") as f:
        data = bytearray()
        while True:
            d = f.read(chunksize)
            if len(d) == 0:
                break
            data = data + bytearray(d)
    data = data + b'\xFF' * (applen - len(data))
    print('\nHashed firmware', binascii.hexlify(double_hash((data))))


# ----------------------------------------------------------------------------------
try:
    openHid()

    printFirmwareHash(fn)

    sendPlainBoot("b") # blink led
    sendPlainBoot("v") # bootloader version
    sendPlainBoot("e") # erase existing firmware (required)
    sendBin(fn)        # send new firmware

    # upload sigs and verify new firmware
    load_result = sendPlainBoot("s" + "0" + sig)
    if load_result[1] == 'V':
        latest_version, = struct.unpack('>I', binascii.unhexlify(load_result[2+64:][:8]))
        app_version, = struct.unpack('>I', binascii.unhexlify(load_result[2+64+8:][:8]))
        print('ERROR: firmware downgrade not allowed. Got version %d, but must be equal or higher to %d' % (app_version, latest_version))
    elif load_result[1] != '0':
        print('ERROR: invalid firmware signature\n\n')
    else:
        print('SUCCESS: valid firmware signature\n\n')

    sendPlainBoot("b") # blink led

except IOError as ex:
    print(ex)
except (KeyboardInterrupt, SystemExit):
    print('Exiting code')
