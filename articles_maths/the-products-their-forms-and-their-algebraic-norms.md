
# __The Products, Their Forms and Their Algebraic Norms__

## Introduction

The underlying $\mathbb{C}$-vector space of $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries **four general products**, and no more, once the two slots of a product are allowed to carry either the identity or the conjugation of the algebra. Writing $\tilde Q_1$ in the left slot as $\tilde Q_1$ or $\tilde Q_1^{\natural}$, and $\tilde Q_2$ in the right slot as $\tilde Q_2$ or $\tilde Q_2^{*}$, gives the four operations

$$
\tilde Q_1\tilde Q_2, \qquad \tilde Q_1\tilde Q_2^{*}, \qquad \tilde Q_1^{\natural}\tilde Q_2, \qquad \tilde Q_1^{\natural}\tilde Q_2^{*} .
$$

Only the first is a multiplication in the strict sense — associative, unital, $\mathbb{C}$-bilinear; the other three are the companions the conjugations produce. This article is the compact reference the rest of the Biquaternions category reads: it states the four general products, their **symmetric and antisymmetric parts**, which are the twelve products, their **scalar parts**, which are the four forms, and their **algebraic norms**, which are the four functions of one element the forms produce. The detailed development — the relations between the four, the comparison of the four, the operators they define, their restriction to the remarkable subspaces — belongs to the companion category *Biquaternioid Algebraic Structures*.

The four products are defined and studied one by one in *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, and the twelve operations obtained from them by symmetrisation and antisymmetrisation are the subject of *The 12 Products of the Biquaternioid Complex Space* and *The 12 Multiplication Tables of the Biquaternioid Complex Space*. The four forms are developed in *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, the four algebraic norms in *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*, and their restriction to the remarkable subspaces in *Remarkable Subspaces and the Four Forms* and *Remarkable Subspaces and the Four Algebraic Norms*. The element, the basis, the table and the conjugations used here are *Introduction to the Biquaternion Algebra* and *The Group of Involutions*.

**Conventions.** $\tilde Q_1 = \sum_{\mu\in\{t,x,y,z\}}Q_{1\mu} e_\mu = Q_{1,0}e_t+\vec Q_1$ and $\tilde Q_2 = Q_{2t}e_t+\vec Q_2$, with coefficients in $\mathbb{C}$; $i$ is central. The conjugations are $\tilde Q^{\natural} = Q_te_t-\vec Q$, $\tilde Q^{*} = \bar Q_te_t-\overline{\vec Q}$ and $(\overline{\tilde Q})_\mu = \bar Q_\mu$, with $\varepsilon = (1,-1,-1,-1)$ the sign vector of $\natural$. The scalar part is written $\mathrm{Sc}$, and the four forms are collected in the single bracket $\langle\cdot,\cdot\rangle$ with a subscript recording the pair.

## The Products

### The Two Slots

**Definition.** The **four general products** are the operations obtained from the plain bilinear product by applying, independently, the identity or the natural conjugation in the first slot and the identity or the star conjugation in the second:

$$
(\tilde Q_1,\tilde Q_2)\longmapsto \tilde Q_1\tilde Q_2, \qquad \tilde Q_1\tilde Q_2^{*}, \qquad \tilde Q_1^{\natural}\tilde Q_2, \qquad \tilde Q_1^{\natural}\tilde Q_2^{*} .
$$

Their names record the two slots: the **general plain bilinear** product $\tilde Q_1\tilde Q_2$, the **general plain sesquilinear** product $\tilde Q_1\tilde Q_2^{*}$, the **general quaternionic bilinear** product $\tilde Q_1^{\natural}\tilde Q_2$ and the **general quaternionic sesquilinear** product $\tilde Q_1^{\natural}\tilde Q_2^{*}$.

**Proposition.** The first slot decides the $\mathbb{C}$-linearity and the Gram matrix; the second decides whether the product is bilinear or sesquilinear:

$$
\text{bilinear} : \tilde Q_1\tilde Q_2,\ \tilde Q_1^{\natural}\tilde Q_2, \qquad\qquad
\text{sesquilinear} : \tilde Q_1\tilde Q_2^{*},\ \tilde Q_1^{\natural}\tilde Q_2^{*} .
$$

The products are $\mathbb{C}$-bilinear in the second slot always (the second slot carries $*$ or its absence in a $\mathbb{C}$-sesquilinear way), and $\mathbb{C}$-linear in the first slot for the plain pair and conjugate-linear for the quaternionic pair.

**Proof.** The natural conjugation is $\mathbb{R}$-linear and $\mathbb{C}$-antilinear, since $(\lambda\tilde Q_1)^{\natural} = \bar\lambda\tilde Q_1^{\natural}$ for $\lambda\in\mathbb{C}$; the star conjugation is likewise $\mathbb{C}$-antilinear. Hence a product whose first factor carries $\natural$ is conjugate-linear in that factor, and the second slot $*$ makes the product conjugate-linear in the second factor. The plain products are linear in the first factor by bilinearity of the multiplication.

### The Symmetric and Antisymmetric Parts

**Definition.** Each of the four general products is split in its two arguments into a **symmetric part** and an **antisymmetric part**, the half-sum and the half-difference of the two orders. The exchange is the interchange of the arguments for the two bilinear products and the conjugate transpose for the two sesquilinear ones; it is the exchange that keeps the class of the product. The four symmetric parts are written with the **full dot** $\bullet$ and the four antisymmetric with the **wedge** $\wedge$, the subscript naming the slot as it does for the forms: none for the plain bilinear product, ${}_{\natural}$ for the quaternionic bilinear, ${}_{*}$ for the plain sesquilinear and ${}_{\natural*}$ for the quaternionic sesquilinear.

**The symmetric parts.** The four half-sums.

**The symmetric plain bilinear product**, the half-sum of the two orders, the **Jordan product** $\tilde Q_1\bullet\tilde Q_2$:

$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr)=\bigl[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1 .
$$

**The symmetric quaternionic bilinear product**, the half-sum of the two orders, the **quaternion form** $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$:

$$
\tilde Q_1\bullet_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1\bigr)=\bigl[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr] .
$$

**The symmetric plain sesquilinear product**, the half-sum under the conjugate transpose, the **Hermitian form** $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$:

$$
\tilde Q_1\bullet_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\bigl[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr] .
$$

**The symmetric quaternionic sesquilinear product**, the half-sum under the conjugate transpose:

$$
\tilde Q_1\bullet_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1 .
$$

**The antisymmetric parts.** The four half-differences under the same exchange; all four have zero scalar part and lie in the vector subspace.

**The antisymmetric plain bilinear product**, the half-difference of the two orders, the **outer product** $\tilde Q_1\wedge\tilde Q_2$:

$$
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr)=\vec Q_1\times\vec Q_2 .
$$

**The antisymmetric quaternionic bilinear product**, the half-difference of the two orders:

$$
\tilde Q_1\wedge_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr)=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

**The antisymmetric plain sesquilinear product**, the half-difference under the conjugate transpose, the vector part $\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$:

$$
\tilde Q_1\wedge_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})=-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2} .
$$

**The antisymmetric quaternionic sesquilinear product**, the half-difference under the conjugate transpose, the cross product $\vec Q_1\times\overline{\vec Q_2}$:

$$
\tilde Q_1\wedge_{\natural*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\vec Q_1\times\overline{\vec Q_2} .
$$

**Proposition.** The dot and the wedge rebuild the four general products, so the eight parts carry the whole of them:

$$
\tilde Q_1\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_1\wedge\tilde Q_2,\qquad
\tilde Q_1^{\natural}\tilde Q_2=\tilde Q_1\bullet_{\natural}\tilde Q_2+\tilde Q_1\wedge_{\natural}\tilde Q_2,\qquad
\tilde Q_1\tilde Q_2^{*}=\tilde Q_1\bullet_{*}\tilde Q_2+\tilde Q_1\wedge_{*}\tilde Q_2,\qquad
\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1\bullet_{\natural*}\tilde Q_2+\tilde Q_1\wedge_{\natural*}\tilde Q_2 .
$$

The eight coordinate formulas and the four reconstructions are verified by recomputation on one hundred random pairs of $\mathbb{B}$.

**Proposition.** Only the plain product is associative, so only its split names a classical algebra: $\tilde Q_1\bullet\tilde Q_2$ is the **Jordan product** of the plain product, commutative and not associative, and $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$ is the **Lie bracket**, the cross product of the vector parts, of algebra $\mathfrak{so}(3)\cong\mathfrak{su}(2)$. The symmetrisations of the other three products are no Jordan algebras, the products being not associative (see §*The Twelve Products and Their Names* of *Conventions in Mathematics*).

### The Collapse to Four by Scalar Part

**Proposition.** The twelve products of the section above collapse to four when the scalar part is taken: the passage to the scalar part keeps the symmetric half and kills the antisymmetric half, so the twelve carry **four scalar parts and no more**, one to each of the four symmetric products and the zero form on the four antisymmetric ones.

**Proof.** The antisymmetric part of $\tilde Q_1\tilde Q_2$ is $\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1) = \vec Q_1\times\vec Q_2$, whose scalar part is $0$; the same holds for the other three, since their symmetrised part has the same scalar part as the product and their antisymmetrised part has none. The count of twelve and the assignment of the four forms to the four symmetric products are *The 12 Products of the Biquaternioid Complex Space*.

## The Four Forms

**Definition.** The **four forms** are the scalar parts of the four general products,

$$
\langle\tilde Q_1,\tilde Q_2\rangle = \mathrm{Sc}(\tilde Q_1\tilde Q_2), \qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}), \qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2), \qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*} = \mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*}),
$$

named the **general plain bilinear**, the **general plain sesquilinear** (the **Hermitian**), the **general quaternionic bilinear** and the **general quaternionic sesquilinear** (the **Krein**) form.

**Theorem.** On the coordinates the four forms read

$$
\langle\tilde Q_1,\tilde Q_2\rangle = \sum_{\mu}\varepsilon_\mu Q_{1\mu} Q_{2\mu}, \qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \sum_{\mu}Q_{1\mu}\bar Q_{2\mu}, \qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \sum_{\mu}Q_{1\mu} Q_{2\mu}, \qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*} = \sum_{\mu}\varepsilon_\mu Q_{1\mu}\bar Q_{2\mu} .
$$

**Proof.** The scalar part of a product of basis elements is $\mathrm{Sc}(e_\mu e_\nu) = \varepsilon_\mu\delta_{\mu\nu}$. Hence $\mathrm{Sc}(\tilde Q_1\tilde Q_2) = \sum_\mu Q_{1\mu} Q_{2\mu}\varepsilon_\mu$; replacing $\tilde Q_2$ by $\tilde Q_2^{*}$, whose $\mu$-th coefficient is $\varepsilon_\mu\bar Q_{2\mu}$, gives $H = \sum_\mu Q_{1\mu}\varepsilon_\mu\bar Q_{2\mu}\varepsilon_\mu = \sum_\mu Q_{1\mu}\bar Q_{2\mu}$; replacing $\tilde Q_1$ by $\tilde Q_1^{\natural}$, of $\mu$-th coefficient $\varepsilon_\mu Q_{1\mu}$, gives $N = \sum_\mu\varepsilon_\mu Q_{1\mu} Q_{2\mu}\varepsilon_\mu = \sum_\mu Q_{1\mu} Q_{2\mu}$; and both replacements give $K = \sum_\mu\varepsilon_\mu Q_{1\mu}\bar Q_{2\mu}$.

**Theorem.** $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are symmetric bilinear forms, of Gram matrices $\mathrm E = \operatorname{diag}(1,-1,-1,-1)$ and $\mathrm I_4$; $\langle\cdot,\cdot\rangle_{*}$ is a Hermitian form of Gram matrix $\mathrm I_4$, positive definite; $\langle\cdot,\cdot\rangle_{\natural*}$ is a Hermitian form of Gram matrix $\mathrm E$, indefinite. Their realifications have signatures

$$
B:(4,4), \qquad H:(8,0), \qquad N:(4,4), \qquad K:(2,6),
$$

and the classical groups that preserve them are $O_4(\mathbb{C})$, $\mathrm{U}(4)$, $O_4(\mathbb{C})$ and $\mathrm{U}(1,3)$, of real dimensions $12$, $16$, $12$ and $16$.

**Proof.** The Gram matrices are read from the coordinate formulas, the $\mu$-th diagonal entry being $\varepsilon_\mu$, $1$, $1$ and $\varepsilon_\mu$ respectively. $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are complex bilinear; their realification on the real basis $e_t,\dots,\vec e_z,ie_t,\dots,i\vec e_z$ doubles each signature, giving $(4,4)$ and $(4,4)$. $\langle\cdot,\cdot\rangle_{*}$ is the standard positive definite Hermitian form, $\langle\tilde Q,\tilde Q\rangle_{*} = \sum_\mu\lvert Q_\mu\rvert^2 > 0$ for $\tilde Q\neq0$, so its realification has signature $(8,0)$. $\langle\cdot,\cdot\rangle_{\natural*}$ has one positive and three negative diagonal entries relative to the complex structure, giving $(2,6)$; the group computations are the classical groups of those forms.

**Corollary.** The Hermitian form $\langle\cdot,\cdot\rangle_{*}$ is the only one of the four that is **positive definite**; it is the square of the Euclidean norm, $\langle\tilde Q,\tilde Q\rangle_{*} = \lVert\tilde Q\rVert_E^2$, and it is the unique topological norm of the space. The plain bilinear form $\langle\cdot,\cdot\rangle$ is the **hyperbolic** one, of index $2$ over $\mathbb{C}$: $h_1 = e_t+\vec e_x$, $h_2 = \tfrac12(e_t-\vec e_x)$, $h_3 = \vec e_y+i\vec e_z$, $h_4 = \tfrac12(i\vec e_z-\vec e_y)$ are isotropic with $\langle h_1,h_2\rangle = \langle h_3,h_4\rangle = 1$ and all other pairings zero.

## The Four Algebraic Norms

**Definition.** The **algebraic norm** attached to a form $\varphi$ is the function of one element obtained by setting the two arguments equal, $\varphi(\tilde Q) = \varphi(\tilde Q,\tilde Q)$. The four forms give

$$
\langle\tilde Q\rangle = \sum_{\mu}\varepsilon_\mu Q_\mu^2, \qquad
\langle\tilde Q\rangle_{*} = \sum_{\mu}\lvert Q_\mu\rvert^2, \qquad
\langle\tilde Q\rangle_{\natural} = \sum_{\mu}Q_\mu^2, \qquad
\langle\tilde Q\rangle_{\natural*} = \sum_{\mu}\varepsilon_\mu\lvert Q_\mu\rvert^2 .
$$

**Theorem.** $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are complex-valued; $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ are real-valued. Only $\langle\cdot,\cdot\rangle_{*}$ is definite — it is $\lVert\tilde Q\rVert_E^2$, positive for $\tilde Q\neq0$. Only $\langle\cdot,\cdot\rangle_{\natural}$ is **multiplicative**,

$$
\langle\tilde Q_1\tilde Q_2\rangle_{\natural} = \langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural},
$$

and it is the reduced norm of the algebra: the determinant in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$, the criterion of invertibility, and the vanishing set $\mathcal N = \{\tilde Q\neq0 : \langle\tilde Q\rangle_{\natural} = 0\}$ is the zero-divisor cone.

**Proof.** The formulas are the definition read from the coordinate forms of the previous section. $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ are sums of $\lvert Q_\mu\rvert^2$ with real coefficients, hence real-valued, while $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are sums of squares and are complex-valued; $H\geq0$ with equality only at the origin. The multiplicativity of $\langle\cdot\rangle_{\natural}$ is the multiplicativity of the determinant under the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ of *Introduction to the Biquaternion Algebra*, where $\langle\tilde Q\rangle_{\natural} = \det\rho(\tilde Q)$; the criterion of invertibility and the zero-divisor cone are the same theorem.

**Corollary.** **No single one of the four is both definite and multiplicative.** The four are the two-slot grid completed: the second slot ($*$ or its absence) decides whether the algebraic norm is real or complex, the first slot ($\natural$ or its absence) whether the Gram matrix is the sign matrix or the identity. On the whole Biquaternions category this is why the word *norm* must be qualified: the *algebraic* norm is the function above, valued in $\mathbb{C}$ or $\mathbb{R}$, while the *topological* norm is the single Euclidean $\lVert\tilde Q\rVert_E$, the square root of $\langle\cdot,\cdot\rangle_{*}$.

| Form | Product | Scalar part | Gram | Kind | Realification | Group |
|---|---|---|---|---|---|---|
| $\langle\cdot,\cdot\rangle$ | $\tilde Q_1\tilde Q_2$ | $\sum_\mu\varepsilon_\mu Q_{1\mu} Q_{2\mu}$ | $\mathrm E$ | symmetric bilinear | $(4,4)$ | $O_4(\mathbb{C})$ |
| $\langle\cdot,\cdot\rangle_{*}$ | $\tilde Q_1\tilde Q_2^{*}$ | $\sum_\mu Q_{1\mu}\bar Q_{2\mu}$ | $\mathrm I_4$ | Hermitian, definite | $(8,0)$ | $\mathrm{U}(4)$ |
| $\langle\cdot,\cdot\rangle_{\natural}$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\sum_\mu Q_{1\mu} Q_{2\mu}$ | $\mathrm I_4$ | symmetric bilinear | $(4,4)$ | $O_4(\mathbb{C})$ |
| $\langle\cdot,\cdot\rangle_{\natural*}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $\sum_\mu\varepsilon_\mu Q_{1\mu}\bar Q_{2\mu}$ | $\mathrm E$ | Hermitian, indefinite | $(2,6)$ | $\mathrm{U}(1,3)$ |

## Summary

The biquaternion $\mathbb{C}$-space carries exactly four general products, obtained from the plain bilinear product by letting each slot carry the identity or a conjugation: $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$ and $\tilde Q_1^{\natural}\tilde Q_2^{*}$. Each splits in its two arguments into a symmetric part $\tilde Q_1\bullet\tilde Q_2$ and an antisymmetric part $\tilde Q_1\wedge\tilde Q_2$, so the four general products give the twelve products, and the dot and the wedge rebuild the four. The twelve collapse to four by scalar part, since antisymmetrisation kills the scalar part and symmetrisation preserves it.

Their scalar parts are the four forms: the general plain bilinear $\langle\cdot,\cdot\rangle$, the general plain sesquilinear or Hermitian $\langle\cdot,\cdot\rangle_{*}$, the general quaternionic bilinear $\langle\cdot,\cdot\rangle_{\natural}$ and the general quaternionic sesquilinear or Krein $\langle\cdot,\cdot\rangle_{\natural*}$, of Gram matrices $\mathrm E, \mathrm I_4, \mathrm I_4, \mathrm E$ and realified signatures $(4,4), (8,0), (4,4), (2,6)$. The first slot decides the Gram matrix and so the signature, the second decides bilinear against sesquilinear and so complex against real values.

Setting the two arguments equal gives the four algebraic norms $\langle\cdot\rangle, \langle\cdot\rangle_{*}, \langle\cdot\rangle_{\natural}, \langle\cdot\rangle_{\natural*}$ of one element, complex or real according to the slot, of which only $\langle\cdot,\cdot\rangle_{*}$ is definite and only $\langle\cdot,\cdot\rangle_{\natural}$ is multiplicative. $\langle\cdot,\cdot\rangle_{*}$ is the Euclidean norm squared and the unique topological norm; $\langle\cdot,\cdot\rangle_{\natural}$ is the reduced norm, the determinant in $\mathbb{B}\cong M_2(\mathbb{C})$, and it is the criterion of invertibility, its zero set being the cone of the zero divisors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1, \tilde Q_2$ | The two elements of a product, left slot and right slot |
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | The four general products |
| $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\bullet_{*}\tilde Q_2$, $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\bullet_{\natural*}\tilde Q_2$ | The four symmetric parts, the half-sums; the Jordan product for the plain slot |
| $\tilde Q_1\wedge\tilde Q_2$, $\tilde Q_1\wedge_{*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | The four antisymmetric parts, the half-differences; the outer or Lie product for the plain slot |
| $(\mathrm{id},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},\mathrm{id})$, $({}^{\natural},{}^{*})$ | The two slots, the subscript of each bracket |
| $\mathrm{Sc}$ | The scalar part, the coefficient of $e_t$ |
| $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{\natural*}$ | The four forms and their algebraic norms |
| $\varepsilon = (1,-1,-1,-1)$ | The sign vector of $\natural$ |
| $\mathrm E = \operatorname{diag}(1,-1,-1,-1)$, $\mathrm I_4$ | Gram matrices of $(B,K)$ and of $(H,N)$ |
| $(4,4), (8,0), (4,4), (2,6)$ | Realified signatures of $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{\natural*}$ |
| $O_4(\mathbb{C}), \mathrm{U}(4), \mathrm{U}(1,3)$ | The groups preserving $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ |
| $h_1,\dots,h_4$ | The hyperbolic basis of $\langle\cdot,\cdot\rangle$ |
| $\langle\tilde Q\rangle_{\natural} = \sum_\mu Q_\mu^2$ | The reduced norm, the multiplicative one |
| $\langle\tilde Q\rangle_{*} = \sum_\mu\lvert Q_\mu\rvert^2$ | The Euclidean norm squared, the definite one |
| $\mathcal N$ | The zero-divisor cone, the null cone of $\langle\cdot,\cdot\rangle_{\natural}$ |

## Further Reading

- *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternioid-c-space.md`), for the four products defined and developed one by one.
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`) and *The 12 Multiplication Tables of the Biquaternioid Complex Space* (`articles_maths/the-12-multiplication-tables-of-the-biquaternioid-complex-space.md`), for the twelve operations and their tables, from which the collapse to four forms is read.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`) and *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the forms and the algebraic norms in full.
- *Introduction to the Biquaternion Algebra* (`articles_maths/introduction-to-the-biquaternion-algebra.md`), for the element, the basis, the multiplication table and the four conjugations used here.
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the group the four conjugations generate.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the reduced norm as the criterion of invertibility and the zero-divisor cone.
- *Remarkable Subspaces and the Four Forms* and *Remarkable Subspaces and the Four Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-four-forms.md`, `articles_maths/remarkable-subspaces-and-the-four-algebraic-norms.md`), for the four forms and their algebraic norms read on the remarkable subspaces.
- *Bilinear Forms*, *Hermitian Forms and Unitary Geometry* and *Quadratic Forms and Polarisation*, for the general theory of a bilinear or sesquilinear form, of its Gram matrix, of its signature and of the group that preserves it.
