# __The 12 Multiplication Tables of the Biquaternion Complex Space__

## Introduction

The complex space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries twelve products, the operations of *Symmetric and Antisymmetric Decomposition of the Four General Products*, and each of the twelve carries a name, a three-letter code and an algebraic structure of its own in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. This article reads the twelve as **tables**. It belongs to the *Algebra* group of the category *Biquaternion Algebraic Structures* and carries the sixteen basis products of each of the twelve.

The reason a table is enough is that each of the twelve products is additive in each variable and obeys one of two scalar rules. It is therefore fixed by the sixteen products $e_\mu\star e_\nu$ of the pairs of basis elements, and those sixteen values are the **multiplication table**. The table is the structure-constant data of the product; the scalar rule is the second half of the data, and it is read off the last letter of the code: a code ending in $\mathrm{A}$ names a $\mathbb{C}$-bilinear product and a code ending in $\mathrm{S}$ a sesquilinear product over $(\mathbb{C},\bar{\cdot}\,)$. The pair (table, class) is the product, and each half of the pair is necessary: the class alone fixes no value and the table alone is ambiguous, since two of the twelve products have the same table and differ only in class.

The article does three things. It defines the table of a product and the two extension rules, and proves that the table together with the class determines the product and is determined by it. It writes the twelve tables out, one to a product, in three groups — the four general products, their four symmetric parts and their four antisymmetric parts. And it reads the correspondence between the tables and the products: the extension of each table recovers its product, the table of a part is the entrywise symmetrisation or antisymmetrisation of the table of its parent, and the table is the structure-constant datum of the product. On the four-element basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the twelve tables take ten distinct values, the two collisions being the two coincidences that the corpus records on the real forms; on the eight-element real basis the twelve are distinct. The count of **structures** is twelve in both readings, because a structure is a product on the complex space and its datum is the table **together with the class**, so the two colliding tables are two structures and not one.

## The Table of a Product

### The Table

**Definition.** Let $\star$ be one of the twelve products. Its **multiplication table** is the $4\times4$ array $T(\star)$ with entries

$$
T(\star)_{\mu\nu}=e_\mu\star e_\nu,\qquad \mu,\nu\in\{t,x,y,z\}.
$$

The row index is the left factor and the column index the right one, so the table has one entry to each ordered pair of basis elements and sixteen entries in all.

**Definition.** Let $T=(T_{\mu\nu})$ be a $4\times4$ array of elements of $\mathbb{B}$. The **bilinear reading** of $T$ is the product $\star_T$ defined on general elements by

$$
\tilde Q_1\star_T\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}Q_{1,\mu} Q_{2,\nu}\,T_{\mu\nu},
$$

and the **sesquilinear reading** of $T$ is the product defined by

$$
\tilde Q_1\star_T\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}Q_{1,\mu}\overline{Q_{2,\nu}}\,T_{\mu\nu}.
$$

The two readings differ in one point alone: whether the second coordinate is used as it stands or through the coefficientwise conjugation.

**Proposition (the class of a reading).** The bilinear reading of a table is additive in each variable and $\mathbb{C}$-bilinear in both; the sesquilinear reading is additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second.

*Proof.* Each coordinate of the value is a finite sum of the terms displayed, and each term is bilinear, or linear in the first coordinate and conjugate-linear in the second, in the coordinates of the two elements; additivity and the two scalar rules are read coordinate by coordinate.

**Theorem (the table and the class determine the product).** Let $T$ be a table and let $r$ be one of the two readings. Then $r(T)$ is the unique product of the class of $r$ whose table is $T$.

*Proof.* The reading $r(T)$ is a product of the class, by the proposition above, and on the basis pair $(e_\mu,e_\nu)$ every coordinate but one vanishes and the surviving term is $T_{\mu\nu}$; so the table of $r(T)$ is $T$, and existence is proved. For uniqueness, let $\star$ be any product of the same class with table $T$. Both $\star$ and $r(T)$ are additive in each variable and obey the same two scalar rules, so they agree on every pair of basis elements — both give $T_{\mu\nu}$ — and therefore, by the two scalar rules again, on every pair of elements; hence $\star=r(T)$. The same argument read backwards shows that the table of a product determines the product once the class is fixed, and so the two assignments are inverse to one another on the products of a fixed class.

**Remark (the class is not decoration).** The table alone does not determine the product. The two readings of one and the same table are in general different products, and on the twelve the difference occurs: the two products $\mathrm{SQA}$ and $\mathrm{SPS}$ have the same table and are separated by the class alone, and so do $\mathrm{APA}$ and $\mathrm{AQS}$ in another pair, as §*The Ten Distinct Tables* proves. A table is a datum about a *typed* product, and the type — the class — is carried by the last letter of the code.

### The Entries Are Real Quaternions

**Proposition.** Every entry of every one of the twelve tables is $0$ or a basis element up to sign, $\pm e_t,\pm \vec e_x,\pm \vec e_y,\pm \vec e_z$. The central imaginary $i$ occurs in no entry.

*Proof.* The entries are computed pair by pair from the twelve products, and the results are the twelve tables of §*The Twelve Tables*; inspection shows every entry to be $0$ or $\pm e_\mu$. The reason is structural: the basis is a real basis of real quaternions, closed under both conjugations up to sign, $\overline{e_\mu}=e_\mu$ and $e_\mu^{\natural}=e_\mu^{*}=\varepsilon_\mu e_\mu$, and the plain product of two real quaternions is a real quaternion; since the central imaginary $i$ is a coefficient and never a factor, no entry can carry it.

**Remark.** The tables are therefore integral: each is a table of integers times basis elements, and a table over $\mathbb{Z}$ rather than over $\mathbb{C}$. This is the table form of the statement that the complex structure of $\mathbb{B}$ lives in the coefficients and not in the multiplication, which is the reading of the multiplication tables in *The Biquaternion Algebra and Its Vector Spaces*, §*The Multiplication Table*, and of the change of scalars in *The Realification and the Effect of the Change of Scalars*.

---

## The Twelve Tables

The twelve tables are written below, one to a product, in the order general, symmetric, antisymmetric, and inside each group the order plain bilinear, quaternionic bilinear, plain sesquilinear, quaternionic sesquilinear. In every table the corner entry is the operation and the row index is the left factor.

### The Four General Tables

**$\mathrm{GPA}$, the general plain bilinear product $\tilde Q_1\tilde Q_2$** (the class $\mathrm A$, $\mathbb{C}$-bilinear). It is the quaternion table, the one already read in *The Biquaternion Algebra and Its Vector Spaces*, §*The Multiplication Table*.

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

The diagonal is $e_t,-e_t,-e_t,-e_t$; the imaginary block is the quaternion block. The table carries the antisymmetry of the three imaginary units, $\vec e_\nu \vec e_\lambda = -\vec e_\lambda \vec e_\nu$ for $\nu \neq \lambda$ in $\{x,y,z\}$.

**$\mathrm{GQA}$, the general quaternionic bilinear product $\tilde Q_1^{\natural}\tilde Q_2$** (the class $\mathrm A$, $\mathbb{C}$-bilinear).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $e_t$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $\vec e_z$ | $e_t$ | $-\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $e_t$ |

The table is the quaternion table with the first imaginary factor negated, that is with the row sign changed on the three vector rows; the diagonal is $e_t$ throughout.

**$\mathrm{GPS}$, the general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$** (the class $\mathrm S$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$). It is the table read in *Introduction to the General Plain Sesqualgebra*, §*The Multiplication Table*, where it is computed as $e_\mu\star e_\nu=\varepsilon_\nu e_\mu e_\nu$.

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $e_t$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $\vec e_z$ | $e_t$ | $-\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $e_t$ |

The diagonal is $e_t$ throughout, the imaginary block anticommutes with the signs of the quaternion block, and the first row is the negation of the identity row, $e_t\star e_\nu=e^{*}_\nu$; the first row is the visible form of the one-sided unit.

**$\mathrm{GQS}$, the general quaternionic sesquilinear product $\tilde Q_1^{\natural}\tilde Q_2^{*}$** (the class $\mathrm S$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

The table is the table of $\mathrm{GPS}$ with the first slot read through the natural conjugation, that is with the row sign changed on the three vector rows; the diagonal is $e_t,-e_t,-e_t,-e_t$.

### The Four Symmetric Tables

**$\mathrm{SPA}$, the symmetric plain bilinear product $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$** (the class $\mathrm A$, $\mathbb{C}$-bilinear, the Jordan product $\tilde Q_1\bullet\tilde Q_2$).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $0$ | $0$ |
| $\vec e_y$ | $\vec e_y$ | $0$ | $-e_t$ | $0$ |
| $\vec e_z$ | $\vec e_z$ | $0$ | $0$ | $-e_t$ |

The table is symmetric, and its off-diagonal imaginary block vanishes: the symmetrisation drops the cross product, and the table records the loss.

**$\mathrm{SQA}$, the symmetric quaternionic bilinear product $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)$** (the class $\mathrm A$, $\mathbb{C}$-bilinear).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $e_t$ | $0$ | $0$ |
| $\vec e_y$ | $0$ | $0$ | $e_t$ | $0$ |
| $\vec e_z$ | $0$ | $0$ | $0$ | $e_t$ |

The table is the identity table, $\delta_{\mu\nu}e_t$: the quaternion form $\langle\cdot,\cdot\rangle_{\natural}$ read as a product, with the whole vector structure of the product gone.

**$\mathrm{SPS}$, the symmetric plain sesquilinear product $\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})e_t$** (the class $\mathrm S$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ read as a product).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $e_t$ | $0$ | $0$ |
| $\vec e_y$ | $0$ | $0$ | $e_t$ | $0$ |
| $\vec e_z$ | $0$ | $0$ | $0$ | $e_t$ |

The table is the identity table again, $e_\mu\star e_\nu=\delta_{\mu\nu}e_t$, read on the basis in *Introduction to the Symmetric Plain Sesqualgebra*, §*The Multiplication Table of the Basis*.

**$\mathrm{SQS}$, the symmetric quaternionic sesquilinear product $\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)$** (the class $\mathrm S$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $-e_t$ | $0$ | $0$ |
| $\vec e_y$ | $-\vec e_y$ | $0$ | $-e_t$ | $0$ |
| $\vec e_z$ | $-\vec e_z$ | $0$ | $0$ | $-e_t$ |

The table is conjugate-symmetric, and its off-diagonal imaginary block vanishes; the first row and the first column are the two halves of the Hermitian conjugation, $e_t\star e_\nu=e^{*}_\nu$ and $e_\nu\star e_t=(e^{*}_\nu)^{\natural}$.

### The Four Antisymmetric Tables

**$\mathrm{APA}$, the antisymmetric plain bilinear product $\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)=\vec Q_1\times\vec Q_2$** (the class $\mathrm A$, $\mathbb{C}$-bilinear, the Lie product $\tilde Q_1\wedge\tilde Q_2$).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $0$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $0$ | $-\vec e_z$ | $0$ | $\vec e_x$ |
| $\vec e_z$ | $0$ | $\vec e_y$ | $-\vec e_x$ | $0$ |

The table is alternating, its identity row and column vanish, and its imaginary block is the cross-product table of $\mathbb{C}^3$, read in *Introduction to the Antisymmetric Plain Algebra*, §*The Sixteen Brackets*.

**$\mathrm{AQA}$, the antisymmetric quaternionic bilinear product $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1)$** (the class $\mathrm A$, $\mathbb{C}$-bilinear).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $0$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $\vec e_z$ | $0$ | $-\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $0$ |

The table is alternating, but its identity row and column do **not** vanish: the block is the mixed term $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ with the cross term removed, and the mixed term survives on the identity.

**$\mathrm{APS}$, the antisymmetric plain sesquilinear product $\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-\overline{\tilde Q_2\tilde Q_1^{*}}\bigr)=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$** (the class $\mathrm S$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $0$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $\vec e_z$ | $0$ | $-\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $0$ |

The table is conjugate-alternating, its diagonal vanishes, and the first row and column are the negation of the vector part of the Hermitian conjugation.

**$\mathrm{AQS}$, the antisymmetric quaternionic sesquilinear product $\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)=\vec Q_1\times\overline{\vec Q_2}$** (the class $\mathrm S$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$).

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $0$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $0$ | $-\vec e_z$ | $0$ | $\vec e_x$ |
| $\vec e_z$ | $0$ | $\vec e_y$ | $-\vec e_x$ | $0$ |

The table is alternating and coincides, entry by entry, with the table of $\mathrm{APA}$; the coincidence is traced in §*The Ten Distinct Tables*.

---

## The Tables and the Twelve Products

### The Extension of Each Table Recovers Its Product

**Theorem (the correspondence).** Let $r$ be the reading of the class of a product $\star$ among the twelve, bilinear for the six codes ending in $\mathrm{A}$ and sesquilinear for the six ending in $\mathrm{S}$. Then $r\bigl(T(\star)\bigr)=\star$. The table of each of the twelve products, extended by the reading of its class, is the product itself, and the table is its structure-constant data.

*Proof.* This is the existence half of the theorem of §*The Table of a Product*, applied to the table of the product: the reading of $T(\star)$ is a product of the class whose table is $T(\star)$, and the table fixes the product among the products of that class, so the reading of $T(\star)$ is $\star$. The assertion was recomputed pair by pair on the sixteen basis products of each of the twelve, and on the general elements it is the identity of the two double sums.

**Corollary (the table is a definition).** Once the class is named, the sixteen entries of $T(\star)$ define $\star$ and are defined by it; the table is a presentation of the product and needs no other product to be read. This is the sense in which the table of a product stands on its own, the reading rule of the class being the only further datum.

### The Table of a Part Is the Entrywise Part

The four symmetric and the four antisymmetric products are built from the four general products by an exchange, and the exchange acts on the tables entry by entry.

**Theorem (the entrywise part).** For the two $\mathbb{C}$-bilinear families the exchange is the interchange of the two arguments, and the tables of the parts are the entrywise symmetrisation and antisymmetrisation of the table of the parent,

$$
\boxed{\;T(\mathrm{SPA})_{\mu\nu}=\tfrac12\bigl(T(\mathrm{GPA})_{\mu\nu}+T(\mathrm{GPA})_{\nu\mu}\bigr),\qquad
T(\mathrm{APA})_{\mu\nu}=\tfrac12\bigl(T(\mathrm{GPA})_{\mu\nu}-T(\mathrm{GPA})_{\nu\mu}\bigr)\;},
$$

and the same two identities with $\mathrm{GQA}$, $\mathrm{SQA}$, $\mathrm{AQA}$ in place of $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{APA}$. For the two sesquilinear families the exchange is the interchange followed by the coefficientwise conjugation of the value, and the tables of the parts are the entrywise conjugate-symmetrisation and conjugate-antisymmetrisation of the table of the parent,

$$
\boxed{\;T(\mathrm{SPS})_{\mu\nu}=\tfrac12\bigl(T(\mathrm{GPS})_{\mu\nu}+\overline{T(\mathrm{GPS})_{\nu\mu}}\bigr),\qquad
T(\mathrm{APS})_{\mu\nu}=\tfrac12\bigl(T(\mathrm{GPS})_{\mu\nu}-\overline{T(\mathrm{GPS})_{\nu\mu}}\bigr)\;},
$$

and the same two identities with $\mathrm{GQS}$, $\mathrm{SQS}$, $\mathrm{AQS}$ in place of $\mathrm{GPS}$, $\mathrm{SPS}$, $\mathrm{APS}$.

*Proof.* The identities are the definitions of the parts of *Symmetric and Antisymmetric Decomposition of the Four General Products*, §*The Method of the Decomposition*, read on the basis pair $(e_\mu,e_\nu)$. In the bilinear case the value of the exchanged product at that pair is $e_\nu\star e_\mu=T(\star)_{\nu\mu}$ for $\star$ equal to $\mathrm{GPA}$ or $\mathrm{GQA}$, and the definition is the half-sum or the half-difference of the two values. In the sesquilinear case the exchanged value is $\overline{e_\nu\star e_\mu}=\overline{T(\star)_{\nu\mu}}$, the coefficientwise conjugation of the value being the second half of the adapted exchange of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the definition is again the half-sum or the half-difference. The general construction of the two splits is *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. The eight identities were recomputed entry by entry and hold exactly.

**Corollary (the reconstruction, entrywise).** The eight identities invert:

$$
\boxed{\;T(\mathrm{GPA})=T(\mathrm{SPA})+T(\mathrm{APA}),\qquad T(\mathrm{GQA})=T(\mathrm{SQA})+T(\mathrm{AQA})\;},
$$

$$
T(\mathrm{GPS})=T(\mathrm{SPS})+T(\mathrm{APS}),\qquad T(\mathrm{GQS})=T(\mathrm{SQS})+T(\mathrm{AQS}),
$$

entry by entry. The four general tables are therefore the sums of the eight part tables, and the twelve tables carry the reconstruction of *Symmetric and Antisymmetric Decomposition of the Four General Products*, §*The Reconstruction, Product by Product*, read on the basis.

**Remark (the four general tables are the independent data).** The eight part tables are read from the four general tables by the eight entrywise formulas above, so the table data of the twelve is the table data of the four. This is the table form of the statement that the twelve products are generated by the four general products and their exchange; it is a relation among the twelve and not a construction of any one of them from another.

### The Ten Distinct Tables

The basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is a real basis, and the coefficientwise conjugation fixes it, $\overline{e_\mu}=e_\mu$. Two of the coincidences that the corpus records on the real forms therefore show up on the basis, at the level of the tables.

**Theorem (the ten distinct tables).** On the four-element basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the twelve tables take exactly ten distinct values. The table of $\mathrm{SQA}$ equals the table of $\mathrm{SPS}$, both the identity table $\delta_{\mu\nu}e_t$, and the table of $\mathrm{AQS}$ equals the table of $\mathrm{APA}$, both the cross-product table. Every other pair of the twelve has distinct tables.

*Proof.* The twelve tables are the twelve arrays of §*The Twelve Tables*; comparing them entry by entry, the only coincidences are the two stated. The first is the equality of the two diagonals $\delta_{\mu\nu}e_t$ computed from $\mathrm{SQA}$ and from $\mathrm{SPS}$; the second is the equality of the two cross-product tables computed from $\mathrm{APA}$ and from $\mathrm{AQS}$, whose $\overline{\vec Q}$ reduces to $\vec Q$ on the real basis elements.

**Corollary (the class separates each coincident pair).** The pair $\mathrm{SQA},\mathrm{SPS}$ has one table and two products, and the pair $\mathrm{APA},\mathrm{AQS}$ likewise. In each pair the two members have the same table and differ in the class: $\mathrm{SQA}$ is $\mathbb{C}$-bilinear and $\mathrm{SPS}$ sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, and $\mathrm{APA}$ is $\mathbb{C}$-bilinear and $\mathrm{AQS}$ sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$. The table and the class together separate the pair, and the table alone does not; this is the caution of §*The Table of a Product*.

**Remark (the separation, on the smallest element off the basis).** The two members of each coincident pair differ as soon as a complex element enters. For the first pair,

$$
\vec e_x\star \vec e_x=e_t \quad\text{for both, while}\quad \vec e_x\star(i\vec e_x)=+ie_t \text{ for } \mathrm{SQA} \text{ and } -ie_t \text{ for } \mathrm{SPS},
$$

and for the second pair,

$$
\vec e_x\star \vec e_y=\vec e_z \quad\text{for both, while}\quad \vec e_x\star(i\vec e_y)=+i\vec e_z \text{ for } \mathrm{APA} \text{ and } -i\vec e_z \text{ for } \mathrm{AQS}.
$$

In each case the bilinear member reads the coefficient $i$ as it stands and the sesquilinear member reads its conjugate $-i$, so the two members differ by the sign of the central imaginary alone. The differences were recomputed at the two elements.

**Remark (the table reading of the ten on the real part).** The fall from twelve tables to ten is the table form of the corpus's statement that the twelve products fall to ten operations on the real part of the space, where the antisymmetric plain bilinear product equals the antisymmetric quaternionic sesquilinear product and the symmetric plain sesquilinear product equals the symmetric quaternionic bilinear product (*Symmetric and Antisymmetric Decomposition of the Four General Products*, §*The Twelve Are Distinct, and Ten on the Real Part*). The basis is the smallest real form, and it already sees the two coincidences; a computation on the basis alone therefore cannot separate the members of either pair, and the class is the datum that restores the distinction. The four general tables, and with them the eight part tables by the entrywise identities, are pairwise distinct and are unaffected by the collapse.

### The Ten Tables and the Twelve Structures

The count of ten is the count of $4\times4$ tables on the four-element basis $e_t,\vec e_x,\vec e_y,\vec e_z$. That basis is a **real** basis of $\mathbb{B}$, and the two colliding pairs are separated as soon as the basis is enlarged to a real basis of the real vector space $\mathbb{B}$, which is eight-dimensional.

**Theorem (the twelve tables of the real basis).** Let $g_0,\dots,g_7$ be the eight-element real basis $g_0=e_t$, $g_1=\vec e_x$, $g_2=\vec e_y$, $g_3=\vec e_z$, $g_{4+\mu}=ie_\mu$. Each of the twelve products is $\mathbb{R}$-bilinear, so each is determined by its $8\times8$ table of values $g_m\star g_n$ in $\mathbb{B}$. The twelve $8\times8$ tables are pairwise distinct.

*Proof.* Each product is additive in each variable, and each of the two scalar rules reads the coefficients $\mathbb{R}$-linearly — the bilinear rule plainly, the sesquilinear rule through the conjugation, which is $\mathbb{R}$-linear; so each product is $\mathbb{R}$-bilinear and is determined by its values on the $8\times8$ pairs of the real basis. For distinctness, every pair of the twelve other than the two collisions already has distinct $4\times4$ tables by §*The Ten Distinct Tables*, so only the two collisions have to be separated; and with the two displayed pairs,

$$
\vec e_x\star \vec e_x=e_t \ \text{for both}\ \mathrm{SQA}\ \text{and}\ \mathrm{SPS},
\qquad
\vec e_x\star(i\vec e_x)=+ie_t\ \text{for}\ \mathrm{SQA}\ \text{and}\ -ie_t\ \text{for}\ \mathrm{SPS},
$$

$$
\vec e_x\star \vec e_y=\vec e_z \ \text{for both}\ \mathrm{APA}\ \text{and}\ \mathrm{AQS},
\qquad
\vec e_x\star(i\vec e_y)=+i\vec e_z\ \text{for}\ \mathrm{APA}\ \text{and}\ -i\vec e_z\ \text{for}\ \mathrm{AQS},
$$

the bilinear member carrying the coefficient $i$ as it stands and the sesquilinear member carrying its conjugate $-i$. Hence the two members of each colliding pair have distinct $8\times8$ tables, and the twelve are pairwise distinct. The two displayed entries were recomputed at the pairs $(\vec e_x,i\vec e_x)$ and $(\vec e_x,i\vec e_y)$.

**Corollary (ten tables, twelve structures).** The count of distinct tables is ten on the four-element basis and twelve on the eight-element real basis, while the count of structures is **twelve** in both readings. A structure is a product on the complex space, and its datum is the table **together with the class**: the two members of each colliding pair of $4\times4$ tables have different classes, one $\mathbb{C}$-bilinear and one sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, so the twelve pairs (table, class) are distinct. The ten is the count that forgets the class; it is equivalently the count of distinct products restricted to the real part of the space, which is the count of *Symmetric and Antisymmetric Decomposition of the Four General Products*, §*The Twelve Are Distinct, and Ten on the Real Part*. Read on the eight-element real basis the class is no longer needed to separate the twelve, and the $8\times8$ tables are the ordinary multiplication tables of the twelve as real multiplications on the eight-dimensional real space $\mathbb{B}$.

### What the Tables Decide

**The class.** The last letter of the code is the class, and the tables exhibit it: the six tables of the codes ending in $\mathrm{A}$ are read by the bilinear rule and the six ending in $\mathrm{S}$ by the sesquilinear rule, and the two readings of one table differ whenever the second factor has a non-real coefficient.

**The unit.** A right unit of $\star$ is an element $e$ with $T(\star)_{\mu e}=e_\mu$ for every $\mu$, and a left unit one with $T(\star)_{e\nu}=e_\nu$ for every $\nu$; the tables therefore exhibit the units. The identity column of $T(\mathrm{GPA})$ reproduces the basis, so $e_t$ is a two-sided unit; the identity column of $T(\mathrm{GPS})$ reproduces the basis and the identity row is its negation, so $e_t$ is a right unit and not a left one; the identity row of $T(\mathrm{GQA})$ reproduces the basis and the identity column is its negation, so $e_t$ is a left unit and not a right one; and $T(\mathrm{GQS})$ has neither, its identity row and column both negating the basis. The one-sided units of the four general products are read in *The Four General Products and Their Relations over the Biquaternion Algebra* and *Introduction to the General Plain Sesqualgebra*, §*The Right Unit*.

**The commutativity and the alternation.** A table for a $\mathbb{C}$-bilinear product is commutative exactly when it is symmetric, $T_{\mu\nu}=T_{\nu\mu}$, and alternating exactly when it is antisymmetric with zero diagonal; the tables of $\mathrm{SPA}$ and $\mathrm{SQA}$ are symmetric and those of $\mathrm{APA}$ and $\mathrm{AQA}$ are antisymmetric with zero diagonal, as the symmetries of the parts require. For a sesquilinear product the corresponding symmetries are read up to the coefficientwise conjugation, $T_{\mu\nu}=\overline{T_{\nu\mu}}$ for the conjugate-commutative blocks $\mathrm{SPS}$ and $\mathrm{SQS}$, and $T_{\mu\nu}=-\overline{T_{\nu\mu}}$ for the conjugate-alternating blocks $\mathrm{APS}$ and $\mathrm{AQS}$, the latter two with vanishing diagonal.

**What the tables do not decide.** The table of a product places the sixteen basis products and nothing else; the associativity, the Jacobi and the Jordan identities, the zero divisors, the ideals and the representations of the product are not read off the table without the extension, and even with the extension they are the matter of the structure articles. *Symmetric and Antisymmetric Decomposition of the Four General Products* owns the laws and the failures, and the twelve structure articles own the objects.

---

## Summary

Each of the twelve products carried by the complex space of the biquaternion algebra is additive in each argument and obeys one of two scalar rules, so it is fixed by its sixteen values on the pairs of basis elements. Those values are the multiplication table of the product, and the table together with the class — $\mathbb{C}$-bilinear for a code ending in $\mathrm{A}$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ for a code ending in $\mathrm{S}$ — determines the product and is determined by it. The table alone does not determine the product, and the class is not decoration: two of the twelve pairs of products share a $4\times4$ table on the real basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and are separated by the class alone.

The twelve tables are written out, one to a product, in the three groups general, symmetric, antisymmetric. Their entries are $0$ or a basis element up to sign; the central imaginary $i$ occurs in none, because the four-element basis is real and closed under the conjugations up to sign. The table of a symmetric or an antisymmetric part is the entrywise symmetrisation or antisymmetrisation of the table of its parent, under the interchange in the two $\mathbb{C}$-bilinear families and under the interchange followed by the coefficientwise conjugation in the two sesquilinear families, so the four general tables are the independent table data and the reconstruction of each general product from its two parts holds entry by entry.

On the four-element basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the twelve tables take ten distinct values. The table of $\mathrm{SQA}$ equals the table of $\mathrm{SPS}$, both the identity table, and the table of $\mathrm{AQS}$ equals the table of $\mathrm{APA}$, both the cross-product table; every other pair is distinct. The two collisions are the table form of the fall of the twelve products to ten operations on the real part, and each pair is separated by the class, or by the sign of the central imaginary at the smallest complex element off the basis. On the eight-element real basis $g_0,\dots,g_7=\{e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ the twelve tables are pairwise distinct, the two collisions above being separated there by the entries carrying $i$. The count of **structures** is twelve in both readings: a structure is a product on the complex space, its datum is the table together with the class, and the two members of each colliding pair have different classes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_t,\vec e_x,\vec e_y,\vec e_z$, central imaginary $i$ |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion, its scalar and vector parts |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | the natural, the coefficientwise and the Hermitian conjugation |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector, $e_\mu^{\natural}=e_\mu^{*}=\varepsilon_\mu e_\mu$ |
| $T(\star)$ | the multiplication table of $\star$, $T(\star)_{\mu\nu}=e_\mu\star e_\nu$ |
| $\star_T$, the bilinear reading | $\tilde Q_1\star_T\tilde Q_2=\sum_{\mu,\nu}Q_{1,\mu} Q_{2,\nu} T_{\mu\nu}$ |
| the sesquilinear reading | $\tilde Q_1\star_T\tilde Q_2=\sum_{\mu,\nu}Q_{1,\mu}\overline{Q_{2,\nu}}T_{\mu\nu}$ |
| the class | $\mathbb{C}$-bilinear for a code ending in $\mathrm{A}$, sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ for one ending in $\mathrm{S}$ |
| $\mathrm{GPA}$, $\mathrm{GQA}$ | the two general $\mathbb{C}$-bilinear products, $\tilde Q_1\tilde Q_2$ and $\tilde Q_1^{\natural}\tilde Q_2$ |
| $\mathrm{GPS}$, $\mathrm{GQS}$ | the two general sesquilinear products, $\tilde Q_1\tilde Q_2^{*}$ and $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
| $\mathrm{SPA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{SQS}$ | their four symmetric parts |
| $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$ | their four antisymmetric parts |
| $T_{\mu\nu}=T_{\nu\mu}$ | the table of a commutative $\mathbb{C}$-bilinear product |
| $T_{\mu\nu}=\overline{T_{\nu\mu}}$ | the table of a conjugate-commutative sesquilinear product |

## Further Reading

- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve products, their formulas and laws, the method of the decomposition and the reconstruction product by product; the tables of the present article are those products read on the basis.
- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html), for the names, the three-letter codes and the structures the twelve define, and for what the last letter claims.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four general products on the coordinates.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), §*The Multiplication Table* and §*Bilinearity and the Determination by the Table*, for the table of $\mathrm{GPA}$ and the determination of a bilinear product by its table.
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), §*The Multiplication Table*, and [Introduction to the Symmetric Plain Sesqualgebra](introduction-to-the-symmetric-plain-sesqualgebra.html), §*The Multiplication Table of the Basis*, for the tables of $\mathrm{GPS}$ and $\mathrm{SPS}$ and the table form of a sesquilinear product.
- [The Symmetric and Antisymmetric Parts of an Algebra Product](the-symmetric-and-antisymmetric-parts-of-an-algebra-product.html) and [The Symmetric and Antisymmetric Parts of a Sesqualgebra Product](the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.html), for the two exchanges and the two splits whose entrywise reading is the content of §*The Table of a Part Is the Entrywise Part*.
- The twelve structure articles — [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra-of-quaternioid.html), [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), [Introduction to the General Quaternionic Sesqualgebra](introduction-to-the-general-quaternionic-sesqualgebra.html), and the eight introductions to the symmetric and antisymmetric algebras and sesqualgebras of biquaternions — each for the sixteen basis products of its own structure.
- [The Realification and the Effect of the Change of Scalars](the-realification-and-the-effect-of-the-change-of-scalars.html), for the reading of the twelve over $\mathbb{R}$ and the fall to ten operations on the real forms.
- [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html), for the group of the involutions, the conjugations and the remarkable subspaces used in the conventions above.
