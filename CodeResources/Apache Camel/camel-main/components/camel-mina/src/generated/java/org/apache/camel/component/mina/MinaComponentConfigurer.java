/* Generated by camel build tools - do NOT edit this file! */
package org.apache.camel.component.mina;

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
public class MinaComponentConfigurer extends PropertyConfigurerSupport implements GeneratedPropertyConfigurer, PropertyConfigurerGetter {

    private org.apache.camel.component.mina.MinaConfiguration getOrCreateConfiguration(MinaComponent target) {
        if (target.getConfiguration() == null) {
            target.setConfiguration(new org.apache.camel.component.mina.MinaConfiguration());
        }
        return target.getConfiguration();
    }

    @Override
    public boolean configure(CamelContext camelContext, Object obj, String name, Object value, boolean ignoreCase) {
        MinaComponent target = (MinaComponent) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "allowdefaultcodec":
        case "allowDefaultCodec": getOrCreateConfiguration(target).setAllowDefaultCodec(property(camelContext, boolean.class, value)); return true;
        case "autowiredenabled":
        case "autowiredEnabled": target.setAutowiredEnabled(property(camelContext, boolean.class, value)); return true;
        case "bridgeerrorhandler":
        case "bridgeErrorHandler": target.setBridgeErrorHandler(property(camelContext, boolean.class, value)); return true;
        case "cachedaddress":
        case "cachedAddress": getOrCreateConfiguration(target).setCachedAddress(property(camelContext, boolean.class, value)); return true;
        case "clientmode":
        case "clientMode": getOrCreateConfiguration(target).setClientMode(property(camelContext, boolean.class, value)); return true;
        case "codec": getOrCreateConfiguration(target).setCodec(property(camelContext, org.apache.mina.filter.codec.ProtocolCodecFactory.class, value)); return true;
        case "configuration": target.setConfiguration(property(camelContext, org.apache.camel.component.mina.MinaConfiguration.class, value)); return true;
        case "decodermaxlinelength":
        case "decoderMaxLineLength": getOrCreateConfiguration(target).setDecoderMaxLineLength(property(camelContext, int.class, value)); return true;
        case "disconnect": getOrCreateConfiguration(target).setDisconnect(property(camelContext, boolean.class, value)); return true;
        case "disconnectonnoreply":
        case "disconnectOnNoReply": getOrCreateConfiguration(target).setDisconnectOnNoReply(property(camelContext, boolean.class, value)); return true;
        case "encodermaxlinelength":
        case "encoderMaxLineLength": getOrCreateConfiguration(target).setEncoderMaxLineLength(property(camelContext, int.class, value)); return true;
        case "encoding": getOrCreateConfiguration(target).setEncoding(property(camelContext, java.lang.String.class, value)); return true;
        case "filters": getOrCreateConfiguration(target).setFilters(property(camelContext, java.util.List.class, value)); return true;
        case "lazysessioncreation":
        case "lazySessionCreation": getOrCreateConfiguration(target).setLazySessionCreation(property(camelContext, boolean.class, value)); return true;
        case "lazystartproducer":
        case "lazyStartProducer": target.setLazyStartProducer(property(camelContext, boolean.class, value)); return true;
        case "maximumpoolsize":
        case "maximumPoolSize": getOrCreateConfiguration(target).setMaximumPoolSize(property(camelContext, int.class, value)); return true;
        case "minalogger":
        case "minaLogger": getOrCreateConfiguration(target).setMinaLogger(property(camelContext, boolean.class, value)); return true;
        case "noreplyloglevel":
        case "noReplyLogLevel": getOrCreateConfiguration(target).setNoReplyLogLevel(property(camelContext, org.apache.camel.LoggingLevel.class, value)); return true;
        case "orderedthreadpoolexecutor":
        case "orderedThreadPoolExecutor": getOrCreateConfiguration(target).setOrderedThreadPoolExecutor(property(camelContext, boolean.class, value)); return true;
        case "sslcontextparameters":
        case "sslContextParameters": getOrCreateConfiguration(target).setSslContextParameters(property(camelContext, org.apache.camel.support.jsse.SSLContextParameters.class, value)); return true;
        case "sync": getOrCreateConfiguration(target).setSync(property(camelContext, boolean.class, value)); return true;
        case "textline": getOrCreateConfiguration(target).setTextline(property(camelContext, boolean.class, value)); return true;
        case "textlinedelimiter":
        case "textlineDelimiter": getOrCreateConfiguration(target).setTextlineDelimiter(property(camelContext, org.apache.camel.component.mina.MinaTextLineDelimiter.class, value)); return true;
        case "timeout": getOrCreateConfiguration(target).setTimeout(property(camelContext, long.class, value)); return true;
        case "transferexchange":
        case "transferExchange": getOrCreateConfiguration(target).setTransferExchange(property(camelContext, boolean.class, value)); return true;
        case "useglobalsslcontextparameters":
        case "useGlobalSslContextParameters": target.setUseGlobalSslContextParameters(property(camelContext, boolean.class, value)); return true;
        case "writetimeout":
        case "writeTimeout": getOrCreateConfiguration(target).setWriteTimeout(property(camelContext, long.class, value)); return true;
        default: return false;
        }
    }

    @Override
    public Class<?> getOptionType(String name, boolean ignoreCase) {
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "allowdefaultcodec":
        case "allowDefaultCodec": return boolean.class;
        case "autowiredenabled":
        case "autowiredEnabled": return boolean.class;
        case "bridgeerrorhandler":
        case "bridgeErrorHandler": return boolean.class;
        case "cachedaddress":
        case "cachedAddress": return boolean.class;
        case "clientmode":
        case "clientMode": return boolean.class;
        case "codec": return org.apache.mina.filter.codec.ProtocolCodecFactory.class;
        case "configuration": return org.apache.camel.component.mina.MinaConfiguration.class;
        case "decodermaxlinelength":
        case "decoderMaxLineLength": return int.class;
        case "disconnect": return boolean.class;
        case "disconnectonnoreply":
        case "disconnectOnNoReply": return boolean.class;
        case "encodermaxlinelength":
        case "encoderMaxLineLength": return int.class;
        case "encoding": return java.lang.String.class;
        case "filters": return java.util.List.class;
        case "lazysessioncreation":
        case "lazySessionCreation": return boolean.class;
        case "lazystartproducer":
        case "lazyStartProducer": return boolean.class;
        case "maximumpoolsize":
        case "maximumPoolSize": return int.class;
        case "minalogger":
        case "minaLogger": return boolean.class;
        case "noreplyloglevel":
        case "noReplyLogLevel": return org.apache.camel.LoggingLevel.class;
        case "orderedthreadpoolexecutor":
        case "orderedThreadPoolExecutor": return boolean.class;
        case "sslcontextparameters":
        case "sslContextParameters": return org.apache.camel.support.jsse.SSLContextParameters.class;
        case "sync": return boolean.class;
        case "textline": return boolean.class;
        case "textlinedelimiter":
        case "textlineDelimiter": return org.apache.camel.component.mina.MinaTextLineDelimiter.class;
        case "timeout": return long.class;
        case "transferexchange":
        case "transferExchange": return boolean.class;
        case "useglobalsslcontextparameters":
        case "useGlobalSslContextParameters": return boolean.class;
        case "writetimeout":
        case "writeTimeout": return long.class;
        default: return null;
        }
    }

    @Override
    public Object getOptionValue(Object obj, String name, boolean ignoreCase) {
        MinaComponent target = (MinaComponent) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "allowdefaultcodec":
        case "allowDefaultCodec": return getOrCreateConfiguration(target).isAllowDefaultCodec();
        case "autowiredenabled":
        case "autowiredEnabled": return target.isAutowiredEnabled();
        case "bridgeerrorhandler":
        case "bridgeErrorHandler": return target.isBridgeErrorHandler();
        case "cachedaddress":
        case "cachedAddress": return getOrCreateConfiguration(target).isCachedAddress();
        case "clientmode":
        case "clientMode": return getOrCreateConfiguration(target).isClientMode();
        case "codec": return getOrCreateConfiguration(target).getCodec();
        case "configuration": return target.getConfiguration();
        case "decodermaxlinelength":
        case "decoderMaxLineLength": return getOrCreateConfiguration(target).getDecoderMaxLineLength();
        case "disconnect": return getOrCreateConfiguration(target).isDisconnect();
        case "disconnectonnoreply":
        case "disconnectOnNoReply": return getOrCreateConfiguration(target).isDisconnectOnNoReply();
        case "encodermaxlinelength":
        case "encoderMaxLineLength": return getOrCreateConfiguration(target).getEncoderMaxLineLength();
        case "encoding": return getOrCreateConfiguration(target).getEncoding();
        case "filters": return getOrCreateConfiguration(target).getFilters();
        case "lazysessioncreation":
        case "lazySessionCreation": return getOrCreateConfiguration(target).isLazySessionCreation();
        case "lazystartproducer":
        case "lazyStartProducer": return target.isLazyStartProducer();
        case "maximumpoolsize":
        case "maximumPoolSize": return getOrCreateConfiguration(target).getMaximumPoolSize();
        case "minalogger":
        case "minaLogger": return getOrCreateConfiguration(target).isMinaLogger();
        case "noreplyloglevel":
        case "noReplyLogLevel": return getOrCreateConfiguration(target).getNoReplyLogLevel();
        case "orderedthreadpoolexecutor":
        case "orderedThreadPoolExecutor": return getOrCreateConfiguration(target).isOrderedThreadPoolExecutor();
        case "sslcontextparameters":
        case "sslContextParameters": return getOrCreateConfiguration(target).getSslContextParameters();
        case "sync": return getOrCreateConfiguration(target).isSync();
        case "textline": return getOrCreateConfiguration(target).isTextline();
        case "textlinedelimiter":
        case "textlineDelimiter": return getOrCreateConfiguration(target).getTextlineDelimiter();
        case "timeout": return getOrCreateConfiguration(target).getTimeout();
        case "transferexchange":
        case "transferExchange": return getOrCreateConfiguration(target).isTransferExchange();
        case "useglobalsslcontextparameters":
        case "useGlobalSslContextParameters": return target.isUseGlobalSslContextParameters();
        case "writetimeout":
        case "writeTimeout": return getOrCreateConfiguration(target).getWriteTimeout();
        default: return null;
        }
    }

    @Override
    public Object getCollectionValueType(Object target, String name, boolean ignoreCase) {
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "filters": return org.apache.mina.core.filterchain.IoFilter.class;
        default: return null;
        }
    }
}

