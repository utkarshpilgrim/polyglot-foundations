public interface PaymentProcessor {
    PaymentResult process(PaymentRequest req) throws ValidationException, ProviderException;
}