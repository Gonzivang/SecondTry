/* Generated by camel build tools - do NOT edit this file! */
package org.apache.camel.component.hl7;

import org.apache.camel.CamelContext;
import org.apache.camel.CamelContextAware;
import org.apache.camel.DeferredContextBinding;
import org.apache.camel.Exchange;
import org.apache.camel.TypeConversionException;
import org.apache.camel.TypeConverterLoaderException;
import org.apache.camel.spi.TypeConverterLoader;
import org.apache.camel.spi.TypeConverterRegistry;
import org.apache.camel.support.SimpleTypeConverter;
import org.apache.camel.support.TypeConverterSupport;
import org.apache.camel.util.DoubleMap;

/**
 * Generated by camel build tools - do NOT edit this file!
 */
@SuppressWarnings("unchecked")
@DeferredContextBinding
public final class HL722ConverterLoader implements TypeConverterLoader, CamelContextAware {

    private CamelContext camelContext;

    public HL722ConverterLoader() {
    }

    @Override
    public void setCamelContext(CamelContext camelContext) {
        this.camelContext = camelContext;
    }

    @Override
    public CamelContext getCamelContext() {
        return camelContext;
    }

    @Override
    public void load(TypeConverterRegistry registry) throws TypeConverterLoaderException {
        try {
            registerConverters(registry);
        } catch (Throwable e) {
            // ignore on load error
        }
    }

    private void registerConverters(TypeConverterRegistry registry) {
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ACK.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toACK((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ACK.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toACK((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADR_A19.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdrA19((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADR_A19.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdrA19((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A04.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA04((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A04.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA04((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A05.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA05((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A05.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA05((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A06.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA06((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A06.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA06((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A07.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA07((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A07.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA07((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A08.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA08((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A08.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA08((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A09.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA09((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A09.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA09((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A10.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA10((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A10.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA10((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A11.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA11((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A11.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA11((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A12.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA12((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A12.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA12((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A13.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA13((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A13.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA13((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A14.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA14((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A14.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA14((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A15.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA15((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A15.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA15((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A16.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA16((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A16.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA16((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A17.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA17((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A17.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA17((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A18.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA18((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A18.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA18((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A20.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA20((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A20.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA20((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A21.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA21((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A21.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA21((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A22.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA22((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A22.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA22((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A23.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA23((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A23.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA23((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A24.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA24((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A24.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA24((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A25.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA25((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A25.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA25((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A26.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA26((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A26.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA26((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A27.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA27((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A27.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA27((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A28.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA28((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A28.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA28((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A29.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA29((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A29.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA29((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A30.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA30((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A30.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA30((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A31.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA31((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A31.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA31((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A32.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA32((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A32.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA32((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A33.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA33((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A33.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA33((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A34.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA34((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A34.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA34((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A35.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA35((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A35.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA35((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A36.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA36((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A36.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA36((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A37.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA37((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_A37.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtA37((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_AXX.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtAXX((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ADT_AXX.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toAdtAXX((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.BAR_P01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toBarP01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.BAR_P01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toBarP01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.BAR_P02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toBarP02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.BAR_P02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toBarP02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DFT_P03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDftP03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DFT_P03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDftP03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_P04.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrP04((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_P04.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrP04((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_Q01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrQ01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_Q01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrQ01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_Q03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrQ03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_Q03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrQ03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_R03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrR03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.DSR_R03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toDsrR03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFD_M01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfdM01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFD_M01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfdM01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFD_M02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfdM02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFD_M02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfdM02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFD_M03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfdM03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFD_M03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfdM03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFK_M01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfkM01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFK_M01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfkM01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFK_M02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfkM02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFK_M02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfkM02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFK_M03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfkM03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFK_M03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfkM03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFN_M01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfnM01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFN_M01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfnM01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFN_M02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfnM02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFN_M02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfnM02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFN_M03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfnM03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFN_M03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfnM03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFQ_M01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfqM01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFQ_M01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfqM01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFQ_M02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfqM02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFQ_M02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfqM02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFQ_M03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfqM03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFQ_M03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfqM03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFR_M01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfrM01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFR_M01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfrM01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFR_M02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfrM02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFR_M02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfrM02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFR_M03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfrM03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.MFR_M03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toMfrM03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.NMD_N01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toNmdN01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.NMD_N01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toNmdN01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.NMQ_N02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toNmqN02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.NMQ_N02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toNmqN02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.NMR_N02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toNmrN02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.NMR_N02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toNmrN02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORF_R04.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOrfR04((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORF_R04.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOrfR04((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORM_O01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOrmO01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORM_O01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOrmO01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORR_O02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOrrO02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORR_O02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOrrO02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORU_R01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOruR01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORU_R01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOruR01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORU_R03.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOruR03((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.ORU_R03.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toOruR03((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_A19.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryA19((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_A19.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryA19((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_P04.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryP04((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_P04.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryP04((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_Q01.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryQ01((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_Q01.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryQ01((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_Q02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryQ02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_Q02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryQ02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_R02.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryR02((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.QRY_R02.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toQryR02((java.lang.String) value));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.UDM_Q05.class, byte[].class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toUdmQ05((byte[]) value, exchange));
        addTypeConverter(registry, ca.uhn.hl7v2.model.v22.message.UDM_Q05.class, java.lang.String.class, false,
            (type, exchange, value) -> org.apache.camel.component.hl7.HL722Converter.toUdmQ05((java.lang.String) value));
    }

    private static void addTypeConverter(TypeConverterRegistry registry, Class<?> toType, Class<?> fromType, boolean allowNull, SimpleTypeConverter.ConversionMethod method) { 
        registry.addTypeConverter(toType, fromType, new SimpleTypeConverter(allowNull, method));
    }

}
