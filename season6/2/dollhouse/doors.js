// Doors.js

const DEFAULT = "An ordinary door";
const GATE = "A gate to another dimension";

const Doors = {
  // Level 1 - Room 0
  '7659ecce3626e8ba076db778dcfee78ec61e15c2e7233fe8b7b549fb70aefe9e': { 
    name: "DOOR ONE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 1
  },
  // Level 1 - Room 1
  '96bf5a7887fb67460c6fe44058f4c800ebbb6447f58826b3a0a621ead3225711': {
    name: "DOOR TWO",
    description: DEFAULT,
    facing: "NORTH",
    level: 1
  },
  'c9e5a0f63c5573d0a3da978afb7f15bf9e01ec9a190d2030055533115d3970d6': {
    name: "DOOR THREE",
    description: DEFAULT,
    facing: "EAST",
    level: 1
  },
  // Level 1 - Room 2
  '0bdf79272c01db3432640b3841b0cc268e458521c65e46f3e4ce29cad777abaa': {
    name: "DOOR FOUR",
    description: DEFAULT,
    facing: "WEST",
    level: 1
  },
  '346eca8873fd9375a33c8f47e549b9a780945eb7b14fb0e3781261407a2322dc': {
    name: "DOOR FIVE",
    description: GATE,
    facing: "NORTH",
    level: 2,
    secret: "2ddbd6b38d5fa0b798711c20e77973c85bb68d81383e470b1b7ddd5130eec6d4"
  },
  // Level 2 - Room 3
  '1b4f258e87bf501e3c50d947ba059e3be905663ae12c2d4eb28519ada88f79fe': {
    name: "DOOR SIX",
    description: DEFAULT,
    facing: "SOUTH",
    level: 1
  },
  'fb20aa46f9acd024556ff7db3bca0aafb15601b130a27a562cd3f08bc3033491': {
    name: "DOOR SEVEN",
    description: DEFAULT,
    facing: "EAST",
    level: 2
  },
  // Level 2 - Room 4
  'bd3f011a1fedac7e3f69fc3d52957d449c4df15ab7d05e4a2c58522d7b7ff4a5': {
    name: "DOOR EIGHT",
    description: DEFAULT,
    facing: "WEST",
    level: 2
  },
  'ea0ab58cf5edf86a79434ba04061a1b1f9c416a121bbe88fa667e88bdfa40a97': {
    name: "DOOR NINE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 2
  },
  // Level 2 - Room 5
  '811cda60e1204bcbce44736ca67eee99a3ef0fd60ff0e2ccbedef5e94986e4fa': {
    name: "DOOR TEN",
    description: DEFAULT,
    facing: "NORTH",
    level: 2
  },
  '3f6510c3c36f1f636afb42b5aad5a8204742d16f68433cb4f030da97a61a4577': {
    name: "DOOR ELEVEN",
    description: DEFAULT,
    facing: "EAST",
    level: 2
  },
  // Level 2 - Room 6
  '6c9b64a654dc67140ffcf5a5780998fa454aac1f7231cdebab454f25dca4eacf': {
    name: "DOOR TWELVE",
    description: DEFAULT,
    facing: "WEST",
    level: 2
  },
  'c05ed0afc94a35303c17b08adae223f9ef4d9c288c156a13e75716e0281703a6': {
    name: "DOOR TWELVE",
    description: GATE,
    facing: "NORTH",
    level: 3,
    secret: "0b40787be490872e135fe20e911150c62d301d335421bec3cad0f206448a3c03"
  },
  // Level 3 - Room 7
  '2d889408bcd6325392922f3728e301b0299cf3148ed1e80cbb6ddd65560becc5': {
    name: "DOOR THIRTEEN",
    description: DEFAULT,
    facing: "SOUTH",
    level: 2
  },
  '5ddf571e01e94909b8db5024f3e23b4082add484020178b2071c0c75641bd6df': {
    name: "DOOR FOURTEEN",
    description: GATE,
    facing: "NORTH",
    level: 4,
    secret: "256836338cb5b89dcab7714811dfad26ef363526365db4f4293f89d671a08a30"
  },
  '8ae7f3f439e343ee9fd8fbf894618cadd606559321056b3b270d8b14c7222da1': {
    name: "DOOR FIFTEEN",
    description: DEFAULT,
    facing: "EAST",
    level: 3
  },
  // Level 3 - Room 10
  'db3fc82b30dffd33fea9170e7ded372eb4c93d93deb7ae5b4bbc650db4bd7a35': {
    name: "DOOR SIXTEEN",
    description: DEFAULT,
    facing: "WEST",
    level: 3
  },
  'd9494d774c3cb1bef1fc59adf1a165ea5ba85f175b0fbfb6317df1447970d437': {
    name: "DOOR SEVENTEEN",
    description: GATE,
    facing: "NORTH",
    level: 4,
    secret: "256836338cb5b89dcab7714811dfad26ef363526365db4f4293f89d671a08a30"
  },
  'abfc020e5bc29e3b3ad05f1eea0bf1a5cc87540dc83c79d22ca924e7289b7b19': {
    name: "DOOR EIGHTEEN",
    description: DEFAULT,
    facing: "EAST",
    level: 3
  },
  // Level 3 - Room 11
  'e102a49cfaa3d35c204187b2908243bc9960268cbb270573d104e1b1f225a985': {
    name: "DOOR NINETEEN",
    description: DEFAULT,
    facing: "WEST",
    level: 3
  },
  'abe4abc2a83f3f518f8490a18e7e5a715a2bec11809a8e64a123a65702768fec': {
    name: "DOOR TWENTY",
    description: GATE,
    facing: "NORTH",
    level: 4,
    secret: "256836338cb5b89dcab7714811dfad26ef363526365db4f4293f89d671a08a30"
  },
  '36634a32358c02330ee430ea6d54d1dff11e1bf0e7bfd25e06f7b92d287882d4': {
    name: "DOOR TWENTY-ONE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 3
  },
  '68b0e5de35a82fa6fc84683fb588a6c529e8164ccbae58cfb40e5a327db00bbe': {
    name: "DOOR TWENTY-TWO",
    description: DEFAULT,
    facing: "EAST",
    level: 3
  },
  // Level 3 - Room 12
  '4d8bf39980e356c4fb7d728967ab70f1924764266f979b9692fd5474e76829e3': {
    name: "DOOR TWENTY-THREE",
    description: DEFAULT,
    facing: "NORTH",
    level: 3
  },
  // Level 3 - Room 15
  '142ab03d204f9f1658940920bb4da216021808568e6a8ecf00dbaf5a3ed0e463': {
    name: "DOOR TWENTY-FOUR",
    description: DEFAULT,
    facing: "WEST",
    level: 3
  },
  '46ec3154b77621b5793139a49b9ef7a409986d206a0af6c0b1ff22d5a34e86e1': {
    name: "DOOR TWENTY-FIVE",
    description: GATE,
    facing: "NORTH",
    level: 4,
    secret: "256836338cb5b89dcab7714811dfad26ef363526365db4f4293f89d671a08a30"
  },
  '7600308629375cd3ec2086ad4d91c836e4c9defef58809e620f11b49e3dffd6d': {
    name: "DOOR TWENTY-SIX",
    description: GATE,
    facing: "EAST",
    level: 5,
    secret: "c72b354bc0a2092dd4f21d0356186fa9cf72f1b1f777448b90feb27aa4074638"
  },
  // Level 4 - Room 8
  'ec5237a5053bc72d1338f063f83dcca1a1d801e4ad4584ad155ee357be9e47f3': {
    name: "DOOR TWENTY-SEVEN",
    description: DEFAULT,
    facing: "SOUTH",
    level: 3
  },
  '41a49b432ae8af3ccafa36d64aab94184ed2ff3582b19a78c1baf0141fddec52': {
    name: "DOOR TWENTY-EIGHT",
    description: DEFAULT,
    facing: "EAST",
    level: 4
  },
  // Level 4 - Room 9
  'd0d35a1f012c57eff0355ffc7c5a825b4a1a2734684e90b85a8e0504e7d1377b': {
    name: "DOOR TWENTY-NINE",
    description: DEFAULT,
    facing: "WEST",
    level: 4
  },
  '90639508a57ff4dd2998382c1d12bb53d89124dfa61b6aa1ad44181affaf02db': {
    name: "DOOR THIRTY",
    description: DEFAULT,
    facing: "SOUTH",
    level: 3
  },
  '41a974b4e6d04b0f52f0e7b63a69bcc4aaaed1292731d6dc985b5dab3e61179f': {
    name: "DOOR THIRTY-ONE",
    description: DEFAULT,
    facing: "EAST",
    level: 4
  },
  // Level 4 - Room 13
  '11a4de0114da117ca263e3a97a0f7160066541aeef60b6478df78344ba7f54a4': {
    name: "DOOR THIRTY-TWO",
    description: DEFAULT,
    facing: "WEST",
    level: 4
  },
  '501117849500318f1070847f1a83f230f3e831b9ea639bebb6a04569ec600cf9': {
    name: "DOOR THIRTY-THREE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 3
  },
  'fdcaed46ced9b1388de4e56e3a6a1bbaa622e732c6d03e271c1ab797e00cd224': {
    name: "DOOR THIRTY-FOUR",
    description: DEFAULT,
    facing: "EAST",
    level: 4
  },
  // Level 4 - Room 14
  '047b5cea561486ee8411842a6255a7cc28bddf926c14222dac512fc71adbdfe7': {
    name: "DOOR THIRTY-FIVE",
    description: DEFAULT,
    facing: "WEST",
    level: 4
  },
  'a95e56556a00dbd907c34d52cbe909fa12574e9261a9b98feb20dcd0a42ddcc2': {
    name: "DOOR THIRTY-SIX",
    description: DEFAULT,
    facing: "SOUTH",
    level: 3
  },
  // Level 5 - Room 16
  'f37852686bca32ee67379af67d692d6ec001b50a85e0906fe19ee5a5757a4b01': {
    name: "DOOR THIRTY-SEVEN",
    description: DEFAULT,
    facing: "WEST",
    level: 3
  },
  '83c5da5232ad960b80e180faf0e98551427710c54e62d5e988b646798aa948b2': {
    name: "DOOR THIRTY-EIGHT",
    description: DEFAULT,
    facing: "NORTH",
    level: 5
  },
  'a8d0f03ece1a441e391a1af06cf189e138249ffb06a3740c482a0e21f69c7869': {
    name: "DOOR THIRTY-NINE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 5
  },
  // Level 5 - Room 17
  'bcbd9ff05b52e6aa9de3dced0b7e3e091c77dc7d840ef66883dd7a4c14c9d819': {
    name: "DOOR FORTY",
    description: DEFAULT,
    facing: "SOUTH",
    level: 5
  },
  // Level 5 - Room 18
  '48dbcada9b3347866c6689cc6ccde565fa03e3a2ebf2896477fa98646af63435': {
    name: "DOOR FORTY-ONE",
    description: DEFAULT,
    facing: "NORTH",
    level: 5
  },
  'add0a6fcf2a6a0160e93a379bb325e42927949be68ef0a279129ef8570f271bc': {
    name: "DOOR FORTY-TWO",
    description: GATE,
    facing: "EAST",
    level: 6,
    secret: "a442958f6a219a1e540bd489f80e282672ea291ce4add91e8f33b4d62134e082"
  },
  // Level 6 - Room 19
  'd6ab29511425e46eb6584d5ad038a69c028f4330279b741a809045dd704f685a': {
    name: "DOOR FORTY-THREE",
    description: DEFAULT,
    facing: "WEST",
    level: 5,
  },
  '0d2dfa0a9c95bdad93bbf4776489b25f3dceaf5450972e09956d8b8a3158ac7c': {
    name: "DOOR FORTY-FOUR",
    description: DEFAULT,
    facing: "NORTH",
    level: 6,
  },
  '124622a7a5f80f96afee1bd739ecacdc885ded9e991773cdc0d3bc2d44d71551': {
    name: "DOOR FORTY-FIVE",
    description: GATE,
    facing: "EAST",
    level: 7,
    secret: "e2c6b70a211fe01e16521b50b5d1fd3ebaf91d8bcbd222e5673e588846ad8003"
  },
  // Level 6 - Room 20
  'fab14a2a53ec1ef71ff9c08701d18ca88f233abfc156589f87cd00cf1a3d1e7e': {
    name: "DOOR FORTY-SIX",
    description: DEFAULT,
    facing: "SOUTH",
    level: 6,
  },
  'edf1e6d070dbcb27c7326519253634f613574cdf84af4afab19fa25e4e13274f': {
    name: "DOOR FORTY-SEVEN",
    description: GATE,
    facing: "EAST",
    level: 7,
    secret: "e2c6b70a211fe01e16521b50b5d1fd3ebaf91d8bcbd222e5673e588846ad8003"
  },
  // Level 7 - Room 21
  '80d8527f349e8fc8784d9ecf63befce2aea40f02e1e0e9d96b38188e593cfdb3': {
    name: "DOOR FORTY-EIGHT",
    description: DEFAULT,
    facing: "WEST",
    level: 6,
  },
  '20b728084624ea64b4f2cc7bb631661716a66b8d29d3c1ca5de1d841a4ab8c89': {
    name: "DOOR FORTY-NINE",
    description: DEFAULT,
    facing: "NORTH",
    level: 7,
  },
  '5ecff753e88ec81941dd4ee096baf51a01ee123a410ae05f5c73d000f082f6f7': {
    name: "DOOR FIFTY",
    description: GATE,
    facing: "EAST",
    level: 8,
    secret: "f50ee08c2f20075329d57e4145b292cfdb74cfd5823f1c3a5d8feb825bd8c560"
  },
  '28e120200a461b3b027a91b0164b107c4341cfe6031b042cbe7e526aee3136c5': {
    name: "DOOR FIFTY-ONE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 7,
  },
  // Level 7 - Room 22
  '200c6afb0fdad93752322136cde0867f4f09e48a847b60192a8b47e35be68431': {
    name: "DOOR FIFTY-TWO",
    description: DEFAULT,
    facing: "WEST",
    level: 6,
  },
  'cfa3d3fc766751e45fa297e49eb355ee82a58cb0bb22c2134cb2b5df34ab6892': {
    name: "DOOR FIFTY-THREE",
    description: DEFAULT,
    facing: "NORTH",
    level: 7,
  },
  // Level 7 - Room 23
  '2821a2cd7e864912d542155ed06237e60faa5efe0bcf3ea110e2bccc0bb36811': {
    name: "DOOR FIFTY-FOUR",
    description: DEFAULT,
    facing: "WEST",
    level: 7,
  },
  '186b67b8996b46391f96282ae69640d90ebaf29fd702996541bac777acbd4124': {
    name: "DOOR FIFTY-FIVE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 7,
  },
  '58e399ca001a396aa6c92b5512d12a7c72a9542f693c5e5ca5e27f0d6ab24629': {
    name: "DOOR FIFTY-SIX",
    description: GATE,
    facing: "EAST",
    level: 8,
    secret: "f50ee08c2f20075329d57e4145b292cfdb74cfd5823f1c3a5d8feb825bd8c560"
  },
  // Level 7 - Room 24
  'cae3733dc4712f1d321c60935f1c29c44e77ef45974a7dd60beb4bbe1b8178f5': {
    name: "DOOR FIFTY-SEVEN",
    description: DEFAULT,
    facing: "EAST",
    level: 7,
  },
  // Level 8 - Room 25
  'dfa1612bacf78857c0dfea80d63c509cc2dae443575349a0a90ac4f7adb83d4e': {
    name: "DOOR FIFTY-EIGHT",
    description: DEFAULT,
    facing: "WEST",
    level: 7,
  },
  'b8eae8d0400ca3db6eca43d561f99790d1edafa0cbae9bbe74c059ad36f97205': {
    name: "DOOR FIFTY-NINE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 8,
  },
  // Level 8 - Room 26
  'bd0348dd8bcbeab592026570ee0044bea29a4d62d07a785f5b55f01410396f70': {
    name: "DOOR SIXTY",
    description: DEFAULT,
    facing: "NORTH",
    level: 8,
  },
  '167e9d630ce75eddcd426db4dc0b4c4cdb02b1011db58c4fa7bef9e96b3475aa': {
    name: "DOOR SIXTY-ONE",
    description: DEFAULT,
    facing: "WEST",
    level: 8,
  },
  // Level 8 - Room 27
  '8ad17a4afa3f337f09613d357023f1af9f9c1c9f4fcc590c379308695c7cb7a8': {
    name: "DOOR SIXTY-TWO",
    description: DEFAULT,
    facing: "EAST",
    level: 7,
  },
  'dfb7dda3c034b1eecaaf29849994f842425a65b04320ac760afdd0492421aed7': {
    name: "DOOR SIXTY-THREE",
    description: DEFAULT,
    facing: "SOUTH",
    level: 8,
  },
  'e0c652b9e2c848ce5e4d11fc59d5f008516484a891bd8481b7011e3a56249bb9': {
    name: "DOOR SIXTY-FOUR",
    description: DEFAULT,
    facing: "WEST",
    level: 8,
  },
  // Level 8 - Room 28
  'ab8474bd1585408f676774774af6eb27deab1fd0416c5def0c19772812f39c02': {
    name: "DOOR SIXTY-FIVE",
    description: DEFAULT,
    facing: "NORTH",
    level: 8,
  },
  'ecf9c0f1fc9351d650f65e8990c5dc2a1cab59d98ca07c2d7a24c420805cca33': {
    name: "DOOR SIXTY-FIVE",
    description: DEFAULT,
    facing: "EAST",
    level: 9,
    secret: "782cc7422e60c651ba6b174ef6858ce60a68766ab09dd9d9440129984f66ed19"
  },
  // Level 9 - Door 29
  '4ca967f56ec331573e0c42a50949f531cd6e32e8deb9f73ccae7ff11a862fae0': {
    name: "DOOR SIXTY-SIX",
    description: DEFAULT,
    facing: "WEST",
    level: 8,
  }
};

export default { Doors };