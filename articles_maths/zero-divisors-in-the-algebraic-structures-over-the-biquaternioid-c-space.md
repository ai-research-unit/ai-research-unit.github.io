# __Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space__

## Introduction

Let $\star$ be a product on the biquaternion algebra $\mathbb{B}$. A nonzero $\tilde Q\in\mathbb{B}$ is a **zero divisor of $\star$** when it kills a nonzero partner: when $\tilde Q\star\tilde Q_1=0$ or $\tilde Q_1\star\tilde Q=0$ for some nonzero $\tilde Q_1$. The first case makes it a left zero divisor, the second a right zero divisor, and an element of both kinds a two-sided zero divisor.

**The twelve names.** The algebra carries twelve products, so the generic definition poses twelve questions; this article answers them once for all twelve. Each of the twelve products has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the first slot, $\mathrm P$ plain and $\mathrm Q$ quaternionic; the third is the family, $\mathrm A$ the algebra over $\mathbb{C}$ and $\mathrm S$ the sesqualgebra over $\mathbb{C}$. The twelve are read in the four families and the three operations of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*,

| the operation | the plain algebra | the plain sesqualgebra | the quaternionic algebra | the quaternionic sesqualgebra |
|---|---|---|---|---|
| the general | $\mathrm{GPA}$ | $\mathrm{GPS}$ | $\mathrm{GQA}$ | $\mathrm{GQS}$ |
| the symmetric | $\mathrm{SPA}$ | $\mathrm{SPS}$ | $\mathrm{SQA}$ | $\mathrm{SQS}$ |
| the antisymmetric | $\mathrm{APA}$ | $\mathrm{APS}$ | $\mathrm{AQA}$ | $\mathrm{AQS}$ |

and every table of the article follows the new order: the four general structures first, then their four symmetric parts, then their four antisymmetric parts; and inside each group the plain algebra, then the plain sesqualgebra, then the quaternionic algebra, then the quaternionic sesqualgebra.

**Scope and owners.** The general vocabulary, the zero divisor, the annihilator, the idempotent and the nilpotent stated once for a general product, is *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*. The plain-product criterion and the classification of the cone's elements are *Zero Divisors of the Biquaternion Algebra*. The four general products and their eight parts are *The 12 Products of the Biquaternioid Complex Space* and *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, whose three-letter code is used throughout. The eight criteria of the derived structures stay owned by their articles, cited one by one in §*The Twelve Structures and the Cone*. The property table and the four unit entries are *Comparison Between the Four General Products*; the four idempotent sets are *Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*; the four root problems are *Square Roots of Minus One, Zero and Plus One in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* and *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*; the annihilators of one element are *Annihilators in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, and the square-zero sets are *Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*. The cone's own geometry, topology and ideals, which name no product, are gathered in §*The Cone in the Wider Mathematics*.

## The Zero-Divisor Cone

**Definition.** The **zero-divisor cone** is the vanishing set of the norm,

$$
\mathcal{C}=\{\tilde Q\in\mathbb{B}:\mathrm{Norm}(\tilde Q)=0\} ,
$$

the **generic norm** of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*, after *Conventions in Mathematics* §*The form convention and the norm convention*, the norm of the statement at hand. This article instantiates it by the reduced norm, $\mathrm{Norm}(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$. It is the common zero-divisor set of the four general products.

**Definition.** A subset of $\mathbb{B}$ is a **complex cone** when it contains $\lambda\tilde Q$ for every $\tilde Q$ it contains and every $\lambda\in\mathbb{C}$. Its **apex** is the origin.

### The Cone Is the Complement of the Group of Units

The elements of $\mathbb{B}$ fall into three classes. The invertible elements of the plain product, the units, are exactly those of non-vanishing norm, $\mathbb{B}^{\times}=\{\tilde Q:\mathrm{Norm}(\tilde Q)\neq0\}$ (*Zero Divisors of the Biquaternion Algebra*); the origin is never a zero divisor; and the remaining elements are the zero divisors of the four general products. Hence

$$
\mathbb{B}=\{0\}\cup\mathbb{B}^{\times}\cup\bigl(\mathcal{C}\setminus\{0\}\bigr) .
$$

So an element is a unit exactly when it lies off the cone, and a zero divisor exactly when it lies on the cone and not at the apex. The cone is the complement of the group of units, and the zero-divisor set together with the origin is that complement read as the cone.

## The Twelve Structures and the Cone

The four general products split into the twelve structures through the class-preserving exchange (*The 12 Products of the Biquaternioid Complex Space*). A zero divisor names its product, so each of the twelve carries a zero-divisor set of its own; the table of §*Results* records them, one family to a block and, inside a block, the general structure first, the product written by its defining formula.

**Theorem (the cone is the mark of the four general products).** Among the twelve structures the zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$ exactly for the four general structures $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQA}$ and $\mathrm{GQS}$, and for no other. The eight derived sets are strictly larger: the six antisymmetric and scalar-valued symmetric structures $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$ and $\mathrm{AQS}$ have the whole punctured space, and the two remaining symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_t=0\}\cup\mathcal{C})\setminus\{0\}$.

The twelve structures are read one by one below; each names the product, its zero-divisor set and the reason. The four general rows are read together in §*Results*.

**Corollary (the cone is the common core).** The punctured cone $\mathcal{C}\setminus\{0\}$ is contained in the zero-divisor set of each of the twelve structures, and it is equal to the set of exactly four of them, the four general products.

*Proof.* Every row of the table of §*Results* contains the cone: the four general rows equal it, the rows of $\mathrm{SPA}$ and $\mathrm{SQS}$ contain it by their second clause, and the remaining six rows are the whole punctured space.

Two consequences follow. First, because the cone lies in every set, an element of vanishing norm admits an annihilating factor in all twelve products, and the cone is the largest subset on which the twelve agree; the converse fails, since the derived sets are strictly larger. Second, the ring-theoretic picture breaks on the derived structures: the unit $\vec e_x$, whose norm is $1$, is a zero divisor of $\mathrm{SPA}$ and of $\mathrm{SQS}$, because $\vec e_x\bullet \vec e_y=\tfrac12(\vec e_x \vec e_y+\vec e_y \vec e_x)=0$ for the Jordan product and $\vec e_x\star \vec e_y=0$ for the symmetric quaternionic sesquilinear product, and it is invertible in the algebra. A zero divisor need not be a non-unit unless the product has a two-sided unit.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde P\tilde Q$, its conjugate is $\tilde P^{\natural}$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_tQ_t+(\vec P,\vec Q) .
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the scalar of the central element $\tilde P^{\natural}\tilde P$. Write $\tilde P=P_te_t+\vec P$ with $\vec P=P_x\vec e_x+P_y\vec e_y+P_z\vec e_z$ and $\tilde P^{\natural}=P_te_t-\vec P$. Since $\vec e_\lambda \vec e_\rho+\vec e_\rho \vec e_\lambda=0$ for $\lambda \neq \rho$ and $\vec e_\lambda^{2}=-e_t$, the vector part squares to $\vec P^{2}=-(P_x^{2}+P_y^{2}+P_z^{2})e_t$, so

$$
\tilde P^{\natural}\tilde P=(P_te_t-\vec P)(P_te_t+\vec P)=P_t^{2}e_t-\vec P^{2}=(P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2})e_t ,
$$

and its scalar is the norm $\mathrm{Norm}(\tilde P)=P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2}$.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The cone is the vanishing set of the norm, $\mathcal{C}=\{\tilde P:P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2}=0\}$, one complex quadric in the four coordinates, of complex dimension three. On $\mathcal{C}$ the product $\tilde P\tilde P^{\natural}$ vanishes with $\tilde P^{\natural}\neq0$, so every nonzero element of the cone is a zero divisor; off $\mathcal{C}$ the norm is nonzero and $\tilde P^{-1}=\tilde P^{\natural}/\mathrm{Norm}(\tilde P)$ is a two-sided inverse.

The units are the elements off the cone, $\mathbb{B}^{\times}=\{\tilde P:\mathrm{Norm}(\tilde P)\neq0\}$, and this is the one structure of the twelve whose invertible elements form a genuine group, with the two-sided unit $e_t$ and the two-sided inverse $\tilde P^{-1}=\tilde P^{\natural}/\mathrm{Norm}(\tilde P)$; the complement of the zero-divisor set is that group together with the origin, $\mathbb{B}\setminus(\mathcal{C}\setminus\{0\})=\mathbb{B}^{\times}\cup\{0\}$.

### $\mathrm{GPS}$, the general plain sesqualgebra

The product is $\tilde P\tilde Q^{*}$, its conjugate is $\tilde P^{*}$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_t\overline{Q_t}+(\vec P,\overline{\vec Q}) .
$$

The norm is the form at the two equal arguments, $\langle\tilde P\rangle_{*}=\mathrm{Form}(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P\tilde P^{*})=|P_t|^{2}+|\vec P|^{2}$, definite.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The definite norm $\langle\cdot\rangle_{*}$ vanishes at the origin alone and cuts no cone. Put $\tilde Q=\tilde Y^{*}$; then $\tilde P\tilde Q^{*}=\tilde P\tilde Y$ is the plain product, whose form is $\mathrm{Sc}(\tilde P^{\natural}\tilde Y)$ and whose scalar at the two equal arguments is the reduced norm $\mathrm{Norm}(\tilde P)=P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2}$ of §*The General Plain Algebra (GPA)*. The criterion is therefore $\mathrm{Norm}(\tilde P)=0$, the witness is $\tilde Q=(\tilde P^{\natural})^{*}$, since $\tilde P\tilde Q^{*}=\tilde P\tilde P^{\natural}=\mathrm{Norm}(\tilde P)e_t=0$ on the cone.

The element $e_t$ is a right unit alone, $e_t\star\tilde Q=\tilde Q^{*}$, and an element off the cone has the two-sided solution $(\tilde P^{-1})^{*}$ of the inverse equations; the invertible elements are the complement of the cone and, the product being non-associative, they form no group.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde P^{\natural}\tilde Q$, its conjugate is $\tilde P^{\natural}$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_tQ_t+(\vec P,\vec Q) .
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the scalar of the central element $\tilde P^{\natural}\tilde P$ of §*The General Plain Algebra (GPA)*, $\mathrm{Norm}(\tilde P)=P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2}$; the natural conjugation sends $\vec P$ to $-\vec P$, so $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$. Here the norm is the criterion.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The cone is the quadric $\mathcal{C}$ of §*The General Plain Algebra (GPA)*. If $\mathrm{Norm}(\tilde P)=0$ the partner $\tilde Q=\tilde P^{\natural}$ annihilates, since $\tilde P^{\natural}\tilde P^{\natural}=\mathrm{Norm}(\tilde P^{\natural})e_t=0$; conversely, multiplying $\tilde P^{\natural}\tilde Q=0$ on the left by $\tilde P$ gives $\mathrm{Norm}(\tilde P)\tilde Q=0$.

The element $e_t$ is a left unit alone, and an element off the cone has the two-sided solution $(\tilde P^{-1})^{\natural}$ of the inverse equations; the invertible elements are the complement of the cone, and since the product is not associative they form no group.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra

The product is $\tilde P^{\natural}\tilde Q^{*}$, its conjugates are $\natural$ and $*$, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_t\overline{Q_t}-(\vec P,\overline{\vec Q}) .
$$

The norm is the form at the two equal arguments, $\langle\tilde P\rangle_{\natural*}=\mathrm{Form}(\tilde P,\tilde P)=\mathrm{Sc}(\tilde P^{\natural}\tilde P^{*})=|P_t|^{2}-|\vec P|^{2}$, indefinite.

**The zero-divisor set is the punctured cone $\mathcal{C}\setminus\{0\}$.** The indefinite norm $\langle\cdot\rangle_{\natural*}$ vanishes on a real cone of its own, distinct from $\mathcal{C}$. Put $\tilde Q=\tilde Y^{*}$; then $\tilde P^{\natural}\tilde Q^{*}=\tilde P^{\natural}\tilde Y$ is the plain product of $\tilde P^{\natural}$, whose form is $\mathrm{Sc}(\tilde P\tilde Y)$ and whose scalar at the two equal arguments is $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$ of §*The General Plain Algebra (GPA)*. The criterion is therefore $\mathrm{Norm}(\tilde P)=0$, the witness is $\tilde Q=(\tilde P^{\natural})^{*}$.

There is no unit on either side, and an element off the cone has the two-sided solution $(\tilde P^{-1})^{\natural*}$ of the inverse equations; the elements off the cone satisfy both inverse equations, but they form no group, and the structure carries no unit.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, the symmetrisation of the plain product, so its form is the same,

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_tQ_t+(\vec P,\vec Q) ,
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the reduced norm $\mathrm{Norm}(\tilde P)=P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2}$ of §*The General Plain Algebra (GPA)*.

**The zero-divisor set is the enlarged set**

$$
\bigl(\{P_t=0\}\cup\mathcal{C}\bigr)\setminus\{0\} .
$$

Read the Jordan product from the quaternion table, $\tilde P\circ\tilde Q=P_tQ_te_t+P_t\vec Q+Q_t\vec P-(\vec P,\vec Q)e_t$. If $P_t\neq0$ the vector part forces $\vec Q=-(Q_t/P_t)\vec P$, and the scalar part becomes $Q_t\,\mathrm{Norm}(\tilde P)/P_t$; a nonzero annihilator therefore exists exactly when $\mathrm{Norm}(\tilde P)=0$, and it is then $\tilde P^{\natural}$. If $P_t=0$ and $\tilde P\neq0$, any nonzero $\vec Q$ orthogonal to $\vec P$ annihilates.

The plane $P_t=0$ of the pure elements is a second family beside the cone.

The unit $e_t$ is two-sided, as for $\mathrm{GPA}$, and the invertible elements are again the elements of non-vanishing norm; but the product is not associative, so they form no group, and the complement of the zero-divisor set, $\{P_t\neq0,\ \mathrm{Norm}(\tilde P)\neq0\}\cup\{0\}$, is not the invertible set: the pure element $\vec e_x$ is a zero divisor and invertible at once, $\vec e_x\bullet(-\vec e_x)=e_t$, the failure of *zero divisor if and only if non-unit*.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra

The product is $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$, central, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_t\overline{Q_t}+(\vec P,\overline{\vec Q}) ,
$$

The norm is the form at the two equal arguments, $\langle\tilde P\rangle_{*}=\mathrm{Form}(\tilde P,\tilde P)=|P_t|^{2}+|\vec P|^{2}$, definite.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** The value is the central read of the form, $\mathrm{Sc}(\tilde P\tilde Q^{*})e_t$. The norm $\langle\cdot\rangle_{*}$ is definite and does not decide; the equation $\mathrm{Sc}(\tilde P\tilde Q^{*})=0$ is one complex linear equation in the conjugated components of $\tilde Q$, and its solutions fill a complex hyperplane.

There is no unit, the values lying in the centre, so there is no group of units and the complement of the zero-divisor set, the whole punctured space, is the origin alone.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$, central, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_tQ_t+(\vec P,\vec Q) ,
$$

The norm is the form at the two equal arguments, $\mathrm{Norm}(\tilde P)=\mathrm{Form}(\tilde P,\tilde P)$, the reduced norm $\mathrm{Norm}(\tilde P)=P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2}$.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** The value is the central read of the form, $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)e_t$; check on $\tilde P=\tilde Q=\vec e_x$: $\tilde P^{\natural}\tilde P=e_t$, of scalar $1=0+1$. The form is nondegenerate, its matrix being the identity in the four coordinates, so for $\tilde P\neq0$ the equation $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=0$ is one complex linear equation in the four components of $\tilde Q$ and its solutions fill a complex hyperplane of nonzero vectors.

There is no unit — the values lie in the centre and $e_t$ acts as $\langle e_t,\tilde Q\rangle_{\natural}e_t=Q_te_t$, not as an identity — so there is no group of units and the complement of the zero-divisor set, the whole punctured space, is the origin alone.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra

The product is $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$, central, and the form of the product is

$$
\mathrm{Form}(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=P_t\overline{Q_t}-(\vec P,\overline{\vec Q}) ,
$$

The norm is the form at the two equal arguments, $\langle\tilde P\rangle_{\natural*}=\mathrm{Form}(\tilde P,\tilde P)=|P_t|^{2}-|\vec P|^{2}$, indefinite.

**The zero-divisor set is the enlarged set $\left(\{P_t=0\}\cup\mathcal{C}\right)\setminus\{0\}$.** Put $\tilde Y=\tilde Q^{*}$; the two conjugations commute and the product becomes the Jordan product of $\tilde P^{\natural}$ with $\tilde Y$,

$$
\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})=\tfrac12(\tilde P^{\natural}\tilde Y+\tilde Y\tilde P^{\natural}).
$$

By §*The Symmetric Plain Algebra (SPA)* the criterion is read on $\tilde P^{\natural}$: the natural conjugation leaves $P_t$ unchanged and $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$, so the condition is $P_t=0$ or $P_t^{2}+P_x^{2}+P_y^{2}+P_z^{2}=0$, (*Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*).

There is no unit, both symmetrised terms conjugating a factor, so $e_t$ acts as $\tilde Q^{*}$ on one side and $\tilde Q^{\natural}$ on the other; the complement of the enlarged zero-divisor set is $\{P_t\neq0,\ \mathrm{Norm}(\tilde P)\neq0\}\cup\{0\}$, which is no group of units.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$. It is alternating, so at the two equal arguments it vanishes, $\tilde P\star\tilde P=\tfrac12(\tilde P\tilde P-\tilde P\tilde P)=0$; there is no form there and no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** Every nonzero element is annihilated by itself.

There is no unit, the values lying in the vector subspace, so there is no group of units and the complement of the zero-divisor set — the whole punctured space — is the origin alone.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra

The product is $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})=\mathrm{Vect}(\tilde P\tilde Q^{*})$. At the two equal arguments it gives the vector part of $\tilde P\tilde P^{*}$, not a scalar; there is no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** Off the cone, $\mathrm{Norm}(\tilde P)\neq0$ and $\tilde Q=(\tilde P^{-1})^{*}$ gives $\tilde P\tilde Q^{*}=e_t$, whose vector part is zero; on the cone, $\tilde Q=\tilde P^{\natural}$ gives $\tilde P\tilde Q^{*}=0$. Every nonzero element is a zero divisor.

There is no unit, the values lying in the vector subspace, so there is no group of units and the complement of the zero-divisor set is the origin alone.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$. It is alternating, $\tilde P\star\tilde P=\tfrac12(\tilde P^{\natural}\tilde P-\tilde P^{\natural}\tilde P)=0$, so at the two equal arguments there is no form and no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** Every nonzero element is annihilated by itself.

There is no unit, the values lying in the vector subspace, so there is no group of units and the complement of the zero-divisor set is the origin alone.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra

The product is $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})=\vec P\times\overline{\vec Q}$. At the two equal arguments it gives $\vec P\times\overline{\vec P}$, a pure vector; there is no norm.

**The zero-divisor set is the whole punctured space $\mathbb{B}\setminus\{0\}$.** If $\vec P\neq0$, take $\tilde Q=\overline{\tilde P}$: its vector part $\overline{\vec P}$ is parallel to $\vec P$, and a cross product of parallel vectors vanishes. If $\vec P=0$ the element is central and the product vanishes for every $\tilde Q$. Every nonzero element is a zero divisor.

There is no unit, the values lying in the vector subspace, so there is no group of units and the complement of the zero-divisor set is the origin alone.

## Results

The four general products share one zero-divisor set, the punctured cone $\mathcal{C}\setminus\{0\}$ of §*The Zero-Divisor Cone*. The twelve structures are tabulated against it, the four that coincide are separated out, and the cone itself is read in coordinates and in its two families.

### The Twelve Zero-Divisor Sets

Read against the cone $\mathcal{C}$ and against the whole space, the twelve sets are

| family | structure | the product | the zero-divisor set |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde P\tilde Q$ | $\mathcal{C}\setminus\{0\}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\tilde P\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\tilde P^{\natural}\tilde Q$ | $\mathcal{C}\setminus\{0\}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\tilde P^{\natural}\tilde Q^{*}$ | $\mathcal{C}\setminus\{0\}$ |
| the plain algebra | $\mathrm{SPA}$ | $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | $(\{P_t=0\}\cup\mathcal{C})\setminus\{0\}$ |
| the plain sesqualgebra | $\mathrm{SPS}$ | $\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic algebra | $\mathrm{SQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic sesqualgebra | $\mathrm{SQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $(\{P_t=0\}\cup\mathcal{C})\setminus\{0\}$ |
| the plain algebra | $\mathrm{APA}$ | $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| the plain sesqualgebra | $\mathrm{APS}$ | $\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic algebra | $\mathrm{AQA}$ | $\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | $\mathbb{B}\setminus\{0\}$ |
| the quaternionic sesqualgebra | $\mathrm{AQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde P^{*}})$ | $\mathbb{B}\setminus\{0\}$ |

The four general products have one and the same set, the punctured cone. The six structures $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$ and $\mathrm{AQS}$ have the whole punctured space. The two remaining symmetric structures $\mathrm{SPA}$ and $\mathrm{SQS}$ have the enlarged set $(\{Q_t=0\}\cup\mathcal{C})\setminus\{0\}$. The cone is therefore the zero-divisor set of exactly four of the twelve structures, and it is contained in all twelve, so that it is the common core of the twelve. The theorem below and §*The Twelve Structures and the Cone* prove the table, and the sections that follow read its consequences.

### The Four General Products Coincide

**Theorem (the four zero-divisor sets coincide, and they are the cone).** For the four general products the zero-divisor sets coincide. A nonzero element $\tilde P$ is a left, a right or a two-sided zero divisor of one of the four general products exactly when $\mathrm{Norm}(\tilde P)=0$, that is exactly when $\tilde P$ lies on the cone $\mathcal{C}$, and then it is a zero divisor of all four, on both sides. In symbols,

$$
\{\tilde P\neq0:\tilde P\text{ admits an annihilating factor in }\star\}=\mathcal{C}\setminus\{0\} \qquad\text{for each of the four general products }\star .
$$

*Proof.* Read each product in the model $\mathsf{M}_2$. Each general product is the plain product with a conjugation in one or both slots, a bijection of $\mathbb{B}$; a bijection in a slot identifies the kernel of the left multiplication by $\tilde P$ with the kernel of the plain left multiplication by $\tilde P$ or by $\tilde P^{\natural}$. Now $\mathsf{M}_2(\tilde P^{\natural})$ is $\mathsf{M}_2(\tilde P)$ up to conjugation by a fixed invertible matrix, and $\mathrm{Norm}(\tilde P^{\natural})=\mathrm{Norm}(\tilde P)$, so the plain left multiplication is singular exactly when $\mathrm{Norm}(\tilde P)=0$. In each case the deciding condition is the vanishing of the norm, read from the singularity of $\mathsf{M}_2(\tilde P)$ or of its conjugate $\mathsf{M}_2(\tilde P^{\natural})$. For the cone itself and for a nonzero $\tilde P$ with $\mathrm{Norm}(\tilde P)=0$, the witness is the natural conjugate, $\tilde P\tilde P^{\natural}=\tilde P^{\natural}\tilde P=\mathrm{Norm}(\tilde P)e_t=0$, on both sides.

The four conditions are thus one condition, and the reason is structural. Each general product is the plain product with a conjugation in one or both slots; each conjugation is a bijection that either fixes or conjugates the norm; and the norm is the single invariant that decides the invertibility of the element. Composing a one-sided multiplication with a bijection changes its kernel by the bijection, so the singularity is transported from product to product.

| product | left condition | right condition | the set |
|---|---|---|---|
| $\mathrm{GPA}$, $\tilde P\tilde Q$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GPS}$, $\tilde P\tilde Q^{*}$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GQA}$, $\tilde P^{\natural}\tilde Q$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |
| $\mathrm{GQS}$, $\tilde P^{\natural}\tilde Q^{*}$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathrm{Norm}(\tilde P)=0$ | $\mathcal{C}\setminus\{0\}$ |

The four rows are identical, and that is the theorem. **The word is *coincide*, not *independent*.** The zero divisor is defined by an equation that names a product, so the notion belongs to the product and the four products are four definitions, not one. What the theorem says is that in the biquaternion algebra the four definitions select one and the same subset of $\mathbb{B}$; it does not say that they must, and it does not extend to the eight derived structures of §*The Twelve Structures and the Cone*.

### The Cone in Coordinates and Its Apex

Written on the coordinates, the cone common to the four general products is one complex equation in the four complex coordinates,

$$
Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0 .
$$

**Proposition (the cone and its singular point).** The set $\mathcal{C}$ is a complex cone with apex at the origin, and the origin is its only singular point. Away from the apex it is a complex manifold of complex dimension three, hence a real manifold of real dimension six.

*Proof.* The norm is homogeneous of degree two, $\mathrm{Norm}(\lambda\tilde Q)=\lambda^{2}\mathrm{Norm}(\tilde Q)$, so its vanishing set is a cone. One complex equation in four complex unknowns cuts a complex hypersurface of $\mathbb{C}^{4}$, of complex dimension three wherever its gradient does not vanish; the gradient of $\mathrm{Norm}$ is proportional to $(Q_t,Q_x,Q_y,Q_z)$, which vanishes only at the origin, so the complement of the apex is smooth of complex dimension three. The origin is singular because the only term of $\mathrm{Norm}$ of degree two is the leading term, so the tangent cone at the origin is $\mathcal{C}$ itself and not a hyperplane.

### The Two Families

The scalar part cuts the cone into two families, and the criterion and the square read differently on each.

**Definition.** An element is **pure** when its scalar part vanishes, $Q_t=0$, and **non-pure** when $Q_t\neq0$.

On a pure element the scalar square $Q_t^{2}$ drops out of the criterion, which becomes $(\vec Q,\vec Q)=0$; on a non-pure element the criterion is the full vanishing of the norm.

| | pure, $Q_t=0$ | non-pure, $Q_t\neq0$ |
|---|---|---|
| criterion | $(\vec Q,\vec Q)=0$ | $\mathrm{Norm}(\tilde Q)=0$ |
| square in the plain product | $\tilde Q^{2}=0$ | $\tilde Q^{2}=2Q_t\tilde Q$ |
| structure | the nilpotents | the complex multiples of the nontrivial idempotents |
| real dimension | $4$ | $6$ |

The square of a pure zero divisor vanishes because $\tilde Q^{2}=-(Q_x^{2}+Q_y^{2}+Q_z^{2})e_t=0$; the square of a non-pure one satisfies $\tilde Q^{2}=2Q_t\tilde Q-\mathrm{Norm}(\tilde Q)e_t=2Q_t\tilde Q$, and the element $\tilde\Pi=\tilde Q/(2Q_t)$ is then a nontrivial idempotent of the plain product. The two families are read in the remarkable subspaces in *Introduction to the Remarkable Subspaces*: the pure ones fill the nilpotent cone of the vector subspace, the non-pure ones the double cones of the two Hermitian subspaces, and a generic point of the cone lies in none of the remarkable subspaces.

## The Cone in the Wider Mathematics

The results above are the cone read inside the grid. The corpus proves five further statements about the cone that name no product, and they are gathered here because they are the cone's own geometry and topology rather than a property of any of the twelve.

**One cone among four null sets.** The space carries four forms — the two bilinear $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ and the two sesquilinear $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ — and their null sets have four different shapes. $\langle\cdot,\cdot\rangle$ has the complex cone $\sum_\mu\varepsilon_\mu Q_\mu^{2}=0$ of real dimension six, $H$ is positive definite and has the origin alone, $\langle\cdot\rangle_{*}$ has the zero-divisor cone $\mathcal{C}$ of real dimension six, and $K$ is indefinite and has the **Krein cone** $\mathcal{K}$ of real dimension seven (*The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, *The Krein Level Sets and the Hyperbolic Structure*). The two dimension-six null sets do not agree, so the cone of this article is the null set of $\langle\cdot,\cdot\rangle_{\natural}$ and of no other form.

On the remarkable subspaces the four null sets are cut to two shapes (*Remarkable Subspaces and the Four Forms*). On the centre all four vanish at the origin alone. On the vector subspace $B$ and $N$ vanish on the complex cone of real dimension four, the pure zero divisors, while $H$ and $K$ vanish at the origin. On the quaternion subspace $B$ and $K$ vanish on the real light cone of real dimension three. On each sector the two indefinite forms $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ vanish on the light cone of real dimension three, while the two definite forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ vanish at the origin. The cone's real dimension therefore drops from six to four to three as the subspace shrinks, and at every stage the cone is carried by the indefinite forms alone.

**The cone as a topological space.** The full cone is contractible, its apex is its only singular point, and its link, the intersection with the unit sphere $S^{7}_{E}$, is a closed connected real five-manifold, an $S^{1}$-bundle over $\mathbb{P}^{1}\times\mathbb{P}^{1}\cong S^{2}\times S^{2}$ with $\pi_x=0$ and $\pi_y\cong\mathbb{Z}$; the projectivised cone is the **Segre quadric**, whose two rulings are the two families of chiral null planes (*The Topology of the Zero-Divisor Cone*, *The Null Quadric and Its Projective Geometry*). Its real slice, the Minkowski light cone, has real dimension three and link the disjoint union $S^{2}\sqcup S^{2}$, one sphere per nappe (*Biquaternion Lorentzian and Conformal Geometry*). The one cone carries two links, the complex one over $S^{2}\times S^{2}$ and the real one over $S^{2}\sqcup S^{2}$.

**The cone is the complement of the unit group.** The units are exactly the elements off the cone, and the group they form is $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$, with $\pi_x(\mathbb{B}^{\times})\cong\mathbb{Z}$, $\pi_y(\mathbb{B}^{\times})=0$ and $\pi_z(\mathbb{B}^{\times})\cong\mathbb{Z}$, covered two-to-one by the centre and the determinant-one group (*The Biquaternion Unit Group as a Topological Group*). The cone and the unit group are complementarily read in homotopy: the cone's link has $\pi_y\cong\mathbb{Z}$, and the unit group has $\pi_y=0$.

**The cone's isotropic lines are its Peirce lines.** A **doubly null line** is an isotropic line that lies in the norm cone as well, and the doubly null lines are exactly the **Peirce lines** $\mathbb{C}(e_t\pm i\vec u)$ spanned by the rank-one Hermitian idempotents; each generates a minimal left and a minimal right ideal of complex dimension two all of whose elements are zero divisors, and the intersection of the cone with the Krein null set is the union of those lines, a cone of real dimension four (*The Isotropic Structure of the General Quaternionic Sesqualgebra*, *Ideals and Peirce Decomposition of the Biquaternion Algebra*). The maximal totally isotropic subspaces are the objects of the Witt index, and the maximal one is not confined to the cone: the complex line $\mathbb{C}(e_t+\vec e_x)$ is totally isotropic but has nonzero norm and is not a zero divisor.

**The cone is the boundary of the Hermitian level sets.** The level sets of the Hermitian form are the real hyperboloids, the hyperboloid model of hyperbolic space, against the complex hypersurfaces of $\langle\cdot,\cdot\rangle_{\natural}$; on a Minkowski slice the intersection degenerates to the two nappes of the light cone, and the future nappe is the Hermitian cone (*The Krein Level Sets and the Hyperbolic Structure*). The cone is thus the boundary of the real hyperbolic picture attached to the definite form, and it is the largest nontrivial vanishing set of a square: the natural square $\tilde Q\tilde Q^{\natural}$ vanishes exactly on the cone, while the sesquilinear square $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ vanishes at the origin alone (*The Squares and the Positive Cone of the Biquaternioid Sesqualgebra*).

These five statements are not about the twelve products. They are about the one quadratic form the twelve inherit, and they are the reason the cone is the meeting point of the grid rather than one of its cells.

## The One-Sided Inverse Equations

Only the plain product has a two-sided unit, so the classical equivalence *zero divisor if and only if not a unit* is available for it alone, and there it is exact: for a nonzero $\tilde P$ the statements *$\tilde P$ is a zero divisor of the plain product*, *$\mathrm{Norm}(\tilde P)=0$* and *$\tilde P$ is not invertible* are equivalent (*Zero Divisors of the Biquaternion Algebra*). The substitute for the other three products is the one-sided inverse criterion.

**Theorem (the inverse equations).** Let $\star$ be one of the four general products and let $\tilde P\neq0$. Then $\tilde P$ is a zero divisor of $\star$ exactly when neither of the two equations

$$
\tilde P\star\tilde X=e_t , \qquad \tilde X\star\tilde P=e_t
$$

has a solution; equivalently, both have a solution exactly when $\mathrm{Norm}(\tilde P)\neq0$.

*Proof.* If $\tilde P\star\tilde X=e_t$ holds, then in the model the equation is $\mathsf{M}_2(\tilde P)M=\mathrm{I}_2$ or $\mathsf{M}_2(\tilde P^{\natural})M=\mathrm{I}_2$ for an invertible $M$, so $\mathsf{M}_2(\tilde P)$ is invertible and $\mathrm{Norm}(\tilde P)\neq0$. Conversely, if $\mathrm{Norm}(\tilde P)\neq0$ then $\tilde P$ is invertible and the four solutions are those of the table below.

The solutions are written with the inverse $\tilde P^{-1}=\tilde P^{\natural}/\mathrm{Norm}(\tilde P)$ of the algebra, which exists for $\mathrm{Norm}(\tilde P)\neq0$. The two conjugations commute, ${}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural}=\overline{\cdot}$, so the order of the two superscripts in the last row is immaterial.

| product | $\tilde X$ with $\tilde P\star\tilde X=e_t$ | $\tilde X$ with $\tilde X\star\tilde P=e_t$ |
|---|---|---|
| $\tilde P\tilde Q$ | $\tilde P^{-1}$ | $\tilde P^{-1}$ |
| $\tilde P^{\natural}\tilde Q$ | $(\tilde P^{-1})^{\natural}$ | $(\tilde P^{-1})^{\natural}$ |
| $\tilde P\tilde Q^{*}$ | $(\tilde P^{-1})^{*}$ | $(\tilde P^{-1})^{*}$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | $(\tilde P^{-1})^{\natural*}$ | $(\tilde P^{-1})^{\natural*}$ |

This criterion uses the fixed element $e_t$, invariant under both conjugations, and makes no appeal to a unit of the product; it reads the same in the four products, and it says that the zero divisors are exactly the elements that cannot be inverted on either side.

## Summary

A zero divisor is defined by an equation that names a product, so the twelve products of the biquaternion algebra define twelve zero-divisor sets. For the four general products the sets coincide: for each of them, and for a nonzero element, being a left zero divisor, being a right zero divisor and lying on the cone are the same condition, the cone being the vanishing set of the norm $\mathrm{Norm}(\tilde Q)=\sum_\mu Q_\mu^{2}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)$ of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*.

The common set is the zero-divisor set $\mathcal{C}\setminus\{0\}$, a complex cone with apex at the origin, smooth away from the apex, of complex dimension three and real dimension six, whose nonzero members are the rank-one elements of the matrix model and whose left ideals are the minimal left ideals. Its complement is the group of units together with the origin, and it splits by the scalar part into the pure family of the nilpotents, of real dimension four, and the non-pure family of the complex multiples of the nontrivial idempotents, which fills the cone in real dimension six.

The annihilators of a fixed element of the cone, two complex planes per product, are *Annihilators in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*; the square-zero sets are *Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*. The cone is the zero-divisor set of the four general products alone: the four antisymmetric structures and the two scalar-valued symmetric structures $\mathrm{SPS}$ and $\mathrm{SQA}$ have the whole punctured space, and $\mathrm{SPA}$ and $\mathrm{SQS}$ have $(\{Q_t=0\}\cup\mathcal{C})\setminus\{0\}$. The cone is contained in all twelve sets and is the largest subset on which they agree. What a product does not change is the detection of the units: an element off the cone is invertible, and the one-sided inverse equations replace the classical equivalence for the three products that have no two-sided unit.

Beyond the grid the same set is one of four null sets. The bilinear form $\langle\cdot,\cdot\rangle$ has a complex cone of real dimension six different from $\mathcal{C}$, the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ has the origin alone, and the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ has the Krein cone of real dimension seven; on the remarkable subspaces the cone drops from real dimension six to four on the vector subspace and to three on the quaternion subspace and on the sectors, carried at every stage by the indefinite forms. As a topological space the cone is contractible with the apex as its only singular point, its link over $S^{7}_{E}$ is an $S^{1}$-bundle over $S^{2}\times S^{2}$ with $\pi_y\cong\mathbb{Z}$ against the link $S^{2}\sqcup S^{2}$ of its Minkowski slice, and its projectivisation is the Segre quadric. Its complement is the unit group $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$; its isotropic lines are the Peirce lines, the doubly null lines, and the cone meets the Krein null set in their union; its level-set companion is the real hyperboloid of the Hermitian form. These statements name no product, and they are the content of §*The Cone in the Wider Mathematics*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | one of the twelve products of $\mathbb{B}$; the four general products in the theorems |
| $\tilde P\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q$, $\tilde P^{\natural}\tilde Q^{*}$ | the four general products |
| $\mathrm{Form}(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | the general quaternionic bilinear form, the polar form of the norm |
| $\mathrm{Norm}(\tilde Q)$ | the norm of the statement, written where a statement holds for all four norms; this article instantiates it by the reduced norm, $\mathrm{Norm}(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $\mathrm{Norm}(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the reduced norm, the general quaternionic bilinear algebraic norm, the scalar of the central square $\tilde Q\tilde Q^{\natural}=\mathrm{Norm}(\tilde Q)e_t$ |
| $\mathcal{C}=\{\tilde Q:\mathrm{Norm}(\tilde Q)=0\}$ | the zero-divisor cone, of complex dimension three and real dimension six |
| $\mathcal{C}\setminus\{0\}$ | the zero-divisor set of the four general products |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | the centre, where the central square lies |
| pure, non-pure | scalar part zero, scalar part nonzero |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\tilde P^{-1}=\tilde P^{\natural}/\mathrm{Norm}(\tilde P)$ | the inverse of an element with $\mathrm{Norm}(\tilde P)\neq0$ |
| $(\vec P,\vec Q)$ | the general plain bilinear dot product of the two vector parts |
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ | the general plain bilinear form, whose isotropic cone is not $\mathcal{C}$ |
| $\langle\tilde P\rangle_{*}=\mathrm{Sc}(\tilde P\tilde P^{*})$ | the general plain sesquilinear algebraic norm, definite |
| $\langle\tilde P\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde P^{*})$ | the general quaternionic sesquilinear algebraic norm, indefinite |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space: the four general products and their eight symmetric and antisymmetric parts |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the general vocabulary: the zero divisor, the annihilator, the idempotent, the nilpotent and the rest, each stated once for a general product.
- *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the form $\langle\cdot,\cdot\rangle_{\natural}$ and the four algebraic norms read at the two equal arguments.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), for the plain-product criterion, the classification of the cone's elements and the parametrisation of the pure family.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the four idempotent sets, the four square-root problems and the four unit entries.
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the four general products and their symmetric and antisymmetric parts.
- *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the twelve names, the three letters of each and the class of each.
- *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four idempotent sets of the four general products and their reading among the twelve.
- *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`) (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four root problems.
- *Annihilators in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the two one-sided annihilators of one element of the cone and their relation by the conjugations.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four square-zero sets and the twelve square-zero readings.
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the isomorphism and the singular matrices.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the general plain bilinear form and its isotropic cone.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the subspaces, the pure cone and the non-pure families.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the criterion $Q_t=0$ or $\mathrm{Norm}(\tilde Q)=0$ of the enlarged set of $\mathrm{SPA}$.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the same criterion of the enlarged set of $\mathrm{SQS}$ and its two families.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the two scalar-valued symmetric structures whose zero-divisor set is the whole punctured space.
- *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four alternating structures whose zero-divisor set is the whole punctured space.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the natural product's criterion and the coincidence of its two annihilators.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the equation $\overline{\tilde P}\tilde P=0$ and its two halves.
- *The Squares and the Positive Cone of the Biquaternioid Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternioid-sesqualgebra.md`), for the definiteness of the general plain sesquilinear square.
- *Ideals and Peirce Decomposition of the Biquaternion Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.md`), for the minimal left ideals of the rank-one elements.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra.md`), for the isotropic cones of the two bilinear forms, which are not the cone $\mathcal{C}$.
- *The Topology of the Zero-Divisor Cone* (`articles_maths/the-topology-of-the-zero-divisor-cone.md`), for the cone as a topological space.
- *Remarkable Subspaces and the Four Forms* (`articles_maths/remarkable-subspaces-and-the-four-forms.md`) and *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the four null sets cut by the remarkable subspaces, the Krein cone and the real hyperboloids whose boundary the cone is.
- *The Null Quadric and Its Projective Geometry* (`articles_maths/the-null-quadric-and-its-projective-geometry.md`), for the Segre quadric, its two rulings and the projectivised cone.
- *Biquaternion Lorentzian and Conformal Geometry* (`articles_maths/biquaternion-lorentzian-and-conformal-geometry.md`), for the Minkowski slice, its real light cone of dimension three and its link $S^{2}\sqcup S^{2}$.
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the units as the complement of the cone, the covering and the homotopy groups.
- *The Isotropic Structure of the General Quaternionic Sesqualgebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.md`), for the Peirce lines, the minimal ideals and the doubly null lines in which the cone meets the Krein null set.
