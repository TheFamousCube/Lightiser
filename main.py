import python_artnet as Artnet

artNet = Artnet.Artnet(BINDIP='192.168.66.106', UNILENGTH=1)

while True:
    try:
        artNetPacket = artNet.readBuffer()[0]
        dmxPacket = artNetPacket.data
        if dmxPacket is not None:
            print(dmxPacket[1])
    except KeyboardInterrupt: break

artNet.close()