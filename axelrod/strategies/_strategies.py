from .alternator import Alternator
from .adaptive import Adaptive
from .ann import EvolvedANN, EvolvedANN5, EvolvedANNNoise05
from .apavlov import APavlov2006, APavlov2011
from .appeaser import Appeaser
from .averagecopier import AverageCopier, NiceAverageCopier
from .axelrod_first import (
    Davis, RevisedDowning, Feld, Grofman, Nydegger, Joss, Shubik, Tullock,
    UnnamedStrategy)
from .axelrod_second import Champion, Eatherley, Tester
from .backstabber import BackStabber, DoubleCrosser
from .better_and_better import BetterAndBetter
from .calculator import Calculator
from .cooperator import Cooperator, TrickyCooperator
from .cycler import (
    AntiCycler, Cycler, CyclerCCD, CyclerCCCD, CyclerCCCCCD,
    CyclerDC, CyclerDDC, CyclerCCCDCD)
from .darwin import Darwin
from .defector import Defector, TrickyDefector
from .doubler import Doubler
from .finite_state_machines import (
    Fortress3, Fortress4, Predator, Pun1, Raider, Ripoff, SolutionB1,
    SolutionB5, Thumper, FSMPlayer, EvolvedFSM4, EvolvedFSM16,
    EvolvedFSM16Noise05)
from .forgiver import Forgiver, ForgivingTitForTat
from .geller import Geller, GellerCooperator, GellerDefector
from .gambler import (
    Gambler, PSOGambler1_1_1, PSOGambler2_2_2, PSOGambler2_2_2_Noise05,
    PSOGamblerMem1)
from .gobymajority import (GoByMajority,
    GoByMajority10, GoByMajority20, GoByMajority40,
    GoByMajority5,
    HardGoByMajority, HardGoByMajority10, HardGoByMajority20, HardGoByMajority40,
    HardGoByMajority5)
from .gradualkiller import GradualKiller
from .grudger import (Grudger, ForgetfulGrudger, OppositeGrudger, Aggravater,
    SoftGrudger, GrudgerAlternator, EasyGo)
from .grumpy import Grumpy
from .handshake import Handshake
from .hmm import HMMPlayer, EvolvedHMM5
from .human import Human
from .hunter import (
    DefectorHunter, CooperatorHunter, CycleHunter, AlternatorHunter,
    MathConstantHunter, RandomHunter, EventualCycleHunter)
from .inverse import Inverse
from .lookerup import (LookerUp,
    EvolvedLookerUp0_0_1, EvolvedLookerUp0_0_2, EvolvedLookerUp0_0_3,
    EvolvedLookerUp1_1_0, EvolvedLookerUp1_1_1, EvolvedLookerUp1_1_2,
    EvolvedLookerUp1_1_3, EvolvedLookerUp1_1_4, EvolvedLookerUp2_2_0,
    EvolvedLookerUp2_2_1, EvolvedLookerUp2_2_2, EvolvedLookerUp2_2_3,
    EvolvedLookerUp2_2_4, EvolvedLookerUp3_3_1, EvolvedLookerUp3_3_2,
    EvolvedLookerUp3_3_3, EvolvedLookerUp4_4_1, EvolvedLookerUp4_4_2,
    Winner12, Winner21)
from .mathematicalconstants import Golden, Pi, e
from .memoryone import (
    MemoryOnePlayer, ALLCorALLD, FirmButFair, GTFT, SoftJoss,
    StochasticCooperator, StochasticWSLS, ZDExtort2, ZDExtort2v2, ZDExtort4,
    ZDGen2, ZDGTFT2, ZDSet2, WinStayLoseShift, WinShiftLoseStay)
from .memorytwo import MEM2
from .mindcontrol import MindController, MindWarper, MindBender
from .mindreader import MindReader, ProtectedMindReader, MirrorMindReader
from .mutual import Desperate, Hopeless, Willing
from .negation import Negation
from .oncebitten import OnceBitten, FoolMeOnce, ForgetfulFoolMeOnce, FoolMeForever
from .prober import (CollectiveStrategy, Prober, Prober2, Prober3, Prober4,
                     HardProber, NaiveProber, RemorsefulProber)
from .punisher import Punisher, InversePunisher
from .qlearner import (
    RiskyQLearner, ArrogantQLearner, HesitantQLearner, CautiousQLearner)
from .rand import Random
from .retaliate import (
    Retaliate, Retaliate2, Retaliate3, LimitedRetaliate, LimitedRetaliate2,
    LimitedRetaliate3)
from .sequence_player import SequencePlayer, ThueMorse, ThueMorseInverse
from .titfortat import (
    TitForTat, TitFor2Tats, TwoTitsForTat, Bully, SneakyTitForTat,
    SuspiciousTitForTat, AntiTitForTat, HardTitForTat, HardTitFor2Tats,
    OmegaTFT, Gradual, ContriteTitForTat, SlowTitForTwoTats, AdaptiveTitForTat,
    SpitefulTitForTat)
from .worse_and_worse import (WorseAndWorse, KnowledgeableWorseAndWorse,
                              WorseAndWorse2, WorseAndWorse3)

# Note: Meta* strategies are handled in .__init__.py

all_strategies = [
    Adaptive,
    AdaptiveTitForTat,
    Aggravater,
    ALLCorALLD,
    Alternator,
    AlternatorHunter,
    AntiCycler,
    AntiTitForTat,
    APavlov2006,
    APavlov2011,
    Appeaser,
    ArrogantQLearner,
    AverageCopier,
    BetterAndBetter,
    BackStabber,
    Bully,
    Calculator,
    CautiousQLearner,
    Champion,
    CollectiveStrategy,
    ContriteTitForTat,
    Cooperator,
    CooperatorHunter,
    CycleHunter,
    CyclerCCCCCD,
    CyclerCCCD,
    CyclerCCD,
    CyclerDC,
    CyclerDDC,
    CyclerCCCDCD,
    Darwin,
    Davis,
    Defector,
    DefectorHunter,
    Desperate,
    DoubleCrosser,
    Doubler,
    EasyGo,
    Eatherley,
    EventualCycleHunter,
    EvolvedANN,
    EvolvedANN5,
    EvolvedANNNoise05,
    EvolvedFSM4,
    EvolvedFSM16,
    EvolvedFSM16Noise05,
    EvolvedLookerUp1_1_1,
    EvolvedLookerUp2_2_2,
    EvolvedHMM5,
    Feld,
    FirmButFair,
    FoolMeForever,
    FoolMeOnce,
    ForgetfulFoolMeOnce,
    ForgetfulGrudger,
    Forgiver,
    ForgivingTitForTat,
    Fortress3,
    Fortress4,
    GTFT,
    Geller,
    GellerCooperator,
    GellerDefector,
    GoByMajority,
    GoByMajority10,
    GoByMajority20,
    GoByMajority40,
    GoByMajority5,
    Golden,
    Gradual,
    GradualKiller,
    Grofman,
    Grudger,
    GrudgerAlternator,
    Grumpy,
    Handshake,
    HardGoByMajority,
    HardGoByMajority10,
    HardGoByMajority20,
    HardGoByMajority40,
    HardGoByMajority5,
    HardProber,
    HardTitFor2Tats,
    HardTitForTat,
    HesitantQLearner,
    Hopeless,
    Inverse,
    InversePunisher,
    Joss,
    KnowledgeableWorseAndWorse,
    LimitedRetaliate,
    LimitedRetaliate2,
    LimitedRetaliate3,
    MathConstantHunter,
    NaiveProber,
    MEM2,
    MindBender,
    MindController,
    MindReader,
    MindWarper,
    MirrorMindReader,
    Negation,
    NiceAverageCopier,
    Nydegger,
    OmegaTFT,
    OnceBitten,
    OppositeGrudger,
    Pi,
    Predator,
    Prober,
    Prober2,
    Prober3,
    Prober4,
    ProtectedMindReader,
    Pun1,
    PSOGambler1_1_1,
    PSOGambler2_2_2,
    PSOGambler2_2_2_Noise05,
    PSOGamblerMem1,
    Punisher,
    Raider,
    Random,
    RandomHunter,
    RemorsefulProber,
    Retaliate,
    Retaliate2,
    Retaliate3,
    RevisedDowning,
    Ripoff,
    RiskyQLearner,
    Shubik,
    SlowTitForTwoTats,
    SneakyTitForTat,
    SoftGrudger,
    SoftJoss,
    SolutionB1,
    SolutionB5,
    SpitefulTitForTat,
    StochasticCooperator,
    StochasticWSLS,
    SuspiciousTitForTat,
    Tester,
    ThueMorse,
    ThueMorseInverse,
    Thumper,
    TitForTat,
    TitFor2Tats,
    TrickyCooperator,
    TrickyDefector,
    Tullock,
    TwoTitsForTat,
    Willing,
    Winner12,
    Winner21,
    WinShiftLoseStay,
    WinStayLoseShift,
    WorseAndWorse,
    WorseAndWorse2,
    WorseAndWorse3,
    ZDExtort2,
    ZDExtort2v2,
    ZDExtort4,
    ZDGTFT2,
    ZDGen2,
    ZDSet2,
    e,
]
