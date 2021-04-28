#version 330 core
// TODO: complete the loop for TP7 exercise 1

// ---- camera geometry
uniform mat4 model, projection, view;

// ---- skinning globals and attributes
const int MAX_VERTEX_BONES=4, MAX_BONES=128;
uniform mat4 bone_matrix[MAX_BONES];

// ---- vertex attributes
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec4 bone_ids;
layout(location = 3) in vec4 bone_weights;
layout(location = 4) in vec3 tex_coordinates;

// ----- interpolated attribute variables to be passed to fragment shader

out vec3 w_position, w_normal;

out vec2 frag_tex_coords;

void main() {

    // ------ creation of the skinning deformation matrix
    mat4 skin_matrix = mat4(0);
    if (bone_weights == vec4(0))
        skin_matrix = model;  // pas de poids de skinning: calcul de transformation à partir de model
    else {
        skin_matrix= mat4(0);
        for (int b=0; b < MAX_VERTEX_BONES; b++)
            skin_matrix +=  bone_weights[b] * bone_matrix[int(bone_ids[b])];
    }

    // ------ compute world and normalized eye coordinates of our vertex
    vec4 w_position4 = skin_matrix * vec4(position, 1.0);
    gl_Position = projection * view * w_position4;

    // fragment position in world coordinates
    w_position = w_position4.xyz / w_position4.w;  // dehomogenize

    // fragment normal in world coordinates
    mat3 nit_matrix = transpose(inverse(mat3(model)));
    w_normal = normalize(nit_matrix * normal);

    frag_tex_coords = tex_coordinates.xy;
}
