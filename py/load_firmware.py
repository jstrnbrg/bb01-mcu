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
    print('\nHashed firmware', binascii.hexlify(Hash((data))))


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
