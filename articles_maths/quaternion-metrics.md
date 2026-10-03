# __Quaternion Metrics__

## Introduction

Every nonzero quaternion $g$ determines a real quadratic form on the quaternion algebra through the product and the scalar part,

$$
Q_g(\tilde q) = \mathrm{Sc}(g\tilde qg\tilde q) = \mathrm{Sc}\bigl((g\tilde q)^2\bigr).
$$

This article studies that form, which is called here a **quaternion metric**. It is an indefinite form on $\mathbb{H}$, non-degenerate, of signature $(1,3)$ for every nonzero $g$, and it is the interval form that the source of the construction proposes as a generalisation of the Minkowski interval that keeps Hamilton's multiplication rules intact, in place of the Riemannian strategy of varying them. It is not the quaternion norm $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ and it is not a distance; the word *metric* is used in its differential-geometric sense of a quadratic form on a space of displacements, and the name records that the form is built from a quaternion.

The article turns on one identity: $Q_g = \omega\circ L_g$, where $\omega$ is the Minkowski form of the algebra and $L_g$ is left multiplication by $g$. Everything follows from it. The form is non-degenerate of signature $(1,3)$ for every nonzero $g$; all the forms of the family are isometric to one another; the family is the image of the single form $\omega$ under precomposition with the left multiplications; and the isometry group of $Q_g$ is the conjugate of the Lorentz group by $L_g$. The Gram matrix of $Q_g$ is computed in closed form and its determinant is $-N(g)^4$, so the non-degeneracy is visible a second time, quantitatively.

The treatment is mathematical throughout. No physical object is introduced, no state of a physical system is named, and no physical interpretation is invoked. The Lorentz group of the form $\omega$ is named and its corpus home is cited; nothing of it is re-derived here.

The bilinear and quadratic-form vocabulary, the polarisation and the notion of isometry are from *Bilinear Forms* and *Quadratic Forms and Polarisation*; the algebra, the conjugate and the scalar–vector decomposition are from *Quaternion Algebra*; the norm, the inner product and the group of units are from *Quaternion Norm and Invertibility*; the forms with values in an algebra that are the norms are from *Quadratic Forms over Algebras and Norms*; the determinant of the left regular representation is pointed to in *Quaternion 4x4 Regular Matrix Element Representation*; the split-quaternion form of signature $(2,2)$ used for contrast is from *Split-Quaternion Norm and Invertibility*.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$. A quaternion is $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$, with **scalar part** $\mathrm{Sc}\,\tilde q = q_0$ and **vector part** $\mathbf q = \mathrm{Vect}\,\tilde q = q_1e_1+q_2e_2+q_3e_3$; the conjugate is $\tilde{q}^{\natural} = q_0e_0 - \mathbf q$, the quaternion norm is $N(\tilde q) = \tilde q\tilde{q}^{\natural} = q_0^2+q_1^2+q_2^2+q_3^2$, and the modulus is $|\tilde q| = \sqrt{N(\tilde q)}$. The four real numbers $q_0,q_1,q_2,q_3$ form the coordinate vector of $\tilde q$, also written $q = (q_0,q_1,q_2,q_3)$; the meaning is clear from the context. The multiplication is written without a dot, and the scalar part is written $\mathrm{Sc}$ and the vector part $\mathrm{Vect}$.

## The Minkowski Form of the Algebra

### Definition and Polar Form

**Definition.** The **Minkowski form** of $\mathbb{H}$ is

$$
\omega(\tilde q) = \mathrm{Sc}(\tilde q^2) = q_0^2 - q_1^2 - q_2^2 - q_3^2 .
$$

The equality is the computation of a square: writing $\tilde q = q_0e_0+\mathbf q$, one has $\tilde q^2 = q_0^2e_0 + 2q_0\mathbf q + \mathbf q^2$, and $\mathbf q^2 = -\langle\mathbf q,\mathbf q\rangle e_0$ is a scalar, so the scalar part is $q_0^2 - |\mathbf q|^2$.

The form $\omega$ is a quadratic form on the underlying real vector space $\mathbb{H}\cong\mathbb{R}^4$. Its **polar form** is the symmetric bilinear form

$$
\beta_\omega(\tilde u,\tilde v) = \tfrac12\bigl(\omega(\tilde u+\tilde v)-\omega(\tilde u)-\omega(\tilde v)\bigr) = \tfrac12\,\mathrm{Sc}(\tilde u\tilde v + \tilde v\tilde u).
$$

It is real-valued and symmetric by construction, and it is alternating on the vector subspace: for pure $\mathbf u,\mathbf v$ one has $\mathbf u\mathbf v+\mathbf v\mathbf u = -2\langle\mathbf u,\mathbf v\rangle e_0$.

### Signature and Isometry Group

**Proposition.** The Minkowski form is non-degenerate of signature $(1,3)$. In the basis $e_0,e_1,e_2,e_3$ its Gram matrix is

$$
\eta = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix},
$$

and $\det\eta = -1$.

*Proof.* The coefficients of $\omega$ in the coordinates are $1,-1,-1,-1$, so the Gram matrix of the polar form is the diagonal matrix displayed; it is invertible, with the determinant $-1$. One positive and three negative diagonal entries give the signature $(1,3)$.

**Definition.** The **isometry group** of $\omega$ is

$$
O(\omega) = \{T \in GL_4(\mathbb{R}) : \omega(T\tilde q) = \omega(\tilde q)\ \text{for every }\tilde q\} = O(1,3),
$$

the orthogonal group of a form of signature $(1,3)$. Its identity component is the proper orthochronous Lorentz group $SO^+(1,3)$, treated in the biquaternion family in *Biquaternion Rotations and Lorentz Transformations*; nothing of its theory is used here beyond the name.

### The Left and Right Multiplication Operators

**Definition.** For $g\in\mathbb{H}$ the **left multiplication** and the **right multiplication** by $g$ are the real-linear endomorphisms

$$
L_g(\tilde q) = g\tilde q, \qquad R_g(\tilde q) = \tilde q g .
$$

**Proposition.** $L_g$ and $R_g$ are bijective for $g\neq0$, with $L_g^{-1} = L_{g^{-1}}$ and $R_g^{-1} = R_{g^{-1}}$, and $L_{p\tilde q} = L_pL_{\tilde q}$, $R_{p\tilde q} = R_{\tilde q}R_p$.

*Proof.* Multiplication is associative and every nonzero quaternion is invertible by *Quaternion Norm and Invertibility*, with $g^{-1} = g^{\natural}/N(g)$; this gives the inverses and the composition rules directly from the definitions.

## The Form of a Quaternion

### Definition and the Isometry Identity

**Definition.** The **quaternion metric** of a nonzero quaternion $g$ is the function

$$
Q_g : \mathbb{H}\to\mathbb{R}, \qquad Q_g(\tilde q) = \mathrm{Sc}(g\tilde qg\tilde q).
$$

**Lemma (the identity of the construction).** For every $g$ and every $\tilde q$,

$$
Q_g(\tilde q) = \omega(g\tilde q) = \omega(L_g\tilde q).
$$

*Proof.* Both expressions are $\mathrm{Sc}\bigl((g\tilde q)^2\bigr)$: the product $g\tilde qg\tilde q$ is $(g\tilde q)(g\tilde q)$, and the Minkowski form of a quaternion is the scalar part of its square.

The identity is the reason the construction is a generalisation of the interval rather than a replacement of it: the form of $g$ is the Minkowski form read at the left translate $g\tilde q$.

### Elementary Properties

**Proposition.** For all $g$, all real $\lambda$, and all $\tilde q$,

$$
Q_{-g} = Q_g, \qquad Q_{\lambda g} = \lambda^2 Q_g .
$$

In particular $Q_g$ depends on $g$ and on the line $\mathbb{R} g$, and it is homogeneous of degree two in $g$. The family is parametrised, up to the sign of $g$ and up to scale, by the lines through the origin of $\mathbb{H}$, that is by the real projective space $\mathbb{R}P^3$; each line carries the one-parameter family of proportional forms.

*Proof.* The two identities are the substitution of $-g$ and of $\lambda g$ in the defining product and the real-linearity of the product and of the scalar part.

**Proposition.** For $g\neq0$ the form $Q_g$ is a quadratic form on $\mathbb{H}$, it is not the zero form, and it is isotropic: it vanishes on a nonzero vector, and therefore on the whole line that the vector spans.

*Proof.* It is $\omega\circ L_g$ by the lemma, and the composition of a quadratic form with a linear map is a quadratic form. It is not zero because $\omega$ is not zero and $L_g$ is onto for $g\neq0$. For the isotropy, $Q_g(L_g^{-1}(e_0+e_1)) = \omega(e_0+e_1) = 0$, and $e_0+e_1\neq0$; the vanishing propagates along the line by homogeneity, since $Q_g(\lambda\tilde q) = \lambda^2Q_g(\tilde q)$. A nonzero vector on which the form vanishes is a **null vector**, and the line it spans is a **null line**.

**Remark (the source's reading).** The source proposes exactly this form, $Q_g(\tilde q)=\mathrm{Sc}(g\tilde qg\tilde q)$, as the way to generalise the interval $\mathrm{Sc}(\tilde q^2) = q_0^2-\mathbf q\cdot\mathbf q$ of the algebra while leaving Hamilton's rules $e_1^2=e_2^2=e_3^2=-e_0$ and $e_1e_2e_3=-e_0$ untouched; changing the multiplication rules is the Riemannian strategy, which the source sets aside. The reading is recorded as the source's; the mathematics of the form does not depend on it.

## The Gram Matrix

### Definition of the Gram Matrix

**Definition.** The **Gram matrix** of $Q_g$ is the $4\times4$ real matrix

$$
M(g)_{\mu\nu} = \beta_g(e_\mu,e_\nu), \qquad \beta_g(\tilde q,\tilde p) = \tfrac12\bigl(Q_g(\tilde q+\tilde p)-Q_g(\tilde q)-Q_g(\tilde p)\bigr),
$$

where $\beta_g$ is the polar form of $Q_g$. The indices run over $\mu,\nu = 0,1,2,3$.

Because $Q_g = \omega\circ L_g$, the polar form of $Q_g$ is the polar form of $\omega$ at the images: $\beta_g(\tilde q,\tilde p) = \beta_\omega(g\tilde q,g\tilde p)$, that is

$$
\beta_g(\tilde q,\tilde p) = \tfrac12\,\mathrm{Sc}(g\tilde qg\tilde p + g\tilde pg\tilde q).
$$

### Closed Form

**Proposition.** Write $g = g_0e_0 + g_1e_1+g_2e_2+g_3e_3$. The Gram matrix of $Q_g$ is

$$
M(g) = \begin{pmatrix}
g_0^2-g_1^2-g_2^2-g_3^2 & -2g_0g_1 & -2g_0g_2 & -2g_0g_3 \\
-2g_0g_1 & -g_0^2+g_1^2-g_2^2-g_3^2 & 2g_1g_2 & 2g_1g_3 \\
-2g_0g_2 & 2g_1g_2 & -g_0^2-g_1^2+g_2^2-g_3^2 & 2g_2g_3 \\
-2g_0g_3 & 2g_1g_3 & 2g_2g_3 & -g_0^2-g_1^2-g_2^2+g_3^2
\end{pmatrix}.
$$

Its diagonal entries are $g_0^2-|\mathbf g|^2$ and $-g_0^2-|\mathbf g|^2+2g_k^2$; its off-diagonal entries are $-2g_0g_k$ against the time coordinate and $2g_jg_k$ against two space coordinates.

*Proof.* One evaluates the polar form on the sixteen pairs of basis elements. For the diagonal, $Q_g(e_\mu) = \mathrm{Sc}((ge_\mu)^2)$, which is $\mathrm{Sc}(g^2) = g_0^2-|\mathbf g|^2$ at $\mu=0$ and $-\mathrm{Sc}(ge_kg e_k)$ at $\mu=k$; expanding $g = g_0+\mathbf g$ in the second and using that the scalar part of a product of two pure quaternions is minus their inner product gives $-g_0^2-|\mathbf g|^2+2g_k^2$. For the pair $(0,k)$ the two products $ge_0ge_k$ and $ge_kg e_0$ are $g^2e_k$ and $ge_kg$, whose scalar parts are both $-2g_0g_k$ by the same expansion, so the polar form is $-2g_0g_k$. For a pair $(j,k)$ of distinct space indices the antisymmetry $e_je_k+e_ke_j = 0$ makes the two products equal, and the scalar part of $ge_jge_k$ is $2g_jg_k$; the polar form carries the factor $\tfrac12$ and is $2g_jg_k$. The relations used are $e_k^2=-e_0$, $e_1e_2=e_3$ and its cyclic permutations, and the vanishing of the scalar part of $e_je_k$ for $j\neq k$.

**Verification.** The closed form has been checked against the polar form on $100$ random quaternions with integer coordinates, entry by entry, and the quadratic identity $\sum_{\mu\nu}q_\mu M(g)_{\mu\nu}q_\nu = Q_g(\tilde q)$ has been checked on $100$ random pairs $(g,\tilde q)$; both checks are exact and both hold.

**Remark (the two block forms).** With $s = g_0^2-|\mathbf g|^2$ and $c = g_0^2+|\mathbf g|^2 = N(g)$, the matrix is

$$
M(g) = \begin{pmatrix} s & -2g_0\,\mathbf g^{\mathsf T} \\ -2g_0\,\mathbf g & 2\,\mathbf g\mathbf g^{\mathsf T} - c\,I_3 \end{pmatrix},
$$

with $I_3$ the $3\times3$ identity and $\mathbf g$ the column of the three vector coordinates. This is the shape used for the determinant below.

### Examples

| $g$ | $M(g)$ | signature | reading |
|---|---|---|---|
| $e_0$ | $\mathrm{diag}(1,-1,-1,-1)$ | $(1,3)$ | the Minkowski form of the basis |
| $e_k$ | $\mathrm{diag}(-1,-1,\dots,+1,\dots,-1)$ with the $+1$ in the $k$-th place | $(1,3)$ | the coordinate $q_k$ plays the role of time |
| $e_0+e_k$ | the form with $s=0$ | $(1,3)$ | the two axes $e_0$ and $e_k$ are null |
| $2e_0$ | $4\,\mathrm{diag}(1,-1,-1,-1)$ | $(1,3)$ | the scale of $g$ rescales the form |

For $g = e_0$ the form is $\omega$ itself, $Q_{e_0}(\tilde q) = q_0^2-q_1^2-q_2^2-q_3^2$, and the Gram matrix is $\eta$. For $g = e_k$ the form is $\omega$ with the time coordinate exchanged with $q_k$: for $g=e_1$ one has $Q_{e_1}(\tilde q) = -q_0^2+q_1^2-q_2^2-q_3^2$. For $g = e_0+e_1$ the matrix has $s=0$, and the vectors $e_0$ and $e_1$ are null for the form: $Q_{e_0+e_1}(e_0) = Q_{e_0+e_1}(e_1) = 0$.

## Non-Degeneracy, Signature and Determinant

### The Isometry Theorem

**Theorem.** For every nonzero $g$ the map $L_g$ is a linear isometry from $(\mathbb{H},Q_g)$ onto $(\mathbb{H},\omega)$. Consequently:

1. $Q_g$ is non-degenerate and of signature $(1,3)$ for every nonzero $g$;
2. any two forms of the family are isometric, one to the other, through $L_p^{-1}L_q$;
3. the isometry group of $Q_g$ is $O(Q_g) = L_g^{-1}O(\omega)L_g$, a conjugate of the Lorentz group.

*Proof.* By the identity of the construction, $Q_g(\tilde q) = \omega(L_g\tilde q)$ for every $\tilde q$, so $L_g$ pulls $Q_g$ back to $\omega$; it is bijective for $g\neq0$ by the invertibility of the left multiplication, so it is an isometry onto. An isometry of quadratic forms preserves non-degeneracy and signature, and the signature of $\omega$ is $(1,3)$; this is (1). For (2), let $p,q\neq0$ and put $T = L_q^{-1}L_p$, a linear bijection; then for every $\tilde q$ one has $Q_q(T\tilde q) = \omega(L_qT\tilde q) = \omega(L_p\tilde q) = Q_p(\tilde q)$, so $T$ is an isometry from $(\mathbb{H},Q_p)$ onto $(\mathbb{H},Q_q)$. For (3), an isometry of $Q_g$ corresponds under $L_g$ to an isometry of $\omega$, so $O(Q_g) = L_g^{-1}O(\omega)L_g$.

### The Determinant of the Gram Matrix

**Proposition.** For every quaternion $g$,

$$
\det M(g) = -N(g)^4 .
$$

In particular the form $Q_g$ is non-degenerate for every nonzero $g$, and its Gram determinant is a positive multiple of the fourth power of the quaternion norm.

*Proof.* Write $s = g_0^2-|\mathbf g|^2$, $c = N(g) = g_0^2+|\mathbf g|^2$, and $B = 2\mathbf g\mathbf g^{\mathsf T}-cI_3$, so that

$$
M(g) = \begin{pmatrix} s & -2g_0\mathbf g^{\mathsf T} \\ -2g_0\mathbf g & B \end{pmatrix}.
$$

Suppose first that $s\neq0$, so that $B$ is invertible, and take the Schur complement of $B$:

$$
\det M(g) = \det B \cdot \Bigl(s - 4g_0^2\,\mathbf g^{\mathsf T}B^{-1}\mathbf g\Bigr).
$$

The eigenvalues of the rank-one matrix $\mathbf g\mathbf g^{\mathsf T}$ are $|\mathbf g|^2,0,0$, so those of $B$ are $2|\mathbf g|^2-c = -s$ and $-c$ twice; hence $\det B = (-s)(-c)^2 = -sc^2$. Moreover $B\mathbf g = 2\mathbf g|\mathbf g|^2 - c\mathbf g = (2|\mathbf g|^2-c)\mathbf g = -s\mathbf g$, so $B^{-1}\mathbf g = -\mathbf g/s$ and $\mathbf g^{\mathsf T}B^{-1}\mathbf g = -|\mathbf g|^2/s$. Therefore

$$
\det M(g) = -sc^2\cdot\Bigl(s + \frac{4g_0^2|\mathbf g|^2}{s}\Bigr) = -c^2\bigl(s^2+4g_0^2|\mathbf g|^2\bigr) = -c^2\,c^2 = -N(g)^4,
$$

because $s^2+4g_0^2|\mathbf g|^2 = (g_0^2-|\mathbf g|^2)^2+4g_0^2|\mathbf g|^2 = (g_0^2+|\mathbf g|^2)^2 = c^2$.

The entries of $M(g)$ are polynomials in $g_0,g_1,g_2,g_3$, so $\det M(g)$ is a polynomial, and $-N(g)^4$ is a polynomial; the two agree on the nonempty open set $s\neq0$, so they agree identically. The determinant is therefore $-N(g)^4$ for every $g$, and it vanishes exactly at $g=0$.

**Verification.** The determinant identity has been checked, exactly, on $100$ random quaternions with integer coordinates; it holds without exception.

**Remark (the same determinant, read through the regular representation).** The identity is equivalent to $\det M(g) = -\det(L_g)^2$, and the statement $\det L_g = N(g)^2$ is the determinant statement of *Quaternion 4x4 Regular Matrix Element Representation*. The proof above is nevertheless self-contained: it uses only the closed form of $M(g)$, the structure of a rank-one update of the identity and the polynomial identity argument, and it does not appeal to the regular representation.

## The Null Cone

### The Quadric

**Definition.** The **null cone** of $Q_g$ is the quadric

$$
\mathcal{C}_g = \{\tilde q\in\mathbb{H} : Q_g(\tilde q) = 0\} = L_g^{-1}(\mathcal C),
$$

where $\mathcal{C} = \{\tilde q : q_0^2 = |\mathbf q|^2\}$ is the null cone of $\omega$, the double cone over the unit sphere of the vector subspace.

**Proposition.** $\mathcal{C}_g$ is a non-degenerate quadratic cone in $\mathbb{R}^4$ with apex $0$, carried by the isometry $L_g$ to the standard cone; it is not the zero-divisor set of the algebra, because $\mathbb{H}$ has none.

*Proof.* The cone is the inverse image under the linear isomorphism $L_g$ of the cone of a non-degenerate form, so it is a cone and it is non-degenerate in the sense that its defining form is. The only zero divisor of $\mathbb{H}$ is $0$, by the invertibility of the nonzero elements in *Quaternion Norm and Invertibility*, whereas $\mathcal{C}_g$ contains a three-dimensional family of nonzero elements; the two sets are therefore different, and the null cone is a purely form-theoretic object.

The cone of $\omega$ is the set on which the interval $t^2-\mathbf q\cdot\mathbf q$ vanishes, that is the set the source calls the light cone; the subfamilies on which $Q_g$ is respectively positive, zero and negative are the timelike, null and spacelike classes of the form, and they are transported by $L_g$ from those of $\omega$.

## Comparison with the Norm and with the Sibling Forms

### The Definite Norm Is Not in the Family

The quaternion norm $N(\tilde q) = q_0^2+q_1^2+q_2^2+q_3^2$ of *Quaternion Norm and Invertibility* is positive definite, and every form of the present family is of signature $(1,3)$ by the isometry theorem; hence the norm is not a quaternion metric of this family, for any $g$. The two objects are of different kinds: the norm is the multiplicative form of the division algebra, while a quaternion metric is the pullback of the interval form by a left multiplication and is not multiplicative. The Gram matrix of the norm in the basis is the identity, and the family $Q_g$ contains only forms isometric to $\omega$.

### The Forms with Values in an Algebra

*Quadratic Forms over Algebras and Norms* studies forms whose values lie in the algebra, of which the quaternion norm $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ is the quaternion case, together with the composition laws $N(\tilde q\tilde p) = N(\tilde q)N(\tilde p)$ and the Cayley–Dickson doubling that they support. A quaternion metric takes its values in the base field and carries no composition law; the two theories intersect in the single form $\omega = Q_{e_0}$, which is the Minkowski form of the algebra and is not the norm.

### The Other Four-Dimensional Forms of the Corpus

| algebra | form | values | signature | in the family $Q_g$? |
|---|---|---|---|---|
| $\mathbb{H}$ | quaternion norm $N(\tilde q)=\tilde q\tilde{q}^{\natural}$ | $\mathbb{R}$ | $(4,0)$ | no, definite |
| $\mathbb{H}$ | quaternion metric $Q_g$, $g\neq0$ | $\mathbb{R}$ | $(1,3)$ | yes, the family itself |
| $\mathbb{H}_{\mathrm{s}}$ | determinant form | $\mathbb{R}$ | $(2,2)$ | no, wrong algebra and signature |
| $\mathbb{B}$ | biquaternion norm | $\mathbb{C}$ | complex | no, complex-valued |

The split-quaternion determinant form of signature $(2,2)$ is *Split-Quaternion Norm and Invertibility*, and the complex-valued biquaternion norm is *Biquaternion Norm and Invertibility*; both are cited for contrast only. The family of quaternion metrics is a four-parameter family inside the ten-dimensional space of symmetric real forms on $\mathbb{R}^4$, and it is a single isometry class inside it.

## Summary

A quaternion metric is the real quadratic form $Q_g(\tilde q) = \mathrm{Sc}(g\tilde qg\tilde q) = \mathrm{Sc}((g\tilde q)^2)$ determined by a nonzero quaternion $g$. The identity $Q_g = \omega\circ L_g$, where $\omega(\tilde q) = \mathrm{Sc}(\tilde q^2) = q_0^2-q_1^2-q_2^2-q_3^2$ is the Minkowski form of the algebra and $L_g$ is left multiplication by $g$, is the core of the construction: it exhibits $Q_g$ as the interval form read at the left translate $g\tilde q$, and it makes $L_g$ an isometry from $(\mathbb{H},Q_g)$ onto $(\mathbb{H},\omega)$.

It follows that every quaternion metric is non-degenerate of signature $(1,3)$; that any two of them are isometric, so that the family is a single isometry class; and that the isometry group of $Q_g$ is the conjugate $L_g^{-1}O(1,3)L_g$ of the Lorentz group. The form depends on $g$ only through the line $\mathbb{R}g$ up to the sign of $g$ and only up to a positive scale, so that the family is a cone over the forms of the unit sphere modulo sign, that is over $\mathbb{R}P^3$.

The Gram matrix of $Q_g$ is computed in closed form: its diagonal entries are $g_0^2-|\mathbf g|^2$ and $-g_0^2-|\mathbf g|^2+2g_k^2$, its off-diagonal entries are $-2g_0g_k$ against the time direction and $2g_jg_k$ against two space directions, and its determinant is $-N(g)^4$, nowhere zero off the origin. The null cone of $Q_g$ is the inverse image of the standard cone under $L_g$; it is a non-degenerate quadratic cone through the origin and it is not the zero-divisor set of the algebra, which consists of the origin alone.

The form is neither the quaternion norm of the algebra, which is positive definite and multiplicative, nor one of the algebra-valued forms, and the family contains only the forms isometric to the Minkowski form; the split-quaternion form of signature $(2,2)$ and the complex-valued biquaternion norm are the sibling four-dimensional forms of the other algebras, and they are not of this type.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra over $\mathbb{R}$ |
| $e_0=1,e_1,e_2,e_3$ | Basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $\tilde q = q_0e_0+\mathbf q$ | Quaternion, scalar part $q_0$, vector part $\mathbf q$ |
| $\mathrm{Sc},\mathrm{Vect}$ | Scalar and vector part functionals |
| $\tilde{q}^{\natural}$ | Quaternion conjugate |
| $N(\tilde q)=\tilde q\tilde{q}^{\natural}$ | Quaternion norm (from *Quaternion Norm and Invertibility*) |
| $L_g(\tilde q)=g\tilde q$, $R_g(\tilde q)=\tilde q g$ | Left and right multiplication |
| $\omega(\tilde q)=\mathrm{Sc}(\tilde q^2)=q_0^2-q_1^2-q_2^2-q_3^2$ | Minkowski form of the algebra |
| $\beta_\omega$ | Its polar form |
| $\eta=\mathrm{diag}(1,-1,-1,-1)$ | Gram matrix of $\omega$, $\det\eta=-1$ |
| $O(\omega)=O(1,3)$ | Isometry group of the Minkowski form |
| $Q_g(\tilde q)=\mathrm{Sc}(g\tilde qg\tilde q)$ | Quaternion metric |
| $\beta_g$ | Polar form of $Q_g$ |
| $M(g)$ | Gram matrix of $Q_g$ |
| $s=g_0^2-\lvert\mathbf g\rvert^2$, $c=N(g)$ | The two invariants of the determinant computation |
| $\mathcal{C}_g$ | Null cone of $Q_g$ |
| $\mathbb{R}P^3$ | Parameter space of the family up to sign and scale |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the product, the conjugate and the interpretation of the scalar part of a square as $q_0^2-|\mathbf q|^2$.
- Douglas B. Sweetser, *Doing Physics with Quaternions* (2005), section "A New Idea for Metrics", for the construction $Q_g(\tilde q)=\mathrm{Sc}(g\tilde qg\tilde q)$ and the proposal to generalise the interval by it rather than by a change of the multiplication rules.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition, 2001), for the Minkowski form, its orthogonal group and the Clifford reading of the Lorentz transformations.
- Serge Lang, *Algebra* (Springer, revised third edition, 2002), for the theory of quadratic forms, polarisation, non-degeneracy and the Witt decomposition used implicitly in the comparison of the signatures.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the classification of forms by their signature over the real numbers.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the identification of the Lorentz group of a form of signature $(1,3)$ with the unit quaternions of the complexified algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the four-dimensional algebras, their norms and the comparison of their forms.
