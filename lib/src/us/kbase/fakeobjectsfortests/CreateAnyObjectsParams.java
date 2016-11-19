
package us.kbase.fakeobjectsfortests;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: CreateAnyObjectsParams</p>
 * <pre>
 * ws_id/ws_name - two alternative ways to set target workspace,
 * obj_names - list of names for target workspace objects,
 * metadata - optional metadata.
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "ws_id",
    "ws_name",
    "obj_names",
    "metadata"
})
public class CreateAnyObjectsParams {

    @JsonProperty("ws_id")
    private Long wsId;
    @JsonProperty("ws_name")
    private java.lang.String wsName;
    @JsonProperty("obj_names")
    private List<String> objNames;
    @JsonProperty("metadata")
    private Map<String, String> metadata;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("ws_id")
    public Long getWsId() {
        return wsId;
    }

    @JsonProperty("ws_id")
    public void setWsId(Long wsId) {
        this.wsId = wsId;
    }

    public CreateAnyObjectsParams withWsId(Long wsId) {
        this.wsId = wsId;
        return this;
    }

    @JsonProperty("ws_name")
    public java.lang.String getWsName() {
        return wsName;
    }

    @JsonProperty("ws_name")
    public void setWsName(java.lang.String wsName) {
        this.wsName = wsName;
    }

    public CreateAnyObjectsParams withWsName(java.lang.String wsName) {
        this.wsName = wsName;
        return this;
    }

    @JsonProperty("obj_names")
    public List<String> getObjNames() {
        return objNames;
    }

    @JsonProperty("obj_names")
    public void setObjNames(List<String> objNames) {
        this.objNames = objNames;
    }

    public CreateAnyObjectsParams withObjNames(List<String> objNames) {
        this.objNames = objNames;
        return this;
    }

    @JsonProperty("metadata")
    public Map<String, String> getMetadata() {
        return metadata;
    }

    @JsonProperty("metadata")
    public void setMetadata(Map<String, String> metadata) {
        this.metadata = metadata;
    }

    public CreateAnyObjectsParams withMetadata(Map<String, String> metadata) {
        this.metadata = metadata;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((("CreateAnyObjectsParams"+" [wsId=")+ wsId)+", wsName=")+ wsName)+", objNames=")+ objNames)+", metadata=")+ metadata)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
