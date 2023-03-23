procedure p-read-worker-pay-distribution-json:

    define input  parameter ipcha-type       as character no-undo.
    define output parameter vcha-associateOID as character no-undo.
    define output parameter vcha-workerid as character no-undo.
    define output parameter opcha-error-code as character no-undo.

    define variable vobj-json-body    as JsonObject        no-undo.
    define variable vobj-json-array   as JsonArray         no-undo.
    define variable vobj-json-element as JsonObject        no-undo.
    define variable vobj-json-temp    as JsonObject        no-undo.
    define variable vint-array-length as integer           no-undo.
    define variable vint-count        as integer           no-undo.
    define variable vobj-parser       as ObjectModelParser no-undo.

    assign vobj-parser    = NEW ObjectModelParser()
           vobj-json-body = CAST(vobj-parser:Parse(cha-pad-body-input), JsonObject).

    if valid-object (vobj-json-body) and vobj-json-body:has('events') then do:

        assign vobj-json-array   = vobj-json-body:GetJsonArray('events')
               vint-array-length = vobj-json-array:length.

        if vint-array-length <> 1
        then do:
            assign opcha-error-code = "POST-7".
            return.
        end.

        assign vobj-json-element = vobj-json-array:GetJsonObject(1).

        run p-populate-default-fields (input vobj-json-element).

        if  vobj-json-element:Has("data")
        and vobj-json-element:GetJsonObject("data"):Has("eventContext")
        and vobj-json-element:GetJsonObject("data"):GetJsonObject("eventContext"):Has("worker")
        then do:

            assign vobj-json-temp = vobj-json-element:GetJsonObject("data"):GetJsonObject("eventContext"):GetJsonObject("worker").

            if  vobj-json-temp:Has("associateOID")
            and vobj-json-temp:Has("workerID")
            and vobj-json-temp:GetJsonObject("workerID"):Has("idValue")
            then do:
                assign vcha-associateOID = vobj-json-temp:GetCharacter("associateOID")
                       vcha-workerid     = vobj-json-temp:GetJsonObject("workerID"):GetCharacter("idValue").
            end.

            if ipcha-type <> "REMOVE"
            and vobj-json-element:GetJsonObject("data"):Has("transform")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):Has("payDistribution")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):Has("distributionInstructions")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):Has("distributionPurposeCode")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):Has("depositAccount")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):Has("paymentMethodCode")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonObject("distributionPurposeCode"):Has("shortName__1__2")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):Has("BBAN")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):Has("financialAccount")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):Has("financialParty")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("paymentMethodCode"):Has("codeValue")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("paymentMethodCode"):Has("shortName__1__2__3")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialAccount"):Has("accountNumber")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialAccount"):Has("currencyCode")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialAccount"):Has("typeCode")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):Has("branchNameCode")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):Has("nameCode")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):Has("routingTransitID")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialAccount"):GetJsonObject("typeCode"):Has("shortName__1__2__3__4__5__6")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):GetJsonObject("branchNameCode"):Has("codeValue__1__2")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):GetJsonObject("branchNameCode"):Has("shortName__1__2__3__4__5")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):GetJsonObject("nameCode"):Has("codeValue__1")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):GetJsonObject("nameCode"):Has("shortName__1__2__3__4")
and vobj-json-element:GetJsonObject("data"):GetJsonObject("transform"):GetJsonObject("payDistribution"):GetJsonArray("distributionInstructions"):GetJsonObject(1):GetJsonObject("depositAccount"):GetJsonObject("financialParty"):GetJsonObject("routingTransitID"):Has("idValue__1")
            then do:

            end.
        end.
    end.
end procedure.