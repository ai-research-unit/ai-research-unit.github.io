# __The 12 Products of the Biquaternion Complex Space__

## Introduction

The biquaternion complex space carries four multiplications, the **four general products** of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*. Every one of the four is split into a **symmetric part** and an **antisymmetric part**, and the two parts are operations of the same class as the product they split, so the space carries the **twelve products**. This article writes each of the twelve out and reads the laws that separate them; the twelve names they carry, the abbreviations and the structure each of them defines are the matter of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The general construction, with the obstruction of the class and the two projections, is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the method of the decomposition is §*The Method of the Decomposition*, below.

The article assumes the four general products from *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, the elements, the basis and the four conjugations from *Biquaternions as a Vector Space over $\mathbb{C}$*, and the split itself, in its two forms, from *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**Conventions.** The complex space is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$. An element is $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_k e_k$ and $Q_\mu\in\mathbb{C}$. The natural conjugation ${}^{\natural}$ negates the vector part, the coefficientwise one $\bar{\cdot}$ conjugates the coefficients, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The four general products are the **general plain bilinear** $\tilde{P}\tilde{Q}$, the **general quaternionic bilinear** $\tilde{P}^{\natural}\tilde{Q}$, the **general plain sesquilinear** $\tilde{P}\tilde{Q}^{*}$ and the **general quaternionic sesquilinear** $\tilde{P}^{\natural}\tilde{Q}^{*}$ (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*), and the split of each of them into its two parts is §*The Method of the Decomposition*, below. The dot product $(\mathbf{P},\mathbf{Q})$ and the cross product $\mathbf{P}\times\mathbf{Q}$ are the general plain bilinear ones, and $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ are the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces (*Introduction to the Remarkable Subspaces*). A vector expression such as $i\,\mathrm{Im}(\mathbf{v})$ is read componentwise. The **cyclic sum** of a bracket $b$ is the outer form $b(b(x,y),z)+b(b(y,z),x)+b(b(z,x),y)$ of *The Symmetric and Antisymmetric Parts of an Algebra Product*, §*Lie-Admissible Algebras*, so that a bracket written without the factor $\tfrac12$ has its cyclic sum multiplied by four.

Throughout, the element $\tilde P = P_0 + \mathbf P$ separates the complex scalar part $P_0$ from the complex vector part $\mathbf P = P_1e_1+P_2e_2+P_3e_3$; $\overline{\mathbf P}$ is the coefficientwise conjugate of the vector part, $(\mathbf P,\mathbf Q)$ the complex bilinear dot product and $\mathbf P\times\mathbf Q$ the complex bilinear cross product, as in *Biquaternions as a Vector Space over $\mathbb{C}$*.

---

## The Four General Products

The four general products are the four multiplications of the space. Written on the coordinates, they are

$$
\tilde P\tilde Q = \bigl[P_0Q_0-(\mathbf P,\mathbf Q)\bigr]+P_0\mathbf Q+Q_0\mathbf P+\mathbf P\times\mathbf Q,
$$

$$
\tilde P^{\natural}\tilde Q = \bigl[P_0Q_0+(\mathbf P,\mathbf Q)\bigr]+P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q,
$$

$$
\tilde P\tilde Q^{*} = \bigl[P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})\bigr]-P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q},
$$

$$
\tilde P^{\natural}\tilde Q^{*} = \bigl[P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})\bigr]-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P+\mathbf P\times\overline{\mathbf Q}.
$$

The first two are $\mathbb C$-bilinear in both slots; they differ only in the reading of the first factor through the natural conjugation ${}^{\natural}$. The last two are $\mathbb C$-linear in the first slot and conjugate-linear in the second, and differ in the same way. No two of the four agree on every pair. The four are developed, with the identities that link them and their property table, in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *Relations Between the Four General Products* and *Comparison Between the Four General Products*.

---

## The Method of the Decomposition

Every one of the four general products is split into a **symmetric part** and an **antisymmetric part**, and the split is a different operation in the two families of products. There are two definitions, one to a family.

**The bilinear case.** The general plain bilinear product $\tilde{P}\tilde{Q}$ and the general quaternionic bilinear product $\tilde{P}^{\natural}\tilde{Q}$ have two $\mathbb{C}$-linear slots. Their exchange is the interchange of the two arguments, and the two parts are

$$
f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr),\qquad f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P})\bigr).
$$

**The sesquilinear case.** The general plain sesquilinear product $\tilde{P}\tilde{Q}^{*}$ and the general quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$ have one linear slot and one conjugate-linear slot, and the interchange alone returns a product of the opposite type, $\tilde{Q}\tilde{P}^{*}$, which is not a product of the class at all. The exchange is the interchange followed by the coefficientwise conjugation of the value, and the two parts are

$$
f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+\overline{f(\tilde{Q},\tilde{P})}\bigr),\qquad f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-\overline{f(\tilde{Q},\tilde{P})}\bigr).
$$

**The two definitions are not one.** The interchange keeps the class of a product exactly when its two slots have the same type, which is the bilinear case; in the sesquilinear case it does not, and it is the conjugation of the value that repairs the class. The two definitions agree only for the two $\mathbb{C}$-bilinear products, and the split of a bilinear product and the split of a sesquilinear product share their shape and not their definition. Both exchanges are involutions of the class — the interchange of the interchange, and the conjugate transpose of the conjugate transpose, return the product they start from — so the two parts are well defined in both cases. The adapted exchange, with the obstruction of the class and the two projections of the space of products, is developed in *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**What the two cases share.** The two parts carry the reconstruction $f=f^{\mathrm{s}}+f^{\mathrm{a}}$; the symmetric part is fixed by the exchange and the antisymmetric part is negated by it; and the pair is unique, since $f=s+t$ with $s$ fixed and $t$ negated forces $s=f^{\mathrm{s}}$ and $t=f^{\mathrm{a}}$. Both parts are products of the class of $f$ — $\mathbb{C}$-bilinear in the bilinear case, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ in the sesquilinear case — and it is for that closure that the exchange of the sesquilinear case is adapted and not bare.

**The square and its diagonal, where the two part company.** In the **bilinear case** the antisymmetric part vanishes on the diagonal, since $f^{\mathrm{a}}(\tilde{Q},\tilde{Q})=-f^{\mathrm{a}}(\tilde{Q},\tilde{Q})$, so the square is the symmetric part alone, $f(\tilde{Q},\tilde{Q})=f^{\mathrm{s}}(\tilde{Q},\tilde{Q})$, and the polarisation of the square recovers the symmetric part off the diagonal. In the **sesquilinear case** the antisymmetric part on the diagonal is the antisymmetrised square,

$$
f^{\mathrm{a}}(\tilde{Q},\tilde{Q})=\tfrac12\bigl(f(\tilde{Q},\tilde{Q})-\overline{f(\tilde{Q},\tilde{Q})}\bigr),
$$

which **need not vanish**: it vanishes exactly when the square of the element is fixed by the coefficientwise conjugation. The polarisation of the square then recovers the **plain** symmetrisation — the half-sum with the bare interchange — and not the symmetric part. The bilinear case has no antisymmetric diagonal, the sesquilinear case has one and it is not zero in general.

**The bare interchange is not the exchange.** The two halves of the bare interchange of a sesquilinear product are only $\mathbb{R}$-bilinear and are not products of the class: they are the symmetrised sesquilinear product $x\circ y$ of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator*. They are not the two parts read below, in the sesquilinear case or in any case. The reading of the four splits from the side of the order symmetry is §*The Twelve Products, One by One*, below, where the exchange that keeps the class is contrasted with the bare interchange.

---

## The Twelve Products, One by One

Each product is read with its two parts, the general product first and its symmetric and its antisymmetric part after it, so that the two parts stand directly under the product they split. The two $\mathbb{C}$-bilinear families come first, then the two sesquilinear ones; the laws are collected in the table, below, and the classical identities in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

Throughout the reading, $f$ is the product being read and $s$ and $a$ are its symmetric and its antisymmetric part, defined as in §*The Method of the Decomposition*: the plain interchange of the two arguments in the two $\mathbb{C}$-bilinear families and the conjugate transpose in the two sesquilinear ones.

### The General Plain Bilinear Product

$$
\tilde{P}\tilde{Q}=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}.
$$

The general plain bilinear product, the multiplication of the two elements as they stand: scalar part $P_0Q_0-(\mathbf{P},\mathbf{Q})$ and vector part $P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$. It is $\mathbb{C}$-bilinear, **associative**, and $e_0$ is a unit on both sides. It is the only associative product of the twelve.

Its values fill the whole space $\mathbb{B}$.

### The Symmetric Plain Bilinear Product

The symmetric part of the general plain bilinear product above.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr)=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}.
$$

The Jordan product $\tilde{P}\bullet\tilde{Q}$, the general plain bilinear product with the cross term dropped. It is commutative, $e_0$ is a unit on both sides, and it satisfies the **Jordan identity**; it is the only one of the four symmetric parts that does, and it is the only part of the eight that has a unit at all. The identity is not put to the four general products, which are neither symmetrisations nor antisymmetrisations; the counts over the parts are in §*The Counts of the Failures*.

### The Antisymmetric Plain Bilinear Product

The antisymmetric part of the general plain bilinear product above.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr)=\mathbf{P}\times\mathbf{Q}.
$$

The outer product $\tilde{P}\wedge\tilde{Q}$, the cross product of the two vector parts alone: scalar part zero, vector part $\mathbf{P}\times\mathbf{Q}$. It is alternating, its values lie in the vector subspace $\mathrm{Vect}(\mathbb{B})$, and it satisfies the **Jacobi identity**; it is the only one of the twelve that does. It is half the commutator of the general plain bilinear product, $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$.

### The General Quaternionic Bilinear Product

$$
\tilde{P}^{\natural}\tilde{Q}=\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}.
$$

The general quaternionic bilinear product, the general plain bilinear product with the first factor read through ${}^{\natural}$. It is $\mathbb{C}$-bilinear, **not associative**, and $e_0$ is a unit on the **left** only. Its exchange is the natural conjugation of its value, $\tilde{Q}^{\natural}\tilde{P}=(\tilde{P}^{\natural}\tilde{Q})^{\natural}$.

Its values fill the whole space $\mathbb{B}$.

### The Symmetric Quaternionic Bilinear Product

The symmetric part of the general quaternionic bilinear product above.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P}\bigr)=\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr].
$$

The quaternion form $B(\tilde{P},\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$ of *Comparison Between the Four General Products* read as a product; its scalar part is $B$ and its vector part is zero. It is commutative, its values lie in the centre $\mathbb{C}_{\mathbb{B}}$ — it compares two elements and returns a multiple of $e_0$ — and it has no unit. It is **not** a Jordan product.

### The Antisymmetric Quaternionic Bilinear Product

The antisymmetric part of the general quaternionic bilinear product above.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}\bigr)=P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}.
$$

The quaternionic product with its scalar part removed: scalar part zero, vector part the mixed term with the cross term subtracted. It is alternating, its values lie in the vector subspace, and it **fails** the Jacobi identity, with witness $(e_0,e_1,e_2)$ where the cyclic sum is $-e_3\neq0$. It is half the commutator $[\tilde{P},\tilde{Q}]_{\natural}=\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}$.

### The General Plain Sesquilinear Product

$$
\tilde{P}\tilde{Q}^{*}=\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The general plain sesquilinear product, the second factor read through the Hermitian conjugation ${}^{*}$. Both products of the pair are the natural conjugates of the two orders of one underlying product,
$$
\tilde{P}\tilde{Q}^{*}=\bigl(\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)^{\natural},\qquad
\tilde{Q}\tilde{P}^{*}=\bigl(\overline{\tilde{P}}\tilde{Q}^{\natural}\bigr)^{\natural}.
$$
It is sesquilinear over $(\mathbb{C},\bar{\cdot})$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second; it is **not associative**, and $e_0$ is a unit on the **right** only.

Its values fill the whole space $\mathbb{B}$.

### The Symmetric Plain Sesquilinear Product

The symmetric part of the general plain sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+(\tilde{P}\tilde{Q}^{*})^{\natural}\bigr)
=\mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{*}\bigr)
=\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr].
$$

The value $\tilde{P}\tilde{Q}^{*}$ has scalar part $H=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ and vector part $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$; the conjugate transpose sends the value to its conjugate with the vector part negated, $\overline{\tilde{Q}\tilde{P}^{*}}=(\tilde{P}\tilde{Q}^{*})^{\natural}$, so the half-sum keeps the scalar part and cancels the vector part. The operation is the **Hermitian form** $H(\tilde{P},\tilde{Q})=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ of *Biquaternion Norm and Invertibility* read as a product, and it is **central**: its values lie in the centre $\mathbb{C}_{\mathbb{B}}$. It is **conjugate-commutative**, $s(\tilde{P},\tilde{Q})=\overline{s(\tilde{Q},\tilde{P})}$, rather than commutative, and it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, conjugate-linear in the second argument. Its diagonal is the square read through the form, $s(\tilde{Q},\tilde{Q})=H(\tilde{Q},\tilde{Q})=|Q_0|^{2}+(\mathbf{Q},\overline{\mathbf{Q}})$, which is real and strictly positive off the origin. Being central-valued it has no unit, and it **fails** the Jordan identity on the whole space, with witness $x=y=e_1$, where the two sides are $0$ and $e_0$.

### The Antisymmetric Plain Sesquilinear Product

The antisymmetric part of the general plain sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-(\tilde{P}\tilde{Q}^{*})^{\natural}\bigr)
=\mathrm{Vect}\bigl(\tilde{P}\tilde{Q}^{*}\bigr)
=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The same value as the symmetric part, with the difference in place of the sum: the half-difference cancels the scalar part and keeps the vector part. It is **pure vector**, so its image is the vector subspace $\mathrm{Vect}(\mathbb{B})$. It is **conjugate-alternating**, $a(\tilde{P},\tilde{Q})=-\overline{a(\tilde{Q},\tilde{P})}$, and its diagonal is the **vector part of the square**,
$$
a(\tilde{Q},\tilde{Q})=\mathrm{Vect}(\tilde{Q}\tilde{Q}^{*}),
$$
which is **not zero** in general: for $\tilde{Q}=e_1+ie_2$ it is $2ie_3$. It has no unit, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jacobi identity, with witness $(e_0,e_1,e_2)$ where the cyclic sum is $e_3$.

### The General Quaternionic Sesquilinear Product

$$
\tilde{P}^{\natural}\tilde{Q}^{*}=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The general quaternionic sesquilinear product, both slots read through a conjugation. Both products of the pair are the natural conjugates of the two orders of one underlying product,
$$
\tilde{P}^{\natural}\tilde{Q}^{*}=\bigl(\overline{\tilde{Q}}\tilde{P}\bigr)^{\natural},\qquad
\tilde{Q}^{\natural}\tilde{P}^{*}=\bigl(\overline{\tilde{P}}\tilde{Q}\bigr)^{\natural}.
$$
It is sesquilinear over $(\mathbb{C},\bar{\cdot})$, **not associative**, and it has a unit on **neither** side. It is the product whose ternary product fails the Jordan triple identity (*Why the Fourth Product Is a Gauge Structure and Not a State Space*).

Its values fill the whole space $\mathbb{B}$.

### The Symmetric Quaternionic Sesquilinear Product

The symmetric part of the general quaternionic sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)
=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P},
$$

since $\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}=\tilde{Q}^{*}\tilde{P}^{\natural}$. The value $\tilde{P}^{\natural}\tilde{Q}^{*}$ has scalar part $K=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ and vector part $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$; the conjugate transpose is not the conjugation of the value here — the two cross products cancel between the two orders instead of adding — so the half-sum keeps the scalar part and the mixed term and cancels the cross product. Its scalar part is the general quaternionic sesquilinear form $K$ of *The Krein Gram Matrix and the Restrictions of the Form* and its vector part is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$, so its values lie in **no** subspace of the remarkable subspaces. It is **conjugate-commutative**, $s(\tilde{P},\tilde{Q})=\overline{s(\tilde{Q},\tilde{P})}$, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jordan identity, with witness $x=y=e_1$ where the two sides are $-e_0$ and $e_0$. Its diagonal is not central in general: at $\tilde{Q}=e_0+e_1$ it is $-2e_1$, while the real vector directions, among them $e_1$, carry central diagonals.

### The Antisymmetric Quaternionic Sesquilinear Product

The antisymmetric part of the general quaternionic sesquilinear product above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The cross products of the two orders add in the difference while the scalar part and the mixed term cancel, so the half-difference is the **cross product** $\mathbf{P}\times\overline{\mathbf{Q}}$ of the vector part of the first argument with the conjugate of the vector part of the second. It is **pure vector**, so its image is the vector subspace $\mathrm{Vect}(\mathbb{B})$; it is **conjugate-alternating**, $a(\tilde{P},\tilde{Q})=-\overline{a(\tilde{Q},\tilde{P})}$, and its diagonal is the cross product of the vector part with its conjugate, $a(\tilde{Q},\tilde{Q})=\mathbf{Q}\times\overline{\mathbf{Q}}$, which is **not zero** in general: for $\tilde{Q}=e_1+ie_2$ it is $-2ie_3$. It has no unit, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jacobi identity, with witness $(e_1,e_1,ie_2)$, where the cyclic sum is $-2ie_2$. This is the only one of the three failing brackets whose witness needs a complex element off the real basis, which is why the failure is invisible on the real forms.

### The Exchange Behind the Split

The twelve products are read against the exchange of §*The Method of the Decomposition*: the interchange for the two $\mathbb{C}$-bilinear products, whose two slots have the same type, and the conjugate transpose for the two sesquilinear products, whose slots are one linear and one conjugate-linear. It is an involution of the class in both cases, and it is the exchange that makes the count $4\times3$ while keeping every part in the class of its parent: the six $\mathbb{C}$-bilinear parts and the six sesquilinear parts.

The bare interchange does not keep the class, and its two halves — the symmetrised sesquilinear product $x\circ y$ of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator* — are **not** the two parts of the general plain sesquilinear product read here; the two readings are set side by side in §*The Adapted Exchange* of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**Whether the exchange is read on the value.** The split needs only the involution, which §*The Method of the Decomposition*, above settles for the four general products; whether the exchange can be read on the value of the product is a second question, and the two sesquilinear families answer it differently. The **sesquilinear** product has it, since $\overline{\tilde{Q}\tilde{P}^{*}}=(\tilde{P}\tilde{Q}^{*})^{\natural}$, which is why the two parts of the general plain sesquilinear product are the scalar and the vector part of the one value $\tilde{P}\tilde{Q}^{*}$, valued in the centre $\mathbb{C}_{\mathbb{B}}$ and in the vector subspace. The **general quaternionic sesquilinear** product has it not: the value $\tilde{P}^{\natural}\tilde{Q}^{*}=(\overline{\tilde{Q}}\tilde{P})^{\natural}$ determines only the general plain bilinear product $\overline{\tilde{Q}}\tilde{P}$, whose factorisation into $\overline{\tilde{Q}}$ and $\tilde{P}$ is not unique, and two pairs with the same value have different swaps — the pairs $(\tilde{P},\tilde{Q})=(-ie_3,-ie_0)$ and $(e_2,e_1)$ both have the value $-e_3$, while the swapped values $\tilde{Q}^{\natural}\tilde{P}^{*}$ are $-e_3$ and $e_3$ — so no conjugation of $\tilde{P}^{\natural}\tilde{Q}^{*}$ is $\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}=\tilde{Q}^{*}\tilde{P}^{\natural}$. The two parts of the general quaternionic sesquilinear product are therefore the half-sum and the half-difference of the two values $\tilde{P}^{\natural}\tilde{Q}^{*}$ and $\tilde{Q}^{*}\tilde{P}^{\natural}$, and they are valued in no subspace of the remarkable subspaces. The shape is the same in both rows: each of the four parts is a half-sum or a half-difference of the two orders of one plain product read through the conjugations — $\overline{\tilde{Q}}\tilde{P}^{\natural}$ in the plain row and $\overline{\tilde{Q}}\tilde{P}$ in the quaternionic row — and the two rows differ only by the ${}^{\natural}$ on the second factor.

---

## The Table of the Twelve Products

| the product | the operation | scalar part | vector part | scalars | law | unit | image |
|---|---|---|---|---|---|---|---|
| the general plain bilinear product | $\tilde{P}\tilde{Q}$ | $\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | associative | $e_0$, both sides | all of $\mathbb{B}$ |
| the symmetric plain bilinear product | $\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | $\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}+Q_0\mathbf{P}$ | $\mathbb{C}$ | commutative, **Jordan** | $e_0$, both sides | all of $\mathbb{B}$ |
| the antisymmetric plain bilinear product | $\tfrac12(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | $\bigl[0\bigr]$ | $\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | alternating, **Jacobi** | none | $\mathrm{Vect}(\mathbb{B})$ |
| the general quaternionic bilinear product | $\tilde{P}^{\natural}\tilde{Q}$ | $\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | not associative | $e_0$, left only | all of $\mathbb{B}$ |
| the symmetric quaternionic bilinear product | $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})$ | $\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]$ | $0$ | $\mathbb{C}$ | commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| the antisymmetric quaternionic bilinear product | $\tfrac12(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P})$ | $\bigl[0\bigr]$ | $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| the general plain sesquilinear product | $\tilde{P}\tilde{Q}^{*}$ | $\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | not associative | $e_0$, right only | all of $\mathbb{B}$ |
| the symmetric plain sesquilinear product | $\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)$ | $\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $0$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| the antisymmetric plain sesquilinear product | $\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| the general quaternionic sesquilinear product | $\tilde{P}^{\natural}\tilde{Q}^{*}$ | $\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | not associative | none | all of $\mathbb{B}$ |
| the symmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)$ | $\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | no subspace of the remarkable subspaces |
| the antisymmetric quaternionic sesquilinear product | $\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |

The **first column** is the product; the **second** is the operation as a product of the two elements: the four general products
themselves, and for each part the half-sum or the half-difference of the product and its
class-preserving exchange, written with the second monomial in the collapsed form of the
exchange, $\overline{\tilde{Q}\tilde{P}^{*}}=\overline{\tilde{Q}}\tilde{P}^{\natural}$ for the
plain sesquilinear product and $\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}=\tilde{Q}^{*}\tilde{P}^{\natural}$
for the general quaternionic one. The **third** column is the **scalar part** of the value and the
**fourth** is the **vector part**, each written out, $0$ where the part vanishes. Here
$\mathbf{Q}$ and $\overline{\mathbf{Q}}$ are the vector part of the second element and of its
coefficientwise conjugate, $(\cdot,\cdot)$ is the bilinear dot product and $\times$ the
bilinear cross product. The two central operations, the symmetric quaternionic bilinear product and the symmetric plain
sesquilinear product, have no vector part, and the four antisymmetric ones, the antisymmetric product
of each of the four families, have no scalar part; the scalar part plus the vector part of an operation
is its product.

Six of the twelve are $\mathbb{C}$-bilinear, the three operations of each of the two bilinear families, and the remaining six are the six sesquilinear operations of the two sesquilinear families. In the two bilinear families the symmetric part is commutative and the antisymmetric part is alternating, with zero diagonal; in the two sesquilinear families the same two symmetries hold **up to the coefficientwise conjugation**, the symmetric part being conjugate-commutative, $s(\tilde{P},\tilde{Q})=\overline{s(\tilde{Q},\tilde{P})}$, and the antisymmetric part conjugate-alternating, $a(\tilde{P},\tilde{Q})=-\overline{a(\tilde{Q},\tilde{P})}$. The diagonal of the two sesquilinear antisymmetric parts is the vector part of the square and does not vanish in general. These symmetries hold by the definitions alone, for every product.

### The Reconstruction, Product by Product

Each product is the sum of its two parts, one identity to a product:

$$
f_{\mathrm{pb}}=s_{\mathrm{pb}}+a_{\mathrm{pb}},\qquad
f_{\mathrm{qb}}=s_{\mathrm{qb}}+a_{\mathrm{qb}},\qquad
f_{\mathrm{ps}}=s_{\mathrm{ps}}+a_{\mathrm{ps}},\qquad
f_{\mathrm{qs}}=s_{\mathrm{qs}}+a_{\mathrm{qs}},
$$
the subscripts $\mathrm{pb}$, $\mathrm{qb}$, $\mathrm{ps}$, $\mathrm{qs}$ naming the four families — plain bilinear, quaternionic bilinear, plain sesquilinear, general quaternionic sesquilinear — and $s$ and $a$ the symmetric and the antisymmetric part.

These four identities and the four definitions of the general products are the only relations among the twelve: no part of one family is a conjugate of a part of another family, since the four general products are related to one another by the slots while the twelve operations are not. The square of a product of a $\mathbb{C}$-bilinear family reads its symmetric part alone, $f(\tilde{Q},\tilde{Q})=s(\tilde{Q},\tilde{Q})$ for the plain and for the general quaternionic bilinear product, and its polarised square is twice the symmetric part. In the two sesquilinear families the square is split by the exchange instead: its diagonal is the pair $\bigl(s(\tilde{Q},\tilde{Q}),a(\tilde{Q},\tilde{Q})\bigr)$, the antisymmetric side being the vector part of the square and not zero, and the polarised square recovers the plain symmetrisation of the bare interchange and not the symmetric part (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Diagonal and the Square*).

### The Twelve Are Distinct, and Ten on the Real Part

The twelve operations are pairwise distinct on the complex space. On the real part of the space — the real span of $e_0,e_1,e_2,e_3$, where the coefficientwise conjugation acts trivially — two pairs coincide: the antisymmetric plain bilinear product equals the antisymmetric quaternionic sesquilinear product, and the symmetric quaternionic bilinear product equals the symmetric plain sesquilinear product, both on the real elements. So the real part of the space carries **ten** operations and not twelve: the count twelve is the count for the complex space. The first coincidence is the equality of the two cross products on real vectors; the second is the equality of the two scalar forms of the pair, $N=H$ on the real elements.

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
article *A Bracket Invisible on the Real Forms: the Complex Witness of the Jacobi Failure* and not to this
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
| Jacobi, over the four antisymmetric parts | $\mathrm{APA}$ | $\mathrm{AQA}$, $144$ of the $512$ triples; $\mathrm{APS}$, $252$; $\mathrm{AQS}$, $72$ |
| Jordan, over the four symmetric parts | $\mathrm{SPA}$ | $\mathrm{SQA}$ at $6$ of the $8$ elements; $\mathrm{SPS}$ at $7$; $\mathrm{SQS}$ at $4$ |

On the Jacobi side the failure of $\mathrm{AQS}$ is the sparsest and the only one whose witness needs a
complex element, and the failure of $\mathrm{APS}$ is the densest, failing on half the triples. On the Jordan
side the two sesquilinear parts are the denser and they fail at almost every element: $\mathrm{SPS}$ fails at
every basis element but $e_0$ and $\mathrm{SQS}$ at $e_1,e_2,e_3,ie_0$, while $\mathrm{SQA}$ fails at
$e_1,e_2,e_3,ie_1,ie_2,ie_3$. The witnesses of the three Jordan failures are of two shapes, the central shift
of $\mathrm{SQS}$ with sides $-e_0$ and $e_0$, and the outright vanishing of $\mathrm{SQA}$ and
$\mathrm{SPS}$ with sides $0$ and $e_0$; a shift needs a product with a non-central diagonal, and it is the
mark of the sesquilinear block. The identity, put to the two general sesquilinear products although it is not
asked of them, fails there as well, on $32$ of the $64$ pairs for each.

The counts above are the counts of the identity each part is asked for. If the Jordan identity is put instead to the four antisymmetric parts, of which the corpus does not ask it, the two bilinear ones satisfy it vacuously, their diagonal vanishing, and the two sesquilinear ones satisfy it on the whole real part and fail it as soon as a complex element enters: $\mathrm{APS}$ fails at $\tilde X=e_0+ie_1$, where $\tilde X^{2}=2ie_1$ and the two sides are $2ie_1$ and $0$, and $\mathrm{AQS}$ at $\tilde X=e_1+e_2+ie_3$, where $\tilde X^{2}=-2ie_1+2ie_2$ and the two sides are its negative and $0$. The failure of a sesquilinear antisymmetric part is therefore invisible on the real forms, exactly as the Jacobi failure of $\mathrm{AQS}$ is, and the real part separates these two operations on the Jordan identity no better than it separates them on the Jacobi identity.

**Two cautions.** The counts are counts on a chosen basis and are not invariants of the operation; they are
given as the shape of each failure and they change with the basis. And each identity is tested in the single
form the corpus declares, the Jordan identity in its two-variable form and not in a rearrangement that
coincides with it at $y=x$ alone, which would answer a weaker question; the forms are therefore written out.
Recomputed on the basis, and on random complex pairs and triples.

---

## Summary

The complex space of the biquaternion algebra carries four general products, and each is split into a symmetric and an antisymmetric part by an exchange that keeps the class, so it carries the twelve products. The exchange is the plain interchange of the two arguments for the two $\mathbb{C}$-bilinear families and the conjugate transpose, the interchange followed by the coefficientwise conjugation of the value, for the two sesquilinear families. Each of the twelve is the multiplication of an algebraic structure of its own kind; the names, the codes and the structures are read in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The six operations of the two bilinear families are $\mathbb{C}$-bilinear and the six of the two sesquilinear families are sesquilinear over $(\mathbb{C},\bar{\cdot})$; in the two sesquilinear families the symmetric product is conjugate-commutative, the antisymmetric product is conjugate-alternating, and the diagonal of the antisymmetric product is the vector part of the square and does not vanish. The twelve are pairwise distinct on the complex space and fall to ten on the real part, where the antisymmetric plain bilinear product equals the antisymmetric quaternionic sesquilinear product and the symmetric quaternionic bilinear product equals the symmetric plain sesquilinear product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_0,e_1,e_2,e_3$, central imaginary $i$ |
| $\tilde{Q}=Q_0e_0+\mathbf{Q}$ | a biquaternion, its scalar and vector parts |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | the natural, the coefficientwise and the Hermitian conjugation |
| $\tilde{P}\tilde{Q}$, $\tilde{P}^{\natural}\tilde{Q}$, $\tilde{P}\tilde{Q}^{*}$, $\tilde{P}^{\natural}\tilde{Q}^{*}$ | the four general products: general plain bilinear, general quaternionic bilinear, general plain sesquilinear, general quaternionic sesquilinear |
| $f(\tilde{Q},\tilde{P})$ | the interchange of the two arguments, the exchange of a $\mathbb{C}$-bilinear product |
| $\overline{f(\tilde{Q},\tilde{P})}$ | the conjugate transpose, the exchange of a sesquilinear product |
| $f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr)$ | the symmetric part of a $\mathbb{C}$-bilinear product |
| $f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P})\bigr)$ | the antisymmetric part of a $\mathbb{C}$-bilinear product |
| $f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+\overline{f(\tilde{Q},\tilde{P})}\bigr)$ | the symmetric part of a sesquilinear product |
| $f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-\overline{f(\tilde{Q},\tilde{P})}\bigr)$ | the antisymmetric part of a sesquilinear product |
| $B(\tilde{P},\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$ | the quaternion form, the scalar part of the symmetric quaternionic bilinear product |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces |
| Jacobi, Jordan | the two identities that single out the antisymmetric plain bilinear product and the symmetric plain bilinear product |
| $\overline{\mathbf{Q}}$ | the coefficientwise conjugate of the vector part |
| $(\mathbf{P},\mathbf{Q})$, $\mathbf{P}\times\mathbf{Q}$ | the complex bilinear dot product and cross product |

## Further Reading

- *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *Relations Between the Four General Products* and *Comparison Between the Four General Products*, for the four general products, their developed forms and the identities that link them.
- *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the two definitions of the split, the obstruction of the class and the two admissibility conditions.
- *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, for the adapted exchange that keeps the class.
- *Introduction to the General Plain Algebra of Biquaternions*, *Introduction to the General Quaternionic Algebra of Biquaternions*, *Introduction to the General Plain Sesqualgebra of Biquaternions* and *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, for the four general products.
- *Remarkable Subspaces and the Four General Products*, for what the twelve do on the remarkable subspaces, and *The Sesquilinear Commutator*, for the sesquilinear bracket.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the names, the codes, the structure each product defines and the two that are Lie and Jordan products, and *The Unitary Lie Algebra* and *The Hermitian Jordan Algebra*, for the two structures that pass.
