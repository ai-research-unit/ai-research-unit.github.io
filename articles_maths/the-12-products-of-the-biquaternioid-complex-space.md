# __The 12 Products of the Biquaternioid Complex Space__

## Introduction

The biquaternion complex space carries four multiplications, the **four general products** of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*. Every one of the four is split into a **symmetric part** and an **antisymmetric part**, and the two parts are operations of the same class as the product they split, so the space carries the **twelve products**. This article writes each of the twelve out and reads the laws that separate them; the twelve names they carry, the abbreviations and the structure each of them defines are the matter of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

The general construction, with the obstruction of the class and the two projections, is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the method of the decomposition is §*The Method of the Decomposition*, below.

The article assumes the four general products from *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, the elements, the basis and the four conjugations from *The Biquaternioid as a Vector Space over $\mathbb{C}$*, and the split itself, in its two forms, from *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**Conventions.** The complex space is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$. An element is $\tilde Q_2=Q_{2,0}e_0+\vec Q_2$ with $\vec Q_2=\sum_{k=1}^{3}Q_{2,k} e_k$ and $Q_{2,\mu}\in\mathbb{C}$. The natural conjugation ${}^{\natural}$ negates the vector part, the coefficientwise one $\bar{\cdot}$ conjugates the coefficients, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The four general products are the **general plain bilinear** $\tilde Q_1\tilde Q_2$, the **general plain sesquilinear** $\tilde Q_1\tilde Q_2^{*}$, the **general quaternionic bilinear** $\tilde Q_1^{\natural}\tilde Q_2$ and the **general quaternionic sesquilinear** $\tilde Q_1^{\natural}\tilde Q_2^{*}$ (*The Four General Products of the Biquaternioid $\mathbb{C}$ Space*), and the split of each of them into its two parts is §*The Method of the Decomposition*, below. The dot product $(\vec Q_1,\vec Q_2)$ and the cross product $\vec Q_1\times\vec Q_2$ are the general plain bilinear ones, and $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ are the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces (*Introduction to the Remarkable Subspaces*). A vector expression such as $i\,\mathrm{Im}(\vec v)$ is read componentwise. The **cyclic sum** of a bracket $b$ is the outer form $b(b(x,y),z)+b(b(y,z),x)+b(b(z,x),y)$ of *The Symmetric and Antisymmetric Parts of an Algebra Product*, §*Lie-Admissible Algebras*, so that a bracket written without the factor $\tfrac12$ has its cyclic sum multiplied by four.

Throughout, the element $\tilde Q_1 = Q_{1,0} + \vec Q_1$ separates the complex scalar part $Q_{1,0}$ from the complex vector part $\vec Q_1 = Q_{1,1}e_1+Q_{1,2}e_2+Q_{1,3}e_3$; $\overline{\vec Q_1}$ is the coefficientwise conjugate of the vector part, $(\vec Q_1,\vec Q_2)$ the complex bilinear dot product and $\vec Q_1\times\vec Q_2$ the complex bilinear cross product, as in *The Biquaternioid as a Vector Space over $\mathbb{C}$*.

---

## The Four General Products

The four general products are the four multiplications of the space. Written on the coordinates, they are

$$
\tilde Q_1\tilde Q_2 = \bigl[Q_{1,0}Q_{2,0}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1,0}\vec Q_2+Q_{2,0}\vec Q_1+\vec Q_1\times\vec Q_2,
$$

$$
\tilde Q_1\tilde Q_2^{*} = \bigl[Q_{1,0}\overline{Q_{2,0}}+(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2,0}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2},
$$

$$
\tilde Q_1^{\natural}\tilde Q_2 = \bigl[Q_{1,0}Q_{2,0}+(\vec Q_1,\vec Q_2)\bigr]+Q_{1,0}\vec Q_2-Q_{2,0}\vec Q_1-\vec Q_1\times\vec Q_2,
$$

$$
\tilde Q_1^{\natural}\tilde Q_2^{*} = \bigl[Q_{1,0}\overline{Q_{2,0}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2,0}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}.
$$

The two bilinear products are $\mathbb C$-bilinear in both slots; they differ only in the reading of the first factor through the natural conjugation ${}^{\natural}$. The two sesquilinear products are $\mathbb C$-linear in the first slot and conjugate-linear in the second, and differ in the same way. No two of the four agree on every pair. The four are developed, with the identities that link them and their property table, in *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, *Relations Between the Four General Products* and *Comparison Between the Four General Products*.

---

## The Method of the Decomposition

Every one of the four general products is split into a **symmetric part** and an **antisymmetric part**, and the split is a different operation in the two families of products. There are two definitions, one to a family.

**The bilinear case.** The general plain bilinear product $\tilde Q_1\tilde Q_2$ and the general quaternionic bilinear product $\tilde Q_1^{\natural}\tilde Q_2$ have two $\mathbb{C}$-linear slots. Their exchange is the interchange of the two arguments, and the two parts are

$$
f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+f(\tilde Q_2,\tilde Q_1)\bigr),\qquad f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)-f(\tilde Q_2,\tilde Q_1)\bigr).
$$

**The sesquilinear case.** The general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ and the general quaternionic sesquilinear product $\tilde Q_1^{\natural}\tilde Q_2^{*}$ have one linear slot and one conjugate-linear slot, and the interchange alone returns a product of the opposite type, $\tilde Q_2\tilde Q_1^{*}$, which is not a product of the class at all. The exchange is the interchange followed by the coefficientwise conjugation of the value, and the two parts are

$$
f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+\overline{f(\tilde Q_2,\tilde Q_1)}\bigr),\qquad f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)-\overline{f(\tilde Q_2,\tilde Q_1)}\bigr).
$$

**The two definitions are not one.** The interchange keeps the class of a product exactly when its two slots have the same type, which is the bilinear case; in the sesquilinear case it does not, and it is the conjugation of the value that repairs the class. The two definitions agree only for the two $\mathbb{C}$-bilinear products, and the split of a bilinear product and the split of a sesquilinear product share their shape and not their definition. Both exchanges are involutions of the class — the interchange of the interchange, and the conjugate transpose of the conjugate transpose, return the product they start from — so the two parts are well defined in both cases. The adapted exchange, with the obstruction of the class and the two projections of the space of products, is developed in *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**What the two cases share.** The two parts carry the reconstruction $f=f^{\mathrm{s}}+f^{\mathrm{a}}$; the symmetric part is fixed by the exchange and the antisymmetric part is negated by it; and the pair is unique, since $f=s+t$ with $s$ fixed and $t$ negated forces $s=f^{\mathrm{s}}$ and $t=f^{\mathrm{a}}$. Both parts are products of the class of $f$ — $\mathbb{C}$-bilinear in the bilinear case, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ in the sesquilinear case — and it is for that closure that the exchange of the sesquilinear case is adapted and not bare.

**The square and its algebraic norm, where the two part company.** In the **bilinear case** the antisymmetric part vanishes at the two equal arguments, since $f^{\mathrm{a}}(\tilde Q_2,\tilde Q_2)=-f^{\mathrm{a}}(\tilde Q_2,\tilde Q_2)$, so the square is the symmetric part alone, $f(\tilde Q_2,\tilde Q_2)=f^{\mathrm{s}}(\tilde Q_2,\tilde Q_2)$, and the polarisation of the square recovers the symmetric part away from the two equal arguments. In the **sesquilinear case** the antisymmetric part at the two equal arguments is the antisymmetrised square,

$$
f^{\mathrm{a}}(\tilde Q_2,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_2,\tilde Q_2)-\overline{f(\tilde Q_2,\tilde Q_2)}\bigr),
$$

which **need not vanish**: it vanishes exactly when the square of the element is fixed by the coefficientwise conjugation. The polarisation of the square then recovers the **plain** symmetrisation — the half-sum with the bare interchange — and not the symmetric part. The bilinear case has no antisymmetric algebraic norm, the sesquilinear case has one and it is not zero in general.

**The bare interchange is not the exchange.** The two halves of the bare interchange of a sesquilinear product are only $\mathbb{R}$-bilinear and are not products of the class: they are the symmetrised sesquilinear product $x\circ y$ of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator*. They are not the two parts read below, in the sesquilinear case or in any case. The reading of the four splits from the side of the order symmetry is §*The Twelve Products, One by One*, below, where the exchange that keeps the class is contrasted with the bare interchange.

---

## The Twelve Products, One by One

Each product is read with its two parts. The four general products come first, then their four symmetric parts, then their four antisymmetric parts; and inside each group of four the order is the plain bilinear, the plain sesquilinear, the quaternionic bilinear and the quaternionic sesquilinear product. The laws are collected in the table, below, and the classical identities in *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

Throughout the reading, $f$ is the product being read and $s$ and $a$ are its symmetric and its antisymmetric part, defined as in §*The Method of the Decomposition*: the plain interchange of the two arguments in the two $\mathbb{C}$-bilinear families and the conjugate transpose in the two sesquilinear ones.

### The General Plain Bilinear Product

$$
\tilde Q_1\tilde Q_2=\bigl[Q_{1,0}Q_{2,0}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1,0}\vec Q_2+Q_{2,0}\vec Q_1+\vec Q_1\times\vec Q_2.
$$

The general plain bilinear product, the multiplication of the two elements as they stand: scalar part $Q_{1,0}Q_{2,0}-(\vec Q_1,\vec Q_2)$ and vector part $Q_{1,0}\vec Q_2+Q_{2,0}\vec Q_1+\vec Q_1\times\vec Q_2$. It is $\mathbb{C}$-bilinear, **associative**, and $e_0$ is a unit on both sides. It is the only associative product of the twelve.

Its values fill the whole space $\mathbb{B}$.

### The General Plain Sesquilinear Product

$$
\tilde Q_1\tilde Q_2^{*}=\bigl[Q_{1,0}\overline{Q_{2,0}}+(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2,0}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}.
$$

The general plain sesquilinear product, the second factor read through the Hermitian conjugation ${}^{*}$. Both products of the pair are the natural conjugates of the two orders of one underlying product,
$$
\tilde Q_1\tilde Q_2^{*}=\bigl(\overline{\tilde Q}_2\tilde Q_1^{\natural}\bigr)^{\natural},\qquad
\tilde Q_2\tilde Q_1^{*}=\bigl(\overline{\tilde Q}_1\tilde Q_2^{\natural}\bigr)^{\natural}.
$$
It is sesquilinear over $(\mathbb{C},\bar{\cdot})$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second; it is **not associative**, and $e_0$ is a unit on the **right** only.

Its values fill the whole space $\mathbb{B}$.

### The General Quaternionic Bilinear Product

$$
\tilde Q_1^{\natural}\tilde Q_2=\bigl[Q_{1,0}Q_{2,0}+(\vec Q_1,\vec Q_2)\bigr]+Q_{1,0}\vec Q_2-Q_{2,0}\vec Q_1-\vec Q_1\times\vec Q_2.
$$

The general quaternionic bilinear product, the general plain bilinear product with the first factor read through ${}^{\natural}$. It is $\mathbb{C}$-bilinear, **not associative**, and $e_0$ is a unit on the **left** only. Its exchange is the natural conjugation of its value, $\tilde Q_2^{\natural}\tilde Q_1=(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}$.

Its values fill the whole space $\mathbb{B}$.

### The General Quaternionic Sesquilinear Product

$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl[Q_{1,0}\overline{Q_{2,0}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2,0}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}.
$$

The general quaternionic sesquilinear product, both slots read through a conjugation. Both products of the pair are the natural conjugates of the two orders of one underlying product,
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl(\overline{\tilde Q}_2\tilde Q_1\bigr)^{\natural},\qquad
\tilde Q_2^{\natural}\tilde Q_1^{*}=\bigl(\overline{\tilde Q}_1\tilde Q_2\bigr)^{\natural}.
$$
It is sesquilinear over $(\mathbb{C},\bar{\cdot})$, **not associative**, and it has a unit on **neither** side. It is the product whose ternary product fails the Jordan triple identity (*The Biquaternioid General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*).

Its values fill the whole space $\mathbb{B}$.

### The Symmetric Plain Bilinear Product

The symmetric part of the general plain bilinear product above.

$$
\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr)=\bigl[Q_{1,0}Q_{2,0}-(\vec Q_1,\vec Q_2)\bigr]+Q_{1,0}\vec Q_2+Q_{2,0}\vec Q_1.
$$

The Jordan product $\tilde Q_1\bullet\tilde Q_2$, the general plain bilinear product with the cross term dropped. It is commutative, $e_0$ is a unit on both sides, and it satisfies the **Jordan identity**; it is the only one of the four symmetric parts that does, and it is the only part of the eight that has a unit at all. The identity is not put to the four general products, which are neither symmetrisations nor antisymmetrisations; the counts over the parts are in §*The Counts of the Failures*.

### The Symmetric Plain Sesquilinear Product

The symmetric part of the general plain sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)
=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)
=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)
=\bigl[Q_{1,0}\overline{Q_{2,0}}+(\vec Q_1,\overline{\vec Q_2})\bigr].
$$

The value $\tilde Q_1\tilde Q_2^{*}$ has scalar part $H=Q_{1,0}\overline{Q_{2,0}}+(\vec Q_1,\overline{\vec Q_2})$ and vector part $-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2,0}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$; the conjugate transpose sends the value to its conjugate with the vector part negated, $\overline{\tilde Q_2\tilde Q_1^{*}}=(\tilde Q_1\tilde Q_2^{*})^{\natural}$, so the half-sum keeps the scalar part and cancels the vector part. The operation is the **Hermitian form** $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=Q_{1,0}\overline{Q_{2,0}}+(\vec Q_1,\overline{\vec Q_2})$ of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* read as a product, and it is **central**: its values lie in the centre $\mathbb{C}_{\mathbb{B}}$. It is **conjugate-commutative**, $s(\tilde Q_1,\tilde Q_2)=\overline{s(\tilde Q_2,\tilde Q_1)}$, rather than commutative, and it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, conjugate-linear in the second argument. Its algebraic norm is the square read through the form, $s(\tilde Q_2,\tilde Q_2)=\langle\tilde Q_2,\tilde Q_2\rangle_{*}=|Q_{2,0}|^{2}+(\vec Q_2,\overline{\vec Q_2})$, which is real and strictly positive off the origin. Being central-valued it has no unit, and it **fails** the Jordan identity on the whole space, with witness $x=y=e_1$, where the two sides are $0$ and $e_0$.

### The Symmetric Quaternionic Bilinear Product

The symmetric part of the general quaternionic bilinear product above.

$$
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1\bigr)=\bigl[Q_{1,0}Q_{2,0}+(\vec Q_1,\vec Q_2)\bigr].
$$

The quaternion form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1,0}Q_{2,0}+(\vec Q_1,\vec Q_2)$ of *Comparison Between the Four General Products* read as a product; its scalar part is $\langle\cdot\rangle$ and its vector part is zero. It is commutative, its values lie in the centre $\mathbb{C}_{\mathbb{B}}$ — it compares two elements and returns a multiple of $e_0$ — and it has no unit. It is **not** a Jordan product.

### The Symmetric Quaternionic Sesquilinear Product

The symmetric part of the general quaternionic sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}\bigr)
=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)
=\bigl[Q_{1,0}\overline{Q_{2,0}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2,0}}\vec Q_1,
$$

since $\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}=\tilde Q_2^{*}\tilde Q_1^{\natural}$. The value $\tilde Q_1^{\natural}\tilde Q_2^{*}$ has scalar part $K=Q_{1,0}\overline{Q_{2,0}}-(\vec Q_1,\overline{\vec Q_2})$ and vector part $-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2,0}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$; the conjugate transpose is not the conjugation of the value here — the two cross products cancel between the two orders instead of adding — so the half-sum keeps the scalar part and the mixed term and cancels the cross product. Its scalar part is the general quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$ of *The Krein Gram Matrix and the Restrictions of the Form* and its vector part is $-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2,0}}\vec Q_1$, so its values lie in **no** subspace of the remarkable subspaces. It is **conjugate-commutative**, $s(\tilde Q_1,\tilde Q_2)=\overline{s(\tilde Q_2,\tilde Q_1)}$, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jordan identity, with witness $x=y=e_1$ where the two sides are $-e_0$ and $e_0$. Its algebraic norm is not central in general: at $\tilde Q_2=e_0+e_1$ it is $-2e_1$, while the real vector directions, among them $e_1$, carry central algebraic norms.

### The Antisymmetric Plain Bilinear Product

The antisymmetric part of the general plain bilinear product above.

$$
\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr)=\vec Q_1\times\vec Q_2.
$$

The outer product $\tilde Q_1\wedge\tilde Q_2$, the cross product of the two vector parts alone: scalar part zero, vector part $\vec Q_1\times\vec Q_2$. It is alternating, its values lie in the vector subspace $\mathrm{Vect}(\mathbb{B})$, and it satisfies the **Jacobi identity**; it is the only one of the twelve that does. It is half the commutator of the general plain bilinear product, $[\tilde Q_1,\tilde Q_2]=\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1$.

### The Antisymmetric Plain Sesquilinear Product

The antisymmetric part of the general plain sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)
=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)
=\mathrm{Vect}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)
=-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2,0}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}.
$$

The same value as the symmetric part, with the difference in place of the sum: the half-difference cancels the scalar part and keeps the vector part. It is **pure vector**, so its image is the vector subspace $\mathrm{Vect}(\mathbb{B})$. It is **conjugate-alternating**, $\mathfrak{a}(\tilde Q_1,\tilde Q_2)=-\overline{\mathfrak{a}(\tilde Q_2,\tilde Q_1)}$, and its algebraic norm is the **vector part of the square**,
$$
\mathfrak{a}(\tilde Q_2,\tilde Q_2)=\mathrm{Vect}(\tilde Q_2\tilde Q_2^{*}),
$$
which is **not zero** in general: for $\tilde Q_2=e_1+ie_2$ it is $2ie_3$. It has no unit, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jacobi identity, with witness $(e_0,e_1,e_2)$ where the cyclic sum is $e_3$.

### The Antisymmetric Quaternionic Bilinear Product

The antisymmetric part of the general quaternionic bilinear product above.

$$
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr)=Q_{1,0}\vec Q_2-Q_{2,0}\vec Q_1-\vec Q_1\times\vec Q_2.
$$

The quaternionic product with its scalar part removed: scalar part zero, vector part the mixed term with the cross term subtracted. It is alternating, its values lie in the vector subspace, and it **fails** the Jacobi identity, with witness $(e_0,e_1,e_2)$ where the cyclic sum is $-e_3\neq0$. It is half the commutator $[\tilde Q_1,\tilde Q_2]_{\natural}=\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1$.

### The Antisymmetric Quaternionic Sesquilinear Product

The antisymmetric part of the general quaternionic sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}\bigr)
=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)
=\vec Q_1\times\overline{\vec Q_2}.
$$

The cross products of the two orders add in the difference while the scalar part and the mixed term cancel, so the half-difference is the **cross product** $\vec Q_1\times\overline{\vec Q_2}$ of the vector part of the first argument with the conjugate of the vector part of the second. It is **pure vector**, so its image is the vector subspace $\mathrm{Vect}(\mathbb{B})$; it is **conjugate-alternating**, $\mathfrak{a}(\tilde Q_1,\tilde Q_2)=-\overline{\mathfrak{a}(\tilde Q_2,\tilde Q_1)}$, and its algebraic norm is the cross product of the vector part with its conjugate, $\mathfrak{a}(\tilde Q_2,\tilde Q_2)=\vec Q_2\times\overline{\vec Q_2}$, which is **not zero** in general: for $\tilde Q_2=e_1+ie_2$ it is $-2ie_3$. It has no unit, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jacobi identity, with witness $(e_1,e_1,ie_2)$, where the cyclic sum is $-2ie_2$. This is the only one of the three failing brackets whose witness needs a complex element off the real basis, which is why the failure is invisible on the real forms.

### The Exchange Behind the Split

The twelve products are read against the exchange of §*The Method of the Decomposition*: the interchange for the two $\mathbb{C}$-bilinear products, whose two slots have the same type, and the conjugate transpose for the two sesquilinear products, whose slots are one linear and one conjugate-linear. It is an involution of the class in both cases, and it is the exchange that makes the count $4\times3$ while keeping every part in the class of its parent: the six $\mathbb{C}$-bilinear parts and the six sesquilinear parts.

The bare interchange does not keep the class, and its two halves — the symmetrised sesquilinear product $x\circ y$ of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator* — are **not** the two parts of the general plain sesquilinear product read here; the two readings are set side by side in §*The Adapted Exchange* of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**Whether the exchange is read on the value.** The split needs only the involution, which §*The Method of the Decomposition*, above settles for the four general products; whether the exchange can be read on the value of the product is a second question, and the two sesquilinear families answer it differently. The **sesquilinear** product has it, since $\overline{\tilde Q_2\tilde Q_1^{*}}=(\tilde Q_1\tilde Q_2^{*})^{\natural}$, which is why the two parts of the general plain sesquilinear product are the scalar and the vector part of the one value $\tilde Q_1\tilde Q_2^{*}$, valued in the centre $\mathbb{C}_{\mathbb{B}}$ and in the vector subspace. The **general quaternionic sesquilinear** product has it not: the value $\tilde Q_1^{\natural}\tilde Q_2^{*}=(\overline{\tilde Q}_2\tilde Q_1)^{\natural}$ determines only the general plain bilinear product $\overline{\tilde Q}_2\tilde Q_1$, whose factorisation into $\overline{\tilde Q}_2$ and $\tilde Q_1$ is not unique, and two pairs with the same value have different swaps — the pairs $(\tilde Q_1,\tilde Q_2)=(-ie_3,-ie_0)$ and $(e_2,e_1)$ both have the value $-e_3$, while the swapped values $\tilde Q_2^{\natural}\tilde Q_1^{*}$ are $-e_3$ and $e_3$ — so no conjugation of $\tilde Q_1^{\natural}\tilde Q_2^{*}$ is $\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}=\tilde Q_2^{*}\tilde Q_1^{\natural}$. The two parts of the general quaternionic sesquilinear product are therefore the half-sum and the half-difference of the two values $\tilde Q_1^{\natural}\tilde Q_2^{*}$ and $\tilde Q_2^{*}\tilde Q_1^{\natural}$, and they are valued in no subspace of the remarkable subspaces. The shape is the same in both rows: each of the four parts is a half-sum or a half-difference of the two orders of one plain product read through the conjugations — $\overline{\tilde Q}_2\tilde Q_1^{\natural}$ in the plain row and $\overline{\tilde Q}_2\tilde Q_1$ in the quaternionic row — and the two rows differ only by the ${}^{\natural}$ on the second factor.

---

## The Table of the Twelve Products

| the product | the operation | scalar part | vector part | scalars | law | unit | image |
|---|---|---|---|---|---|---|---|
| the general plain bilinear product | $\tilde Q_1\tilde Q_2$ | $\bigl[Q_{1,0}Q_{2,0}-(\vec Q_1,\vec Q_2)\bigr]$ | $+Q_{1,0}\vec Q_2+Q_{2,0}\vec Q_1+\vec Q_1\times\vec Q_2$ | $\mathbb{C}$ | associative | $e_0$, both sides | all of $\mathbb{B}$ |
| the general plain sesquilinear product | $\tilde Q_1\tilde Q_2^{*}$ | $\bigl[Q_{1,0}\overline{Q_{2,0}}+(\vec Q_1,\overline{\vec Q_2})\bigr]$ | $-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2,0}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | $\mathbb{C},\bar{\cdot}$ | not associative | $e_0$, right only | all of $\mathbb{B}$ |
| the general quaternionic bilinear product | $\tilde Q_1^{\natural}\tilde Q_2$ | $\bigl[Q_{1,0}Q_{2,0}+(\vec Q_1,\vec Q_2)\bigr]$ | $+Q_{1,0}\vec Q_2-Q_{2,0}\vec Q_1-\vec Q_1\times\vec Q_2$ | $\mathbb{C}$ | not associative | $e_0$, left only | all of $\mathbb{B}$ |
| the general quaternionic sesquilinear product | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $\bigl[Q_{1,0}\overline{Q_{2,0}}-(\vec Q_1,\overline{\vec Q_2})\bigr]$ | $-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2,0}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$ | $\mathbb{C},\bar{\cdot}$ | not associative | none | all of $\mathbb{B}$ |
| the symmetric plain bilinear product | $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | $\bigl[Q_{1,0}Q_{2,0}-(\vec Q_1,\vec Q_2)\bigr]$ | $+Q_{1,0}\vec Q_2+Q_{2,0}\vec Q_1$ | $\mathbb{C}$ | commutative, **Jordan** | $e_0$, both sides | all of $\mathbb{B}$ |
| the symmetric plain sesquilinear product | $\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+\overline{\tilde Q}_2\tilde Q_1^{\natural}\bigr)$ | $\bigl[Q_{1,0}\overline{Q_{2,0}}+(\vec Q_1,\overline{\vec Q_2})\bigr]$ | $0$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| the symmetric quaternionic bilinear product | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$ | $\bigl[Q_{1,0}Q_{2,0}+(\vec Q_1,\vec Q_2)\bigr]$ | $0$ | $\mathbb{C}$ | commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| the symmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)$ | $\bigl[Q_{1,0}\overline{Q_{2,0}}-(\vec Q_1,\overline{\vec Q_2})\bigr]$ | $-Q_{1,0}\overline{\vec Q_2}-\overline{Q_{2,0}}\vec Q_1$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | no subspace of the remarkable subspaces |
| the antisymmetric plain bilinear product | $\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)$ | $\bigl[0\bigr]$ | $\vec Q_1\times\vec Q_2$ | $\mathbb{C}$ | alternating, **Jacobi** | none | $\mathrm{Vect}(\mathbb{B})$ |
| the antisymmetric plain sesquilinear product | $\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q}_2\tilde Q_1^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $-Q_{1,0}\overline{\vec Q_2}+\overline{Q_{2,0}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| the antisymmetric quaternionic bilinear product | $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$ | $\bigl[0\bigr]$ | $Q_{1,0}\vec Q_2-Q_{2,0}\vec Q_1-\vec Q_1\times\vec Q_2$ | $\mathbb{C}$ | alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| the antisymmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $\vec Q_1\times\overline{\vec Q_2}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |

The **first column** is the product; the **second** is the operation as a product of the two elements: the four general products
themselves, and for each part the half-sum or the half-difference of the product and its
class-preserving exchange, written with the second monomial in the collapsed form of the
exchange, $\overline{\tilde Q_2\tilde Q_1^{*}}=\overline{\tilde Q}_2\tilde Q_1^{\natural}$ for the
plain sesquilinear product and $\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}=\tilde Q_2^{*}\tilde Q_1^{\natural}$
for the general quaternionic one. The **third** column is the **scalar part** of the value and the
**fourth** is the **vector part**, each written out, $0$ where the part vanishes. Here
$\vec Q_2$ and $\overline{\vec Q_2}$ are the vector part of the second element and of its
coefficientwise conjugate, $(\cdot,\cdot)$ is the bilinear dot product and $\times$ the
bilinear cross product. The two central operations, the symmetric plain sesquilinear product and the symmetric quaternionic
bilinear product, have no vector part, and the four antisymmetric ones, the antisymmetric product
of each of the four families, have no scalar part; the scalar part plus the vector part of an operation
is its product.

Six of the twelve are $\mathbb{C}$-bilinear, the three operations of each of the two bilinear families, and the remaining six are the six sesquilinear operations of the two sesquilinear families. In the two bilinear families the symmetric part is commutative and the antisymmetric part is alternating, with zero diagonal; in the two sesquilinear families the same two symmetries hold **up to the coefficientwise conjugation**, the symmetric part being conjugate-commutative, $s(\tilde Q_1,\tilde Q_2)=\overline{s(\tilde Q_2,\tilde Q_1)}$, and the antisymmetric part conjugate-alternating, $\mathfrak{a}(\tilde Q_1,\tilde Q_2)=-\overline{\mathfrak{a}(\tilde Q_2,\tilde Q_1)}$. The algebraic norm of the two sesquilinear antisymmetric parts is the vector part of the square and does not vanish in general. These symmetries hold by the definitions alone, for every product.

**Remark (the two classifications of the table are independent).** The rows of the table above are the slot settings and the columns are the readings. The rows carry the slot calculus of *Comparison Between the Four General Products*, §*The Table of the Slots* — the second slot fixes whether the operation is a composition and the first fixes what the form reads — and the columns fix the algebraic norm alone, the square of an element. Neither classification refines the other: a row property such as associativity holds for $\mathrm{GPA}$ alone and cuts across the columns, and the norm of a column is not read from the row. The twelve names record both.

**Remark (the one unital non-associative structure).** $\mathrm{SPA}$ is commutative and has $e_0$ as a unit on both sides, and it is not associative: it is the symmetrisation $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$, and the symmetrisation of an associative product need not be associative. Among the twelve it is the only structure that is unital without being associative, and its algebraic norm is the plain one, $\tilde Q_1\bullet\tilde Q_1=\tilde Q_1^{2}$.

### The Reconstruction, Product by Product

Each product is the sum of its two parts, one identity to a product:

$$
f_{\mathrm{pb}}=s_{\mathrm{pb}}+a_{\mathrm{pb}},\qquad
f_{\mathrm{ps}}=s_{\mathrm{ps}}+a_{\mathrm{ps}},\qquad
f_{\mathrm{qb}}=s_{\mathrm{qb}}+a_{\mathrm{qb}},\qquad
f_{\mathrm{qs}}=s_{\mathrm{qs}}+a_{\mathrm{qs}},
$$
the subscripts $\mathrm{pb}$, $\mathrm{ps}$, $\mathrm{qb}$, $\mathrm{qs}$ naming the four families — plain bilinear, plain sesquilinear, quaternionic bilinear, general quaternionic sesquilinear — and $s$ and $a$ the symmetric and the antisymmetric part.

These four identities and the four definitions of the general products are the only relations among the twelve: no part of one family is a conjugate of a part of another family, since the four general products are related to one another by the slots while the twelve operations are not. The square of a product of a $\mathbb{C}$-bilinear family reads its symmetric part alone, $f(\tilde Q_2,\tilde Q_2)=s(\tilde Q_2,\tilde Q_2)$ for the plain and for the general quaternionic bilinear product, and its polarised square is twice the symmetric part. In the two sesquilinear families the square is split by the exchange instead: its algebraic norm is the pair $\bigl(s(\tilde Q_2,\tilde Q_2),\mathfrak{a}(\tilde Q_2,\tilde Q_2)\bigr)$, the antisymmetric side being the vector part of the square and not zero, and the polarised square recovers the plain symmetrisation of the bare interchange and not the symmetric part (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Equal Arguments and the Square*).

### The Twelve Are Distinct, and Ten on the Real Part

The twelve operations are pairwise distinct on the complex space. On the real part of the space — the real span of $e_0,e_1,e_2,e_3$, where the coefficientwise conjugation acts trivially — two pairs coincide: the antisymmetric plain bilinear product equals the antisymmetric quaternionic sesquilinear product, and the symmetric plain sesquilinear product equals the symmetric quaternionic bilinear product, both on the real elements. So the real part of the space carries **ten** operations and not twelve: the count twelve is the count for the complex space. The first coincidence is the equality of the two cross products on real vectors; the second is the equality of the two scalar forms of the pair, $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}$ on the real elements.

**Caution (a real-form computation sees ten, not twelve).** The fall from twelve to ten is a loss of
distinctions, and it is exact: two pairs that are different on the complex space become one on the real
part. It follows that a computation restricted to real elements cannot separate the members of either
coincident pair, and a property that holds for one member of a pair and fails for the other is invisible
there. A reader who checks an identity — an associativity, a Jacobi or a Jordan condition — on real
elements only therefore risks reporting an obstruction as absent, or a structure as present, when the
distinction between the two members of a coincident pair has simply been erased by the reality
condition. The twelve are the objects of the complex space; a real form carries ten of them, and every
statement of this article is a statement about the complex space unless it says otherwise. The fall
itself is proved here; its physical reading — that a classical, real description cannot separate the member
of a coincident pair that satisfies an identity from the member that fails it — belongs to the physics
article *The Biquaternioid Antisymmetric Quaternionic Sesqualgebra (AQS) over $\mathbb{C}$* and not to this
catalogue.

### The Counts of the Failures

The law column above names one witness per failure. The **count** on the eight-element basis
$\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}$ gives the shape of each failure, and it is worth tabulating because
the failures are far from equally dense. The identities are the ones the corpus declares and the counts are
taken in the same forms: the Jacobi identity in the cyclic form of the Conventions above, and the Jordan
identity in the form
$x^{2}\bullet(y\bullet x)=(x^{2}\bullet y)\bullet x$ of *The Symmetric and Antisymmetric Parts of an Algebra
Product*, with $x^{2}=x\bullet x$, read at $y=x$ as the corpus's own witnesses do. Neither identity is put to
the four general products, which are neither symmetrisations nor antisymmetrisations; each is put to the four
parts of its kind, and exactly one part of each kind holds it.

| identity | the part that holds it | the parts that fail it, with the count on the eight-element basis |
|---|---|---|
| Jacobi, over the four antisymmetric parts | $\mathrm{APA}$ | $\mathrm{APS}$, $252$ of the $512$ triples; $\mathrm{AQA}$, $144$; $\mathrm{AQS}$, $72$ |
| Jordan, over the four symmetric parts | $\mathrm{SPA}$ | $\mathrm{SPS}$ at $7$ of the $8$ elements; $\mathrm{SQA}$ at $6$; $\mathrm{SQS}$ at $4$ |

On the Jacobi side the failure of $\mathrm{AQS}$ is the sparsest and the only one whose witness needs a
complex element, and the failure of $\mathrm{APS}$ is the densest, failing on half the triples. On the Jordan
side the two sesquilinear parts are the denser and they fail at almost every element: $\mathrm{SPS}$ fails at
every basis element but $e_0$ and $\mathrm{SQS}$ at $e_1,e_2,e_3,ie_0$, while $\mathrm{SQA}$ fails at
$e_1,e_2,e_3,ie_1,ie_2,ie_3$. The witnesses of the three Jordan failures are of two shapes, the central shift
of $\mathrm{SQS}$ with sides $-e_0$ and $e_0$, and the outright vanishing of $\mathrm{SQA}$ and
$\mathrm{SPS}$ with sides $0$ and $e_0$; a shift needs a product with a non-central algebraic norm, and it is the
mark of the sesquilinear block. The identity, put to the two general sesquilinear products although it is not
asked of them, fails there as well, on $32$ of the $64$ pairs for each.

The counts above are the counts of the identity each part is asked for. If the Jordan identity is put instead to the four antisymmetric parts, of which the corpus does not ask it, the two bilinear ones satisfy it vacuously, their algebraic norm vanishing, and the two sesquilinear ones satisfy it on the whole real part and fail it as soon as a complex element enters: $\mathrm{APS}$ fails at $\tilde X=e_0+ie_1$, where $\tilde X^{2}=2ie_1$ and the two sides are $2ie_1$ and $0$, and $\mathrm{AQS}$ at $\tilde X=e_1+e_2+ie_3$, where $\tilde X^{2}=-2ie_1+2ie_2$ and the two sides are its negative and $0$. The failure of a sesquilinear antisymmetric part is therefore invisible on the real forms, exactly as the Jacobi failure of $\mathrm{AQS}$ is, and the real part separates these two operations on the Jordan identity no better than it separates them on the Jacobi identity.

**Two cautions.** The counts are counts on a chosen basis and are not invariants of the operation; they are
given as the shape of each failure and they change with the basis. And each identity is tested in the single
form the corpus declares, the Jordan identity in its two-variable form and not in a rearrangement that
coincides with it at $y=x$ alone, which would answer a weaker question; the forms are therefore written out.

---

## Summary

The complex space of the biquaternion algebra carries four general products, and each is split into a symmetric and an antisymmetric part by an exchange that keeps the class, so it carries the twelve products. The exchange is the plain interchange of the two arguments for the two $\mathbb{C}$-bilinear families and the conjugate transpose, the interchange followed by the coefficientwise conjugation of the value, for the two sesquilinear families. Each of the twelve is the multiplication of an algebraic structure of its own kind; the names, the codes and the structures are read in *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

The six operations of the two bilinear families are $\mathbb{C}$-bilinear and the six of the two sesquilinear families are sesquilinear over $(\mathbb{C},\bar{\cdot})$; in the two sesquilinear families the symmetric product is conjugate-commutative, the antisymmetric product is conjugate-alternating, and the algebraic norm of the antisymmetric product is the vector part of the square and does not vanish. The twelve are pairwise distinct on the complex space and fall to ten on the real part, where the antisymmetric plain bilinear product equals the antisymmetric quaternionic sesquilinear product and the symmetric plain sesquilinear product equals the symmetric quaternionic bilinear product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_0,e_1,e_2,e_3$, central imaginary $i$ |
| $\tilde Q_2=Q_{2,0}e_0+\vec Q_2$ | a biquaternion, its scalar and vector parts |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | the natural, the coefficientwise and the Hermitian conjugation |
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the four general products: general plain bilinear, general plain sesquilinear, general quaternionic bilinear, general quaternionic sesquilinear |
| $f(\tilde Q_2,\tilde Q_1)$ | the interchange of the two arguments, the exchange of a $\mathbb{C}$-bilinear product |
| $\overline{f(\tilde Q_2,\tilde Q_1)}$ | the conjugate transpose, the exchange of a sesquilinear product |
| $f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+f(\tilde Q_2,\tilde Q_1)\bigr)$ | the symmetric part of a $\mathbb{C}$-bilinear product |
| $f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)-f(\tilde Q_2,\tilde Q_1)\bigr)$ | the antisymmetric part of a $\mathbb{C}$-bilinear product |
| $f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+\overline{f(\tilde Q_2,\tilde Q_1)}\bigr)$ | the symmetric part of a sesquilinear product |
| $f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)-\overline{f(\tilde Q_2,\tilde Q_1)}\bigr)$ | the antisymmetric part of a sesquilinear product |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1,0}Q_{2,0}+(\vec Q_1,\vec Q_2)$ | the quaternion form, the scalar part of the symmetric quaternionic bilinear product |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces |
| Jacobi, Jordan | the two identities that single out the antisymmetric plain bilinear product and the symmetric plain bilinear product |
| $\overline{\vec Q_2}$ | the coefficientwise conjugate of the vector part |
| $(\vec Q_1,\vec Q_2)$, $\vec Q_1\times\vec Q_2$ | the complex bilinear dot product and cross product |

## Further Reading

- *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, *Relations Between the Four General Products* and *Comparison Between the Four General Products*, for the four general products, their developed forms and the identities that link them.
- *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the two definitions of the split, the obstruction of the class and the two admissibility conditions.
- *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, for the adapted exchange that keeps the class.
- *Introduction to the Biquaternion Algebra*, *Introduction to the General Plain Sesqualgebra*, *Introduction to the General Quaternionic Algebra* and *Introduction to the General Quaternionic Sesqualgebra*, for the four general products.
- *Remarkable Subspaces and the Four General Products*, for what the twelve do on the remarkable subspaces, and *The Sesquilinear Commutator*, for the sesquilinear bracket.
- *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, for the names, the codes, the structure each product defines and the two that are Lie and Jordan products, and *The Unitary Lie Algebra* and *The Hermitian Jordan Algebra*, for the two structures that pass.
