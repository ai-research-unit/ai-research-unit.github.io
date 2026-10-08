
# __Hermitian Forms and the Group Algebra__

## Introduction

A unitary representation is an action of the group that preserves a Hermitian form, and a Hermitian form on the group algebra that is compatible with the involution produces such an action by the GNS construction. The Hermitian forms on the group algebra are therefore the same object as the unitary representations, read through the algebra rather than through the group: a positive functional is a positive Hermitian form of a special kind, and a positive definite function is the form of a single vector. This article unfolds the correspondence. It fixes the Hermitian forms compatible with the involution, identifies the positive ones, relates them to the bilinear forms by the Cayley transform of the involution, and describes the unitary group of a form and the degeneracy that the construction must quotient out.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$, its involution and its product from *The Convolution Algebra $L^1(G)$*; the involution, the Hermitian elements, the positive cone and the positive functionals from *The Group Algebra as an Involutive Algebra*; the positive definite functions, the sesquilinear form and the GNS construction from *Positive Definite Functions and the Gelfand–Raikov Theorem*; the abstract Hermitian forms on a module over an involutive ring, their positivity and the unitary group they define from *Hermitian Forms over an Involution Ring and the Unitary Witt Group* and *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*; the `*`-representations, the Hilbert spaces and the bounded operators from *Operator Algebras*; and the abstract GNS construction from *The GNS Construction*. The adjoint of an operator on the group algebra is the `- * Operator Theory` group below; the measure-algebra involution is *The Involution on the Measure Algebra*, next; the Plancherel measure is *Unitary Representations and the Plancherel Theorem*, earlier in this group.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$; the algebra $\mathcal{A} = L^1(G)$ carries the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$. A **Hermitian form** on $\mathcal{A}$ is a map $B : \mathcal{A}\times\mathcal{A}\to\mathbb{C}$, conjugate-linear in the first variable and linear in the second, with

$$
B(f,g) = \overline{B(g,f)} \qquad (f,g\in\mathcal{A}) ;
$$

it is **positive semidefinite** when $B(f,f)\geq0$ for all $f$, **positive definite** when moreover $B(f,f) = 0$ forces $f = 0$, and **compatible** with the involution when the associativity identity below holds. The **$L^2$ form** is

$$
\langle f,g\rangle_2 = \int_G f(x)\,\overline{g(x)}\,dx .
$$

## The Standard Hermitian Forms

**Proposition (the $L^2$ form is positive definite).** The form $\langle\cdot,\cdot\rangle_2$ is Hermitian, positive definite, and invariant under left translation, $\langle L_xf, L_xg\rangle_2 = \langle f,g\rangle_2$ for $(L_xf)(y) = f(x^{-1}y)$; it is the form of the regular representation.

**Proof.** Hermitian symmetry and linearity are immediate; positive definiteness is the positivity of the integral of $|f|^2$; and left invariance is the left invariance of $dx$, which is the statement that the left regular representation is unitary for this form. $\square$

**Theorem (the forms of the positive functionals).** Let $\omega$ be a functional on $\mathcal{A}$ and set

$$
B_\omega(f,g) = \omega(g^*\!*f) .
$$

Then $B_\omega$ is Hermitian exactly when $\omega$ is Hermitian, $\omega(h^*) = \overline{\omega(h)}$, and $B_\omega$ is positive semidefinite exactly when $\omega$ is a positive functional, $\omega(h^*\!*h)\geq0$; in that case $B_\omega$ is compatible with the involution,

$$
B_\omega(h*f,\,g) = B_\omega(f,\,h^*\!*g) \qquad (f,g,h\in\mathcal{A}),
$$

and invariant under the left translations realised by the unitary elements, $B_\omega(L_xf,L_xg) = B_\omega(f,g)$ whenever $\delta_x$ acts.

**Proof.** Hermitian symmetry of $B_\omega$ is $\omega(g^*f) = \overline{\omega(f^*g)}$, which is the Hermitian property of $\omega$ because $(g^*f)^* = f^*g$. Positivity: $B_\omega(f,f) = \omega(f^*\!*f)\geq0$. Compatibility: $B_\omega(h*f,g) = \omega(g^*\!*h*\!f) = \omega((h^*\!*g)^*\!*f) = B_\omega(f,h^*\!*g)$, using $(h*g)^* = g^*\!*h^*$. Invariance: $L_xf = \delta_x*\!f$ and $\delta_x^*\!*\delta_x = \delta_e$. $\square$

**Corollary (the positive definite functions).** Every positive definite function $\phi$ of *Positive Definite Functions and the Gelfand–Raikov Theorem* gives a positive semidefinite Hermitian form

$$
B_\phi(f,g) = \int_G\int_G \phi(y^{-1}x)\,f(x)\,\overline{g(y)}\,dx\,dy ,
$$

and the assignment $\phi\mapsto B_\phi$ is the composition of the identification $\phi\leftrightarrow\omega_\phi$ of positive functionals with the theorem above; it is positive definite exactly when the GNS representation of $\phi$ is nondegenerate.

**Proof.** The double integral is $B_{\omega_\phi}$ after a change of variable and an application of Fubini; the positivity is the defining inequality for $\phi$, and its null space is the space $N$ quotiented out in the GNS construction. $\square$

## The Associated Unitary Representations

**Definition.** Let $B$ be a positive semidefinite Hermitian form on $\mathcal{A}$ compatible with the involution. The **null space** is $N_B = \{f : B(f,f) = 0\}$; the **associated Hilbert space** is the completion $\mathcal{H}_B$ of $\mathcal{A}/N_B$ for the induced inner product; and the **unitary group** of $B$ is

$$
U(B) = \{h\in\mathcal{A} : B(h*f,h*g) = B(f,g)\ \text{for all }f,g\} .
$$

**Theorem (compatibility gives the representation).** If $B = B_\omega$ for a positive functional $\omega$, then the quotient $\mathcal{A}/N_B$ carries a unique unitary representation $\pi_B$ with $\pi_B(x)(f + N_B) = L_xf + N_B$, and the vector $\xi_B = u + N_B$ of a normalised approximate identity is cyclic with $B_\omega(f,\xi_B) = \omega(f)$; the representation is the GNS representation of $\phi_\omega = \omega$ read on the group.

**Proof.** Compatibility makes $N_B$ a left ideal, so the quotient is a pre-Hilbert space; left translation preserves the form by the invariance in the theorem above, so it descends to a unitary, and multiplicativity of $L$ gives the representation. Cyclicity and the vector statement are the GNS construction of *Positive Definite Functions and the Gelfand–Raikov Theorem*. $\square$

**Theorem (the unitary group of the form).** For a positive semidefinite compatible $B$, the unitary group $U(B)$ is a group, the **form-preserving elements**, and the assignment $h\mapsto\pi_B(h)$ embeds $U(B)$ into the unitary group $\mathcal{U}(\mathcal{H}_B)$; the set $U(B)$ is closed in $\mathcal{A}$ in the strong topology of the representation, and it contains the unitary elements of any unital subalgebra on which $B$ is defined.

**Proof.** The composition of two form-preserving elements is form-preserving, and the identity is; the map $h\mapsto\pi_B(h)$ is multiplicative and preserves the form by definition, so its image is unitary. Closedness is the closedness of the isometry group of a Hilbert space under strong convergence, pulled back along the continuous representation. $\square$

## Hermitian and Bilinear Forms

**Theorem (the involution converts the two kinds of form).** Let $C$ be a bilinear form on $\mathcal{A}$, linear in both variables. Then

$$
B(f,g) = C(f,g^*) , \qquad C(f,g) = B(f,g^*)
$$

is Hermitian, $B(f,g) = \overline{B(g,f)}$, if and only if $C$ satisfies the compatibility

$$
C(f^*,g^*) = \overline{C(g,f)} ,
$$

and $B$ is positive semidefinite if and only if $C(f,f^*) = B(f,f)\geq0$ for all $f$; in particular the natural bilinear form $C(f,g) = \int_Gf(x)g(x^{-1})\Delta(x)^{-1}dx$ corresponds to the $L^2$ form.

**Proof.** Substitute $g^*$ for $g$ and use $g^{**} = g$, with the compatibility of $C$ in the form $C(a,b) = \overline{C(b^*,a^*)}$: then $B(g,f) = C(g,f^*) = \overline{C(f,g^*)} = \overline{B(f,g)}$, which is the Hermitian property, and conversely. The positivity statement is the substitution $g = f^*$, which gives $B(f,f) = C(f,f^*)$. The identification of $C$ with the $\langle\cdot,\cdot\rangle_2$ form is the substitution $g\to g^*$ in the integral, using $g^*(x^{-1}) = \overline{g(x)}\Delta(x)$ and $\Delta(x)\Delta(x)^{-1} = 1$. $\square$

**Corollary (real structures).** The map $B\mapsto C$ of the theorem is an involution on the set of forms, trading Hermitian forms for bilinear forms with the compatibility; the Hermitian form of a field of a representation is the image of its invariant bilinear form, and the two carry the same information whenever the involution is invertible on the algebra, which holds in the unital discrete case and, distributionally, in the measure algebra.

**Proof.** The two displayed identities are inverse to each other, and the compatibility of $C$ characterises the image. For a unital discrete group the involution is an invertible conjugation of the algebra and the correspondence is literal; in general one works with the involution in the multiplier algebra. $\square$

**Remark (degeneracy).** A positive semidefinite compatible form need not be definite, and the quotient by the null space is what the theory must take. The null space is a left ideal, so the quotient is an algebra quotient; the inner product it inherits is definite by construction, and the representation acts on it. A form whose null space is the whole algebra gives the zero representation; a form with trivial null space is a genuine inner product, and the corresponding representation is faithful on the image of the algebra.

## The Three-Way Correspondence

**Theorem (functions, functionals and forms).** The positive definite functions, the positive functionals and the compatible positive semidefinite Hermitian forms are related by

$$
\phi(x) = \omega(\text{point mass at }x), \qquad \omega(f) = \int_G f(x)\phi(x)\,dx, \qquad B(f,g) = \omega(g^*\!*f),
$$

so that the continuous positive definite functions stand in bijection with the positive functionals on the group algebra, and the positive functionals embed injectively into the compatible positive semidefinite Hermitian forms; on a unital algebra the last correspondence is a bijection, with inverse $\omega(f) = B(f,\delta_e)$, and in general the form recovers the functional only on the left ideal generated by an approximate identity. The associated unitary representations, the cyclic vectors modulo null space, and the classes of the forms under their unitary groups are carried along by these maps.

**Proof.** The first identity identifies a positive definite function $\phi$ with the functional $\omega_\phi(f) = \int f\phi$, and the second is its definition; the two are inverse by evaluation at the point masses, which are available in the measure algebra that contains $L^1(G)$. The third is the theorem on the forms of positive functionals; injectivity holds because $\omega(f) = B_\omega(f,\xi_B)$ for the class of an approximate identity, and in the unital case $\xi_B$ may be taken to be $\delta_e$. The transport of the representations is the GNS construction. $\square$

**Remark (what the article does not do).** The abstract theory of Hermitian forms over an involutive ring, the Witt group and the unitary group are *Hermitian Forms over an Involution Ring and the Unitary Witt Group* and *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*, cited and not restated. The adjoint of an operator with respect to one of these forms is the `- * Operator Theory` group of this category; the involution on the measure algebra and its adjoint of convolution are *The Involution on the Measure Algebra*, next; the positive definite functions and the GNS construction are the earlier article in this group, and the Plancherel measure is named only.

## Summary

A Hermitian form on the group algebra is conjugate-linear in the first variable, linear in the second and Hermitian; the $L^2$ form $\langle f,g\rangle_2 = \int f\overline{g}$ is positive definite and invariant under left translation; the form $B_\omega(f,g) = \omega(g^*\!*f)$ attached to a functional is Hermitian exactly when the functional is, and positive semidefinite exactly when the functional is positive; it is compatible with the involution, $B_\omega(h*f,g) = B_\omega(f,h^*\!*g)$, and invariant under the left translations by the unitary elements, so it descends to a unitary representation on the quotient by its null space, which is a left ideal, and the vector of an approximate identity is cyclic. Positive definite functions are the positive functionals are the compatible positive semidefinite forms, in a three-way bijection carried by $\phi\mapsto\omega\mapsto B$ and by the GNS construction; the unitary group of a form is the group of form-preserving elements, embedded in the unitary group of the representation space. Finally the involution converts a bilinear form into a Hermitian one by $B(f,g) = C(f,g^*)$ with the compatibility $C(f^*,g^*) = \overline{C(g,f)}$, and the two carry the same information whenever the involution is invertible. The adjoint of an operator with respect to these forms, the involution on the measure algebra and the Plancherel measure are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B$ | Hermitian form, $B(f,g) = \overline{B(g,f)}$ |
| $\langle f,g\rangle_2 = \int_Gf\overline{g}\,dx$ | The $L^2$ form, positive definite and left-invariant |
| $B_\omega(f,g) = \omega(g^*\!*f)$ | The form of a functional; positive iff $\omega$ is positive |
| $B_\omega(h*f,g) = B_\omega(f,h^*\!*g)$ | Compatibility with the involution |
| $N_B = \{f : B(f,f) = 0\}$ | The null space, a left ideal |
| $\mathcal{H}_B$ | The completion of $\mathcal{A}/N_B$ |
| $U(B)$ | The unitary group of the form |
| $B(f,g) = C(f,g^*)$ | The conversion of a bilinear form into a Hermitian one |
| $C(f^*,g^*) = \overline{C(g,f)}$ | The compatibility of the bilinear form $C$ |
| $\phi\leftrightarrow\omega\leftrightarrow B$ | The three-way correspondence |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for Hermitian forms over an involutive ring, their compatibility and the unitary group.
- Sterling K. Berberian, *Baer ${}^*$-Rings* (Springer, 1972), for Hermitian forms on an involutive algebra and the positive cone.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the GNS construction from a positive functional and the correspondence with cyclic representations.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for positive functionals on $L^1(G)$ and the positive definite functions they define.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the algebraic theory of forms over an involutive ring, cited and not used in detail.
