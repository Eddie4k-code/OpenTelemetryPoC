#!/usr/bin/env python3
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

#Configures the tracer
def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = SimpleSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider) #Sets Globally 
    return trace.get_tracer("service1.py", "0.0.1")


def browse():
    print("Visting service1")



if __name__ == "__main__":
    tracer = configure_tracer()
    span = tracer.start_span("visit service1")
    browse()
    span.end()