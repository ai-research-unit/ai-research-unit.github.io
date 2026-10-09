# __The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form__

## Introduction

The layer of *Sesqualgebras with a Form* asks of an object three things: a base $(R,\varsigma)$ with an involution, an $R$-algebra with a $\varsigma$-semilinear involution $*$, and a Hermitian form **compatible with the product**, $h(xy,z) = h(y,x^{*}z)$. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four distinguished pairings, and this article reads it through those three requirements: one of the four satisfies all of them, one more is Hermitian and sesquilinear but fails the compatibility, and the remaining two are bilinear rather than sesquilinear, because both of their slot maps are $\mathbb{C}$-linear. The article is the entry of the biquaternion region from the general layer: it fixes which of the algebra's forms is an object, which is a form on the algebra only, and which belongs to the bilinear layer, and it names the articles in which each is developed.

The classification is a single dichotomy, in the two slots of a pairing. The four pairings are the scalars $\operatorname{Sc}(X\tilde{P}Y\tilde{Q})$ of the four general products, with $X$ one of $\mathrm{id}, {}^{\natural}$ and $Y$ one of $\mathrm{id}, {}^{*}$; the map $\mathrm{id}$ is $\mathbb{C}$-linear, ${}^{\natural}$ is $\mathbb{C}$-linear as well, and ${}^{*}$ is $\mathbb{C}$-antilinear. A pairing is **bilinear** when both slots are linear and **sesquilinear** when exactly one of them is, so the two pairings carrying $Y = \mathrm{id}$ are bilinear and the two carrying $Y = {}^{*}$ are sesquilinear, of which the one with $X = \mathrm{id}$ is the Hermitian positive definite form of the layer and the one with $X = {}^{\natural}$ is the indefinite form whose fundamental symmetry is ${}^{\natural}$ itself. The compatibility is then a computation in $\operatorname{Sc}$-cyclicity, and it selects exactly one: the adjoint of the left multiplication $L_{\tilde{Q}}$ is $L_{\tilde{Q}^{*}}$ for the general plain sesquilinear form and the **right** multiplication $R_{\bar{\tilde{Q}}}$ for the quaternion one, the second moving the multiplication to the right, so the general quaternionic sesquilinear form is a Hermitian form on the algebra and not a form of the layer.

The article reads the four pairings through the layer's vocabulary, verifies the compatibility of the general plain sesquilinear form and the failure of the compatibility of the quaternion one, reads the indefinite form as the definite one composed with a canonical self-adjoint involution, places the unitary elements, records the caution on the linear natural conjugation and the collapse at the real base, and points to the region's articles. The four pairings, their Gram matrices, signatures, isometry groups and the adjoint rules of the left multiplications are *The Four Pairings of the Biquaternion Algebra*; the general plain sesquilinear form and its inner-product structure are *Biquaternion Norm and Invertibility*; the symmetry ${}^{\natural}$, its uniqueness and the bridge identity are *The Fundamental Symmetry of the Biquaternion Algebra*; the failure of the compatibility as a caution about the two layers is *The Indefinite Case and the Signature*, §*The Biquaternion Caution*; the unitary elements and their group are *The Unitary Group of the Biquaternion Algebra*; the norm of the positive definite form is *The Norm Defined by a Form*; the layer's definition, its radical and its collapse are *Sesqualgebras with a Form*; the inequality of the positive definite form is *The Cauchy–Schwarz Inequality for Continuous Sesquilinear Maps*; the positivity and the positive cone are *Positivity and the Positive Cone of a Hermitian Form*; the operators are *Unitary and Isometric Operators of the Form* and *The Adjoint under a Hermitian Form*; the real base is *The Realification of the Four Forms* and *Operators of the Real Biquaternion Algebra*; and the algebra structures are *Introduction to the General Plain Sesqualgebra of Biquaternions* and *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the coefficient basis $\tilde{Q} = Q_{0} + Q_{1}e_{1} + Q_{2}e_{2} + Q_{3}e_{3}$, $Q_{\mu} \in \mathbb{C}$, the products $e_{k}^{2} = -1$ and $e_{1}e_{2} = e_{3}$ cyclic, and $\operatorname{Sc}$ the scalar part, as in *Introduction to the General Plain Algebra of Biquaternions*. The three conjugations of the algebra are the **complex conjugation** $\bar{\cdot}$, the **natural conjugation** ${}^{\natural}$ with $e_{k}^{\natural} = -e_{k}$, and the **Hermitian conjugation** ${}^{*} = {}^{\natural} \circ \bar{\cdot} = \bar{\cdot} \circ {}^{\natural}$, with $\bar{\cdot}$ a $\mathbb{C}$-antilinear automorphism, ${}^{\natural}$ a $\mathbb{C}$-linear anti-automorphism and ${}^{*}$ a $\mathbb{C}$-antilinear anti-automorphism, the three of *The Three Conjugations and the Symmetric Biquaternion Fractals*. The four pairings are those of *The Four Pairings of the Biquaternion Algebra*,

$$
\langle\tilde{P},\tilde{Q}\rangle = \operatorname{Sc}(\tilde{P}\tilde{Q}), \quad
\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q}), \quad
\langle\tilde{P},\tilde{Q}\rangle_{*} = \operatorname{Sc}(\tilde{P}\tilde{Q}^{*}), \quad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}),
$$

with $\varepsilon = (1,-1,-1,-1)$ so that $\operatorname{Sc}(e_{\mu}e_{\nu}) = \varepsilon_{\mu}\delta_{\mu\nu}$; the layer's datum is $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation, the layer's involution is ${}^{*}$, and the layer's form is $\langle\tilde{P},\tilde{Q}\rangle_{*}$, linear in the first slot and $\varsigma$-semilinear in the second, the convention of *Sesqualgebras with a Form*, §*The Definition*.

## The Two Slots and the Two Layers

### The Linearity of the Two Slot Maps

**Proposition (the linearity of the four slot maps).** For $\lambda \in \mathbb{C}$ and $\tilde{Q} \in \mathbb{B}$,

$$
(\lambda\tilde{Q})^{\natural} = \lambda\,\tilde{Q}^{\natural}, \qquad
\overline{\lambda\tilde{Q}} = \varsigma(\lambda)\,\bar{\tilde{Q}}, \qquad
(\lambda\tilde{Q})^{*} = \varsigma(\lambda)\,\tilde{Q}^{*} .
$$

Hence ${}^{\natural}$ is $\mathbb{C}$-linear, and $\bar{\cdot}$ and ${}^{*}$ are $\mathbb{C}$-antilinear, that is $\varsigma$-semilinear for the conjugation $\varsigma$.

*Proof.* The natural conjugation acts on the units, $e_{k}^{\natural} = -e_{k}$, and fixes the centre $\mathbb{C}$, so it commutes with the scalars; the complex conjugation acts on the coefficients, hence conjugates the scalar; the Hermitian conjugation is the composite, and a composite of one linear and one antilinear map is antilinear. $\square$

**Proposition (which pairings are sesquilinear).** A pairing $\operatorname{Sc}(X\tilde{P}\,Y\tilde{Q})$ is $\mathbb{C}$-bilinear when both slot maps are linear and $\mathbb{C}$-sesquilinear when exactly one is. Of the four pairings of the conventions, the two with $\mathrm{id}$ in the second slot, $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, are bilinear, and the two with ${}^{*}$ there, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, are sesquilinear, linear in the first slot and $\varsigma$-semilinear in the second.

*Proof.* The scalar part is $\mathbb{C}$-linear and $\operatorname{Sc}(\overline{X}) = \varsigma(\operatorname{Sc}(X))$, so a $\mathbb{C}$-antilinear map in a slot makes the pairing antilinear in that slot and a $\mathbb{C}$-linear one keeps it linear. $\square$

**Remark (the two layers of the algebra).** The proposition is the entry of the biquaternion algebra into two categories at once. The bilinear pairings are the forms of the bilinear layer, *Bilinear Forms*, developed on the algebra in *The Four Pairings of the Biquaternion Algebra*; the sesquilinear pairings are the forms of the layer of *Sesqualgebras with a Form*, and only one of them is admissible, as the next section shows. The dichotomy is not a property of the particular forms but of the products: the algebra carries the two linear slot maps $\mathrm{id}$ and ${}^{\natural}$ and the two antilinear ones $\bar{\cdot}$ and ${}^{*}$, and a pairing $\operatorname{Sc}(X\tilde{P}Y\tilde{Q})$ is sesquilinear exactly when its second slot carries one of the antilinear maps.

### The Admissible Involution

**Proposition (the conjugations of the algebra, by linearity kind).** The conjugations $\mathrm{id}$ and ${}^{\natural}$ are $\mathbb{C}$-linear and the conjugations $\bar{\cdot}$ and ${}^{*}$ are $\mathbb{C}$-antilinear; ${}^{\natural}$ and ${}^{*}$ are anti-automorphisms and $\mathrm{id}$ and $\bar{\cdot}$ are automorphisms; and ${}^{*}$ alone is both, hence the layer's involution. The natural conjugation ${}^{\natural}$ is a $\mathbb{C}$-linear anti-automorphism of square one, hence an involution over the real base $(\mathbb{R},\mathrm{id})$ but not a $\varsigma$-semilinear involution for the complex datum; the complex conjugation $\bar{\cdot}$ is a $\varsigma$-semilinear **auto**morphism of square one, hence not an involution of the algebra in the layer's sense, which asks for $(xy)^{*} = y^{*}x^{*}$; and the reversal $\flat = -{}^{*}$ of *The Four Pairings of the Biquaternion Algebra*, §*The Involution Group and the Four Pairings*, is an anti-automorphism only up to sign and stands outside the Klein four-group $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$.

*Proof.* The four conjugations, their linearity, their product type, the identity ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and the reversal $\flat = -{}^{*}$ are the table of *The Four Pairings of the Biquaternion Algebra*, §*The Involution Group and the Four Pairings*; the linearity of the slot maps is the preceding proposition. $\square$

**Remark (why the caution is about ${}^{\natural}$ and not about $\bar{\cdot}$).** The automorphic conjugation $\bar{\cdot}$ is antilinear, so the pairing it produces, $\operatorname{Sc}(\tilde{P}\bar{\tilde{Q}})$, is sesquilinear; the anti-automorphic ${}^{\natural}$ is linear, so the pairing it produces is bilinear. The layer's involution is therefore ${}^{*}$ and not ${}^{\natural}$: the two properties required of it, the $\varsigma$-semilinearity and the anti-automorphism, are exactly what separates the complex sesquilinear pairing from the quaternion bilinear one, and the algebra carries one form of each kind because it carries one conjugation of each kind. This is the caution of the article, and it is the source of the phrase "the same algebra, two categories".

## The Hermitian Forms and Their Compatibility

### The General plain Sesquilinear Form

**Theorem (the general plain sesquilinear form is an object of the layer).** The form

$$
h(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{*} = \operatorname{Sc}(\tilde{P}\tilde{Q}^{*}) = \sum_{\mu}P_{\mu}\,\varsigma(Q_{\mu})
$$

is Hermitian, positive definite and nondegenerate with Gram matrix $\mathrm{I}_{4}$ in the coefficient basis and signature $(8,0)$ over $\mathbb{R}$, its radical is zero, its norm is the Euclidean norm $\lVert\tilde{Q}\rVert_{E} = (\sum_{\mu}\lvert Q_{\mu}\rvert^{2})^{1/2}$, and it is **compatible with the product**:

$$
h(\tilde{P}\tilde{Q},\tilde{R}) = h(\tilde{Q},\tilde{P}^{*}\tilde{R}), \qquad \text{equivalently} \qquad (L_{\tilde{P}})^{h} = L_{\tilde{P}^{*}} .
$$

Hence $(\mathbb{B},{}^{*},h)$ is an object of the layer, the left multiplications of the sesqualgebra $\tilde{P} \star \tilde{X} = \tilde{P}\tilde{X}^{*}$ are the layer's $\varsigma$-semilinear operators and the right multiplications its $R$-linear ones, and every operator statement of the layer applies to it as *The Left and Right Multiplications of the Biquaternion Sesqualgebra* records.

*Proof.* The Hermitian property is $\operatorname{Sc}(\tilde{P}\tilde{Q}^{*}) = \varsigma(\operatorname{Sc}(\tilde{Q}\tilde{P}^{*}))$, and the diagonal is $\sum_{\mu}\lvert Q_{\mu}\rvert^{2}$, coefficientwise, so the form is positive definite and its Gram matrix is $\mathrm{I}_{4}$; this is *The Four Pairings of the Biquaternion Algebra*, §*The Four Pairings* and §*The Forms in Comparison*, and the Hilbert structure is *Biquaternion Norm and Invertibility*, §*The Inner Product*. For the compatibility, expand the right side,

$$
h(\tilde{Q},\tilde{P}^{*}\tilde{R}) = \operatorname{Sc}\bigl(\tilde{Q}(\tilde{P}^{*}\tilde{R})^{*}\bigr) = \operatorname{Sc}(\tilde{Q}\tilde{R}^{*}\tilde{P}) = \operatorname{Sc}(\tilde{P}\tilde{Q}\tilde{R}^{*}) = h(\tilde{P}\tilde{Q},\tilde{R}),
$$

using $(\tilde{P}^{*}\tilde{R})^{*} = \tilde{R}^{*}\tilde{P}$ and the cyclicity $\operatorname{Sc}(XYZ) = \operatorname{Sc}(ZXY)$ of the scalar part, which holds in an associative algebra because $\operatorname{Sc}$ is the trace of the regular representation. The adjoint rule is the same identity read as $(L_{\tilde{P}})^{h} = L_{\tilde{P}^{*}}$, the second of the four rules of *The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*. $\square$

**Corollary (the inequality and the positivity are the layer's).** The form is positive definite and the object is of the layer, so the inequality, the norm of the diagonal, the positive cone, the tolerance and the definite quotient are the layer's: they are *The Cauchy–Schwarz Inequality for Continuous Sesquilinear Maps*, *The Norm Defined by a Form* and *Positivity and the Positive Cone of a Hermitian Form*, and they are read on the coefficient space because the Gram matrix is the identity.

### The General quaternionic Sesquilinear Form

**Theorem (the general quaternionic sesquilinear form is Hermitian and not admissible).** The form

$$
g(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = \sum_{\mu}\varepsilon_{\mu}P_{\mu}\,\varsigma(Q_{\mu}) = \operatorname{Sc}(\tilde{P}\bar{\tilde{Q}})
$$

is Hermitian and nondegenerate with Gram matrix $\mathrm{E} = \operatorname{diag}(1,-1,-1,-1)$, of inertia index $(1,3,0)$ over $\mathbb{C}$ and signature $(2,6)$ over $\mathbb{R}$, indefinite with the diagonal $\lvert Q_{0}\rvert^{2} - \lvert Q_{1}\rvert^{2} - \lvert Q_{2}\rvert^{2} - \lvert Q_{3}\rvert^{2}$, and it is **not compatible** with the product. The adjoint of the left multiplication is the **right** multiplication,

$$
(L_{\tilde{P}})^{g} = R_{\bar{\tilde{P}}}, \qquad \text{that is} \qquad g(\tilde{P}\tilde{Q},\tilde{R}) = g(\tilde{Q},\tilde{R}\bar{\tilde{P}}),
$$

and the compatibility identity $g(\tilde{P}\tilde{Q},\tilde{R}) = g(\tilde{Q},\tilde{P}^{*}\tilde{R})$ fails at a witness.

*Proof.* The form is the fourth pairing of *The Four Pairings of the Biquaternion Algebra*, and its Gram matrix, its inertia and its signature are §*The Forms in Comparison*; the Hermitian property is $\sum_{\mu}\varepsilon_{\mu}P_{\mu}\varsigma(Q_{\mu}) = \varsigma(\sum_{\mu}\varepsilon_{\mu}Q_{\mu}\varsigma(P_{\mu}))$, coefficientwise. For the adjoint rule, expand $g(\tilde{Q},\tilde{R}\bar{\tilde{P}}) = \operatorname{Sc}\bigl(\tilde{Q}\,\overline{\tilde{R}\bar{\tilde{P}}}\bigr)$, and $\overline{\tilde{R}\bar{\tilde{P}}} = \bar{\tilde{R}}\tilde{P}$ because $\bar{\cdot}$ is an automorphism of square one, so $g(\tilde{Q},\tilde{R}\bar{\tilde{P}}) = \operatorname{Sc}(\tilde{Q}\bar{\tilde{R}}\tilde{P}) = \operatorname{Sc}(\tilde{P}\tilde{Q}\bar{\tilde{R}}) = g(\tilde{P}\tilde{Q},\tilde{R})$ by cyclicity. The failure of the compatibility with $L_{\tilde{P}^{*}}$ is exhibited at the units $\tilde{P} = e_{1}$, $\tilde{Q} = e_{0}$, $\tilde{R} = e_{1}$: the left side is $g(e_{1}e_{0},e_{1}) = g(e_{1},e_{1}) = -1$, and the right side is $g(e_{0},e_{1}^{*}e_{1}) = g(e_{0},e_{0}) = 1$, so the two differ. $\square$

**Remark (the form is on the algebra and not of the layer).** The theorem is the caution of *The Indefinite Case and the Signature*, §*The Biquaternion Caution*, read in the layer's vocabulary. The compatibility $h(xz,w) = h(z,x^{*}w)$ is the axiom that makes the left multiplications of the algebra the layer's adjointable operators; here the adjoint of $L_{\tilde{P}}$ is the right multiplication $R_{\bar{\tilde{P}}}$, so the quaternion form is Hermitian and nondegenerate on the algebra without being a form of the layer, and the operator theory of *Unitary and Isometric Operators of the Form* does not apply to it. The form is nonetheless the one the Krein structure of the algebra uses, *The Krein Gram Matrix and the Restrictions of the Form* and *The Fundamental Symmetry of the Biquaternion Algebra*, and the point of the article is that being Hermitian and nondegenerate is not being of the layer.

## The Fundamental Symmetry and the Two Forms

### The Bridge Identity

**Theorem (the indefinite form is the definite one composed with a self-adjoint involution).** The natural conjugation $\tilde{Q} \mapsto \tilde{Q}^{\natural}$ is an $h$-self-adjoint involution, $\natural^{2} = \mathrm{id}$ and $h(\tilde{P}^{\natural},\tilde{Q}) = h(\tilde{P},\tilde{Q}^{\natural})$, with the centre $\mathbb{C}e_{0}$ as its $+1$-eigenspace and the vector subspace $\mathbb{C}e_{1} \oplus \mathbb{C}e_{2} \oplus \mathbb{C}e_{3} = \{Q_{0} = 0\}$ as its $-1$-eigenspace, of complex dimensions $(1,3)$ and real dimensions $(2,6)$, the two $h$-orthogonal. The two forms of the article are related by

$$
g(\tilde{P},\tilde{Q}) = h(\tilde{P}^{\natural},\tilde{Q}) = h(\tilde{P},\tilde{Q}^{\natural}),
$$

of which the second equality is the self-adjointness, and on the eigenspaces $g$ is $+h$ and $-h$ respectively, which is why its inertia is $(1,3,0)$.

*Proof.* The identity is the bridge identity $\langle\tilde{P},\tilde{Q}\rangle_{\natural*} = \langle\tilde{P},\tilde{Q}^{\natural}\rangle_{*}$ of *The Fundamental Symmetry of the Biquaternion Algebra*, §*The Natural Conjugation as a Fundamental Symmetry*, which is the displayed equality; the eigenspaces and their orthogonality are §*The Eigenspaces and the Fundamental Decomposition* of the same article; the sign of $g$ on the two eigenspaces is the identity $g = h \circ (\natural,\mathrm{id})$ evaluated on them, since $\natural$ fixes the centre and negates the vector subspace. $\square$

**Corollary (the layer's separation into two steps).** The indefinite form is not of the layer, but it is **the definite form of the layer composed with a canonical involution**, so the layer's definite theory is recovered on $g$ only through the bridge: the positivity, the inequality and the norm of $g$ along the bridge are the layer's, read on $h$, and the layer's object is $(\mathbb{B},{}^{*},h)$ with $g$ read as the associated indefinite pairing. The involution $\natural$ is the **fundamental symmetry** of the pair $(g,h)$, and the article's contribution to the region is the placement: *one form, one symmetry, two categories*.

### The Unitary Elements

**Theorem (the unitary slice).** The unitary elements of the layer, $U = \{\tilde{U} : \tilde{U}^{*}\tilde{U} = e_{0}\} = \{\tilde{U} : \tilde{U}\tilde{U}^{*} = e_{0}\}$, form a group acting on the right and on the left by isometries of $h$,

$$
h(\tilde{U}\tilde{X},\tilde{U}\tilde{Y}) = h(\tilde{X},\tilde{Y}) = h(\tilde{X}\tilde{U},\tilde{Y}\tilde{U}),
$$

and on the slice

$$
h(\tilde{U},\tilde{U}) = 1, \qquad g(\tilde{U},\tilde{U}) = 2\lvert U_{0}\rvert^{2} - 1 \in [-1,1],
$$

so the slice lies in the set $\{\tilde{X} : \lvert g(\tilde{X},\tilde{X})\rvert \leq h(\tilde{X},\tilde{X}) = 1\}$ of the definite form and meets the $g$-null set exactly in the set $\lvert U_{0}\rvert = 1/\sqrt{2}$ of the "balanced" unitary elements. The slice is the layer's unitary group, and as a group it is $U(2)$.

*Proof.* The isometry is the compatibility read twice, $h(\tilde{U}\tilde{X},\tilde{U}\tilde{Y}) = h(\tilde{X},\tilde{U}^{*}\tilde{U}\tilde{Y}) = h(\tilde{X},\tilde{Y})$, and the same on the right; the value $h(\tilde{U},\tilde{U}) = \operatorname{Sc}(\tilde{U}\tilde{U}^{*}) = \operatorname{Sc}(e_{0}) = 1$; for the indefinite form, $g(\tilde{U},\tilde{U}) = \sum_{\mu}\varepsilon_{\mu}\lvert U_{\mu}\rvert^{2} = 2\lvert U_{0}\rvert^{2} - \sum_{\mu}\lvert U_{\mu}\rvert^{2} = 2\lvert U_{0}\rvert^{2} - 1$ because $\sum_{\mu}\lvert U_{\mu}\rvert^{2} = 1$. The group is *The Unitary Group of the Biquaternion Algebra*, where the identification with $U(2)$ and the identification of the isometry property with $\tilde{U}^{*}\tilde{U} = e_{0}$ are established. $\square$

**Remark (the layer's unitary group and the isometry group of the indefinite form).** The elements of the slice are exactly the elements preserving $h$, which is the layer's unitary group of the pair $(\mathbb{B},{}^{*},h)$, and the operators preserving the indefinite form $g$ form the indefinite unitary group $U(1,3)$ of *The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*; the two are different objects, the first an isometry group of the layer's form and the second the isometry group of a form on the algebra. The unitary slice is the layer's object and *The Unitary Group of the Biquaternion Algebra* is its article; the $g$-isometries are *Unitary and Isometric Operators of the Form* read in the indefinite signature, and their spectral theory is *The Indefinite Spectra of the Operators on the Biquaternion Algebra* and *The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra*.

## The Caution on the Natural Conjugation

**Remark (the linear conjugation produces a bilinear form, and it is the symmetry and not the involution).** The natural conjugation ${}^{\natural}$ is $\mathbb{C}$-linear, and it therefore plays three distinct roles in the region, which the article separates. As a **slot map** it produces a bilinear pairing, $\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q})$, which belongs to the bilinear layer and to *The Four Pairings of the Biquaternion Algebra*; as an **involution of the algebra** it is admissible over the real base $(\mathbb{R},\mathrm{id})$ and not over the complex datum, since the layer asks the involution to be $\varsigma$-semilinear; and as an **operator** it is the fundamental symmetry of the pair $(g,h)$ and the isometry of all four pairings, §*The Four Pairings*. The layer uses it in the third role, and the caution is that the first two are the reason the algebra carries a bilinear form and a symmetric structure alongside its sesquilinear one, so that the phrase "the form on the biquaternion algebra" names four objects and the layer selects one.

**Remark (the two automorphic and anti-automorphic conjugations).** The same reading separates the four conjugations: $\mathrm{id}$ and ${}^{\natural}$ are $\mathbb{C}$-linear, $\bar{\cdot}$ and ${}^{*}$ are $\mathbb{C}$-antilinear; $\mathrm{id}$ and $\bar{\cdot}$ are automorphisms, ${}^{\natural}$ and ${}^{*}$ are anti-automorphisms. The layer's involution is the antilinear anti-automorphism ${}^{*}$; the pairing of the antilinear automorphism $\bar{\cdot}$ is the sesquilinear form $g = \operatorname{Sc}(\tilde{P}\bar{\tilde{Q}})$ of the article, which is the same as $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$; and the pair of linear maps produces the two bilinear forms. The four pairings are therefore the four general products read with the two linear and the two antilinear conjugations, and the layer's selection is the pair (anti-automorphism, and hence compatibility) among the two antilinear ones.

## The Collapse at the Real Base

**Theorem (the collapse).** Let the datum be $(\mathbb{R},\mathrm{id})$, so that the scalars are real and the coefficient conjugation is the identity on them; then ${}^{*} = {}^{\natural}$, the four pairings collapse to the two real symmetric bilinear forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, of signatures $(4,4)$ and $(4,4)$ over the eight real coordinates, the Hermitian condition is the symmetry, the natural conjugation becomes an admissible involution, and the layer is the bilinear one. The object of the layer at the complex datum has no collapse: the sesquilinear form $h$ is genuinely sesquilinear, its inner-product structure is genuinely complex, and the realification is a separate reading.

*Proof.* The statement is the collapse of *Sesqualgebras with a Form*, §*The Collapse at the Trivial Involution*, read on the four pairings: at $\varsigma = \mathrm{id}$ the sesquilinear forms have both slots linear, hence are bilinear and symmetric, and the two tables of signatures are those of *The Realification of the Four Forms*, §*The Four Gram Matrices*, and *Operators of the Real Biquaternion Algebra*. $\square$

**Remark (which statements are sesquilinear).** The compatibility, the adjoint rule $L_{\tilde{P}}^{*} = L_{\tilde{P}^{*}}$ and the failure of the corresponding rule for $g$ hold in both categories and are read at the real base as the self-adjointness of the left multiplications for the symmetric forms; the sesquilinear content of the article is the dichotomy of the two slots, the modulus in the Hermitian condition and the fact that the definite form $h$ has a complex Hilbert structure that the realification does not retain. The reading over the real base of the whole region, the signatures and the subalgebras, is *The Realification of the Four Forms*.

## Summary

The biquaternion algebra carries four distinguished pairings, and the layer of *Sesqualgebras with a Form* selects one of them. The selection is a dichotomy in the two slots: $\mathrm{id}$ and the natural conjugation ${}^{\natural}$ are $\mathbb{C}$-linear and the Hermitian conjugation ${}^{*}$ is $\mathbb{C}$-antilinear, so the pairings with $\mathrm{id}$ in the second slot are **bilinear** — the complex and the general quaternionic bilinear forms $\langle\tilde{P},\tilde{Q}\rangle = \operatorname{Sc}(\tilde{P}\tilde{Q})$ and $\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q})$, of the bilinear layer — and the pairings with ${}^{*}$ there are **sesquilinear**, linear in the first slot and $\varsigma$-semilinear in the second. Of the two sesquilinear ones, the complex form $h(\tilde{P},\tilde{Q}) = \operatorname{Sc}(\tilde{P}\tilde{Q}^{*}) = \sum_{\mu}P_{\mu}\varsigma(Q_{\mu})$ is Hermitian, positive definite, nondegenerate with Gram matrix $\mathrm{I}_{4}$ and **compatible with the product**, $h(\tilde{P}\tilde{Q},\tilde{R}) = h(\tilde{Q},\tilde{P}^{*}\tilde{R})$ by $\operatorname{Sc}$-cyclicity, equivalently $(L_{\tilde{P}})^{h} = L_{\tilde{P}^{*}}$, so $(\mathbb{B},{}^{*},h)$ is an **object of the layer**, its unitary elements $\tilde{U}^{*}\tilde{U} = e_{0}$ form the group $U(2)$ acting by isometries of $h$ with $h(\tilde{U},\tilde{U}) = 1$, and its positivity, inequality, norm and operator theory are the layer's. The general quaternionic sesquilinear form $g(\tilde{P},\tilde{Q}) = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = \operatorname{Sc}(\tilde{P}\bar{\tilde{Q}})$ is Hermitian, nondegenerate, of Gram matrix $\mathrm{E} = \operatorname{diag}(1,-1,-1,-1)$ and signature $(2,6)$, but its adjoint rule is $(L_{\tilde{P}})^{g} = R_{\bar{\tilde{P}}}$, a **right** multiplication, so it is a Hermitian form on the algebra and **not** a form of the layer; it is the indefinite companion of $h$ through the **fundamental symmetry** ${}^{\natural}$, $g(\tilde{P},\tilde{Q}) = h(\tilde{P}^{\natural},\tilde{Q})$, with the centre and the vector subspace as its eigenspaces, which is why its inertia is $(1,3,0)$, and on the unitary slice its value is $2\lvert U_{0}\rvert^{2} - 1 \in [-1,1]$. The **caution** of the article is that the natural conjugation is $\mathbb{C}$-linear and hence produces a bilinear form, is admissible as an involution only over the real base, and enters the layer in the third role of a self-adjoint operator and fundamental symmetry; the four pairings are therefore four objects, the layer takes one, and the region's articles — *The Four Pairings of the Biquaternion Algebra*, *Biquaternion Norm and Invertibility*, *The Fundamental Symmetry of the Biquaternion Algebra*, *The Unitary Group of the Biquaternion Algebra* — develop the four, while the placing of the algebra in the general layer is this article.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, $\tilde{Q} = \sum_{\mu}Q_{\mu}e_{\mu}$ | the biquaternion algebra and its coefficient basis |
| $\operatorname{Sc}$, $\varepsilon = (1,-1,-1,-1)$, $\operatorname{Sc}(e_{\mu}e_{\nu}) = \varepsilon_{\mu}\delta_{\mu\nu}$ | the scalar part and the sign string |
| $\bar{\cdot}$, ${}^{\natural}$, ${}^{*} = {}^{\natural}\bar{\cdot}$ | the coefficient conjugation, linear; the natural conjugation, linear; the Hermitian conjugation, antilinear |
| $\bar{\cdot}$ automorphic, ${}^{*}$ anti-automorphic | the layer's involution is the antilinear anti-automorphism |
| $\langle\tilde{P},\tilde{Q}\rangle = \operatorname{Sc}(\tilde{P}\tilde{Q})$, $\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q})$ | the two bilinear pairings, of the bilinear layer |
| $h(\tilde{P},\tilde{Q}) = \langle\tilde{P},\tilde{Q}\rangle_{*} = \operatorname{Sc}(\tilde{P}\tilde{Q}^{*}) = \sum_{\mu}P_{\mu}\varsigma(Q_{\mu})$ | the layer's sesquilinear form, Hermitian, positive definite, Gram $\mathrm{I}_{4}$ |
| $h(\tilde{P}\tilde{Q},\tilde{R}) = h(\tilde{Q},\tilde{P}^{*}\tilde{R})$, $(L_{\tilde{P}})^{h} = L_{\tilde{P}^{*}}$ | the compatibility; the object $(\mathbb{B},{}^{*},h)$ |
| $g(\tilde{P},\tilde{Q}) = \operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*}) = \operatorname{Sc}(\tilde{P}\bar{\tilde{Q}})$ | the general quaternionic sesquilinear form, indefinite, Gram $\mathrm{E}$, signature $(2,6)$ |
| $(L_{\tilde{P}})^{g} = R_{\bar{\tilde{P}}}$, $g(\tilde{P}\tilde{Q},\tilde{R}) = g(\tilde{Q},\tilde{R}\bar{\tilde{P}})$ | the adjoint rule that makes $g$ not of the layer |
| $g(\tilde{P},\tilde{Q}) = h(\tilde{P}^{\natural},\tilde{Q})$ | the bridge identity: ${}^{\natural}$ is the fundamental symmetry of $(g,h)$ |
| $\tilde{U}^{*}\tilde{U} = e_{0}$, $h(\tilde{U},\tilde{U}) = 1$, $g(\tilde{U},\tilde{U}) = 2\lvert U_{0}\rvert^{2}-1$ | the unitary slice $U(2)$ and the two forms on it |
| $\lvert U_{0}\rvert = 1/\sqrt{2}$ | the set where the slice meets the indefinite null set |
| $\varsigma = \mathrm{id}$ | the collapse to the real base: ${}^{*} = {}^{\natural}$, symmetric bilinear forms |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the algebras with involution and the Hermitian forms they carry.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the symmetric and Hermitian forms over a field with involution and the sesquilinear categories.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976), and Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the trace of the regular representation and the cyclicity of the scalar part.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the positive forms, the associated operator theory and the self-adjoint operators.
- J. Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the indefinite forms, the fundamental symmetry and the Krein structure the indefinite companion belongs to.
- Igor R. Shafarevich and Alexei O. Remizov, *Linear Algebra and Geometry* (Springer, 2013), for the classical classification of the sesquilinear and bilinear forms by their Gram matrices and signatures.
- E. Christopher Lance, *Hilbert $\mathrm{C}^{*}$-Modules: A Toolkit for Operator Algebraists* (Cambridge University Press, 1995), for the sesquilinear forms with values in an algebra and the compatibility they generalise.
