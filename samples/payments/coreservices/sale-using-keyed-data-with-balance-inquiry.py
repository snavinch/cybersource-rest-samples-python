from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def sale_using_keyed_data_with_balance_inquiry():
    clientReferenceInformationCode = "123456"
    clientReferenceInformationPartnerThirdPartyCertificationNumber = "123456789012"
    clientReferenceInformationPartner = Ptsv2paymentsClientReferenceInformationPartner(
        third_party_certification_number = clientReferenceInformationPartnerThirdPartyCertificationNumber
    )

    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode,
        partner = clientReferenceInformationPartner.__dict__
    )

    processingInformationCapture = True
    processingInformationCommerceIndicator = "retail"
    processingInformationAuthorizationOptionsPartialAuthIndicator = True
    processingInformationAuthorizationOptionsIgnoreAvsResult = True
    processingInformationAuthorizationOptionsIgnoreCvResult = True
    processingInformationAuthorizationOptions = Ptsv2paymentsProcessingInformationAuthorizationOptions(
        partial_auth_indicator = processingInformationAuthorizationOptionsPartialAuthIndicator,
        ignore_avs_result = processingInformationAuthorizationOptionsIgnoreAvsResult,
        ignore_cv_result = processingInformationAuthorizationOptionsIgnoreCvResult
    )

    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture,
        commerce_indicator = processingInformationCommerceIndicator,
        authorization_options = processingInformationAuthorizationOptions.__dict__
    )

    paymentInformationCardNumber = "4111111111111111"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2031"
    paymentInformationCardSecurityCode = "123"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        security_code = paymentInformationCardSecurityCode
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "100.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    pointOfSaleInformationEntryMode = "keyed"
    pointOfSaleInformationTerminalCapability = 2
    pointOfSaleInformation = Ptsv2paymentsPointOfSaleInformation(
        entry_mode = pointOfSaleInformationEntryMode,
        terminal_capability = pointOfSaleInformationTerminalCapability
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__,
        point_of_sale_information = pointOfSaleInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

if __name__ == "__main__":
    sale_using_keyed_data_with_balance_inquiry()
