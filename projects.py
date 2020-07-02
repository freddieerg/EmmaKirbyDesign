class Project:
    def __init__(self, url, title, subtitle, description, thumbnail, images, plans):
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.thumbnail = 'img/projects/' + thumbnail
        self.images = images
        self.plans = plans


projects = []

projects.append(
    Project(url='winter-and-summer-barns-with-pool',
            title='Winter & Summer Barns With Pool',
            subtitle='Oxfordshire',
            description='Working closely with our clients we designed an area which incorporated a new build, '
                        'traditional oak framed summer barn, swimming pool and a renovated party barn. We '
                        'reconfigured the internal layout of existing barn to create a new kitchen, wine ‘cellar’ and '
                        'large double height room housing a bar, dining and seating areas on the ground floor and a '
                        'guest bedroom and shower room above. \n\nIt is the perfect place for cosy family film nights '
                        'thanks to a hidden screen or big parties with its long dining table, bar and state of the '
                        'art sound system. For the warmer months, we designed and built a beautiful building with the '
                        'help of master craftsmen using traditional methods of oak framing for the structure.\n\nThe '
                        'plant room, shower, changing rooms sit at one of the barn with an open summer kitchen, '
                        'bespoke bar with zinc worktop and 5 metre dining table take up the middle section and a '
                        'cosy, underfloor heated television room means younger children can relax when the sun goes '
                        'down after a full day swimming. Reclaimed clay tiles and wooden cladding help to give the '
                        'feel of age to the barn and metal doors to match the replacement doors we put into the party '
                        'barn unify both buildings.',
            thumbnail='winter-and-summer-barns-with-pool/thumbnail.jpeg',
            images=['psyDmPk6.jpg', 'y7k8dvwj.jpg', '-WHuAFgq.jpg', '1eJPZaS1.jpg', '46koBUpT.jpg', '4wRhxyLw.jpg', 'NgB8YejF.jpg', '-UHo4pAd.jpg', '5WFU54Oo.jpg', '5QhAMOdP.jpg', '7zSYs8PQ.jpg', 'eLWg40Q1.jpg', 'xfajmGyU.jpg', 'c8DQ7kLU.jpg', '_cpBQEvY.jpg', 'pGa9GPQw.jpg', 'Qfb4vJSe.jpg', '7h8CKY60.jpg', '0H67D2MP.jpg', 'dUd58Xe9.jpg', 'hoKgJFl4.jpg', 'pBdpjYpN.jpg', 'HPMtX8Ze.jpg', 'ltdBXa9g.jpg', 'A82xgnMn.jpg', 'XctjSj7O.jpg'],
            plans=[]))

projects.append(
    Project(url='soho-farmhouse',
            title='Soho Farmhouse',
            subtitle='Great Tew, Oxfordshire',
            description='Lying in 100 acres of rolling Oxfordshire countryside, Soho Farmhouse is a private members club just 90 minutes but a world away from London. It was such a pleasure to be part of this hugely exciting project and collaborate with the amazing Soho House team.',
            thumbnail='soho-farmhouse/thumbnail.jpeg',
            images=['uXlZjUMM.jpeg', '6seWC6EI.jpeg', 'kPcqLD1Y.jpeg', 'xwgPWcd1.jpeg', '2wmpVdUZ.jpeg', 'jN6x7don.jpeg', '1Sk3gCOZ.jpeg', 'qGQ3R9Qr.jpeg', 'CRJt219v.jpeg', 'M7x2J0NR.jpeg', 'BizpASHX.jpeg', '8TnvWXZU.jpeg', 'CM2DAZkL.jpeg', 'cZUVxI7k.jpeg', 'A3eZfqiG.jpeg', 'FVof2tuB.jpeg', 'gB8DGYeC.jpeg', 'L4p6a2MP.jpeg', 'QRNsiUjo.jpeg'],
            plans=[]))

projects.append(
    Project(url='village-house-interiors-pool-and-pool-house',
            title='Village House Interiors, Pool & Pool House',
            subtitle='Oxfordshire',
            description='The owners of this beautiful Georgian village house wanted us to redecorate the master and '
                        'guest bedrooms as well as put in a pool and build a pool house to replace a  rather unloved '
                        'walled vegetable garden.  New life has been breathed into the formerly neglected area which '
                        'is now used all summer long. On cooler evenings, meals can be eaten inside the pool house '
                        'which also has a kitchen and wood burning stove, shower and changing areas making it '
                        'completely self contained.',
            thumbnail='village-house-interiors-pool-and-pool-house/thumbnail.jpeg',
            images=['JASEW__k.jpeg', 'zGcHR2Km.jpeg', '7CYh0c5E.jpeg', 'hjtyCIv0.jpeg', 'm_RL2C3h.jpeg', 'SEuT65e1.jpeg', 'ByODXZfw.jpeg', 'wLLhGNoS.jpeg', 'u0xthdMZ.jpeg', '9q8Dzi09.jpeg', '01qY-irj.jpeg', 'A-6cU7NS.jpeg', 'BSVtuhAk.jpeg', 'ilU6hKWU.jpeg'],
            plans=[]))

projects.append(
    Project(url='listed-village-house-extension-and-pool',
            title='Listed Village House Extension & Pool',
            subtitle='Oxfordshire',
            description='Opening up a dark, small kitchen and utility room was the remit from the clients. We had '
                        'already, some years earlier, put built a pool into a walled rose garden. It was a beautiful '
                        'part of the property but the young family never used it and it felt like a waste of garden. '
                        'As it was enclosed on all four sides by barns and Cotswold walling, it seemed like the '
                        'perfect suntrap for the pool. We created a seating area around an outdoor fireplace when the '
                        'nights turn cooler.\n\nIt was lovely to be invited back to help with the house. The '
                        'redecoration of sitting room, master bedroom with dressing room and bathroom were first to '
                        'do followed by the extension design.  A new kitchen with a 4m long island and new Aga was '
                        'the main focus of the space but also allowed for a seating corner with fireplace, '
                        'breakfast area, pantry and boot room.',
            thumbnail='listed-village-house-extension-and-pool/thumbnail.jpg',
            images=['e44QqT7F.jpeg', 'xO9Am0K6.jpeg', '2zkYhVC4.jpeg', '4qFDkTVk.jpeg', 'z-QAOZ4B.jpeg', 'rbbqkM-X.jpeg', 'JNafUbQ7.jpeg', 'tXhGodKW.jpeg', 'd278kzzt.jpeg', 'Wr0K6W4W.jpeg', 'njYw2849.jpeg', 'dWz41ofh.jpeg', 'XmN7fcRq.jpeg', 'RWyadIJb.jpeg', 'd_6-Qv_M.jpeg'],
            plans=[]))

projects.append(
    Project(url='contemporary-london-duplex',
            title='Contemporary London Duplex',
            subtitle='Primrose Hill, London',
            description='A single, young professional bought a rundown duplex in Primrose Hill and wanted a light '
                        'filled, contemporary home. Take a look on our Instagram page for the before and after '
                        'photos.',
            thumbnail='contemporary-london-duplex/thumbnail.jpg',
            images=['yBoPaiMj.jpg', 'mpHZ-GB7.jpg', 'kJqLgZ7L.jpg', 'e74kNaVW.jpg', 'w3ZC50uC.jpg', 'nEe0LlEN.jpg', '3ksgnlmg.jpg', 't-6PyWy3.jpg', 'AvdLVkRS.jpg', 'X80fqLiX.jpg'],
            plans=[]))

projects.append(
    Project(url='new-build-village-house',
            title='New Build Village House',
            subtitle='Oxfordshire',
            description='A single, young professional bought a rundown duplex in Primrose Hill and wanted a light '
                        'filled, contemporary home. Take a look on our Instagram page for the before and after '
                        'photos.',
            thumbnail='new-build-village-house/thumbnail.jpg',
            images=['A-BIUJlM.jpeg', 'UBSYThMa.jpeg', 'bzUM4YwF.jpeg', 'XmATc-cz.jpeg', '6Eqrsszf.jpeg', '8dsOWuxc.jpeg', 'RneVK1V3.jpeg', 'OgPPr7WW.jpeg', 'evYc6YZZ.jpeg', '9MDreQfs.jpeg'],
            plans=[]))
