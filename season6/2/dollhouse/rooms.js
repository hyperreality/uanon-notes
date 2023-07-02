/*********
 * ROOMS *
 *********/

const Levels = {
  level1: [
    {
      title: "ROOM 0",
      text: "734d3ee1c99c1e8d5f254091ee9182a7a3e45061999d29329910601c6a8ef3ef",
      level: 1,
      options: ["S"],
      paths: {
        "S": 1
      },
      size: {
        w: 5,
        l: 5
      },
      objects: ["WALLS", "GROUND", "SOUTH DOOR"],
      tiles: "f28af6aec3211a1395df905dbfca2d0d56241b1907f8c5d838609fd3ac116164",
      doors: ["7659ecce3626e8ba076db778dcfee78ec61e15c2e7233fe8b7b549fb70aefe9e"],
      chests: "6e9f9344d2b9c4f9a603169d43a43208320c807575cacbaebeb91504eb11d08c"
    },
    {
      title: "ROOM 1",
      text: "f6dfc106ca7bba9aaa0a9f4e30aaf42bb4aff0585a704875a54a3fadcc126bb9",
      level: 1,
      options: ["N","E"],
      paths: {
        "N": 0,
        "E": 2
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "NORTH DOOR", "EAST DOOR"],
      tiles: "47661cb929d39c59d9b007d23147c7409157e7a00174acb707c66f73bb30c9f1",
      doors: [
        "96bf5a7887fb67460c6fe44058f4c800ebbb6447f58826b3a0a621ead3225711", 
        "c9e5a0f63c5573d0a3da978afb7f15bf9e01ec9a190d2030055533115d3970d6"
      ]
    },
    {
      title: "ROOM TWO",
      text: "4fdeedee93e0f306744f8d6b27487bac50ccb2897902b2eb5d5263819d24c710",
      level: 1,
      options: ["W","N"],
      paths: {
        "W": 1,
        "N": 3
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR"],
      tiles: "e834361907abc09a4271e3e85102fa51b4c41fd137439d1f4ea3a460b4a50bfc",
      doors: [
        "0bdf79272c01db3432640b3841b0cc268e458521c65e46f3e4ce29cad777abaa",
        "346eca8873fd9375a33c8f47e549b9a780945eb7b14fb0e3781261407a2322dc"
      ],
      keys: "1ded532de28702c0bf7a979e2c46fdc72c333b8874bb4c76a3a44a4affb16aae"
    }
  ],

  level2: [
    {
      title: "ROOM THREE",
      text: "3cce430008bc944c9bdcabbe5db67cf5bb02656446fbdc0db3282e0d6b87a5c4",
      level: 2,
      options: ["S","E"],
      paths: {
        "S": 2,
        "E": 4
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "SOUTH DOOR", "EAST DOOR"],
      tiles: "717769a65a447faff1b0aeea258c20ca84151bdd2ad09c6d73ba8fece4689412",
      doors: [
        "0x1b4f258e87bf501e3c50d947ba059e3be905663ae12c2d4eb28519ada88f79fe",
        "fb20aa46f9acd024556ff7db3bca0aafb15601b130a27a562cd3f08bc3033491"
      ]
    },
    {
      title: "ROOM 4",
      text: "7203607d9c28987983a906602f61e07e6b77fc0af0b2296bffe9f039db4a469c",
      level: 2,
      options: ["W","S"],
      paths: {
        "W": 3,
        "S": 5
      },
      size: {
        w: 4,
        l: 4
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "SOUTH DOOR"],
      tiles: "49711f0f8c2e213389e72549e4ec5560fd475d13b56d9fb828cd369f925b24c2",
      doors: [
        "bd3f011a1fedac7e3f69fc3d52957d449c4df15ab7d05e4a2c58522d7b7ff4a5",
        "ea0ab58cf5edf86a79434ba04061a1b1f9c416a121bbe88fa667e88bdfa40a97"
      ]
    },
    {
      title: "ROOM FIVE",
      text: "67741a18e6cce4e052e7aa200e9a4a751037a3f184ec99e51b34e19a18938d5d",
      level: 2,
      options: ["N","E"],
      paths: {
        "N": 4,
        "E": 6
      },
      size: {
        w: 5,
        l: 5
      },
      objects: ["WALLS", "GROUND", "NORTH DOOR", "EAST DOOR"],
      tiles: "ca65f2b5592d7c9b4c9cb38fb5766746fed4e6b68a3358b623d3a4d7f2264c67",
      doors: [
        "811cda60e1204bcbce44736ca67eee99a3ef0fd60ff0e2ccbedef5e94986e4fa",
        "3f6510c3c36f1f636afb42b5aad5a8204742d16f68433cb4f030da97a61a4577"
      ]
    },
    {
      title: "ROOM SIX",
      text: "7f674e1c74cf62a1d5cfb70cc27f29abfe0b4459e069028bcbf2cea80f2aaee8",
      level: 2,
      options: ["W","N"],
      paths: {
        "W": 5,
        "N": 7
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR"],
      tiles: "fad7e53cabec94b55fe3d20118012162915a493f783bd4d7e7d6162e28002068",
      doors: [
        "6c9b64a654dc67140ffcf5a5780998fa454aac1f7231cdebab454f25dca4eacf",
        "c05ed0afc94a35303c17b08adae223f9ef4d9c288c156a13e75716e0281703a6"
      ],
      keys: "31518cbbe3308a643e96e39fee169103b855a4c1cc711ea17486782256c56cf0"
    }
  ],

  level3: [
    {
      title: "ROOM SEVEN",
      text: "e1c91b1ae476978afdf23c1b3212d66a7f428c8761404d5fd7d0a59cbf3e3768",
      level: 3,
      options: ["S","N","E"],
      paths: {
        "S": 6,
        "N": 8,
        "E": 10
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "SOUTH DOOR", "NORTH DOOR", "EAST DOOR"],
      tiles: "92bd5f84b7a763bde33f49e54cbdbf3e87bc3cd4ee883e23c2e5107e18230978",
      doors: [
        "2d889408bcd6325392922f3728e301b0299cf3148ed1e80cbb6ddd65560becc5",
        "5ddf571e01e94909b8db5024f3e23b4082add484020178b2071c0c75641bd6df",
        "8ae7f3f439e343ee9fd8fbf894618cadd606559321056b3b270d8b14c7222da1"
      ]
    },
    {
      title: "ROOM TEN",
      text: "592571bcfd4027e31f632a11dd2dbc209fb59f717eee6225b079b3f83ee95558",
      level: 3,
      options: ["W","N","E"],
      paths: {
        "W": 7,
        "N": 9,
        "E": 11
      },
      size: {
        w: 4,
        l: 4
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR", "EAST DOOR"],
      tiles: "8f5ff0724d89c87a57f9ae151ba22a3b09240cbfab2a923b5b1ab9f692604dff",
      doors: [
        "db3fc82b30dffd33fea9170e7ded372eb4c93d93deb7ae5b4bbc650db4bd7a35",
        "d9494d774c3cb1bef1fc59adf1a165ea5ba85f175b0fbfb6317df1447970d437",
        "abfc020e5bc29e3b3ad05f1eea0bf1a5cc87540dc83c79d22ca924e7289b7b19"
      ]
    },
    {
      title: "ROOM ELEVEN",
      text: "3f890b352e439b925c6cb965c8924ddd22b39c1c8f1ab7b025312e4f0e27ccf4",
      level: 3,
      options: ["W","N","S","E"],
      paths: {
        "W": 10,
        "N": 13,
        "S": 12,
        "E": 15
      },
      size: {
        w: 9,
        l: 9
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR", "SOUTH DOOR", "EAST DOOR"],
      tiles: "be58fecb95b9dd3dbec8f7ff62e0f7f8fd6a6bb9ed8eb39be8aeb7cee64d29e0",
      doors: [
        "e102a49cfaa3d35c204187b2908243bc9960268cbb270573d104e1b1f225a985",
        "abe4abc2a83f3f518f8490a18e7e5a715a2bec11809a8e64a123a65702768fec",
        "36634a32358c02330ee430ea6d54d1dff11e1bf0e7bfd25e06f7b92d287882d4",
        "68b0e5de35a82fa6fc84683fb588a6c529e8164ccbae58cfb40e5a327db00bbe"
      ],
      keys: "d1f48a4255c77f557ac7aa2b7ff4048d9ec4e0dea9609bbd990f67cd84e9cb2e"
    },
    {
      title: "ROOM TWELVE",
      text: "f497400c94b33ba5cdfb6d05f268e1e455d0d8a05209b43cd476a71862980c3e",
      level: 3,
      options: ["N"],
      paths: {
        "N": 11
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "NORTH DOOR"],
      tiles: "e976385971cb8d1456f90c63f1f48d5d4b25bf922e85e0ea0d39d7d2251407a8",
      doors: ["4d8bf39980e356c4fb7d728967ab70f1924764266f979b9692fd5474e76829e3"],
      chests: "d74c962748b5af0c2001c15ca51aea16641ffc2a6e281f546e7b7494840b0861"
    },
    {
      title: "ROOM FIFTEEN",
      text: "781462bbed548209273574385ce2d0ce51849319256f619d360455447c229bfd",
      level: 3,
      options: ["W","N","E"],
      paths: {
        "W": 11,
        "N": 14,
        "E": 16
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR", "EAST DOOR"],
      tiles: "7e7cedfb54ef7c259ccdce5383d69adc2773b10ae0b7d7572d854c77cc30f563",
      doors: [
        "142ab03d204f9f1658940920bb4da216021808568e6a8ecf00dbaf5a3ed0e463",
        "46ec3154b77621b5793139a49b9ef7a409986d206a0af6c0b1ff22d5a34e86e1",
        "7600308629375cd3ec2086ad4d91c836e4c9defef58809e620f11b49e3dffd6d"
      ]
    }
  ],

  level4: [
    {
      title: "ROOM EIGHT",
      text: "bf5ced32555c0b59da1fe86afa8ce7b59d3fc8cdcbb720d4b424f2c74436dc4a",
      level: 4,
      options: ["S","E"],
      paths: {
        "S": 7,
        "E": 9
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "SOUTH DOOR", "EAST DOOR"],
      tiles: "2b7129711667f98189c333f1beed8084d47f48536c79030545904a8a4fe90347",
      doors: [
        "ec5237a5053bc72d1338f063f83dcca1a1d801e4ad4584ad155ee357be9e47f3",
        "41a49b432ae8af3ccafa36d64aab94184ed2ff3582b19a78c1baf0141fddec52"
      ],
      keys: "f322af7f7e207246736274cc193f5bf0c1a6be8fb944a45b5b5d733bde447aab"
    },
    {
      title: "ROOM NINE",
      text: "587f7b3964b1175334c3c66d4e9578ef9163016603142392372caeea0afea57a",
      level: 4,
      options: ["W","S","E"],
      paths: {
        "W": 8,
        "S": 10,
        "E": 13
      },
      size: {
        w: 7,
        l: 7
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "SOUTH DOOR", "EAST DOOR"],
      tiles: "26c6e6ea520c2b545244e989c44aa44ad6de9d6c4012a50fab9d142a6392d4bc",
      doors: [
        "d0d35a1f012c57eff0355ffc7c5a825b4a1a2734684e90b85a8e0504e7d1377b",
        "90639508a57ff4dd2998382c1d12bb53d89124dfa61b6aa1ad44181affaf02db",
        "41a974b4e6d04b0f52f0e7b63a69bcc4aaaed1292731d6dc985b5dab3e61179f"
      ]
    },
    {
      title: "ROOM THIRTEEN",
      text: "5e5885bcc0e72b1d95ab4cffd152c8e8c6e2c6487229f2fd483efce20ec8909c",
      level: 4,
      options: ["W","S","E"],
      paths: {
        "W": 9,
        "S": 11,
        "E": 14
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "SOUTH DOOR", "EAST DOOR"],
      tiles: "e6c4646e948d72b34aed4ba36fa3ec6353781f40b5ab1de3c3b54d93b7cca137",
      doors: [
        "11a4de0114da117ca263e3a97a0f7160066541aeef60b6478df78344ba7f54a4",
        "501117849500318f1070847f1a83f230f3e831b9ea639bebb6a04569ec600cf9",
        "fdcaed46ced9b1388de4e56e3a6a1bbaa622e732c6d03e271c1ab797e00cd224"
      ]
    },
    {
      title: "ROOM FOURTEEN",
      text: "495c85ea3fa7cd14a68187a46c5213a49c8d1d6e7cd4209f5200f697b21ef3bc",
      level: 4,
      options: ["W","S"],
      paths: {
        "W": 13,
        "S": 15
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "SOUTH DOOR"],
      tiles: "31e889869af344afa4fe72f6f1f81420dfb5bda9fcd65bab11f59495c82aabe9",
      doors: [
        "047b5cea561486ee8411842a6255a7cc28bddf926c14222dac512fc71adbdfe7",
        "a95e56556a00dbd907c34d52cbe909fa12574e9261a9b98feb20dcd0a42ddcc2"
      ]
    }
  ],

  level5: [
    {
      title: "ROOM SIXTEEN",
      text: "d63bf86c6961425c45e80a7cf6f05135d1753b8d35110931f4a1e1241e854780",
      level: 5,
      options: ["W","N","S"],
      paths: {
        "W": 15,
        "N": 17,
        "S": 18
      },
      size: {
        w: 4,
        l: 4
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR", "SOUTH DOOR"],
      tiles: "416014a3a7bb086467e9f033ddec58520717c8182b4495036a062501f87f6920",
      doors: [
        "f37852686bca32ee67379af67d692d6ec001b50a85e0906fe19ee5a5757a4b01",
        "83c5da5232ad960b80e180faf0e98551427710c54e62d5e988b646798aa948b2",
        "a8d0f03ece1a441e391a1af06cf189e138249ffb06a3740c482a0e21f69c7869"
      ],
      keys: "19c8b0fc383e227cac730c32c08c8ce1cfbb5615a99f9ed6e0f15ddc6e9404ca"
    },
    {
      title: "ROOM SEVENTEEN",
      text: "ac16d16acdd02b1054b71613212eca3a906ede51e4d26d716ad522a74029008b",
      level: 5,
      options: ["S"],
      paths: {
        "S": 16
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "SOUTH DOOR"],
      tiles: "71ca8fe844e6c944502a89c74d58f2b220df0253fb0849bb347da25e0164b9f1",
      doors: ["bcbd9ff05b52e6aa9de3dced0b7e3e091c77dc7d840ef66883dd7a4c14c9d819"],
      chests: "767ef159fceb5a5e0efcdc42348b7171890ec2c0b33bc0b0ec6c5cadb874e30c"
    },
    {
      title: "ROOM EIGHTEEN",
      text: "9964f3a9ce96e4fefa6cece34a459a1f5e446163f081164e17f1813abb0c2f82",
      level: 5,
      options: ["N","E"],
      paths: {
        "N": 16,
        "E": 19
      },
      size: {
        w: 5,
        l: 5
      },
      objects: ["WALLS", "GROUND", "NORTH DOOR", "EAST DOOR"],
      tiles: "6cad792f4edb16558365158919ec47bb65b1c122c0cd82876cd214c120061415",
      doors: [
        "48dbcada9b3347866c6689cc6ccde565fa03e3a2ebf2896477fa98646af63435",
        "add0a6fcf2a6a0160e93a379bb325e42927949be68ef0a279129ef8570f271bc"
      ]
    }
  ],

  level6: [
    {
      title: "ROOM NINETEEN",
      text: "e70b0377a56e75c7020aceae7df511360fc0c86e68587f76d644c6291061fa44",
      level: 6,
      options: ["W","N","E"],
      paths: {
        "W": 18,
        "N": 20,
        "E": 22
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR", "EAST DOOR"],
      tiles: "b44c845a43c4735d3042d70e42aa27dd848c0eafefe3e91706b2e35f011ba8cc",
      doors: [
        "d6ab29511425e46eb6584d5ad038a69c028f4330279b741a809045dd704f685a",
        "0d2dfa0a9c95bdad93bbf4776489b25f3dceaf5450972e09956d8b8a3158ac7c",
        "124622a7a5f80f96afee1bd739ecacdc885ded9e991773cdc0d3bc2d44d71551"
      ],
      keys: "914a9325a7b2dddae56a431a282f5c5a9a26e086d7a77db7d01546be8038521a"
    },
    {
      title: "ROOM TWENTY",
      text: "e0dd2893d8f31e6e9c236e95ffd31d450fd7d425e2b886d086370a53c039af65",
      level: 6,
      options: ["S","E"],
      paths: {
        "S": 19,
        "E": 21
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "SOUTH DOOR", "EAST DOOR"],
      tiles: "6d3504070b8f1fff2a6829c398cf6453c4c52e3809c6eb1ad610d9af6d640984",
      doors: [
        "fab14a2a53ec1ef71ff9c08701d18ca88f233abfc156589f87cd00cf1a3d1e7e",
        "edf1e6d070dbcb27c7326519253634f613574cdf84af4afab19fa25e4e13274f"
      ]
    }
  ],

  level7: [
    {
      title: "ROOM TWENTY-ONE",
      text: "6431a6683db76bf7458a683c18bedbea33a2793ffa5975ce4ea67ba613ac65ce",
      level: 7,
      options: ["W","N","E","S"],
      paths: {
        "W": 20,
        "N": 23,
        "E": 27,
        "S": 22
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR", "EAST DOOR", "SOUTH DOOR"],
      tiles: "6c84337d6a16e9eb6c5c184ef5dc4ff6ecfb371925ac421d9244eb8fca7fc3ab",
      doors: [
        "80d8527f349e8fc8784d9ecf63befce2aea40f02e1e0e9d96b38188e593cfdb3",
        "20b728084624ea64b4f2cc7bb631661716a66b8d29d3c1ca5de1d841a4ab8c89",
        "5ecff753e88ec81941dd4ee096baf51a01ee123a410ae05f5c73d000f082f6f7",
        "28e120200a461b3b027a91b0164b107c4341cfe6031b042cbe7e526aee3136c5"
      ]
    },
    {
      title: "ROOM TWENTY-TWO",
      text: "46fd06ce6cb079bb3d99872593d05cb02722df1ddb56d240d31ec73895984068",
      level: 7,
      options: ["W","N"],
      paths: {
        "W": 19,
        "N": 21
      },
      size: {
        w: 7,
        l: 7
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "NORTH DOOR"],
      tiles: "4e7fcfd07fea12a2466e4dbce3beaa493570b90ea07139c6597ff1db24b3935b",
      doors: [
        "200c6afb0fdad93752322136cde0867f4f09e48a847b60192a8b47e35be68431",
        "cfa3d3fc766751e45fa297e49eb355ee82a58cb0bb22c2134cb2b5df34ab6892"
      ]
    },
    {
      title: "ROOM TWENTY-THREE",
      text: "042eabe1691f2a097069610790cf6bc7dab3b844b19c45827530295b04082956",
      level: 7,
      options: ["W","S","E"],
      paths: {
        "W": 24,
        "S": 21,
        "E": 25
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "SOUTH DOOR", "EAST DOOR"],
      tiles: "3213cf18c02dc09a494a76043072918d4f3df7ae21eb8f8b147c484719bd6503",
      doors: [
        "2821a2cd7e864912d542155ed06237e60faa5efe0bcf3ea110e2bccc0bb36811",
        "186b67b8996b46391f96282ae69640d90ebaf29fd702996541bac777acbd4124",
        "58e399ca001a396aa6c92b5512d12a7c72a9542f693c5e5ca5e27f0d6ab24629"
      ],
      keys: "1ded532de28702c0bf7a979e2c46fdc72c333b8874bb4c76a3a44a4affb16aae"
    },
    {
      title: "ROOM TWENTY-FOUR",
      text: "d944a9360a3ba1ce56d4999d54f1b72903d6a214422b27971f7914e261ed6cc1",
      level: 7,
      options: ["E"],
      paths: {
        "E": 23
      },
      size: {
        w: 5,
        l: 5
      },
      objects: ["WALLS", "GROUND", "EAST DOOR"],
      tiles: "9e1635ea8e094f50d349cbdf908d66f7192b4d687dd9dc729eb732f83be25768",
      doors: ["cae3733dc4712f1d321c60935f1c29c44e77ef45974a7dd60beb4bbe1b8178f5"]
    }
  ],

  level8: [
    {
      title: "ROOM TWENTY-FIVE",
      text: "45d25379fa8295aafa3d5f12948676b08d4b1aa4859defbc83f322052b4f838d",
      level: 8,
      options: ["W","S"],
      paths: {
        "W": 23,
        "S": 26
      },
      size: {
        w: 5,
        l: 5
      },
      objects: ["WALLS", "GROUND", "WEST DOOR", "SOUTH DOOR"],
      tiles: "17a9677e31633c985f271a46cfab3fcbda468bca71a362519895675b70b31a09",
      doors: [
        "dfa1612bacf78857c0dfea80d63c509cc2dae443575349a0a90ac4f7adb83d4e",
        "b8eae8d0400ca3db6eca43d561f99790d1edafa0cbae9bbe74c059ad36f97205"
      ],
      keys: "d1f48a4255c77f557ac7aa2b7ff4048d9ec4e0dea9609bbd990f67cd84e9cb2e"
    },
    {
      title: "ROOM TWENTY-SIX",
      text: "39224eded694f82ab9069e7a45948c09fcb7202b538900268ce358e3d58ef9b0",
      level: 8,
      options: ["N","W"],
      paths: {
        "N": 25,
        "W": 27
      },
      size: {
        w: 5,
        l: 5
      },
      objects: ["WALLS", "GROUND", "NORTH DOOR", "WEST DOOR"],
      tiles: "5d3819575867d82cdbebe107cfdcd6855f754384debccadd2e967cd05e80827d",
      doors: [
        "bd0348dd8bcbeab592026570ee0044bea29a4d62d07a785f5b55f01410396f70",
        "167e9d630ce75eddcd426db4dc0b4c4cdb02b1011db58c4fa7bef9e96b3475aa"
      ]
    },
    {
      title: "ROOM TWENTY-SEVEN",
      text: "45580c8e8605674756172bfbda5b27fba23ced16ecaac3d887da4423fe5daa21",
      level: 8,
      options: ["E","S","W"],
      paths: {
        "E": 26,
        "S": 28,
        "W": 21
      },
      size: {
        w: 8,
        l: 8
      },
      objects: ["WALLS", "GROUND", "EAST DOOR", "SOUTH DOOR", "WEST DOOR"],
      tiles: "789b4f1af7d68a77f9a109f615032f238dcffa58cc61f17a37ea57fbba3b8069",
      doors: [
        "8ad17a4afa3f337f09613d357023f1af9f9c1c9f4fcc590c379308695c7cb7a8",
        "dfb7dda3c034b1eecaaf29849994f842425a65b04320ac760afdd0492421aed7",
        "e0c652b9e2c848ce5e4d11fc59d5f008516484a891bd8481b7011e3a56249bb9"
      ]
    },
    {
      title: "ROOM TWENTY-EIGHT",
      text: "2b53b5b936704c65379ad478d994635e565f3352145e4d26f17b1aadaa575d46",
      level: 8,
      options: ["N","E"],
      paths: {
        "N": 27,
        "E": 29
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "NORTH DOOR", "EAST DOOR"],
      tiles: "24bd477543b5cce692dc5f01fa3569630efe3ffae90cb1812499599f67441cd3",
      doors: [
        "ab8474bd1585408f676774774af6eb27deab1fd0416c5def0c19772812f39c02",
        "ecf9c0f1fc9351d650f65e8990c5dc2a1cab59d98ca07c2d7a24c420805cca33"
      ]
    }
  ],

  level9: [
    {
      title: "ROOM TWENTY-NINE",
      text: "ca5b563e7e44e64d792b5a0609d59b727501864cccf180ada59727e69d2ef102",
      level: 9,
      options: ["W"],
      paths: {
        "W": 28
      },
      size: {
        w: 6,
        l: 6
      },
      objects: ["WALLS", "GROUND", "WEST DOOR"],
      tiles: "012fc8f5ac27a2979bebacd5f67c4dcff4d7a7a1434d134345f1f5da508999b4",
      doors: ["4ca967f56ec331573e0c42a50949f531cd6e32e8deb9f73ccae7ff11a862fae0"]
    }
  ]
};

const Rooms = [
  Levels.level1[0], Levels.level1[1], Levels.level1[2],
  Levels.level2[0], Levels.level2[1], Levels.level2[2], Levels.level2[3],
  Levels.level3[0],
  Levels.level4[0], Levels.level4[1],
  Levels.level3[1], Levels.level3[2], Levels.level3[3],
  Levels.level4[2], Levels.level4[3],
  Levels.level3[4],
  Levels.level5[0], Levels.level5[1], Levels.level5[2],
  Levels.level6[0], Levels.level6[1],
  Levels.level7[0], Levels.level7[1], Levels.level7[2], Levels.level7[3],
  Levels.level8[0], Levels.level8[1], Levels.level8[2], Levels.level8[3],
  Levels.level9[0]
];

export {
  Levels,
  Rooms
};