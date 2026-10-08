# __The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space__

## Introduction

The complex space of the biquaternion algebra carries four products, and each of them is split into a symmetric and an antisymmetric part by an exchange that keeps the class of the product, so the space carries twelve operations. For the two $\mathbb{C}$-bilinear products, whose two slots have the same type, the exchange is the plain interchange of the two arguments; for the two sesquilinear products, whose slots are one linear and one conjugate-linear, it is the interchange followed by the coefficientwise conjugation of the value. Each of the two parts is a product of the class of the product it comes from. The twelve have no name apiece in the corpus, and a sentence about one of them has to describe it instead of naming it. This article gives the twelve a name apiece, writes the product of each out, and reads the laws that separate them.

The name has three letters and is read as a code.

- The **first** letter says which of the three operations of a row is meant: $\mathrm G$ the **general** product, the multiplication itself, $\mathrm S$ its **symmetric** part, $\mathrm A$ its **antisymmetric** part.
- The **second** letter says which of the two products of the family is meant: $\mathrm P$ the **plain** one and $\mathrm Q$ the **quaternionic** one, in the sense of the first slot, read as it stands for $\mathrm P$ and through the natural conjugation ${}^{\natural}$ for $\mathrm Q$.
- The **third** letter says the **family**: $\mathrm A$ the algebra over $\mathbb{C}$, whose second slot is read as it stands, and $\mathrm S$ the sesqualgebra over $\mathbb{C}$, whose second slot carries the Hermitian conjugation ${}^{*}$.

The twelve names are these:

| the product | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

Each row is one product with its two parts, and that is the order in which the twelve are read below.

The four codes that begin with $\mathrm G$ name the four structures the corpus already names apart: $\mathrm{GPA}$ is the multiplication of *Introduction to the General Plain Algebra of Biquaternions*, $\mathrm{GQA}$ of *Introduction to the General Quaternionic Algebra of Biquaternions*, $\mathrm{GPS}$ of *Introduction to the General Plain Sesqualgebra of Biquaternions*, and $\mathrm{GQS}$ of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*. The other eight codes are the symmetrisations and the antisymmetrisations of those four, and this article is where they are read.

**What the last letter does and does not claim.** Only the six structures whose code ends in $\mathrm A$ are algebras over $\mathbb{C}$: the three operations of the plain row and the three of the quaternionic row are $\mathbb{C}$-bilinear, so each is an algebra multiplication in the broad sense. The six whose code ends in $\mathrm S$ are the six operations of the two sesqualgebras over $(\mathbb{C},\bar{\cdot})$: the two general ones, $\mathrm{GPS}$ and $\mathrm{GQS}$, are the multiplications of the two sesqualgebras over $\mathbb{C}$, and their four parts $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{SQS}$ and $\mathrm{AQS}$ are sesquilinear again, because the exchange that splits them carries the conjugation of the value and keeps the class. The bare interchange of the two arguments, which returns a product of the **opposite** parity, has its own two halves — the symmetrised sesquilinear product and the sesquilinear commutator — and those are the only $\mathbb{R}$-bilinear operations of the family. The trailing $\mathrm S$ names the class of the operation, which is the class of the parent product, and it is read that way throughout. The twelve names are read against the class-preserving exchange; §*The exchange behind the names*, at the end of the next section, contrasts it with the bare interchange.

**Remark (one collision).** In the physics part of the corpus the letters $\mathrm{APS}$ also denote the *algebra of physical space*, the paravector space $\mathrm{span}_{\mathbb{R}}\{e_0,\gamma_k\}$ of *Paravectors and the Geometry of Spacetime*. In this article and its siblings the same letters denote the antisymmetric part of the plain sesquilinear product, and the two readings occur in different parts of the corpus.

The general construction, with the obstruction of the class and the two projections, is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. This article owns the method, the naming and the laws.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$. An element is $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_k e_k$ and $Q_\mu\in\mathbb{C}$. The natural conjugation ${}^{\natural}$ negates the vector part, the coefficientwise one $\bar{\cdot}$ conjugates the coefficients, and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The four products are the **plain** $\tilde{P}\tilde{Q}$, the **quaternionic** $\tilde{P}^{\natural}\tilde{Q}$, the **sesquilinear** $\tilde{P}\tilde{Q}^{*}$ and the **general quaternionic sesquilinear** $\tilde{P}^{\natural}\tilde{Q}^{*}$ (*The Four Biquaternion Complex Products*), and §*The Method of the Decomposition*, below, reads the exchange of each of them and its two parts. The dot product $(\mathbf{P},\mathbf{Q})$ and the cross product $\mathbf{P}\times\mathbf{Q}$ are the general plain bilinear ones, and $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ are the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces (*Introduction to the Six Subspaces*). A vector expression such as $i\,\mathrm{Im}(\mathbf{v})$ is read componentwise. The **cyclic sum** of a bracket $b$ is the outer form $b(b(x,y),z)+b(b(y,z),x)+b(b(z,x),y)$ of *The Symmetric and Antisymmetric Parts of an Algebra Product*, §*Lie-Admissible Algebras*, so that a bracket written without the factor $\tfrac12$ has its cyclic sum multiplied by four.

---

## The Method of the Decomposition

Every one of the four products is split into a **symmetric part** and an **antisymmetric part**, and the split is a different operation in the two families of products. There are two definitions, one to a family.

**The algebra case.** The plain product $\tilde{P}\tilde{Q}$ and the quaternionic product $\tilde{P}^{\natural}\tilde{Q}$ have two $\mathbb{C}$-linear slots. Their exchange is the interchange of the two arguments, and the two parts are

$$
f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr),\qquad f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P})\bigr),
$$

**The sesqualgebra case.** The sesquilinear product $\tilde{P}\tilde{Q}^{*}$ and the general quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$ have one linear slot and one conjugate-linear slot, and the interchange alone returns a product of the **opposite** type, $\tilde{Q}\tilde{P}^{*}$, which is not a product of the sesqualgebra at all. The exchange is the interchange **followed by the coefficientwise conjugation of the value**, and the two parts are

$$
f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+\overline{f(\tilde{Q},\tilde{P})}\bigr),\qquad f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-\overline{f(\tilde{Q},\tilde{P})}\bigr),
$$

**The two definitions are not one.** The interchange keeps the class of a product exactly when its two slots have the same type, which is the algebra case; in the sesqualgebra case it does not, and it is the conjugation of the value that repairs the class. **The two definitions agree only for the two $\mathbb{C}$-bilinear products, and the split of an algebra product and the split of a sesqualgebra product share their shape and not their definition.** Both exchanges are involutions of the class — the interchange of the interchange, and the conjugate transpose of the conjugate transpose, return the product they start from — so the two parts are well defined in both cases. The adapted exchange, with the obstruction of the class and the two projections of the space of products, is developed in *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**What the two cases share.** The two parts carry the reconstruction $f=f^{\mathrm{s}}+f^{\mathrm{a}}$; the symmetric part is fixed by the exchange and the antisymmetric part is negated by it; and the pair is unique, since $f=s+t$ with $s$ fixed and $t$ negated forces $s=f^{\mathrm{s}}$ and $t=f^{\mathrm{a}}$. **Both parts are products of the class of $f$** — $\mathbb{C}$-bilinear in the algebra case, sesquilinear over $(\mathbb{C},\bar{\cdot})$ in the sesqualgebra case — and it is for that closure that the exchange of the sesqualgebra case is adapted and not bare.

**The square and its diagonal, where the two part company.** In the **algebra case** the antisymmetric part vanishes on the diagonal, since $f^{\mathrm{a}}(\tilde{Q},\tilde{Q})=-f^{\mathrm{a}}(\tilde{Q},\tilde{Q})$, so the square is the symmetric part alone, $f(\tilde{Q},\tilde{Q})=f^{\mathrm{s}}(\tilde{Q},\tilde{Q})$, and the polarisation of the square recovers the symmetric part off the diagonal. In the **sesqualgebra case** the antisymmetric part on the diagonal is the antisymmetrised square,

$$
f^{\mathrm{a}}(\tilde{Q},\tilde{Q})=\tfrac12\bigl(f(\tilde{Q},\tilde{Q})-\overline{f(\tilde{Q},\tilde{Q})}\bigr),
$$

which **need not vanish**: it vanishes exactly when the square of the element is fixed by the coefficientwise conjugation. The polarisation of the square then recovers the **plain** symmetrisation — the half-sum with the bare interchange — and not the symmetric part. **The algebra case has no antisymmetric diagonal, the sesqualgebra case has one and it is not zero in general.**

**The bare interchange is not the exchange.** The two halves of the bare interchange of a sesquilinear product are only $\mathbb{R}$-bilinear and are not products of the class: they are the symmetrised sesquilinear product $x\circ y$ of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator*. They are not the two parts named below, in the sesqualgebra case or in any case. The reading of the four splits from the side of the order symmetry, with the order-symmetric and order-antisymmetric halves and the worked examples, is *Scalar / Vector decomposition of the Biquaternion Complex Products*; the exchange that keeps the class is contrasted with the bare interchange at the end of the next section.

---

## The Twelve Names, One by One

Each family is read product by product. The three names of a product are taken together — the general product first, then its symmetric and its antisymmetric part — so that the two parts stand directly under the product they split. The six names of the two algebras come first, then the six of the two sesqualgebras; the laws are collected in the table and in the paragraphs on the two identities and the real part, below.

**The plain algebra.** $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$.

### GPA — General Plain Algebra

$$
\tilde{P}\tilde{Q}=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}.
$$

The multiplication of *Introduction to the General Plain Algebra of Biquaternions*, scalar part $P_0Q_0-(\mathbf{P},\mathbf{Q})$ and vector part $P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$. It is $\mathbb{C}$-bilinear, **associative**, and $e_0$ is a unit on both sides. It is the only associative product of the twelve, and the only one that is the multiplication of an associative unital algebra.

### SPA — Symmetric Plain Algebra

The symmetric part of $\mathrm{GPA}$ above.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr)=\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}+Q_0\mathbf{P}.
$$

The Jordan product $\tilde{P}\bullet\tilde{Q}$ of *Scalar / Vector decomposition of the Biquaternion Complex Products*, the plain product with the cross term dropped. It is commutative, $e_0$ is a unit on both sides, and it satisfies the **Jordan identity**; it is the only one of the twelve that does, and it is the only part that has a unit at all.

### APA — Antisymmetric Plain Algebra

The antisymmetric part of $\mathrm{GPA}$ above.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr)=\mathbf{P}\times\mathbf{Q}.
$$

The outer product $\tilde{P}\wedge\tilde{Q}$, the cross product of the two vector parts alone: scalar part zero, vector part $\mathbf{P}\times\mathbf{Q}$. It is alternating, its values lie in the vector subspace $\mathrm{Vect}(\mathbb{B})$, and it satisfies the **Jacobi identity**; it is the only one of the twelve that does. It is half the commutator $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$ of the algebra.

**The quaternionic algebra.** $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$.

### GQA — General Quaternionic Algebra

$$
\tilde{P}^{\natural}\tilde{Q}=\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]+P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}.
$$

The multiplication of *Introduction to the General Quaternionic Algebra of Biquaternions*, the plain product with the first factor read through ${}^{\natural}$. It is $\mathbb{C}$-bilinear, **not associative**, and $e_0$ is a unit on the **left** only. Its exchange is the natural conjugation of its value, $\tilde{Q}^{\natural}\tilde{P}=(\tilde{P}^{\natural}\tilde{Q})^{\natural}$.

### SQA — Symmetric Quaternionic Algebra

The symmetric part of $\mathrm{GQA}$ above.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P}\bigr)=\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr].
$$

The quaternion form $B(\tilde{P},\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$ of *Comparison Between the Four Biquaternion Products* read as a product; its scalar part is $B$ and its vector part is zero. It is commutative, its values lie in the centre $\mathbb{C}_{\mathbb{B}}$ — it compares two elements and returns a multiple of $e_0$ — and it has no unit. It is **not** a Jordan product.

### AQA — Antisymmetric Quaternionic Algebra

The antisymmetric part of $\mathrm{GQA}$ above.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}\bigr)=P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}.
$$

The quaternionic product with its scalar part removed: scalar part zero, vector part the mixed term with the cross term subtracted. It is alternating, its values lie in the vector subspace, and it **fails** the Jacobi identity, with witness $(e_0,e_1,e_2)$ where the cyclic sum is $-e_3\neq0$. It is half the commutator $[\tilde{P},\tilde{Q}]_{\natural}=\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}$.

**The plain sesqualgebra.** $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$.

### GPS — General Plain Sesqualgebra

$$
\tilde{P}\tilde{Q}^{*}=\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The multiplication of *Introduction to the General Plain Sesqualgebra of Biquaternions* and the derived operation of the algebra with its involution. Both products of the pair are the natural conjugates of the two orders of one plain product,
$$
\tilde{P}\tilde{Q}^{*}=\bigl(\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)^{\natural},\qquad
\tilde{Q}\tilde{P}^{*}=\bigl(\overline{\tilde{P}}\tilde{Q}^{\natural}\bigr)^{\natural}.
$$
It is sesquilinear over $(\mathbb{C},\bar{\cdot})$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second; it is **not associative**, and $e_0$ is a unit on the **right** only.

### SPS — Symmetric Plain Sesqualgebra

The symmetric part of $\mathrm{GPS}$ above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+(\tilde{P}\tilde{Q}^{*})^{\natural}\bigr)
=\mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{*}\bigr)
=\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr].
$$

The value $\tilde{P}\tilde{Q}^{*}$ has scalar part $H=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ and vector part $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$; the conjugate transpose sends the value to its conjugate with the vector part negated, $\overline{\tilde{Q}\tilde{P}^{*}}=(\tilde{P}\tilde{Q}^{*})^{\natural}$, so the half-sum keeps the scalar part and cancels the vector part. The operation is the **Hermitian form** $H(\tilde{P},\tilde{Q})=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ of *Biquaternion Norm and Invertibility* read as a product, and it is **central**: its values lie in the centre $\mathbb{C}_{\mathbb{B}}$. It is **conjugate-commutative**, $\mathrm{SPS}(\tilde{P},\tilde{Q})=\overline{\mathrm{SPS}(\tilde{Q},\tilde{P})}$, rather than commutative, and it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, conjugate-linear in the second argument. Its diagonal is the square read through the form, $\mathrm{SPS}(\tilde{Q},\tilde{Q})=H(\tilde{Q},\tilde{Q})=|Q_0|^{2}+(\mathbf{Q},\overline{\mathbf{Q}})$, which is real and strictly positive off the origin. Being central-valued it has no unit, and it **fails** the Jordan identity on the whole space, with witness $x=y=e_1$, where the two sides are $0$ and $e_0$.

### APS — Antisymmetric Plain Sesqualgebra

The antisymmetric part of $\mathrm{GPS}$ above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-(\tilde{P}\tilde{Q}^{*})^{\natural}\bigr)
=\mathrm{Vect}\bigl(\tilde{P}\tilde{Q}^{*}\bigr)
=-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The same value as $\mathrm{SPS}$, with the difference in place of the sum: the half-difference cancels the scalar part and keeps the vector part. It is **pure vector**, so its image is the vector subspace $\mathrm{Vect}(\mathbb{B})$. It is **conjugate-alternating**, $\mathrm{APS}(\tilde{P},\tilde{Q})=-\overline{\mathrm{APS}(\tilde{Q},\tilde{P})}$, and its diagonal is the **vector part of the square**,
$$
\mathrm{APS}(\tilde{Q},\tilde{Q})=\mathrm{Vect}(\tilde{Q}\tilde{Q}^{*}),
$$
which is **not zero** in general: for $\tilde{Q}=e_1+ie_2$ it is $2ie_3$. It has no unit, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jacobi identity, with witness $(e_0,e_1,e_2)$ where the cyclic sum is $e_3$.

**The quaternionic sesqualgebra.** $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$.

### GQS — General Quaternionic Sesqualgebra

$$
\tilde{P}^{\natural}\tilde{Q}^{*}=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The multiplication of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, both slots read through a conjugation. Both products of the pair are the natural conjugates of the two orders of one plain product,
$$
\tilde{P}^{\natural}\tilde{Q}^{*}=\bigl(\overline{\tilde{Q}}\tilde{P}\bigr)^{\natural},\qquad
\tilde{Q}^{\natural}\tilde{P}^{*}=\bigl(\overline{\tilde{P}}\tilde{Q}\bigr)^{\natural}.
$$
It is sesquilinear over $(\mathbb{C},\bar{\cdot})$, **not associative**, and it has a unit on **neither** side. It is the product whose ternary product fails the Jordan triple identity (*Why the Fourth Product Is a Gauge Structure and Not a State Space*).

### SQS — Symmetric Quaternionic Sesqualgebra

The symmetric part of $\mathrm{GQS}$ above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)
=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P},
$$

since $\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}=\tilde{Q}^{*}\tilde{P}^{\natural}$. The value $\tilde{P}^{\natural}\tilde{Q}^{*}$ has scalar part $K=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ and vector part $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$; the conjugate transpose is not the conjugation of the value here — the two cross products cancel between the two orders instead of adding — so the half-sum keeps the scalar part and the mixed term and cancels the cross product. Its scalar part is the general quaternionic sesquilinear form $K$ of *The Krein Gram Matrix and the Restrictions of the Form* and its vector part is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$, so its values lie in **no** subspace of the six. It is **conjugate-commutative**, $\mathrm{SQS}(\tilde{P},\tilde{Q})=\overline{\mathrm{SQS}(\tilde{Q},\tilde{P})}$, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jordan identity, with witness $x=y=e_1$ where the two sides are $-e_0$ and $e_0$. Its diagonal is not central in general: at $\tilde{Q}=e_0+e_1$ it is $-2e_1$, while the real vector directions, among them $e_1$, carry central diagonals.

### AQS — Antisymmetric Quaternionic Sesqualgebra

The antisymmetric part of $\mathrm{GQS}$ above, under the conjugate transpose.

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}\bigr)
=\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}}.
$$

The cross products of the two orders add in the difference while the scalar part and the mixed term cancel, so the half-difference is the **cross product** $\mathbf{P}\times\overline{\mathbf{Q}}$ of the vector part of the first argument with the conjugate of the vector part of the second. It is **pure vector**, so its image is the vector subspace $\mathrm{Vect}(\mathbb{B})$; it is **conjugate-alternating**, $\mathrm{AQS}(\tilde{P},\tilde{Q})=-\overline{\mathrm{AQS}(\tilde{Q},\tilde{P})}$, and its diagonal is the cross product of the vector part with its conjugate, $\mathrm{AQS}(\tilde{Q},\tilde{Q})=\mathbf{Q}\times\overline{\mathbf{Q}}$, which is **not zero** in general: for $\tilde{Q}=e_1+ie_2$ it is $-2ie_3$. It has no unit, it is sesquilinear over $(\mathbb{C},\bar{\cdot})$, and it **fails** the Jacobi identity, with witness $(e_1,e_1,ie_2)$, where the cyclic sum is $-2ie_2$. This is the only one of the three failing brackets whose witness needs a complex element off the real basis, which is why the failure is invisible on the real forms.

### The Exchange Behind the Names

All twelve names are read against the exchange of §*The Method of the Decomposition*: the interchange for the two $\mathbb{C}$-bilinear products, whose two slots have the same type, and the conjugate transpose for the two sesquilinear products, whose slots are one linear and one conjugate-linear. It is an involution of the class in both cases, and it is the exchange that makes the count $4\times3$ while keeping every part in the class of its parent: the six $\mathbb{C}$-bilinear parts of the two algebras and the six sesquilinear parts of the two sesqualgebras.

The bare interchange does not keep the class, and its two halves — the symmetrised sesquilinear product $x\circ y$ of *The Sesquilinear Symmetrised Product* and the sesquilinear commutator of *The Sesquilinear Commutator* — are **not** the two parts named $\mathrm{SPS}$ and $\mathrm{APS}$ of this article; the two readings are set side by side in §*The Other Exchange, and the Class It Keeps* of *Scalar / Vector decomposition of the Biquaternion Complex Products*.

**Whether the exchange is read on the value.** The split needs only the involution, which §*The Method of the Decomposition* settles for the four products; whether the exchange can be read on the value of the product is a second question, and the two sesqualgebra rows answer it differently. The **sesquilinear** product has it, since $\overline{\tilde{Q}\tilde{P}^{*}}=(\tilde{P}\tilde{Q}^{*})^{\natural}$, which is why $\mathrm{SPS}$ and $\mathrm{APS}$ are the scalar and the vector part of the one value $\tilde{P}\tilde{Q}^{*}$, valued in the centre $\mathbb{C}_{\mathbb{B}}$ and in the vector subspace. The **general quaternionic sesquilinear** product has it not: the value $\tilde{P}^{\natural}\tilde{Q}^{*}=(\overline{\tilde{Q}}\tilde{P})^{\natural}$ determines only the plain product $\overline{\tilde{Q}}\tilde{P}$, whose factorisation into $\overline{\tilde{Q}}$ and $\tilde{P}$ is not unique, and two pairs with the same value have different swaps — the pairs $(\tilde{P},\tilde{Q})=(-ie_3,-ie_0)$ and $(e_2,e_1)$ both have the value $-e_3$, while the swapped values $\tilde{Q}^{\natural}\tilde{P}^{*}$ are $-e_3$ and $e_3$ — so no conjugation of $\tilde{P}^{\natural}\tilde{Q}^{*}$ is $\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}=\tilde{Q}^{*}\tilde{P}^{\natural}$. $\mathrm{SQS}$ and $\mathrm{AQS}$ are therefore the half-sum and the half-difference of the two values $\tilde{P}^{\natural}\tilde{Q}^{*}$ and $\tilde{Q}^{*}\tilde{P}^{\natural}$, and they are valued in no subspace of the six. The shape is the same in both rows: each of the four parts is a half-sum or a half-difference of the two orders of one plain product read through the conjugations — $\overline{\tilde{Q}}\tilde{P}^{\natural}$ in the plain row and $\overline{\tilde{Q}}\tilde{P}$ in the quaternionic row — and the two rows differ only by the ${}^{\natural}$ on the second factor.

---

## The Table of the Twelve

| name | the product | scalar part | vector part | scalars | law | unit | image |
|---|---|---|---|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde{P}\tilde{Q}$ | $\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | associative | $e_0$, both sides | all of $\mathbb{B}$ |
| $\mathrm{SPA}$ | $\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | $\bigl[P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}+Q_0\mathbf{P}$ | $\mathbb{C}$ | commutative, **Jordan** | $e_0$, both sides | all of $\mathbb{B}$ |
| $\mathrm{APA}$ | $\tfrac12(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | $\bigl[0\bigr]$ | $\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | alternating, **Jacobi** | none | $\mathrm{Vect}(\mathbb{B})$ |
| $\mathrm{GQA}$ | $\tilde{P}^{\natural}\tilde{Q}$ | $\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]$ | $+P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | not associative | $e_0$, left only | all of $\mathbb{B}$ |
| $\mathrm{SQA}$ | $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})$ | $\bigl[P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr]$ | $0$ | $\mathbb{C}$ | commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| $\mathrm{AQA}$ | $\tfrac12(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P})$ | $\bigl[0\bigr]$ | $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | $\mathbb{C}$ | alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| $\mathrm{GPS}$ | $\tilde{P}\tilde{Q}^{*}$ | $\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | not associative | $e_0$, right only | all of $\mathbb{B}$ |
| $\mathrm{SPS}$ | $\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)$ | $\bigl[P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $0$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | the centre $\mathbb{C}_{\mathbb{B}}$ |
| $\mathrm{APS}$ | $\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}}\tilde{P}^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |
| $\mathrm{GQS}$ | $\tilde{P}^{\natural}\tilde{Q}^{*}$ | $\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | not associative | none | all of $\mathbb{B}$ |
| $\mathrm{SQS}$ | $\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)$ | $\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]$ | $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-commutative, no Jordan | none | no subspace of the six |
| $\mathrm{AQS}$ | $\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr)$ | $\bigl[0\bigr]$ | $\mathbf{P}\times\overline{\mathbf{Q}}$ | $\mathbb{C},\bar{\cdot}$ | conjugate-alternating, no Jacobi | none | $\mathrm{Vect}(\mathbb{B})$ |

The **first column** is the operation as a product of the two elements: the four products
themselves, and for each part the half-sum or the half-difference of the product and its
class-preserving exchange, written with the second monomial in the collapsed form of the
exchange, $\overline{\tilde{Q}\tilde{P}^{*}}=\overline{\tilde{Q}}\tilde{P}^{\natural}$ for the
plain sesqualgebra and $\overline{\tilde{Q}^{\natural}\tilde{P}^{*}}=\tilde{Q}^{*}\tilde{P}^{\natural}$
for the quaternionic one. The **second** column is the **scalar part** of the value and the
**third** is the **vector part**, each written out, $0$ where the part vanishes. Here
$\mathbf{Q}$ and $\overline{\mathbf{Q}}$ are the vector part of the second element and of its
coefficientwise conjugate, $(\cdot,\cdot)$ is the bilinear dot product and $\times$ the
bilinear cross product. The two central operations $\mathrm{SQA}$ and $\mathrm{SPS}$ have no
vector part, and the four antisymmetric operations $\mathrm{APA}$, $\mathrm{AQA}$,
$\mathrm{APS}$, $\mathrm{AQS}$ no scalar part; the scalar part plus the vector part of a row
is its product.

Six of the twelve are $\mathbb{C}$-bilinear, the three operations of each of the two $\mathrm A$-rows, and the remaining six are the six sesquilinear operations of the two sesqualgebra rows. In the two $\mathrm A$-rows the symmetric part is commutative and the antisymmetric part is alternating, with zero diagonal; in the two $\mathrm S$-rows the same two symmetries hold **up to the coefficientwise conjugation**, the symmetric part being conjugate-commutative, $\mathrm{SPS}(\tilde{P},\tilde{Q})=\overline{\mathrm{SPS}(\tilde{Q},\tilde{P})}$ and likewise for $\mathrm{SQS}$, and the antisymmetric part conjugate-alternating, $\mathrm{APS}(\tilde{P},\tilde{Q})=-\overline{\mathrm{APS}(\tilde{Q},\tilde{P})}$ and likewise for $\mathrm{AQS}$. The diagonal of the two sesqualgebra antisymmetric parts is the vector part of the square and does not vanish in general. These symmetries hold by the definitions alone, for every product.

### The Two That Are Lie and Jordan Products

Of the twelve, exactly two are the product of one of the two classical nonassociative algebras, and both sit in the plain row. A symmetrisation is a **Jordan** product only when it satisfies the Jordan identity, an antisymmetrisation a **Lie** product only when it satisfies the Jacobi identity, and of the twelve exactly one of each meets its identity. The two are these:

- $\mathrm{APA}$ is alternating and satisfies the Jacobi identity, so it is a **Lie** product; it is the Lie algebra of *The Unitary Lie Algebra*, with the vector subspace as a Lie subalgebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, the quaternion subspace as $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ and the anti-Hermitian subspace as $\mathfrak{u}(2)$, whose derived algebra is $\mathfrak{su}(2)$ (*The Six Subspaces and the Four Complex Products*).
- $\mathrm{SPA}$ is commutative and satisfies the Jordan identity, so it is a **Jordan** product; it is the special Jordan algebra of degree two, and its Hermitian subspace is the Hermitian Jordan algebra $J(\mathbb{B})$.

The other six parts fail the identity of their kind, and each failure is witnessed on a single triple or a single element:

| name | identity | witness | failure |
|---|---|---|---|
| $\mathrm{AQA}$ | Jacobi | $(e_0,e_1,e_2)$ | $-e_3$ |
| $\mathrm{APS}$ | Jacobi | $(e_0,e_1,e_2)$ | $e_3$ |
| $\mathrm{AQS}$ | Jacobi | $(e_1,e_1,ie_2)$ | $-2ie_2$ |
| $\mathrm{SQA}$ | Jordan | $x=y=e_1$ | the sides are $0$ and $e_0$ |
| $\mathrm{SPS}$ | Jordan | $x=y=e_1$ | the sides are $0$ and $e_0$ |
| $\mathrm{SQS}$ | Jordan | $x=y=e_1$ | the sides are $-e_0$ and $e_0$ |

The last column of the three Jacobi rows is the cyclic sum declared in the Conventions.

The three Jacobi failures have three different reasons. For $\mathrm{AQA}$ the culprit is the non-associativity of the product it comes from; for $\mathrm{APS}$ and $\mathrm{AQS}$ it is the obstruction of *Lie Algebras of Sesqualgebras*, where the antisymmetrisation of a sesquilinear product is a Lie bracket only after the collapse of the two involutions, which a genuine sesqualgebra forbids. The three Jordan failures are witnessed above, the first two on the same element $e_1$ because the two products agree on the real basis. In the three Jordan rows the last column gives the two sides of the identity, $(x^{2}\bullet x)\bullet x$ and $x^{2}\bullet(x\bullet x)$: they differ by $e_0$ for $\mathrm{SQA}$ and $\mathrm{SPS}$, whose symmetric square on $e_1$ is $e_0$, and by $2e_0$ for $\mathrm{SQS}$, whose symmetric square on $e_1$ is $-e_0$.

The four general products are neither symmetrisations nor antisymmetrisations, and neither identity is put to them: $\mathrm{GPA}$ is the one associative product of the twelve, and the other three are not associative.

### The Reconstruction, Row by Row

Each product is the sum of its two parts, one identity to a row:

$$
\mathrm{GPA}=\mathrm{SPA}+\mathrm{APA},\qquad
\mathrm{GQA}=\mathrm{SQA}+\mathrm{AQA},\qquad
\mathrm{GPS}=\mathrm{SPS}+\mathrm{APS},\qquad
\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}.
$$

These four identities and the four definitions of the general products are the only relations among the twelve: no part of one row is a conjugate of a part of another row, since the four general products are related to one another by the slots while the twelve operations are not. The square of an algebra product reads its symmetric part alone, $\mathrm{GPA}(\tilde{Q},\tilde{Q})=\mathrm{SPA}(\tilde{Q},\tilde{Q})$ and $\mathrm{GQA}(\tilde{Q},\tilde{Q})=\mathrm{SQA}(\tilde{Q},\tilde{Q})$, and its polarised square is twice the symmetric part. In the two sesqualgebra rows the square is split by the exchange instead: its diagonal is the pair $\bigl(\mathrm{SPS}(\tilde{Q},\tilde{Q}),\mathrm{APS}(\tilde{Q},\tilde{Q})\bigr)$ in the plain row and $\bigl(\mathrm{SQS}(\tilde{Q},\tilde{Q}),\mathrm{AQS}(\tilde{Q},\tilde{Q})\bigr)$ in the quaternionic row, the antisymmetric side being the vector part of the square and not zero, and the polarised square recovers the plain symmetrisation of the bare interchange and not the symmetric part (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Diagonal and the Square*).

### The Twelve Are Distinct, and Ten on the Real Part

The twelve operations are pairwise distinct on the complex space. On the real part of the space — the real span of $e_0,e_1,e_2,e_3$, where the coefficientwise conjugation acts trivially — two pairs coincide:

$$
\mathrm{APA}=\mathrm{AQS},\qquad \mathrm{SQA}=\mathrm{SPS},
$$

both on the real elements. So the real part of the space carries **ten** operations and not twelve: the count twelve is the count for the complex space. The first coincidence is the equality of the two cross products on real vectors; the second is the equality of the two scalar forms, $B=H$ on the real elements.

---

## Summary

The complex space of the biquaternion algebra carries four products, and each is split into a symmetric and an antisymmetric part by an exchange that keeps the class, so it carries twelve operations. The exchange is the plain interchange of the two arguments for the two $\mathbb{C}$-bilinear products and the conjugate transpose, the interchange followed by the coefficientwise conjugation of the value, for the two sesquilinear products. The name of each is three letters: the part, $\mathrm G$ general or $\mathrm S$ symmetric or $\mathrm A$ antisymmetric; the first slot, $\mathrm P$ plain or $\mathrm Q$ quaternionic; the family, $\mathrm A$ the algebra over $\mathbb{C}$ or $\mathrm S$ the sesqualgebra over $\mathbb{C}$. The four names that begin with $\mathrm G$ are the four structures the corpus names apart, and the other eight are their symmetrisations and antisymmetrisations.

Of the twelve, two are the product of a classical nonassociative algebra and both are in the plain row: $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$ is the one Lie product and $\mathrm{SPA}=\tilde{P}\bullet\tilde{Q}$ the one Jordan product. The other six parts fail the identity of their kind, with witnesses recorded above. The six operations of the two $\mathrm A$-rows are $\mathbb{C}$-bilinear and the six of the two $\mathrm S$-rows are sesquilinear over $(\mathbb{C},\bar{\cdot})$; in the two $\mathrm S$-rows the symmetric part is conjugate-commutative, the antisymmetric part is conjugate-alternating, and the diagonal of the antisymmetric part is the vector part of the square and does not vanish. The twelve are pairwise distinct on the complex space and fall to ten on the real part, where $\mathrm{APA}=\mathrm{AQS}$ and $\mathrm{SQA}=\mathrm{SPS}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_0,e_1,e_2,e_3$, central imaginary $i$ |
| $\tilde{Q}=Q_0e_0+\mathbf{Q}$ | a biquaternion, its scalar and vector parts |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | the natural, the coefficientwise and the Hermitian conjugation |
| $\tilde{P}\tilde{Q}$, $\tilde{P}^{\natural}\tilde{Q}$, $\tilde{P}\tilde{Q}^{*}$, $\tilde{P}^{\natural}\tilde{Q}^{*}$ | the four products: plain, quaternionic, sesquilinear, general quaternionic sesquilinear |
| $f(\tilde{Q},\tilde{P})$ | the interchange of the two arguments, the exchange of a $\mathbb{C}$-bilinear product |
| $\overline{f(\tilde{Q},\tilde{P})}$ | the conjugate transpose, the exchange of a sesquilinear product |
| $f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr)$ | the symmetric part of a $\mathbb{C}$-bilinear product |
| $f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P})\bigr)$ | the antisymmetric part of a $\mathbb{C}$-bilinear product |
| $f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+\overline{f(\tilde{Q},\tilde{P})}\bigr)$ | the symmetric part of a sesquilinear product |
| $f^{\mathrm{a}}(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-\overline{f(\tilde{Q},\tilde{P})}\bigr)$ | the antisymmetric part of a sesquilinear product |

| $\mathrm G$, $\mathrm S$, $\mathrm A$ (first letter) | the general product, its symmetric part, its antisymmetric part |
| $\mathrm P$, $\mathrm Q$ (second letter) | the plain first slot, the quaternionic first slot |
| $\mathrm A$, $\mathrm S$ (third letter) | the family: the algebra over $\mathbb{C}$, the sesqualgebra over $\mathbb{C}$ |
| $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$ | the six operations of the two algebras over $\mathbb{C}$ |
| $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ | the six operations of the two sesqualgebras over $\mathbb{C}$ |
| $B(\tilde{P},\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$ | the quaternion form, $\mathrm{SQA}$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_{+}$, $\mathbb{M}_{-}$ | the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces |
| Jacobi, Jordan | the two identities that name $\mathrm{APA}$ and $\mathrm{SPA}$ |

## Further Reading

- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the adapted exchange, the obstruction of the class and the two projections and the class-preserving alternative of §*The Split That Keeps the Class*.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* and *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the general construction of the two parts, the two projections and the two admissibility conditions.
- *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, for the adapted exchange that keeps the class.
- *Scalar / Vector decomposition of the Biquaternion Complex Products*, for the same splits from the side of the order symmetry, with the worked examples.
- *The Four Biquaternion Complex Products*, *Relations Between the Four Biquaternion Products* and *Comparison Between the Four Biquaternion Products*, for the four products and their forms.
- *Introduction to the General Plain Algebra of Biquaternions*, *Introduction to the General Quaternionic Algebra of Biquaternions*, *Introduction to the General Plain Sesqualgebra of Biquaternions* and *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, for the four general products.
- *The Six Subspaces and the Four Complex Products*, for what the twelve do on the six subspaces, and *The Sesquilinear Commutator*, for the sesquilinear bracket.
- *The Unitary Lie Algebra* and *The Hermitian Jordan Algebra*, for the two structures that pass, $\mathrm{APA}$ and $\mathrm{SPA}$.
