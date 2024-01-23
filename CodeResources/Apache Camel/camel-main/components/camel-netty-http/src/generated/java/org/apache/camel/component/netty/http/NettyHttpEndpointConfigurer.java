/* Generated by camel build tools - do NOT edit this file! */
package org.apache.camel.component.netty.http;

import java.util.Map;

import org.apache.camel.CamelContext;
import org.apache.camel.spi.ExtendedPropertyConfigurerGetter;
import org.apache.camel.spi.PropertyConfigurerGetter;
import org.apache.camel.spi.ConfigurerStrategy;
import org.apache.camel.spi.GeneratedPropertyConfigurer;
import org.apache.camel.util.CaseInsensitiveMap;
import org.apache.camel.component.netty.NettyEndpointConfigurer;

/**
 * Generated by camel build tools - do NOT edit this file!
 */
@SuppressWarnings("unchecked")
public class NettyHttpEndpointConfigurer extends NettyEndpointConfigurer implements GeneratedPropertyConfigurer, PropertyConfigurerGetter {

    @Override
    public boolean configure(CamelContext camelContext, Object obj, String name, Object value, boolean ignoreCase) {
        NettyHttpEndpoint target = (NettyHttpEndpoint) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "bridgeendpoint":
        case "bridgeEndpoint": target.getConfiguration().setBridgeEndpoint(property(camelContext, boolean.class, value)); return true;
        case "chunkedmaxcontentlength":
        case "chunkedMaxContentLength": target.getConfiguration().setChunkedMaxContentLength(property(camelContext, int.class, value)); return true;
        case "compression": target.getConfiguration().setCompression(property(camelContext, boolean.class, value)); return true;
        case "configuration": target.setConfiguration(property(camelContext, org.apache.camel.component.netty.http.NettyHttpConfiguration.class, value)); return true;
        case "cookiehandler":
        case "cookieHandler": target.setCookieHandler(property(camelContext, org.apache.camel.http.base.cookie.CookieHandler.class, value)); return true;
        case "disablestreamcache":
        case "disableStreamCache": target.getConfiguration().setDisableStreamCache(property(camelContext, boolean.class, value)); return true;
        case "headerfilterstrategy":
        case "headerFilterStrategy": target.setHeaderFilterStrategy(property(camelContext, org.apache.camel.spi.HeaderFilterStrategy.class, value)); return true;
        case "httpmethodrestrict":
        case "httpMethodRestrict": target.setHttpMethodRestrict(property(camelContext, java.lang.String.class, value)); return true;
        case "logwarnonbadrequest":
        case "logWarnOnBadRequest": target.getConfiguration().setLogWarnOnBadRequest(property(camelContext, boolean.class, value)); return true;
        case "mapheaders":
        case "mapHeaders": target.getConfiguration().setMapHeaders(property(camelContext, boolean.class, value)); return true;
        case "matchonuriprefix":
        case "matchOnUriPrefix": target.getConfiguration().setMatchOnUriPrefix(property(camelContext, boolean.class, value)); return true;
        case "maxchunksize":
        case "maxChunkSize": target.getConfiguration().setMaxChunkSize(property(camelContext, int.class, value)); return true;
        case "maxheadersize":
        case "maxHeaderSize": target.getConfiguration().setMaxHeaderSize(property(camelContext, int.class, value)); return true;
        case "maxinitiallinelength":
        case "maxInitialLineLength": target.getConfiguration().setMaxInitialLineLength(property(camelContext, int.class, value)); return true;
        case "muteexception":
        case "muteException": target.getConfiguration().setMuteException(property(camelContext, boolean.class, value)); return true;
        case "nettyhttpbinding":
        case "nettyHttpBinding": target.setNettyHttpBinding(property(camelContext, org.apache.camel.component.netty.http.NettyHttpBinding.class, value)); return true;
        case "nettysharedhttpserver":
        case "nettySharedHttpServer": target.setNettySharedHttpServer(property(camelContext, org.apache.camel.component.netty.http.NettySharedHttpServer.class, value)); return true;
        case "okstatuscoderange":
        case "okStatusCodeRange": target.getConfiguration().setOkStatusCodeRange(property(camelContext, java.lang.String.class, value)); return true;
        case "securityconfiguration":
        case "securityConfiguration": target.setSecurityConfiguration(property(camelContext, org.apache.camel.component.netty.http.NettyHttpSecurityConfiguration.class, value)); return true;
        case "securityoptions":
        case "securityOptions": target.setSecurityOptions(property(camelContext, java.util.Map.class, value)); return true;
        case "send503whensuspended":
        case "send503whenSuspended": target.getConfiguration().setSend503whenSuspended(property(camelContext, boolean.class, value)); return true;
        case "throwexceptiononfailure":
        case "throwExceptionOnFailure": target.getConfiguration().setThrowExceptionOnFailure(property(camelContext, boolean.class, value)); return true;
        case "traceenabled":
        case "traceEnabled": target.setTraceEnabled(property(camelContext, boolean.class, value)); return true;
        case "transferexception":
        case "transferException": target.getConfiguration().setTransferException(property(camelContext, boolean.class, value)); return true;
        case "urldecodeheaders":
        case "urlDecodeHeaders": target.getConfiguration().setUrlDecodeHeaders(property(camelContext, boolean.class, value)); return true;
        case "userelativepath":
        case "useRelativePath": target.getConfiguration().setUseRelativePath(property(camelContext, boolean.class, value)); return true;
        default: return super.configure(camelContext, obj, name, value, ignoreCase);
        }
    }

    @Override
    public Class<?> getOptionType(String name, boolean ignoreCase) {
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "bridgeendpoint":
        case "bridgeEndpoint": return boolean.class;
        case "chunkedmaxcontentlength":
        case "chunkedMaxContentLength": return int.class;
        case "compression": return boolean.class;
        case "configuration": return org.apache.camel.component.netty.http.NettyHttpConfiguration.class;
        case "cookiehandler":
        case "cookieHandler": return org.apache.camel.http.base.cookie.CookieHandler.class;
        case "disablestreamcache":
        case "disableStreamCache": return boolean.class;
        case "headerfilterstrategy":
        case "headerFilterStrategy": return org.apache.camel.spi.HeaderFilterStrategy.class;
        case "httpmethodrestrict":
        case "httpMethodRestrict": return java.lang.String.class;
        case "logwarnonbadrequest":
        case "logWarnOnBadRequest": return boolean.class;
        case "mapheaders":
        case "mapHeaders": return boolean.class;
        case "matchonuriprefix":
        case "matchOnUriPrefix": return boolean.class;
        case "maxchunksize":
        case "maxChunkSize": return int.class;
        case "maxheadersize":
        case "maxHeaderSize": return int.class;
        case "maxinitiallinelength":
        case "maxInitialLineLength": return int.class;
        case "muteexception":
        case "muteException": return boolean.class;
        case "nettyhttpbinding":
        case "nettyHttpBinding": return org.apache.camel.component.netty.http.NettyHttpBinding.class;
        case "nettysharedhttpserver":
        case "nettySharedHttpServer": return org.apache.camel.component.netty.http.NettySharedHttpServer.class;
        case "okstatuscoderange":
        case "okStatusCodeRange": return java.lang.String.class;
        case "securityconfiguration":
        case "securityConfiguration": return org.apache.camel.component.netty.http.NettyHttpSecurityConfiguration.class;
        case "securityoptions":
        case "securityOptions": return java.util.Map.class;
        case "send503whensuspended":
        case "send503whenSuspended": return boolean.class;
        case "throwexceptiononfailure":
        case "throwExceptionOnFailure": return boolean.class;
        case "traceenabled":
        case "traceEnabled": return boolean.class;
        case "transferexception":
        case "transferException": return boolean.class;
        case "urldecodeheaders":
        case "urlDecodeHeaders": return boolean.class;
        case "userelativepath":
        case "useRelativePath": return boolean.class;
        default: return super.getOptionType(name, ignoreCase);
        }
    }

    @Override
    public Object getOptionValue(Object obj, String name, boolean ignoreCase) {
        NettyHttpEndpoint target = (NettyHttpEndpoint) obj;
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "bridgeendpoint":
        case "bridgeEndpoint": return target.getConfiguration().isBridgeEndpoint();
        case "chunkedmaxcontentlength":
        case "chunkedMaxContentLength": return target.getConfiguration().getChunkedMaxContentLength();
        case "compression": return target.getConfiguration().isCompression();
        case "configuration": return target.getConfiguration();
        case "cookiehandler":
        case "cookieHandler": return target.getCookieHandler();
        case "disablestreamcache":
        case "disableStreamCache": return target.getConfiguration().isDisableStreamCache();
        case "headerfilterstrategy":
        case "headerFilterStrategy": return target.getHeaderFilterStrategy();
        case "httpmethodrestrict":
        case "httpMethodRestrict": return target.getHttpMethodRestrict();
        case "logwarnonbadrequest":
        case "logWarnOnBadRequest": return target.getConfiguration().isLogWarnOnBadRequest();
        case "mapheaders":
        case "mapHeaders": return target.getConfiguration().isMapHeaders();
        case "matchonuriprefix":
        case "matchOnUriPrefix": return target.getConfiguration().isMatchOnUriPrefix();
        case "maxchunksize":
        case "maxChunkSize": return target.getConfiguration().getMaxChunkSize();
        case "maxheadersize":
        case "maxHeaderSize": return target.getConfiguration().getMaxHeaderSize();
        case "maxinitiallinelength":
        case "maxInitialLineLength": return target.getConfiguration().getMaxInitialLineLength();
        case "muteexception":
        case "muteException": return target.getConfiguration().isMuteException();
        case "nettyhttpbinding":
        case "nettyHttpBinding": return target.getNettyHttpBinding();
        case "nettysharedhttpserver":
        case "nettySharedHttpServer": return target.getNettySharedHttpServer();
        case "okstatuscoderange":
        case "okStatusCodeRange": return target.getConfiguration().getOkStatusCodeRange();
        case "securityconfiguration":
        case "securityConfiguration": return target.getSecurityConfiguration();
        case "securityoptions":
        case "securityOptions": return target.getSecurityOptions();
        case "send503whensuspended":
        case "send503whenSuspended": return target.getConfiguration().isSend503whenSuspended();
        case "throwexceptiononfailure":
        case "throwExceptionOnFailure": return target.getConfiguration().isThrowExceptionOnFailure();
        case "traceenabled":
        case "traceEnabled": return target.isTraceEnabled();
        case "transferexception":
        case "transferException": return target.getConfiguration().isTransferException();
        case "urldecodeheaders":
        case "urlDecodeHeaders": return target.getConfiguration().isUrlDecodeHeaders();
        case "userelativepath":
        case "useRelativePath": return target.getConfiguration().isUseRelativePath();
        default: return super.getOptionValue(obj, name, ignoreCase);
        }
    }

    @Override
    public Object getCollectionValueType(Object target, String name, boolean ignoreCase) {
        switch (ignoreCase ? name.toLowerCase() : name) {
        case "securityoptions":
        case "securityOptions": return java.lang.Object.class;
        default: return super.getCollectionValueType(target, name, ignoreCase);
        }
    }
}

