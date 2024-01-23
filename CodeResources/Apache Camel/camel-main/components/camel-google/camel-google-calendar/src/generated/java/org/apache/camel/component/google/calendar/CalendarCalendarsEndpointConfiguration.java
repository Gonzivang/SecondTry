/*
 * Camel EndpointConfiguration generated by camel-api-component-maven-plugin
 */
package org.apache.camel.component.google.calendar;

import org.apache.camel.spi.ApiMethod;
import org.apache.camel.spi.ApiParam;
import org.apache.camel.spi.ApiParams;
import org.apache.camel.spi.Configurer;
import org.apache.camel.spi.UriParam;
import org.apache.camel.spi.UriParams;

/**
 * Camel endpoint configuration for {@link com.google.api.services.calendar.Calendar.Calendars}.
 */
@ApiParams(apiName = "calendars", 
           description = "The calendars collection of methods",
           apiMethods = {@ApiMethod(methodName = "clear", description="Clears a primary calendar", signatures={"com.google.api.services.calendar.Calendar$Calendars$Clear clear(String calendarId)"}), @ApiMethod(methodName = "delete", description="Deletes a secondary calendar", signatures={"com.google.api.services.calendar.Calendar$Calendars$Delete delete(String calendarId)"}), @ApiMethod(methodName = "get", description="Returns metadata for a calendar", signatures={"com.google.api.services.calendar.Calendar$Calendars$Get get(String calendarId)"}), @ApiMethod(methodName = "insert", description="Creates a secondary calendar", signatures={"com.google.api.services.calendar.Calendar$Calendars$Insert insert(com.google.api.services.calendar.model.Calendar content)"}), @ApiMethod(methodName = "patch", description="Updates metadata for a calendar", signatures={"com.google.api.services.calendar.Calendar$Calendars$Patch patch(String calendarId, com.google.api.services.calendar.model.Calendar content)"}), @ApiMethod(methodName = "update", description="Updates metadata for a calendar", signatures={"com.google.api.services.calendar.Calendar$Calendars$Update update(String calendarId, com.google.api.services.calendar.model.Calendar content)"})}, aliases = {})
@UriParams
@Configurer(extended = true)
public final class CalendarCalendarsEndpointConfiguration extends GoogleCalendarConfiguration {
    @UriParam
    @ApiParam(optional = false, apiMethods = {@ApiMethod(methodName = "clear", description="Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the primary keyword."), @ApiMethod(methodName = "delete", description="Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the primary keyword."), @ApiMethod(methodName = "get", description="Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the primary keyword."), @ApiMethod(methodName = "patch", description="Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the primary keyword."), @ApiMethod(methodName = "update", description="Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the primary keyword.")})
    private String calendarId;
    @UriParam
    @ApiParam(optional = false, apiMethods = {@ApiMethod(methodName = "insert", description="The com.google.api.services.calendar.model.Calendar"), @ApiMethod(methodName = "patch", description="The com.google.api.services.calendar.model.Calendar"), @ApiMethod(methodName = "update", description="The com.google.api.services.calendar.model.Calendar")})
    private com.google.api.services.calendar.model.Calendar content;

    public String getCalendarId() {
        return calendarId;
    }

    public void setCalendarId(String calendarId) {
        this.calendarId = calendarId;
    }

    public com.google.api.services.calendar.model.Calendar getContent() {
        return content;
    }

    public void setContent(com.google.api.services.calendar.model.Calendar content) {
        this.content = content;
    }
}
