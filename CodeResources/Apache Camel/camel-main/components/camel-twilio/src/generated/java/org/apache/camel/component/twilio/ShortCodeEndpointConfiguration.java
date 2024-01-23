/*
 * Camel EndpointConfiguration generated by camel-api-component-maven-plugin
 */
package org.apache.camel.component.twilio;

import org.apache.camel.spi.ApiMethod;
import org.apache.camel.spi.ApiParam;
import org.apache.camel.spi.ApiParams;
import org.apache.camel.spi.Configurer;
import org.apache.camel.spi.UriParam;
import org.apache.camel.spi.UriParams;

/**
 * Camel endpoint configuration for {@link com.twilio.rest.api.v2010.account.ShortCode}.
 */
@ApiParams(apiName = "short-code", 
           description = "",
           apiMethods = {@ApiMethod(methodName = "fetcher", signatures={"com.twilio.rest.api.v2010.account.ShortCodeFetcher fetcher(String pathSid)", "com.twilio.rest.api.v2010.account.ShortCodeFetcher fetcher(String pathAccountSid, String pathSid)"}), @ApiMethod(methodName = "reader", signatures={"com.twilio.rest.api.v2010.account.ShortCodeReader reader()", "com.twilio.rest.api.v2010.account.ShortCodeReader reader(String pathAccountSid)"}), @ApiMethod(methodName = "updater", signatures={"com.twilio.rest.api.v2010.account.ShortCodeUpdater updater(String pathSid)", "com.twilio.rest.api.v2010.account.ShortCodeUpdater updater(String pathAccountSid, String pathSid)"}), }, aliases = {"^creator$=create", "^deleter$=delete", "^fetcher$=fetch", "^reader$=read", "^updater$=update"})
@UriParams
@Configurer(extended = true)
public final class ShortCodeEndpointConfiguration extends TwilioConfiguration {
    @UriParam
    @ApiParam(optional = false, apiMethods = {@ApiMethod(methodName = "fetcher"), @ApiMethod(methodName = "reader"), @ApiMethod(methodName = "updater")})
    private String pathAccountSid;
    @UriParam
    @ApiParam(optional = false, apiMethods = {@ApiMethod(methodName = "fetcher"), @ApiMethod(methodName = "updater")})
    private String pathSid;

    public String getPathAccountSid() {
        return pathAccountSid;
    }

    public void setPathAccountSid(String pathAccountSid) {
        this.pathAccountSid = pathAccountSid;
    }

    public String getPathSid() {
        return pathSid;
    }

    public void setPathSid(String pathSid) {
        this.pathSid = pathSid;
    }
}
