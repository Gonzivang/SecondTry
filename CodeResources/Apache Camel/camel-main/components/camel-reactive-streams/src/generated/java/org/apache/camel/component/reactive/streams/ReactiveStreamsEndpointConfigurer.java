/* Generated by camel build tools - do NOT edit this file! */
package org.apache.camel.component.reactive.streams;

import java.util.Map;

import org.apache.camel.CamelContext;
import org.apache.camel.spi.ExtendedPropertyConfigurerGetter;
import org.apache.camel.spi.PropertyConfigurerGetter;
import org.apache.camel.spi.ConfigurerStrategy;
import org.apache.camel.spi.GeneratedPropertyConfigurer;
import org.apache.camel.util.CaseInsensitiveMap;
import org.apache.camel.support.component.PropertyConfigurerSupport;

/**
 * Generated by camel build tools - do NOT edit this file!
 */
@SuppressWarnings("unchecked")
public class ReactiveStreamsEndpointConfigurer extends PropertyConfigurerSupport implements GeneratedPropertyConfigurer, PropertyConfigurerGetter {

    @Override
    public boolean configure(CamelContext camelContext, Object obj, String name, Object value, boolean ignoreCase) {
        ReactiveStreamsEndpoint target = (ReactiveStreamsEndpoint) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "backpressurestrategy":
        case "backpressureStrategy": target.setBackpressureStrategy(property(camelContext, org.apache.camel.component.reactive.streams.ReactiveStreamsBackpressureStrategy.class, value)); return true;
        case "bridgeerrorhandler":
        case "bridgeErrorHandler": target.setBridgeErrorHandler(property(camelContext, boolean.class, value)); return true;
        case "concurrentconsumers":
        case "concurrentConsumers": target.setConcurrentConsumers(property(camelContext, int.class, value)); return true;
        case "exceptionhandler":
        case "exceptionHandler": target.setExceptionHandler(property(camelContext, org.apache.camel.spi.ExceptionHandler.class, value)); return true;
        case "exchangepattern":
        case "exchangePattern": target.setExchangePattern(property(camelContext, org.apache.camel.ExchangePattern.class, value)); return true;
        case "exchangesrefilllowwatermark":
        case "exchangesRefillLowWatermark": target.setExchangesRefillLowWatermark(property(camelContext, double.class, value)); return true;
        case "forwardoncomplete":
        case "forwardOnComplete": target.setForwardOnComplete(property(camelContext, boolean.class, value)); return true;
        case "forwardonerror":
        case "forwardOnError": target.setForwardOnError(property(camelContext, boolean.class, value)); return true;
        case "lazystartproducer":
        case "lazyStartProducer": target.setLazyStartProducer(property(camelContext, boolean.class, value)); return true;
        case "maxinflightexchanges":
        case "maxInflightExchanges": target.setMaxInflightExchanges(property(camelContext, java.lang.Integer.class, value)); return true;
        default: return false;
        }
    }

    @Override
    public Class<?> getOptionType(String name, boolean ignoreCase) {
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "backpressurestrategy":
        case "backpressureStrategy": return org.apache.camel.component.reactive.streams.ReactiveStreamsBackpressureStrategy.class;
        case "bridgeerrorhandler":
        case "bridgeErrorHandler": return boolean.class;
        case "concurrentconsumers":
        case "concurrentConsumers": return int.class;
        case "exceptionhandler":
        case "exceptionHandler": return org.apache.camel.spi.ExceptionHandler.class;
        case "exchangepattern":
        case "exchangePattern": return org.apache.camel.ExchangePattern.class;
        case "exchangesrefilllowwatermark":
        case "exchangesRefillLowWatermark": return double.class;
        case "forwardoncomplete":
        case "forwardOnComplete": return boolean.class;
        case "forwardonerror":
        case "forwardOnError": return boolean.class;
        case "lazystartproducer":
        case "lazyStartProducer": return boolean.class;
        case "maxinflightexchanges":
        case "maxInflightExchanges": return java.lang.Integer.class;
        default: return null;
        }
    }

    @Override
    public Object getOptionValue(Object obj, String name, boolean ignoreCase) {
        ReactiveStreamsEndpoint target = (ReactiveStreamsEndpoint) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "backpressurestrategy":
        case "backpressureStrategy": return target.getBackpressureStrategy();
        case "bridgeerrorhandler":
        case "bridgeErrorHandler": return target.isBridgeErrorHandler();
        case "concurrentconsumers":
        case "concurrentConsumers": return target.getConcurrentConsumers();
        case "exceptionhandler":
        case "exceptionHandler": return target.getExceptionHandler();
        case "exchangepattern":
        case "exchangePattern": return target.getExchangePattern();
        case "exchangesrefilllowwatermark":
        case "exchangesRefillLowWatermark": return target.getExchangesRefillLowWatermark();
        case "forwardoncomplete":
        case "forwardOnComplete": return target.isForwardOnComplete();
        case "forwardonerror":
        case "forwardOnError": return target.isForwardOnError();
        case "lazystartproducer":
        case "lazyStartProducer": return target.isLazyStartProducer();
        case "maxinflightexchanges":
        case "maxInflightExchanges": return target.getMaxInflightExchanges();
        default: return null;
        }
    }
}

