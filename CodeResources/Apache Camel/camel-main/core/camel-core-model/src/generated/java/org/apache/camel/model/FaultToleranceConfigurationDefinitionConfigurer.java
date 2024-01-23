/* Generated by camel build tools - do NOT edit this file! */
package org.apache.camel.model;

import java.util.Map;

import org.apache.camel.CamelContext;
import org.apache.camel.spi.ExtendedPropertyConfigurerGetter;
import org.apache.camel.spi.PropertyConfigurerGetter;
import org.apache.camel.spi.ConfigurerStrategy;
import org.apache.camel.spi.GeneratedPropertyConfigurer;
import org.apache.camel.util.CaseInsensitiveMap;
import org.apache.camel.model.FaultToleranceConfigurationDefinition;

/**
 * Generated by camel build tools - do NOT edit this file!
 */
@SuppressWarnings("unchecked")
public class FaultToleranceConfigurationDefinitionConfigurer extends org.apache.camel.support.component.PropertyConfigurerSupport implements GeneratedPropertyConfigurer, ExtendedPropertyConfigurerGetter {

    private static final Map<String, Object> ALL_OPTIONS;
    static {
        Map<String, Object> map = new CaseInsensitiveMap();
        map.put("BulkheadEnabled", java.lang.String.class);
        map.put("BulkheadExecutorService", java.lang.String.class);
        map.put("BulkheadMaxConcurrentCalls", java.lang.String.class);
        map.put("BulkheadWaitingTaskQueue", java.lang.String.class);
        map.put("CircuitBreaker", java.lang.String.class);
        map.put("Delay", java.lang.String.class);
        map.put("FailureRatio", java.lang.String.class);
        map.put("Id", java.lang.String.class);
        map.put("RequestVolumeThreshold", java.lang.String.class);
        map.put("SuccessThreshold", java.lang.String.class);
        map.put("TimeoutDuration", java.lang.String.class);
        map.put("TimeoutEnabled", java.lang.String.class);
        map.put("TimeoutPoolSize", java.lang.String.class);
        map.put("TimeoutScheduledExecutorService", java.lang.String.class);
        ALL_OPTIONS = map;
    }

    @Override
    public boolean configure(CamelContext camelContext, Object obj, String name, Object value, boolean ignoreCase) {
        org.apache.camel.model.FaultToleranceConfigurationDefinition target = (org.apache.camel.model.FaultToleranceConfigurationDefinition) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "bulkheadenabled":
        case "BulkheadEnabled": target.setBulkheadEnabled(property(camelContext, java.lang.String.class, value)); return true;
        case "bulkheadexecutorservice":
        case "BulkheadExecutorService": target.setBulkheadExecutorService(property(camelContext, java.lang.String.class, value)); return true;
        case "bulkheadmaxconcurrentcalls":
        case "BulkheadMaxConcurrentCalls": target.setBulkheadMaxConcurrentCalls(property(camelContext, java.lang.String.class, value)); return true;
        case "bulkheadwaitingtaskqueue":
        case "BulkheadWaitingTaskQueue": target.setBulkheadWaitingTaskQueue(property(camelContext, java.lang.String.class, value)); return true;
        case "circuitbreaker":
        case "CircuitBreaker": target.setCircuitBreaker(property(camelContext, java.lang.String.class, value)); return true;
        case "delay":
        case "Delay": target.setDelay(property(camelContext, java.lang.String.class, value)); return true;
        case "failureratio":
        case "FailureRatio": target.setFailureRatio(property(camelContext, java.lang.String.class, value)); return true;
        case "id":
        case "Id": target.setId(property(camelContext, java.lang.String.class, value)); return true;
        case "requestvolumethreshold":
        case "RequestVolumeThreshold": target.setRequestVolumeThreshold(property(camelContext, java.lang.String.class, value)); return true;
        case "successthreshold":
        case "SuccessThreshold": target.setSuccessThreshold(property(camelContext, java.lang.String.class, value)); return true;
        case "timeoutduration":
        case "TimeoutDuration": target.setTimeoutDuration(property(camelContext, java.lang.String.class, value)); return true;
        case "timeoutenabled":
        case "TimeoutEnabled": target.setTimeoutEnabled(property(camelContext, java.lang.String.class, value)); return true;
        case "timeoutpoolsize":
        case "TimeoutPoolSize": target.setTimeoutPoolSize(property(camelContext, java.lang.String.class, value)); return true;
        case "timeoutscheduledexecutorservice":
        case "TimeoutScheduledExecutorService": target.setTimeoutScheduledExecutorService(property(camelContext, java.lang.String.class, value)); return true;
        default: return false;
        }
    }

    @Override
    public Map<String, Object> getAllOptions(Object target) {
        return ALL_OPTIONS;
    }

    @Override
    public Class<?> getOptionType(String name, boolean ignoreCase) {
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "bulkheadenabled":
        case "BulkheadEnabled": return java.lang.String.class;
        case "bulkheadexecutorservice":
        case "BulkheadExecutorService": return java.lang.String.class;
        case "bulkheadmaxconcurrentcalls":
        case "BulkheadMaxConcurrentCalls": return java.lang.String.class;
        case "bulkheadwaitingtaskqueue":
        case "BulkheadWaitingTaskQueue": return java.lang.String.class;
        case "circuitbreaker":
        case "CircuitBreaker": return java.lang.String.class;
        case "delay":
        case "Delay": return java.lang.String.class;
        case "failureratio":
        case "FailureRatio": return java.lang.String.class;
        case "id":
        case "Id": return java.lang.String.class;
        case "requestvolumethreshold":
        case "RequestVolumeThreshold": return java.lang.String.class;
        case "successthreshold":
        case "SuccessThreshold": return java.lang.String.class;
        case "timeoutduration":
        case "TimeoutDuration": return java.lang.String.class;
        case "timeoutenabled":
        case "TimeoutEnabled": return java.lang.String.class;
        case "timeoutpoolsize":
        case "TimeoutPoolSize": return java.lang.String.class;
        case "timeoutscheduledexecutorservice":
        case "TimeoutScheduledExecutorService": return java.lang.String.class;
        default: return null;
        }
    }

    @Override
    public Object getOptionValue(Object obj, String name, boolean ignoreCase) {
        org.apache.camel.model.FaultToleranceConfigurationDefinition target = (org.apache.camel.model.FaultToleranceConfigurationDefinition) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "bulkheadenabled":
        case "BulkheadEnabled": return target.getBulkheadEnabled();
        case "bulkheadexecutorservice":
        case "BulkheadExecutorService": return target.getBulkheadExecutorService();
        case "bulkheadmaxconcurrentcalls":
        case "BulkheadMaxConcurrentCalls": return target.getBulkheadMaxConcurrentCalls();
        case "bulkheadwaitingtaskqueue":
        case "BulkheadWaitingTaskQueue": return target.getBulkheadWaitingTaskQueue();
        case "circuitbreaker":
        case "CircuitBreaker": return target.getCircuitBreaker();
        case "delay":
        case "Delay": return target.getDelay();
        case "failureratio":
        case "FailureRatio": return target.getFailureRatio();
        case "id":
        case "Id": return target.getId();
        case "requestvolumethreshold":
        case "RequestVolumeThreshold": return target.getRequestVolumeThreshold();
        case "successthreshold":
        case "SuccessThreshold": return target.getSuccessThreshold();
        case "timeoutduration":
        case "TimeoutDuration": return target.getTimeoutDuration();
        case "timeoutenabled":
        case "TimeoutEnabled": return target.getTimeoutEnabled();
        case "timeoutpoolsize":
        case "TimeoutPoolSize": return target.getTimeoutPoolSize();
        case "timeoutscheduledexecutorservice":
        case "TimeoutScheduledExecutorService": return target.getTimeoutScheduledExecutorService();
        default: return null;
        }
    }
}

