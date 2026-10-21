# __The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

The multiplication of the block *Introduction to the Antisymmetric Quaternionic Sesqualgebra* is the operation

$$
\tilde Q_1\diamond\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\vec Q_1\times\overline{\vec Q_2},
$$

the cross product of the vector part of the first argument with the **conjugate** of the vector part of the second. The conjugation in the second slot is the whole content of the block: it is what makes the operation sesquilinear rather than bilinear, what makes its diagonal nonzero, and what makes its Jacobi identity fail on a witness that no real element can supply. This article develops the three consequences. The **conjugate cross product** is read first, with its coordinate rule and its position between the ordinary cross product and its conjugate. The **diagonal** $\tilde Q_2\diamond\tilde Q_2=\vec Q_2\times\overline{\vec Q_2}$ is then identified with the conjugate cross product of the vector part with itself, and its vanishing is reduced to a single condition on that vector part — that it be a complex multiple of a real vector — which is a four-real-dimensional condition and cuts an explicit quadric cone. The **failure of the Jacobi identity** is stated with the declared cyclic sum and the witness $(\vec e_x,\vec e_x,i\vec e_y)$, its value $-2i\vec e_y$ is recomputed, and the reason the witness needs a complex element, and the reason the failure is invisible on the real forms, are given. The comparison with the two other failing brackets $\mathrm{AQA}$ and $\mathrm{APS}$ closes the reading.

The product the block splits and its two halves are *Introduction to the General Quaternionic Sesqualgebra* and *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*; the general construction of a sesqualgebra part is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the obstruction behind the failing law is *Lie Algebras of Sesqualgebras*; the ordinary cross product of the real elements is *Introduction to the Antisymmetric Plain Algebra*; and the three failing brackets are tabulated in *The 12 Products of the Biquaternion Complex Space*.

**Conventions.** As in *Introduction to the Antisymmetric Quaternionic Sesqualgebra*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$ and $\vec e_\mu^2=-e_t$; a generic element is $\tilde Q_2=Q_{2t}e_t+\vec Q_2$, with $\vec Q_2=\sum_{\mu\in\{x,y,z\}}Q_{2,\mu}\vec e_\mu$, $\overline{\vec Q_2}=\sum_{\mu\in\{x,y,z\}}\overline{Q_{2,\mu}}\vec e_\mu$, and $Q_{2,\mu}=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu$ real. The product is written $\diamond$ for the block.

## The Conjugate Cross Product

### The Rule and the Conjugation

**Definition.** The **conjugate cross product** is $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$. The name records the two operations it intertwines: it is the ordinary cross product $\vec Q_1\times\vec Q_2$ of the two vector parts with the second factor conjugated. On a real vector the conjugation is invisible, so the operation escapes the cross product only when the second argument carries a complex coordinate.

**Proposition (coordinate rule).** In coordinates,

$$
\tilde Q_1\diamond\tilde Q_2=\bigl(Q_{1,y}\overline{Q_{2,z}}-Q_{1,z}\overline{Q_{2,y}}\bigr)\vec e_x
+\bigl(Q_{1,z}\overline{Q_{2,x}}-Q_{1,x}\overline{Q_{2,z}}\bigr)\vec e_y
+\bigl(Q_{1,x}\overline{Q_{2,y}}-Q_{1,y}\overline{Q_{2,x}}\bigr)\vec e_z .
$$

*Proof.* The three components of the cross product of $\vec Q_1$ and $\overline{\vec Q_2}$, read in the quaternion basis.

**Remark (the two slots).** The first slot enters $\mathbb{C}$-linearly and the second conjugate-linearly, so the operation is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ and not bilinear. This is the class of the block, and it is the class of the two sesqualgebras of the corpus; the general construction of the parts keeps the class by using the class-preserving exchange, and the antisymmetric part is therefore again sesquilinear. The block carries the conjugation in the second slot like the five other sesquilinear operations of the twelve; what singles it out is that its value is the conjugate cross product alone, and every later fact of the block is a consequence of that single asymmetry.

### The Value as a Cross Product with the Conjugate

**Proposition (the value intertwines the two cross products).** For all biquaternions,

$$
\overline{\tilde Q_1\diamond\tilde Q_2}=\overline{\vec Q_1}\times\vec Q_2,\qquad
\tilde Q_2\diamond\tilde Q_1=-\overline{\tilde Q_1\diamond\tilde Q_2}.
$$

*Proof.* $\overline{\vec Q_1\times\overline{\vec Q_2}}=\overline{\vec Q_1}\times\vec Q_2$, and the second identity is the first applied to the swapped pair.

The block and its conjugate share the value $\vec Q_1\times\overline{\vec Q_2}$ only when $\vec Q_1\times\overline{\vec Q_2}$ is real, which is the case on the real basis; off it the conjugate of the value is the cross product with the roles of the conjugations exchanged.

## The Diagonal and Its Cone

### The Diagonal

**Theorem.** For every biquaternion,

$$
\tilde Q_2\diamond\tilde Q_2=\vec Q_2\times\overline{\vec Q_2},
$$

and if $\vec Q_2=\vec a+i\vec b$ with $\vec a,\vec b$ real vectors, then

$$
\vec Q_2\times\overline{\vec Q_2}=-2i\,\vec a\times\vec b.
$$

*Proof.* The rule with $\tilde Q_1=\tilde Q_2$; and $(\vec a+i\vec b)\times(\vec a-i\vec b)=-i\,\vec a\times\vec b+i\,\vec b\times\vec a=-2i\,\vec a\times\vec b$.

**Example.** At $\tilde Q_2=\vec e_x+i\vec e_y$ one has $\vec a=\vec e_x$, $\vec b=\vec e_y$, $\vec a\times\vec b=\vec e_z$ and $\tilde Q_2\diamond\tilde Q_2=-2i\vec e_z$. At a real element the diagonal vanishes, and at $\tilde Q_2=i\vec e_x+i\vec e_y=i(\vec e_x+\vec e_y)$ the diagonal is $i(\vec e_x+\vec e_y)\times\overline{i(\vec e_x+\vec e_y)}=i(\vec e_x+\vec e_y)\times(-i)(\vec e_x+\vec e_y)=0$.

### The Criterion

**Theorem (the vanishing of the diagonal).** The diagonal vanishes at $\tilde Q_2$ exactly when the vector part $\vec Q_2$ is a complex multiple of a real vector; equivalently, exactly when $\vec Q_2$ and $\overline{\vec Q_2}$ are $\mathbb{C}$-linearly dependent.

*Proof.* The condition $\vec Q_2\times\overline{\vec Q_2}=0$ says that $\overline{\vec Q_2}$ is a complex multiple of $\vec Q_2$, that is $\overline{\vec Q_2}=\mu\vec Q_2$ for some $\mu\in\mathbb{C}$, and this is the linear dependence. Write $\mu=p+iq$ and $\vec Q_2=\vec a+i\vec b$ with $\vec a,\vec b$ real. The equation $\vec a-i\vec b=(p+iq)(\vec a+i\vec b)$ splits into the two real vector equations $(1-p)\vec a+q\,\vec b=0$ and $-q\,\vec a-(1+p)\vec b=0$. A nonzero pair $(\vec a,\vec b)$ exists exactly when the determinant $1-p^{2}-q^{2}$ vanishes, that is $|\mu|=1$; and then the two equations force $\vec a$ and $\vec b$ to be real multiples of one another, so $\vec Q_2$ is a complex multiple of the common real direction. Conversely, if $\vec Q_2=\lambda\vec v$ with $\lambda\in\mathbb{C}$ and $\vec v$ real, then $\overline{\vec Q_2}=\overline{\lambda}\vec v$ and $\vec Q_2\times\overline{\vec Q_2}=\lambda\overline{\lambda}\,\vec v\times\vec v=0$.

**Remark (the condition in coordinates).** The two real vectors are $\vec a=(q_x,q_y,q_z)$ and $\vec b=(q'_x,q'_y,q'_z)$, so the condition is the vanishing of the real cross product $\vec a\times\vec b$, that is the vanishing of the three minors $q_yq'_z-q_zq'_y$, $q_zq'_x-q_xq'_z$ and $q_xq'_y-q_yq'_x$. These are three real quadratic equations on the eight real coordinates of $\tilde Q_2$, so the vanishing set is a **quadric cone** of the space, the common zero set of the three, and not a hypersurface.

**Corollary (the cone of the diagonal).** The set $\{\tilde Q_2:\tilde Q_2\diamond\tilde Q_2=0\}$ is the union, over the real directions $\vec v$ of the vector subspace, of the complex planes $\mathbb{C}e_t\oplus\mathbb{C}\vec v$; the scalar coordinate is free, and the vector part runs over the union of the complex lines $\mathbb{C}\vec v$. The cone carried by the vector part has real dimension $4$, and with the free scalar coordinate the vanishing set has real dimension $6$.

*Proof.* A real direction contributes two real parameters, and the complex multiple $\lambda$ two more, so the union of the complex lines $\mathbb{C}\vec v$ in the vector part has real dimension $4$. The diagonal reads the vector parts alone, so the scalar coordinate $Q_{2t}$ is unconstrained and adds two real dimensions: the vanishing set is the union of the complex planes $\mathbb{C}e_t\oplus\mathbb{C}\vec v$, of real dimension $4+2=6$, and it is not the union of the complex lines $\mathbb{C}\vec v$ alone, which lies in the vector subspace.

**Remark (the elements of square zero).** The elements with $\tilde Q_2\diamond\tilde Q_2=0$ are exactly the elements whose vector part lies on one complex line over a real direction, whatever the scalar coordinate; the vanishing therefore holds on the whole centre, on every real vector $\vec Q_2\in\mathbb{R}^{3}$, on every purely imaginary vector $i\mathbb{R}^{3}$, on the complex multiples of any one real direction, and on the sums of any central element with any of these; it fails on a general complex vector, and the witness $\vec e_x+i\vec e_y$ is the smallest failure. The condition on the vector part is a genuine four-real-dimensional one and not the trivial one of the bilinear blocks, where the diagonal of the antisymmetric part vanishes identically.

## The Failure of the Jacobi Identity

### The Declared Cyclic Sum and the Witness

**Theorem.** The block fails the Jacobi identity. With the cyclic sum declared by the corpus,

$$
(\tilde Q_1\diamond\tilde Q_2)\diamond\tilde Q_3+(\tilde Q_2\diamond\tilde Q_3)\diamond\tilde Q_1+(\tilde Q_3\diamond\tilde Q_1)\diamond\tilde Q_2,
$$

the triple $(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(\vec e_x,\vec e_x,i\vec e_y)$ gives the value $-2i\vec e_y$.

*Proof.* The three inner values are $\vec e_x\diamond \vec e_x=0$, $\vec e_x\diamond i\vec e_y=\vec e_x\times(-i\vec e_y)=-i\vec e_z$ and $i\vec e_y\diamond \vec e_x=(i\vec e_y)\times \vec e_x=-i\vec e_z$. The three reassociations are therefore $0$, $(-i\vec e_z)\diamond \vec e_x=(-i\vec e_z)\times \vec e_x=-i\vec e_y$ and $(-i\vec e_z)\diamond \vec e_x=-i\vec e_y$, whose sum is $-2i\vec e_y$.

### Why the Witness Needs a Complex Element

**Proposition.** No triple of the real basis witnesses the failure, and more generally the cyclic sum vanishes on every triple of real elements.

*Proof.* On real elements the block is the ordinary cross product, $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\vec Q_2$, by the coincidence of *Introduction to the Antisymmetric Quaternionic Sesqualgebra*; the cyclic sum is then the Jacobi sum of the cross product, which vanishes identically, the cross product being the Lie bracket of $\mathbb{R}^{3}$. So a witness must use at least one element with a nonzero imaginary coefficient, and the declared witness uses the smallest such element that fails, $i\vec e_y$ together with the pair $\vec e_x,\vec e_x$.

**Remark (the failure is a feature of the complex slot, not of the real part).** The vanishing on the real forms is the general collapse of the corpus: on the real part the twelve operations fall to ten and the block coincides with $\mathrm{APA}$, so every law that depends only on the real part, the Jacobi identity among them, is the law of the cross product and holds. The failure is produced by the conjugate in the second slot, and it appears as soon as the second argument has an imaginary coefficient.

## The Comparison with the Two Other Failing Brackets

**Remark (the three failures and their three reasons).** Of the twelve operations, exactly one antisymmetric part satisfies the Jacobi identity, the plain outer product $\mathrm{APA}=\vec Q_1\times\vec Q_2$, and the other three antisymmetric parts, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$, fail. The three failures have different reasons. For $\mathrm{AQA}$, the antisymmetric part of the quaternionic bilinear product $\tilde Q_1^{\natural}\tilde Q_2$, the culprit is the non-associativity of the product it comes from, and the failure is visible on the real basis. For $\mathrm{APS}$ and $\mathrm{AQS}$, the antisymmetric parts of the two sesquilinear products, the culprit is the obstruction of *Lie Algebras of Sesqualgebras*: the antisymmetrisation of a sesquilinear product is a Lie bracket only after the collapse of the two involutions, which a genuine sesqualgebra forbids. The witness of $\mathrm{APS}$ is a real triple; the witness of $\mathrm{AQS}$ is the complex triple $(\vec e_x,\vec e_x,i\vec e_y)$, and no real triple works, because on the real part the block is again the cross product.

**Remark (the three objects side by side).**

| the operation | the rule | the class | the Jacobi witness |
|---|---|---|---|
| $\mathrm{APA}$ | $\vec Q_1\times\vec Q_2$ | $\mathbb{C}$-bilinear | none; Jacobi holds |
| $\mathrm{AQA}$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | $\mathbb{C}$-bilinear | a real triple |
| $\mathrm{APS}$ | the antisymmetric part of $\tilde Q_1\tilde Q_2^{*}$ | sesquilinear over $(\mathbb{C},\bar{\cdot})$ | a real triple |
| $\mathrm{AQS}$ | $\vec Q_1\times\overline{\vec Q_2}$ | sesquilinear over $(\mathbb{C},\bar{\cdot})$ | $(\vec e_x,\vec e_x,i\vec e_y)$, complex |

**Remark (the two sesquilinear rows and their forms).** The two sesquilinear rows of the twelve carry the two forms $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, but in their **symmetric** parts: the symmetric part of the plain sesquilinear product is the Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ read as a central-valued product, and the symmetric part of the quaternionic sesquilinear product carries the Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ as its scalar part. The two antisymmetric parts carry no form: $\mathrm{APS}$ is pure vector with rule $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ and diagonal $\mathrm{Vect}(\tilde Q_2\tilde Q_2^{*})$, which is $2i\vec e_z$ at $\vec e_x+i\vec e_y$, and $\mathrm{AQS}$ is the block, pure vector with rule $\vec Q_1\times\overline{\vec Q_2}$ and diagonal $-2i\vec e_z$ at the same element. The block is therefore the antisymmetric part of the $K$-row and the companion of $\mathrm{APS}$, the antisymmetric part of the $\langle\cdot,\cdot\rangle_{*}$-row; the pairing of the block with the form $\langle\cdot,\cdot\rangle_{\natural*}$ is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*.

## Summary

The block is the conjugate cross product $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$, the ordinary cross product with the second factor conjugated, and the conjugation is what distinguishes it from the plain outer product $\mathrm{APA}$ on which it collapses on real elements. Its diagonal is $\tilde Q_2\diamond\tilde Q_2=\vec Q_2\times\overline{\vec Q_2}=-2i\,\vec a\times\vec b$ at $\vec Q_2=\vec a+i\vec b$, and it vanishes exactly when the vector part is a complex multiple of a real vector; the vanishing set is a cone of real dimension six, its vector part carrying the four-dimensional cone of the complex multiples of the real directions, and it is exhibited by $\vec e_x+i\vec e_y$, whose diagonal is $-2i\vec e_z$. The Jacobi identity fails, with the declared cyclic sum at $(\vec e_x,\vec e_x,i\vec e_y)$ equal to $-2i\vec e_y$; the witness needs a complex element because on the real forms the block is the cross product and the identity holds there, so the failure is a feature of the complex structure and of the conjugate-linear slot. The comparison with the other failing brackets $\mathrm{AQA}$ and $\mathrm{APS}$ places the block as the $K$-companion of the plain sesquilinear bracket.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\diamond\tilde Q_2=\vec Q_1\times\overline{\vec Q_2}$ | the conjugate cross product |
| $\vec Q_2=\vec a+i\vec b$, $\vec a,\vec b$ real | the real decomposition of the vector part |
| $\tilde Q_2\diamond\tilde Q_2=-2i\,\vec a\times\vec b$ | the diagonal |
| $\vec Q_2$ a complex multiple of a real vector | the vanishing of the diagonal, the vector part on a cone of real dimension $4$ (the vanishing set itself, the scalar coordinate being free, of real dimension $6$) |
| $(\vec e_x,\vec e_x,i\vec e_y)\mapsto-2i\vec e_y$ | the Jacobi witness and its declared cyclic sum |
| $\mathrm{APA}=\vec Q_1\times\vec Q_2$ | the real collapse of the block |
| $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the forms of the two sesquilinear rows, on the central line |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Sesqualgebra*, for the block, its class and its diagonal.
- *The 12 Products of the Biquaternion Complex Space*, for the three Jacobi failures and their witnesses.
- *Lie Algebras of Sesqualgebras*, for the obstruction behind the two sesquilinear failures.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the class-preserving exchange.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, for the square whose conjugate half-difference is the block.
- *Introduction to the Antisymmetric Plain Algebra*, for the cross product on the real part.
- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, for the form of the block.
