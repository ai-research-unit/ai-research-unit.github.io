# __The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

The multiplication of the block *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* is the operation

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}},
$$

the cross product of the vector part of the first argument with the **conjugate** of the vector part of the second. The conjugation in the second slot is the whole content of the block: it is what makes the operation sesquilinear rather than bilinear, what makes its diagonal nonzero, and what makes its Jacobi identity fail on a witness that no real element can supply. This article develops the three consequences. The **conjugate cross product** is read first, with its coordinate rule and its position between the ordinary cross product and its conjugate. The **diagonal** $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}$ is then identified with the conjugate cross product of the vector part with itself, and its vanishing is reduced to a single condition on that vector part — that it be a complex multiple of a real vector — which is a four-real-dimensional condition and cuts an explicit quadric cone. The **failure of the Jacobi identity** is stated with the declared cyclic sum and the witness $(e_1,e_1,ie_2)$, its value $-2ie_2$ is recomputed, and the reason the witness needs a complex element, and the reason the failure is invisible on the real forms, are given. The comparison with the two other failing brackets $\mathrm{AQA}$ and $\mathrm{APS}$ closes the reading.

The product the block splits and its two halves are *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* and *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*; the general construction of a sesqualgebra part is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the obstruction behind the failing law is *Lie Algebras of Sesqualgebras*; the ordinary cross product of the real elements is *Introduction to the Antisymmetric Plain Algebra of Biquaternions*; and the three failing brackets are tabulated in *The 12 Products of the Biquaternion Complex Space*.

**Conventions.** As in *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$ and $e_k^2=-e_0$; a generic element is $\tilde Q=Q_0e_0+\mathbf{Q}$, with $\mathbf{Q}=\sum_kQ_ke_k$, $\overline{\mathbf{Q}}=\sum_k\overline{Q_k}e_k$, and $Q_k=q_k+iq'_k$ with $q_k,q'_k$ real. The product is written $\diamond$ for the block.

## The Conjugate Cross Product

### The Rule and the Conjugation

**Definition.** The **conjugate cross product** is $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$. The name records the two operations it intertwines: it is the ordinary cross product $\mathbf{P}\times\mathbf{Q}$ of the two vector parts with the second factor conjugated. On a real vector the conjugation is invisible, so the operation escapes the cross product only when the second argument carries a complex coordinate.

**Proposition (coordinate rule).** In coordinates,

$$
\tilde P\diamond\tilde Q=\bigl(P_2\overline{Q_3}-P_3\overline{Q_2}\bigr)e_1
+\bigl(P_3\overline{Q_1}-P_1\overline{Q_3}\bigr)e_2
+\bigl(P_1\overline{Q_2}-P_2\overline{Q_1}\bigr)e_3 .
$$

*Proof.* The three components of the cross product of $\mathbf{P}$ and $\overline{\mathbf{Q}}$, read in the quaternion basis. Verified on the coordinate rule.

**Remark (the two slots).** The first slot enters $\mathbb{C}$-linearly and the second conjugate-linearly, so the operation is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ and not bilinear. This is the class of the block, and it is the class of the two sesqualgebras of the corpus; the general construction of the parts keeps the class by using the class-preserving exchange, and the antisymmetric part is therefore again sesquilinear. The block carries the conjugation in the second slot like the five other sesquilinear operations of the twelve; what singles it out is that its value is the conjugate cross product alone, and every later fact of the block is a consequence of that single asymmetry.

### The Value as a Cross Product with the Conjugate

**Proposition (the value intertwines the two cross products).** For all biquaternions,

$$
\overline{\tilde P\diamond\tilde Q}=\overline{\mathbf{P}}\times\mathbf{Q},\qquad
\tilde Q\diamond\tilde P=-\overline{\tilde P\diamond\tilde Q}.
$$

*Proof.* $\overline{\mathbf{P}\times\overline{\mathbf{Q}}}=\overline{\mathbf{P}}\times\mathbf{Q}$, and the second identity is the first applied to the swapped pair. Verified on the coordinate rule.

The block and its conjugate share the value $\mathbf{P}\times\overline{\mathbf{Q}}$ only when $\mathbf{P}\times\overline{\mathbf{Q}}$ is real, which is the case on the real basis; off it the conjugate of the value is the cross product with the roles of the conjugations exchanged.

## The Diagonal and Its Cone

### The Diagonal

**Theorem.** For every biquaternion,

$$
\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}},
$$

and if $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$ with $\mathbf{a},\mathbf{b}$ real vectors, then

$$
\mathbf{Q}\times\overline{\mathbf{Q}}=-2i\,\mathbf{a}\times\mathbf{b}.
$$

*Proof.* The rule with $\tilde P=\tilde Q$; and $(\mathbf{a}+i\mathbf{b})\times(\mathbf{a}-i\mathbf{b})=-i\,\mathbf{a}\times\mathbf{b}+i\,\mathbf{b}\times\mathbf{a}=-2i\,\mathbf{a}\times\mathbf{b}$. Verified on general elements.

**Example.** At $\tilde Q=e_1+ie_2$ one has $\mathbf{a}=e_1$, $\mathbf{b}=e_2$, $\mathbf{a}\times\mathbf{b}=e_3$ and $\tilde Q\diamond\tilde Q=-2ie_3$. At a real element the diagonal vanishes, and at $\tilde Q=ie_1+ie_2=i(e_1+e_2)$ the diagonal is $i(e_1+e_2)\times\overline{i(e_1+e_2)}=i(e_1+e_2)\times(-i)(e_1+e_2)=0$.

### The Criterion

**Theorem (the vanishing of the diagonal).** The diagonal vanishes at $\tilde Q$ exactly when the vector part $\mathbf{Q}$ is a complex multiple of a real vector; equivalently, exactly when $\mathbf{Q}$ and $\overline{\mathbf{Q}}$ are $\mathbb{C}$-linearly dependent.

*Proof.* The condition $\mathbf{Q}\times\overline{\mathbf{Q}}=0$ says that $\overline{\mathbf{Q}}$ is a complex multiple of $\mathbf{Q}$, that is $\overline{\mathbf{Q}}=\mu\mathbf{Q}$ for some $\mu\in\mathbb{C}$, and this is the linear dependence. Write $\mu=p+iq$ and $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$ with $\mathbf{a},\mathbf{b}$ real. The equation $\mathbf{a}-i\mathbf{b}=(p+iq)(\mathbf{a}+i\mathbf{b})$ splits into the two real vector equations $(1-p)\mathbf{a}+q\,\mathbf{b}=0$ and $-q\,\mathbf{a}-(1+p)\mathbf{b}=0$. A nonzero pair $(\mathbf{a},\mathbf{b})$ exists exactly when the determinant $1-p^{2}-q^{2}$ vanishes, that is $|\mu|=1$; and then the two equations force $\mathbf{a}$ and $\mathbf{b}$ to be real multiples of one another, so $\mathbf{Q}$ is a complex multiple of the common real direction. Conversely, if $\mathbf{Q}=\lambda\mathbf{v}$ with $\lambda\in\mathbb{C}$ and $\mathbf{v}$ real, then $\overline{\mathbf{Q}}=\overline{\lambda}\mathbf{v}$ and $\mathbf{Q}\times\overline{\mathbf{Q}}=\lambda\overline{\lambda}\,\mathbf{v}\times\mathbf{v}=0$. Verified on general elements and on a thousand sampled elements, where the vanishing of the cross product agrees with the vanishing of the three real minors at every sample.

**Remark (the condition in coordinates).** The two real vectors are $\mathbf{a}=(q_1,q_2,q_3)$ and $\mathbf{b}=(q'_1,q'_2,q'_3)$, so the condition is the vanishing of the real cross product $\mathbf{a}\times\mathbf{b}$, that is the vanishing of the three minors $q_2q'_3-q_3q'_2$, $q_3q'_1-q_1q'_3$ and $q_1q'_2-q_2q'_1$. These are three real quadratic equations on the eight real coordinates of $\tilde Q$, so the vanishing set is a **quadric cone** of the space, the common zero set of the three, and not a hypersurface.

**Corollary (the cone of the diagonal).** The set $\{\tilde Q:\tilde Q\diamond\tilde Q=0\}$ is the union, over the real directions $\mathbf{v}$ of the vector subspace, of the complex planes $\mathbb{C}e_0\oplus\mathbb{C}\mathbf{v}$; the scalar coordinate is free, and the vector part runs over the union of the complex lines $\mathbb{C}\mathbf{v}$. The cone carried by the vector part has real dimension $4$, and with the free scalar coordinate the vanishing set has real dimension $6$.

*Proof.* A real direction contributes two real parameters, and the complex multiple $\lambda$ two more, so the union of the complex lines $\mathbb{C}\mathbf{v}$ in the vector part has real dimension $4$. The diagonal reads the vector parts alone, so the scalar coordinate $Q_0$ is unconstrained and adds two real dimensions: the vanishing set is the union of the complex planes $\mathbb{C}e_0\oplus\mathbb{C}\mathbf{v}$, of real dimension $4+2=6$, and it is not the union of the complex lines $\mathbb{C}\mathbf{v}$ alone, which lies in the vector subspace. Verified on the basis and on sampled elements, with the scalar coordinate varied independently of the vector part.

**Remark (the elements of square zero).** The elements with $\tilde Q\diamond\tilde Q=0$ are exactly the elements whose vector part lies on one complex line over a real direction, whatever the scalar coordinate; the vanishing therefore holds on the whole centre, on every real vector $\mathbf{Q}\in\mathbb{R}^{3}$, on every purely imaginary vector $i\mathbb{R}^{3}$, on the complex multiples of any one real direction, and on the sums of any central element with any of these; it fails on a general complex vector, and the witness $e_1+ie_2$ is the smallest failure. The condition on the vector part is a genuine four-real-dimensional one and not the trivial one of the bilinear blocks, where the diagonal of the antisymmetric part vanishes identically.

## The Failure of the Jacobi Identity

### The Declared Cyclic Sum and the Witness

**Theorem.** The block fails the Jacobi identity. With the cyclic sum declared by the corpus,

$$
(\tilde P\diamond\tilde Q)\diamond\tilde R+(\tilde Q\diamond\tilde R)\diamond\tilde P+(\tilde R\diamond\tilde P)\diamond\tilde Q,
$$

the triple $(\tilde P,\tilde Q,\tilde R)=(e_1,e_1,ie_2)$ gives the value $-2ie_2$.

*Proof.* The three inner values are $e_1\diamond e_1=0$, $e_1\diamond ie_2=e_1\times(-ie_2)=-ie_3$ and $ie_2\diamond e_1=(ie_2)\times e_1=-ie_3$. The three reassociations are therefore $0$, $(-ie_3)\diamond e_1=(-ie_3)\times e_1=-ie_2$ and $(-ie_3)\diamond e_1=-ie_2$, whose sum is $-2ie_2$. Verified on the witness.

### Why the Witness Needs a Complex Element

**Proposition.** No triple of the real basis witnesses the failure, and more generally the cyclic sum vanishes on every triple of real elements.

*Proof.* On real elements the block is the ordinary cross product, $\tilde P\diamond\tilde Q=\mathbf{P}\times\mathbf{Q}$, by the coincidence of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*; the cyclic sum is then the Jacobi sum of the cross product, which vanishes identically, the cross product being the Lie bracket of $\mathbb{R}^{3}$. So a witness must use at least one element with a nonzero imaginary coefficient, and the declared witness uses the smallest such element that fails, $ie_2$ together with the pair $e_1,e_1$. Verified on the real basis and on sampled real triples.

**Remark (the failure is a feature of the complex slot, not of the real part).** The vanishing on the real forms is the general collapse of the corpus: on the real part the twelve operations fall to ten and the block coincides with $\mathrm{APA}$, so every law that depends only on the real part, the Jacobi identity among them, is the law of the cross product and holds. The failure is produced by the conjugate in the second slot, and it appears as soon as the second argument has an imaginary coefficient.

## The Comparison with the Two Other Failing Brackets

**Remark (the three failures and their three reasons).** Of the twelve operations, exactly one antisymmetric part satisfies the Jacobi identity, the plain outer product $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$, and the other three antisymmetric parts, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$, fail. The three failures have different reasons. For $\mathrm{AQA}$, the antisymmetric part of the quaternionic bilinear product $\tilde P^{\natural}\tilde Q$, the culprit is the non-associativity of the product it comes from, and the failure is visible on the real basis. For $\mathrm{APS}$ and $\mathrm{AQS}$, the antisymmetric parts of the two sesquilinear products, the culprit is the obstruction of *Lie Algebras of Sesqualgebras*: the antisymmetrisation of a sesquilinear product is a Lie bracket only after the collapse of the two involutions, which a genuine sesqualgebra forbids. The witness of $\mathrm{APS}$ is a real triple; the witness of $\mathrm{AQS}$ is the complex triple $(e_1,e_1,ie_2)$, and no real triple works, because on the real part the block is again the cross product.

**Remark (the three objects side by side).**

| the operation | the rule | the class | the Jacobi witness |
|---|---|---|---|
| $\mathrm{APA}$ | $\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$-bilinear | none; Jacobi holds |
| $\mathrm{AQA}$ | $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$-bilinear | a real triple |
| $\mathrm{APS}$ | the antisymmetric part of $\tilde P\tilde Q^{*}$ | sesquilinear over $(\mathbb{C},\bar{\cdot})$ | a real triple |
| $\mathrm{AQS}$ | $\mathbf{P}\times\overline{\mathbf{Q}}$ | sesquilinear over $(\mathbb{C},\bar{\cdot})$ | $(e_1,e_1,ie_2)$, complex |

**Remark (the two sesquilinear rows and their forms).** The two sesquilinear rows of the twelve carry the two forms $H$ and $K$, but in their **symmetric** parts: the symmetric part of the plain sesquilinear product is the Hermitian form $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ read as a central-valued product, and the symmetric part of the quaternionic sesquilinear product carries the Krein form $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ as its scalar part. The two antisymmetric parts carry no form: $\mathrm{APS}$ is pure vector with rule $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ and diagonal $\mathrm{Vect}(\tilde Q\tilde Q^{*})$, which is $2ie_3$ at $e_1+ie_2$, and $\mathrm{AQS}$ is the block, pure vector with rule $\mathbf{P}\times\overline{\mathbf{Q}}$ and diagonal $-2ie_3$ at the same element. The block is therefore the antisymmetric part of the $K$-row and the companion of $\mathrm{APS}$, the antisymmetric part of the $H$-row; the pairing of the block with the form $K$ is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*.

## Summary

The block is the conjugate cross product $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$, the ordinary cross product with the second factor conjugated, and the conjugation is what distinguishes it from the plain outer product $\mathrm{APA}$ on which it collapses on real elements. Its diagonal is $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}=-2i\,\mathbf{a}\times\mathbf{b}$ at $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$, and it vanishes exactly when the vector part is a complex multiple of a real vector; the vanishing set is a cone of real dimension six, its vector part carrying the four-dimensional cone of the complex multiples of the real directions, and it is exhibited by $e_1+ie_2$, whose diagonal is $-2ie_3$. The Jacobi identity fails, with the declared cyclic sum at $(e_1,e_1,ie_2)$ equal to $-2ie_2$; the witness needs a complex element because on the real forms the block is the cross product and the identity holds there, so the failure is a feature of the complex structure and of the conjugate-linear slot. The comparison with the other failing brackets $\mathrm{AQA}$ and $\mathrm{APS}$ places the block as the $K$-companion of the plain sesquilinear bracket.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ | the conjugate cross product |
| $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$, $\mathbf{a},\mathbf{b}$ real | the real decomposition of the vector part |
| $\tilde Q\diamond\tilde Q=-2i\,\mathbf{a}\times\mathbf{b}$ | the diagonal |
| $\mathbf{Q}$ a complex multiple of a real vector | the vanishing of the diagonal, the vector part on a cone of real dimension $4$ (the vanishing set itself, the scalar coordinate being free, of real dimension $6$) |
| $(e_1,e_1,ie_2)\mapsto-2ie_2$ | the Jacobi witness and its declared cyclic sum |
| $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$ | the real collapse of the block |
| $H$, $K$ | the forms of the two sesquilinear rows, on the central line |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, for the block, its class and its diagonal.
- *The 12 Products of the Biquaternion Complex Space*, for the three Jacobi failures and their witnesses.
- *Lie Algebras of Sesqualgebras*, for the obstruction behind the two sesquilinear failures.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the class-preserving exchange.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, for the square whose conjugate half-difference is the block.
- *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, for the cross product on the real part.
- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, for the form of the block.
