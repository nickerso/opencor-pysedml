import sys
import os.path
import libsedml

def printSedML(filename):
    doc = libsedml.readSedML(filename)
    if ( doc.getErrorLog().getNumFailsWithSeverity(libsedml.LIBSEDML_SEV_ERROR) > 0):
        print(doc.getErrorLog().toString())
        sys.exit(2)

    print('The document has {0}" simulation(s).'.format(doc.getNumSimulations()))

    for i in range(0, doc.getNumSimulations()):
        current = doc.getSimulation(i)
        if (current.getTypeCode() == libsedml.SEDML_SIMULATION_UNIFORMTIMECOURSE):
            tc = current
            kisaoid = "none"
            if tc.isSetAlgorithm():
                kisaoid = tc.getAlgorithm().getKisaoID()
            print("\tTimecourse id=", tc.getId(), " start=", tc.getOutputStartTime(), " end=", tc.getOutputEndTime(),
                  " numPoints=", tc.getNumberOfPoints(), " kisao=", kisaoid, "\n")
        else:
            print("\tUncountered unknown simulation. ", current.getId(), "\n")

    print("\n")
    print("The document has ", doc.getNumModels(), " model(s).", "\n")
    for i in range(0, doc.getNumModels()):
        current = doc.getModel(i)
        print("\tModel id=", current.getId(), " language=", current.getLanguage(), " source=", current.getSource(),
              " numChanges=", current.getNumChanges(), "\n")

    print("\n")
    print("The document has ", doc.getNumTasks(), " task(s).", "\n")
    for i in range(0, doc.getNumTasks()):
        current = doc.getTask(i)
        print("\tTask id=", current.getId(), " model=", current.getModelReference(), " sim=",
              current.getSimulationReference(), "\n")

    print("\n")
    print("The document has ", doc.getNumDataGenerators(), " datagenerators(s).", "\n")
    for i in range(0, doc.getNumDataGenerators()):
        current = doc.getDataGenerator(i)
        print("\tDG id=", current.getId(), " math=", libsedml.formulaToString(current.getMath()), "\n")

    print("\n")
    print("The document has ", doc.getNumOutputs(), " output(s).", "\n")
    for i in range(0, doc.getNumOutputs()):
        current = doc.getOutput(i)
        tc = current.getTypeCode()
        if tc == libsedml.SEDML_OUTPUT_REPORT:
            r = (current)
            print("\tReport id=", current.getId(), " numDataSets=", r.getNumDataSets(), "\n")
        elif tc == libsedml.SEDML_OUTPUT_PLOT2D:
            p = (current)
            print("\tPlot2d id=", current.getId(), " numCurves=", p.getNumCurves(), "\n")
        elif tc == libsedml.SEDML_OUTPUT_PLOT3D:
            p = (current)
            print("\tPlot3d id=", current.getId(), " numSurfaces=", p.getNumSurfaces(), "\n")
        else:
            print("\tEncountered unknown output ", current.getId(), "\n")

if __name__ == '__main__':
  printSedML(sys.argv[1])