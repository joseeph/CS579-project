from Framework import UtilFuncs
from Framework.NodeContainer import NodeContainer
from StandfordCitationNetworkAnalysis.CitationNetworkBuilder import CitationNetworkBuilder
from StandfordCitationNetworkAnalysis.CoauthorNetworkBuilder import CoauthorNetworkBuilder
from StandfordCitationNetworkAnalysis.MiscInformationBuilder import MiscInformationBuilder


def BuildCitationGraphDF():
    data_container :NodeContainer = UtilFuncs.PickleRead("./Data/CitationCleaned.dat")
    builder = CitationNetworkBuilder()
    builder.BuildCitationDataFrame(data_container, "./Data/CitationGraphDF.dat")
    
def BuildCoauthorGraphDF():
    data_container :NodeContainer = UtilFuncs.PickleRead("./Data/CitationCleaned.dat")
    builder = CoauthorNetworkBuilder()
    builder.BuildCoauthorDataFrame(data_container, "./Data/CoauthorGraphDF.dat")

def BuildMiscInfoDF():
    data_container :NodeContainer = UtilFuncs.PickleRead("./Data/CitationCleaned.dat")
    builder = MiscInformationBuilder()
    builder.BuildMiscInfoDF(data_container, "./Data/MiscInfoDF.dat")

if __name__ == '__main__':
    # build the dataframes
    BuildCitationGraphDF()
    BuildCoauthorGraphDF()
    BuildMiscInfoDF()