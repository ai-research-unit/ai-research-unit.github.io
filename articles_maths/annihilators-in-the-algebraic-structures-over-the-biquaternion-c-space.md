# __Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space__

## Introduction

**The annihilator of an element in a product is the set of partners that the element kills.** It is defined by an equation that names a product, so the twelve products of the biquaternion space define twelve sets, and each of the twelve is computed below, solved in coordinates and written out with the vectors that generate it. **The two one-sided annihilators are equal in ten of the twelve structures, and they differ in exactly two, the plain product and the general quaternionic sesquilinear product, and there only for an element of vanishing norm.**

## The Annihilator of an Element

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in $\star$ are

$$
A_\star(\tilde Q)=\{\tilde Q_1:\tilde Q\star\tilde Q_1=0\},\qquad B_\star(\tilde Q)=\{\tilde Q_1:\tilde Q_1\star\tilde Q=0\},
$$

and the **two-sided annihilator** is their intersection. Each is the kernel of one of the two multiplications $L_{\tilde Q}$ and $R_{\tilde Q}$, so each is a complex subspace. Its dimension is the number of free complex parameters left by the equation $\tilde Q\star\tilde Q_1=0$, and that is how each set below is solved and stated.

**The mark of the block.** Following the owner articles, the annihilator of a block is written with the mark of that block in place of the star: $A_\bullet$ for a commutative block ($\mathrm{SPA}$), $A_\wedge$ for an alternating plain block ($\mathrm{APA}$) and $A_\diamond$ for an alternating or conjugate-alternating block ($\mathrm{AQA}$, $\mathrm{APS}$, $\mathrm{AQS}$). The mark names the same left annihilator as $A_\star$; it is kept here because it is the symbol the owner article uses.

**Three words, each with its equation.**
- The **cone** is the single complex equation $\mathrm{Norm}(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0$, the vanishing of the norm $\langle\cdot\rangle_{\natural}$ of the element, which the owner articles write $\mathrm{Norm}(\tilde Q)$ or $C(\tilde Q)$. An element off the cone is invertible, $\tilde Q^{-1}=\tilde Q^{\natural}/\mathrm{Norm}(\tilde Q)$; a nonzero element on the cone is a zero divisor of the plain product.
- A **complex plane** is a two-dimensional complex subspace, written $\mathbb{C}\{u,v\}$ with its two generators displayed; a **complex line** is written $\mathbb{C}u$. A plane is checked by multiplying its two generators into the product and finding zero.
- The **centre** is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ and the **vector subspace** is $\mathrm{Vect}(\mathbb{B})=\mathrm{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$.

**Four algebraic norms, and the one that decides.** The twelve products carry four **algebraic norms** and no more (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*): the algebraic norm of a product is its scalar form read at the two equal arguments, each of the four is carried by two products, and the four antisymmetrisations carry none. They are
$$
\langle\tilde Q\rangle=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2},\qquad \langle\tilde Q\rangle_{*}=\lvert Q_t\rvert^{2}+\lvert\vec Q\rvert^{2},\qquad \langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad \langle\tilde Q\rangle_{\natural*}=\lvert Q_t\rvert^{2}-\lvert\vec Q\rvert^{2},
$$
carried by the pairs $(\mathrm{GPA},\mathrm{SPA})$, $(\mathrm{GPS},\mathrm{SPS})$, $(\mathrm{GQA},\mathrm{SQA})$ and $(\mathrm{GQS},\mathrm{SQS})$ in that order. **The norm that decides every annihilator below is the third of the four, $\langle\cdot\rangle_{\natural}$**, the general quaternionic bilinear algebraic norm, $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, also called the **quaternionic norm** $\mathrm{Norm}(\tilde Q)$ in the owner articles and equal to the determinant of the $2\times2$ model. After *Conventions in Mathematics* §*The form convention and the norm convention*, $\mathrm{Norm}$ is the **generic norm of a statement**: it is instantiated, for the statement at hand, by the norm that statement uses, and in this article every statement uses the norm $\langle\cdot\rangle_{\natural}$ of the element it names. The four carried norms do not all decide, and the plain one does not decide at all: at $\tilde Q=e_t+\vec e_x$ the plain algebraic norm is $\langle\cdot\rangle=0$ while the norm of the statement is $\langle\cdot\rangle_{\natural}=2$ and the element is invertible, $\tilde Q^{-1}=\tfrac12(e_t-\vec e_x)$. The two sesquilinear norms $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ cut the hyperplanes of $\mathrm{SPS}$ and $\mathrm{SQS}$ and never decide an inverse, since $\langle\cdot\rangle_{*}$ is definite and $\langle\cdot\rangle_{\natural*}$ is indefinite. **Every statement below names its norm**: the deciding norm is written $\langle\cdot\rangle_{\natural}$, and the generic $\mathrm{Norm}$ of the owner articles is instantiated here by $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$. The four antisymmetrisations carry no algebraic norm, and their annihilators are read from the vector part alone.

In the units $e_t,\vec e_x,\vec e_y,\vec e_z$ of the space $\mathbb{B}$, with $i$ the unit of the complex coefficients, write $\tilde Q=Q_te_t+\vec Q$, and likewise $\tilde Q_2=Q_{2t}e_t+\vec Q_2$ and $\tilde Q_1=Q_{1t}e_t+\vec Q_1$, where $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$; then $\tilde Q^{\natural}=Q_te_t-\vec Q$ and $\tilde Q^{*}=\overline{Q_t}e_t-\overline{\vec Q}$. The **dot product** is $(\vec Q,\vec Q_1)=\sum_{\mu\in\{x,y,z\}}Q_\mu Q_{1\mu}$, the **cross product** is $\vec Q\times\vec Q_1$, and $(\vec Q,\vec Q)$ is read the same way.

The two-sided annihilator lies in the zero-divisor set together with $0$, because a partner that kills every element kills one; the two sets differ wherever a zero divisor is not a killer, and that gap is *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The annihilator and the zero divisors.** **Whatever nonzero biquaternion $\tilde Q$ is taken, every nonzero element of its annihilator is a zero divisor of the same product, and for the four general products the whole annihilator lies inside the cone.** The two notions are one condition read twice: $\tilde Q$ is a **left zero divisor** of $\star$ exactly when its left annihilator is not $\{0\}$, and a **right zero divisor** exactly when its right annihilator is not $\{0\}$ (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The annihilator is therefore the zero-divisor condition with its witnesses displayed: when $\tilde Q\neq0$ kills $\tilde Q_1\neq0$, the element $\tilde Q_1$ is a right zero divisor of $\star$ with witness $\tilde Q$, so every nonzero element of the left annihilator is a right zero divisor, $A_\star(\tilde Q)\setminus\{0\}\subseteq Z_\star$, and likewise $B_\star(\tilde Q)\setminus\{0\}$ consists of left zero divisors. **On the four general products the annihilator lies on the cone.** There the zero-divisor set is the punctured cone, $Z_\star=\mathcal{N}\setminus\{0\}$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*), and with the apex added the whole annihilator is inside the cone, $A_\star(\tilde Q)\subseteq\mathcal{N}$ and $B_\star(\tilde Q)\subseteq\mathcal{N}$ at every $\tilde Q\neq0$; the two planes of a zero divisor, the line of the plain algebra and the plane of the natural product, are totally isotropic subspaces of the quadratic form $\langle\cdot,\cdot\rangle_{\natural}$. **The order of the two sentences matters.** The containment $A_\star(\tilde Q)\subseteq\mathcal{N}$ presupposes a cone, and the cone is the zero-divisor set of the four general products alone. In the eight derived structures the zero-divisor set is strictly larger than the cone, the whole punctured space $\mathbb{B}\setminus\{0\}$ in $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$ and $\mathrm{AQS}$ and the enlarged set $(\{Q_t=0\}\cup\mathcal{N})\setminus\{0\}$ in $\mathrm{SPA}$ and $\mathrm{SQS}$ (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*); the annihilator is still inside the zero-divisor set of its structure, but it leaves the cone: in $\mathrm{SPA}$ at the pure element $\vec e_z$ the annihilator is the plane $\{Q_{1t}=0,\ Q_{1z}=0\}$, which contains the unit $\vec e_x$ of norm $\langle\cdot\rangle_{\natural}=1$. **The origin is the one element to read with care.** The annihilator of $\tilde Q=0$ is $\{0\}$ or all of $\mathbb{B}$, the zero of $\mathbb{B}$ is never a zero divisor, and the sentence "the annihilator of $\tilde Q$ consists of zero divisors" therefore holds for the four general products at $\tilde Q\neq0$; at $\tilde Q=0$ the whole space is its own annihilator and the origin within it is the one exemption.

## The Twelve Structures and their Annihilators

The four general products split into the twelve structures through the class-preserving exchange (*Symmetric and Antisymmetric Decomposition of the Four General Products*). Each structure is read below with its product written out, the criterion in coordinates, and the annihilator with its generators displayed. The twelve are in the order of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### $\mathrm{GPA}$, the general plain algebra

The product is
$$
\tilde Q\tilde Q_2=\bigl(Q_tQ_{2t}-(\vec Q,\vec Q_2)\bigr)e_t+Q_t\vec Q_2+Q_{2t}\vec Q+\vec Q\times\vec Q_2 .
$$

**The plain product carries the algebraic norm $\langle\tilde Q\rangle=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$, and its inverse and its annihilators are decided by the norm $\langle\tilde Q\rangle_{\natural}$, not by $\langle\cdot\rangle$.**

**When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, the two annihilators are $\{0\}$.** Then $\tilde Q^{-1}=\tilde Q^{\natural}/\mathrm{Norm}(\tilde Q)$ and $\tilde Q\tilde Q_1=0$ gives $\tilde Q_1=0$, and the same on the right.

**When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, the two annihilators are distinct complex planes that share the line $\mathbb{C}\tilde Q^{\natural}$.** At the non-pure element $e_t+i\vec e_x$ the left annihilator is the plane of $e_t-i\vec e_x$ and $\vec e_z+i\vec e_y$, and the right annihilator is the plane of $e_t-i\vec e_x$ and $\vec e_z-i\vec e_y$:
$$ \boxed{\; A_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z+i\vec e_y\},\qquad B_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z-i\vec e_y\} \;}. $$
At the pure element $\vec e_x+i\vec e_y$ the left annihilator is the plane of $\vec e_x+i\vec e_y$ and $e_t+i\vec e_z$, and the right annihilator is the plane of $\vec e_x+i\vec e_y$ and $e_t-i\vec e_z$:
$$
A_\star(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x+i\vec e_y,\ e_t+i\vec e_z\},\qquad B_\star(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x+i\vec e_y,\ e_t-i\vec e_z\}.
$$
In each line the first generator is $\tilde Q^{\natural}$, so the two planes share it, and the two second generators differ in one sign, which is what makes the planes distinct. The pure element $\vec e_x+i\vec e_y$ lies in its own annihilators and the non-pure element $e_t+i\vec e_x$ does not. The dimension is two, the kernel of a rank-two multiplication.

The cone is *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*.

### $\mathrm{GPS}$, the general plain sesqualgebra

The product is $\tilde Q\tilde Q_2^{*}$, the plain product with the Hermitian conjugation in the second slot. It is conjugate-commutative, so $A_\star(\tilde Q)=B_\star(\tilde Q)$ at every element.

**The product carries the algebraic norm $\langle\cdot\rangle_{*}$, definite, and the criterion of the cone is the norm $\langle\tilde Q\rangle_{\natural}$.**

**When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, the annihilator is $\{0\}$.** **When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, the annihilator is the plane of the Hermitian conjugates of the $\tilde Q_2$ with $\tilde Q\tilde Q_2=0$.** At $\tilde Q=0$ the annihilator is all of $\mathbb{B}$:
$$
A_\star(\tilde Q)=A_{\text{plain}}(\tilde Q)^{*},\qquad A_{\text{plain}}(\tilde Q)=\{\tilde Q_2:\tilde Q\tilde Q_2=0\},
$$
where $A_{\text{plain}}(\tilde Q)$ is the kernel of the plain left multiplication, the object solved in §*$\mathrm{GPA}$, the general plain algebra*. The equation $\tilde Q\tilde Q_1^{*}=0$ is solved by $\tilde Q_1=\tilde Q_2^{*}$ with $\tilde Q_2\in A_{\text{plain}}(\tilde Q)$, and the Hermitian conjugation is a bijection. At the element $e_t+i\vec e_x$, of norm zero, the plane is
$$
A_\star(e_t+i\vec e_x)=\mathbb{C}\{\vec e_x+ie_t,\ \vec e_y+i\vec e_z\}.
$$

*Annihilators of the General Plain Sesqualgebra* owns the rank and the plane.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde Q^{\natural}\tilde Q_2$, the plain product with the natural conjugation in the first slot. It is the plain product of $\tilde Q^{\natural}$ and $\tilde Q_2$.

**The natural product carries the algebraic norm $\langle\cdot\rangle_{\natural}$, and here the carried norm is the deciding one, $\langle\tilde Q\rangle_{\natural}=\mathrm{Norm}(\tilde Q)$.**

**The two annihilators are always equal, and in every case they equal the plain annihilator of $\tilde Q^{\natural}$.** **When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, they are $\{0\}$.** **When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, they are the complex plane of dimension two that contains the line $\mathbb{C}\tilde Q$.** At $\tilde Q=0$ they are all of $\mathbb{B}$. The equality is the natural conjugation applied to $\tilde Q^{\natural}\tilde Q_1=0$, which gives $\tilde Q_1^{\natural}\tilde Q=0$. At the pure element $\vec e_x+i\vec e_y$ and at the non-pure element $e_t+i\vec e_x$, both of norm zero, the plane contains the element itself:
$$
A_\star(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x+i\vec e_y,\ \vec e_z-ie_t\},\qquad A_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y+i\vec e_z\}.
$$
In both lines the element is its own first generator, so it lies in its own annihilator; the first element is pure and the second is not.

*Annihilators of the General Quaternionic Algebra* owns the equality of the two sides and the plane.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra

The product is $\tilde Q^{\natural}\tilde Q_2^{*}$, the plain product with one conjugation in each slot.

**The product carries the algebraic norm $\langle\cdot\rangle_{\natural*}$, indefinite, and the criterion is the norm $\langle\tilde Q\rangle_{\natural}$.**

**When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, both annihilators are $\{0\}$.** **When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, each annihilator is a complex plane, and the two planes are distinct, meeting exactly in the line $\mathbb{C}\tilde Q^{*}$.** At $\tilde Q=0$ both are all of $\mathbb{B}$. At the element $e_t+i\vec e_x$, of norm zero, the two planes meet in the line of the element:
$$
A_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y-i\vec e_z\},\qquad B_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y+i\vec e_z\}.
$$
The two planes differ in the second generator and meet exactly in the line $\mathbb{C}\tilde Q^{*}$; at $e_t+i\vec e_x$ this line is the line of the element itself. This block is one of the two of the twelve whose two sides are distinct. The left annihilator is the Hermitian-conjugate image of the kernel of the plain left multiplication by $\tilde Q^{\natural}$, and the right one is the same computation in the other order.

*Annihilators of the General Quaternionic Sesqualgebra* owns the two planes.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product
$$
\tfrac12(\tilde Q\tilde Q_2+\tilde Q_2\tilde Q)=\bigl(Q_tQ_{2t}-(\vec Q,\vec Q_2)\bigr)e_t+Q_t\vec Q_2+Q_{2t}\vec Q .
$$
It is commutative, so $A_\bullet(\tilde Q)=B_\bullet(\tilde Q)$ at every element and there is one equation, $Q_t\vec Q_2+Q_{2t}\vec Q=0$ with $Q_tQ_{2t}=(\vec Q,\vec Q_2)$.

**The symmetrisation carries the same algebraic norm $\langle\cdot\rangle$, and the criterion is again the norm $\langle\tilde Q\rangle_{\natural}$, not $\langle\cdot\rangle$.**

**The criterion of the three cases is the norm $\langle\cdot\rangle_{\natural}$ together with the scalar part $Q_t$.**
- **At an element with $Q_t$ not zero and with nonzero norm $\langle\tilde Q\rangle_{\natural}$, the annihilator is $\{0\}$**, the element being invertible in the plain product.
- **At an element with $Q_t$ not zero and with vanishing norm $\langle\tilde Q\rangle_{\natural}$, the annihilator is the line $\mathbb{C}\tilde Q^{\natural}$**, since the vector equation forces $\vec Q_2=-(Q_{2t}/Q_t)\vec Q$ and the scalar equation then forces the vanishing of the norm $\langle\tilde Q\rangle_{\natural}$.
- **At a nonzero element with $Q_t=0$, the annihilator is the plane $\{Q_{1t}=0,\ (\vec Q,\vec Q_1)=0\}$**, because a pure element times $\tilde Q_1$ is $-(\vec Q,\vec Q_1)e_t+Q_{1t}\vec Q$; at $\tilde Q=0$ it is all of $\mathbb{B}$.

Two worked elements show the two families. At the pure element $\vec e_x$ the annihilator is the plane of the pure elements orthogonal to $\vec e_x$, and at the non-pure element $e_t+i\vec e_x$ it is the line of the natural conjugate:
$$
A_\bullet(\vec e_x)=\mathbb{C}\{\vec e_y,\vec e_z\},\qquad A_\bullet(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x\}.
$$
The pure plane $Q_t=0$ is a second family beside the cone, and it is why the block has more zero divisors than the plain algebra.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the operator, its rank and the two families.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra

The product is the symmetrisation of the preceding one, the scalar-valued product
$$
\tilde Q\star\tilde Q_2=\langle\tilde Q,\tilde Q_2\rangle_{*}e_t,\qquad \langle\tilde Q,\tilde Q_2\rangle_{*}=Q_t\overline{Q_{2t}}+(\vec Q,\overline{\vec Q_2}) .
$$
It is conjugate-commutative, so $A_\star(\tilde Q)=B_\star(\tilde Q)$, and the equation is the single complex equation
$$
Q_t\overline{Q_{1t}}+(\vec Q,\overline{\vec Q_1})=0 .
$$

**The symmetrisation carries the same algebraic norm $\langle\cdot\rangle_{*}$, definite, and the annihilator is the polar hyperplane of that norm, $\langle\tilde Q,\tilde Q_1\rangle_{*}=0$, which is the displayed equation. The norm $\langle\cdot\rangle_{*}$ vanishes at the origin alone and decides no inverse, the cone being decided by $\langle\cdot\rangle_{\natural}$.**

**At every nonzero $\tilde Q$ the annihilator is the hyperplane of complex dimension three cut out by this equation.** At $\tilde Q=0$ the annihilator is all of $\mathbb{B}$. At the unit $e_t$ the hyperplane is the vector subspace:
$$
A_\star(e_t)=\{\tilde Q_1:Q_{1t}=0\}=\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\}.
$$
The form $\langle\cdot,\cdot\rangle_{*}$ is definite, so no nonzero element is isotropic and the annihilator is never larger than a hyperplane. This is the Hermitian twin of the symmetric quaternionic algebra: the same hyperplane of the same dimension, cut by the other form.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the hyperplane.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation, the scalar-valued product
$$
\tilde Q\star\tilde Q_2=\langle\tilde Q,\tilde Q_2\rangle_{\natural}e_t,\qquad \langle\tilde Q,\tilde Q_2\rangle_{\natural}=Q_tQ_{2t}+(\vec Q,\vec Q_2) .
$$
It is commutative, so $A_\star(\tilde Q)=B_\star(\tilde Q)$ at every element, and the equation $\tilde Q\star\tilde Q_1=0$ is the single complex equation
$$
Q_tQ_{1t}+(\vec Q,\vec Q_1)=0 .
$$

**At every nonzero $\tilde Q$ the annihilator is the hyperplane of complex dimension three cut out by this equation.** At $\tilde Q=0$ the annihilator is all of $\mathbb{B}$. **The symmetrisation carries the same algebraic norm $\langle\cdot\rangle_{\natural}$, which is the deciding norm, and the hyperplane is its polar form at $\tilde Q_1$, $\langle\tilde Q,\tilde Q_1\rangle_{\natural}=0$.**

At the unit $e_t$ the hyperplane is the vector subspace, and at the isotropic element $\vec e_x+i\vec e_y$ the element lies in its own annihilator:
$$
A_\star(e_t)=\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\},\qquad \vec e_x+i\vec e_y\in A_\star(\vec e_x+i\vec e_y).
$$
The element $\vec e_x+i\vec e_y$ is isotropic, $(\vec Q,\vec Q)=1-1=0$, and an isotropic element lies in its own annihilator; an element that is not isotropic does not. This product gives the largest annihilator a nonzero element can have without killing the whole space.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the hyperplane and the isotropic locus.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra

The product is the symmetrisation of the preceding one; it is conjugate-commutative, so $A_\star(\tilde Q)=B_\star(\tilde Q)$, and its equation is
$$
\tilde Q^{\natural}\tilde Q_1^{*}+\overline{\tilde Q_1^{\natural}\tilde Q^{*}}=0 .
$$

**The symmetrisation carries the algebraic norm $\langle\cdot\rangle_{\natural*}$, $\langle\tilde Q\rangle_{\natural*}=|Q_t|^{2}-|\vec Q|^{2}$, indefinite.** **The annihilator lies in the polar hyperplane $\langle\tilde Q,\tilde Q_1\rangle_{\natural*}=0$, and the norm $\langle\cdot\rangle_{\natural}$ together with the scalar part $Q_t$ decides its dimension.**

**At an element whose scalar part is zero, the annihilator is the plane $\{Q_{1t}=0,\ (\vec Q,\overline{\vec Q_1})=0\}$.** **At a non-pure element of the cone, the annihilator is the line $\mathbb{C}\tilde Q^{*}$.** **At a non-pure element off the cone, the annihilator is $\{0\}$.** At $\tilde Q=0$ the annihilator is all of $\mathbb{B}$. At the pure element $\vec e_x+i\vec e_y$ the annihilator is that plane, and at the non-pure element $e_t+i\vec e_x$ it is the line of the element:
$$
A_\star(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x-i\vec e_y,\ \vec e_z\},\qquad A_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x\}.
$$
At a pure element the scalar part of $\tilde Q_1$ vanishes and its vector part runs over the line conjugate-orthogonal to $\vec Q$, so the annihilator is always a plane of dimension two, whether or not the pure element is a zero divisor; at a non-pure element of the cone the whole of $\tilde Q_1$ is pinned to the line of $\tilde Q^{*}$, and off the cone only $\tilde Q_1=0$ is killed. The block separates the two families of its zero-divisor set by the size of the annihilator, a plane at a pure element against a line at a non-pure one.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the two families.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator
$$
\tfrac12(\tilde Q\tilde Q_2-\tilde Q_2\tilde Q)=\vec Q\times\vec Q_2 ,
$$
the cross product of the two vector parts, an alternating product.

**The commutator carries no algebraic norm, because it vanishes at the two equal arguments, and the vector part alone decides the annihilator.**

**At an element whose vector part is zero, the annihilator is all of $\mathbb{B}$**, because a scalar element has no vector part and kills every partner. **At an element whose vector part is not zero, the annihilator is the plane $\mathbb{C}e_t\oplus\mathbb{C}\vec Q$.** Writing $\tilde Q_1=Q_{1t}e_t+\vec Q_1$, the product is $\vec Q\times\vec Q_1$, which vanishes exactly on the line $\mathbb{C}\vec Q$, and the scalar slot $Q_{1t}$ is free. For example, at the two elements $\vec e_x$ and $e_t+2\vec e_x$ the annihilator is the same plane, spanned by the centre and the vector part:
$$
A_\wedge(\vec e_x)=A_\wedge(e_t+2\vec e_x)=\mathbb{C}\{e_t,\vec e_x\}.
$$
The block is alternating, so every element lies in its own annihilator and every nonzero element is a zero divisor; a central element kills everything and every other element kills only a plane. It is the one structure of the twelve whose annihilator is the whole space at a nonzero element.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the rank and the plane.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra

The product is the antisymmetrisation of the plain sesquilinear product, the vector part of $\tilde Q\tilde Q_2^{*}$. It is conjugate-alternating, so $A_\diamond(\tilde Q)=B_\diamond(\tilde Q)$.

**The antisymmetrisation carries no algebraic norm, and the norm $\langle\tilde Q\rangle_{\natural}$ decides.**

**The common annihilator is the set of the Hermitian conjugates of the $\tilde Q_2$ with $\tilde Q\tilde Q_2$ central.** **When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, it is the line $\mathbb{C}\overline{\tilde Q}$.** **When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, it is the plane $A_{\text{plain}}(\tilde Q)^{*}$.** At $\tilde Q=0$ it is all of $\mathbb{B}$:
$$ \boxed{\; A_\diamond(\tilde Q)=\{\tilde Q_2^{*}:\tilde Q\tilde Q_2\in\mathbb{C}_{\mathbb{B}}\} \;}. $$
At an element of nonzero norm $\langle\cdot\rangle_{\natural}$ the single solution line is $\mathbb{C}\overline{\tilde Q}$, the conjugate of the element, which at the real element $e_t+2\vec e_x+3\vec e_y+4\vec e_z$ is the line of the element itself; at the element $\vec e_x+i\vec e_y$, of norm zero, the annihilator is the plane
$$
A_\diamond(e_t+2\vec e_x+3\vec e_y+4\vec e_z)=\mathbb{C}\{e_t+2\vec e_x+3\vec e_y+4\vec e_z\},\qquad A_\diamond(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x-i\vec e_y,\ e_t+i\vec e_z\}.
$$
At an element of nonzero norm $\langle\cdot\rangle_{\natural}$ the equations $\tilde Q\tilde Q_2=\lambda e_t$ have the single solution line $\mathbb{C}\tilde Q^{-1}$, whose star is the line $\mathbb{C}\overline{\tilde Q}$ of the conjugate element; at an element of the cone they have the plane displayed, and that plane is the star-image of the plain annihilator, $A_\diamond(\tilde Q)=\{\tilde Q_2^{*}:\tilde Q\tilde Q_2=0\}=A_{\text{plain}}(\tilde Q)^{*}$. The block reads the invertibility of the plain product and not its own zero divisors, because it has none. Its product is conjugate-alternating, $\tilde Q\diamond\tilde Q+\overline{\tilde Q\diamond\tilde Q}=0$, so the element lies in its own annihilator exactly when $\tilde Q\diamond\tilde Q$ vanishes, which happens at every element with real coefficients and fails at some elements with complex coefficients, for instance at $\tilde Q=\vec e_x+i\vec e_y$.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the theorem and the two cases.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the antisymmetrisation, the quaternionic cross product, whose value has the vector part
$$
Q_t\vec Q_2-Q_{2t}\vec Q-\vec Q\times\vec Q_2 .
$$
It is alternating, so $A_\diamond(\tilde Q)=B_\diamond(\tilde Q)$ and every element lies in its own annihilator.

**The antisymmetrisation carries no algebraic norm, and the vector part together with the norm $\langle\cdot\rangle_{\natural}$ decides.**

**When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, the annihilator is the line $\mathbb{C}\tilde Q$.** **When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, the annihilator is a complex plane containing that line.** At $\tilde Q=0$ the annihilator is all of $\mathbb{B}$. At the element $e_t$, of norm one, the annihilator is the line of the element itself, and at the element $\vec e_x+i\vec e_y$, of norm zero, it is the larger plane that contains that line:
$$
A_\diamond(e_t)=\mathbb{C}\{e_t\},\qquad A_\diamond(\vec e_x+i\vec e_y)=\mathbb{C}\{\vec e_x+i\vec e_y,\ e_t+i\vec e_z\}.
$$
The element $e_t$ has norm $\langle\cdot\rangle_{\natural}=1$ and its annihilator is the centre, of dimension one; the element $\vec e_x+i\vec e_y$ has norm $\langle\cdot\rangle_{\natural}=0$ and its annihilator is a plane, of dimension two.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the rank table and the plane.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra

The product is the antisymmetrisation of the general quaternionic sesquilinear product; it is the conjugate cross product $\vec Q\times\overline{\vec Q_1}$, conjugate-alternating, so $A_\diamond(\tilde Q)=B_\diamond(\tilde Q)$.

**The antisymmetrisation carries no algebraic norm, and the conjugate of the vector part decides.**

**At an element whose vector part is not zero, the annihilator is the plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q}$.** **At an element whose vector part is zero, the annihilator is all of $\mathbb{B}$.** At the non-central element $\vec e_x+i\vec e_y$ the annihilator is the plane of the centre together with the conjugate line, and at the central element $e_t$ it is all of $\mathbb{B}$:
$$
A_\diamond(\vec e_x+i\vec e_y)=\mathbb{C}\{e_t,\ \vec e_x-i\vec e_y\},\qquad A_\diamond(e_t)=\mathbb{B}.
$$
The operator depends on the vector part alone and only through its conjugate, so an element of the centre has the zero operator and kills everything, and a non-central element has rank two and kills exactly the centre together with the conjugate line of its vector part.

*Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* owns the plane and the rank.

## Results

The twelve are tabulated with the annihilator of a general element, the case split written out in each cell, and the two theorems that hold across them are stated below.

### The Twelve Annihilators

**Read the cells.** The deciding norm is $\langle\cdot\rangle_{\natural}$, $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, the general quaternionic bilinear algebraic norm and the third of the four; it vanishes exactly at the zero divisors of the four general products. Every cell names $\langle\cdot\rangle_{\natural}$ where the cone decides, and the two symmetrisations of sesquilinear products name their own norm as well, $\langle\tilde Q,\tilde Q_1\rangle_{*}=0$ for $\mathrm{SPS}$ and $\langle\tilde Q,\tilde Q_1\rangle_{\natural*}=0$ for $\mathrm{SQS}$. The four algebraic norms $\langle\cdot\rangle$, $\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural}$, $\langle\cdot\rangle_{\natural*}$ and the two products that carry each are stated at the head of the article. The vector part of $\tilde Q$ is $\vec Q$, and the parts of the partner $\tilde Q_1$ are $Q_{1t}$ and $\vec Q_1$. The form $\langle\cdot,\cdot\rangle_{\natural}$ of the symmetric quaternionic algebra is $\langle\tilde Q,\tilde Q_2\rangle_{\natural}=Q_tQ_{2t}+(\vec Q,\vec Q_2)$, and the form $\langle\cdot,\cdot\rangle_{*}$ of the symmetric plain sesqualgebra is $\langle\tilde Q,\tilde Q_2\rangle_{*}=Q_t\overline{Q_{2t}}+(\vec Q,\overline{\vec Q_2})$. The span notation $\mathbb{C}\{u,v\}$ is the complex span of $u$ and $v$. Each cell gives the annihilator of a general element, case by case, and every set it names can be checked by multiplying a generator into the product.

| family | structure | the product | the annihilator of a general element $\tilde Q$ | the two sides |
|---|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde Q\tilde Q_2$ | When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, each of the two annihilators is $\{0\}$. When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, each annihilator is a complex plane of dimension two. The two planes are distinct, both contain the line $\mathbb{C}\tilde Q^{\natural}$, and they meet in exactly that line. At $\tilde Q=0$, each annihilator is all of $\mathbb{B}$. | the two sides differ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\tilde Q\tilde Q_2^{*}$ | When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, the annihilator is $\{0\}$. When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, the annihilator is the plane of dimension two formed by the conjugates $\tilde Q_2^{*}$ of the solutions $\tilde Q_2$ of $\tilde Q\tilde Q_2=0$ in the plain product. At $\tilde Q=0$, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the quaternionic algebra | $\mathrm{GQA}$ | $\tilde Q^{\natural}\tilde Q_2$ | When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, both annihilators are $\{0\}$. When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, both are one and the same plane of dimension two, and that plane contains the line $\mathbb{C}\tilde Q$. At $\tilde Q=0$, both are all of $\mathbb{B}$. | the two sides are equal |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\tilde Q^{\natural}\tilde Q_2^{*}$ | When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, both annihilators are $\{0\}$. When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, the left annihilator is the conjugate of the plain left annihilator of $\tilde Q^{\natural}$, and the right annihilator is the natural conjugate of the plain right annihilator of $\tilde Q^{*}$. The two are distinct planes of dimension two, and they meet in exactly the line $\mathbb{C}\tilde Q^{*}$. At $\tilde Q=0$, both are all of $\mathbb{B}$. | the two sides differ |
| the plain algebra | $\mathrm{SPA}$ | $\tfrac12(\tilde Q\tilde Q_2+\tilde Q_2\tilde Q)$ | At a nonzero element whose scalar part $Q_t$ is zero, the annihilator is the plane $\{Q_{1t}=0,\ (\vec Q,\vec Q_1)=0\}$. At an element with $Q_t$ not zero and with vanishing norm $\langle\tilde Q\rangle_{\natural}$, the annihilator is the line $\mathbb{C}\tilde Q^{\natural}$. At an element with $Q_t$ not zero and with nonzero norm $\langle\tilde Q\rangle_{\natural}$, the annihilator is $\{0\}$. At $\tilde Q=0$, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the plain sesqualgebra | $\mathrm{SPS}$ | $\langle\tilde Q,\tilde Q_2\rangle_{*}e_t$ | At a nonzero element, the annihilator is the hyperplane $\langle\tilde Q,\tilde Q_1\rangle_{*}=0$, that is $Q_t\overline{Q_{1t}}+(\vec Q,\overline{\vec Q_1})=0$, of dimension three. At $\tilde Q=0$, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the quaternionic algebra | $\mathrm{SQA}$ | $\langle\tilde Q,\tilde Q_2\rangle_{\natural}e_t$ | At a nonzero element, the annihilator is the hyperplane $\langle\tilde Q,\tilde Q_1\rangle_{\natural}=0$, that is $Q_tQ_{1t}+(\vec Q,\vec Q_1)=0$, of dimension three. At $\tilde Q=0$, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the quaternionic sesqualgebra | $\mathrm{SQS}$ | the symmetrisation | At a nonzero element whose scalar part $Q_t$ is zero, the annihilator is the plane cut by the two equations $Q_{1t}=0$ and $\langle\tilde Q,\tilde Q_1\rangle_{\natural*}=0$. At an element with $Q_t$ not zero and with vanishing norm $\langle\tilde Q\rangle_{\natural}$, the annihilator is the line $\mathbb{C}\tilde Q^{*}$. At an element with $Q_t$ not zero and with nonzero norm $\langle\tilde Q\rangle_{\natural}$, the annihilator is $\{0\}$. At $\tilde Q=0$, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the plain algebra | $\mathrm{APA}$ | $\tfrac12(\tilde Q\tilde Q_2-\tilde Q_2\tilde Q)$ | At an element whose vector part is not zero, the annihilator is the plane $\mathbb{C}e_t\oplus\mathbb{C}\vec Q$. At an element whose vector part is zero, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the plain sesqualgebra | $\mathrm{APS}$ | the antisymmetrisation | When the norm $\langle\tilde Q\rangle_{\natural}$ is not zero, the annihilator is the line $\mathbb{C}\overline{\tilde Q}$. When the norm $\langle\tilde Q\rangle_{\natural}$ is zero at a nonzero element, the annihilator is the plane of the conjugates of the solutions of $\tilde Q\tilde Q_2=0$ in the plain product, which is the same plane as in the general plain sesqualgebra. At $\tilde Q=0$, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the quaternionic algebra | $\mathrm{AQA}$ | the antisymmetrisation | At an element whose vector part is not zero and whose norm $\langle\tilde Q\rangle_{\natural}$ is not zero, the annihilator is the line $\mathbb{C}\tilde Q$. At an element whose vector part is not zero and whose norm $\langle\tilde Q\rangle_{\natural}$ is zero, the annihilator is the plane of the solutions of $Q_t\vec Q_1-Q_{1t}\vec Q-\vec Q\times\vec Q_1=0$, and that plane contains the line $\mathbb{C}\tilde Q$. At an element whose vector part is zero and which is not zero, the annihilator is the line $\mathbb{C}e_t$. At $\tilde Q=0$, the annihilator is all of $\mathbb{B}$. | the two sides are equal |
| the quaternionic sesqualgebra | $\mathrm{AQS}$ | the antisymmetrisation | At an element whose vector part is not zero, the annihilator is the plane $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q}$. At an element whose vector part is zero, the annihilator is all of $\mathbb{B}$. | the two sides are equal |

Four facts follow from the table. The two one-sided annihilators differ in exactly two rows, the plain product and the general quaternionic sesquilinear product, and they differ there only at an element of norm zero. In two rows some nonzero element has the whole space as its annihilator, and those rows are the two antisymmetrisations, whose value is a cross product. In two rows every nonzero element has a hyperplane of dimension three as its annihilator, and those rows are the two symmetrisations that collapse the product to a form. In the remaining six rows the annihilator is small at an element off the cone but not always trivial: the four general products have $\{0\}$ there and a plane on the cone, the two antisymmetric sesquilinear structures already have the line $\mathbb{C}\tilde Q$, or its conjugate, at an element of nonzero norm and a plane on the cone, and the two symmetric structures have a plane at every pure element, whether or not the norm vanishes.

### The Two One-Sided Annihilators

**Theorem (the two sides are equal in ten structures and differ in two).** The two annihilators of an element are equal at every element for $\mathrm{GPS}$, $\mathrm{GQA}$, $\mathrm{SPA}$, $\mathrm{SPS}$, $\mathrm{SQA}$, $\mathrm{SQS}$, $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$ and $\mathrm{AQS}$, and, for $\mathrm{GPA}$ and $\mathrm{GQS}$, they are equal at every element with $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}\neq0$. For those two, when $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0$, they are distinct complex planes of dimension two: the two of the plain product meet in the line $\mathbb{C}\tilde Q^{\natural}$, and the two of the general quaternionic sesquilinear product meet in the line $\mathbb{C}\tilde Q^{*}$.

*Proof.* The products $\mathrm{SPA}$ and $\mathrm{SQA}$ are commutative and the products $\mathrm{SPS}$ and $\mathrm{SQS}$ are conjugate-commutative, so the two products vanish together and the two annihilators are one set. The products $\mathrm{APA}$, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$ are alternating or conjugate-alternating, so the sign that exchanges the two factors does not change whether a product vanishes. The products $\mathrm{GQA}$ and $\mathrm{GPS}$ carry their involution in one slot, and the natural or the Hermitian conjugation, an anti-automorphism of order two, exchanges the two sides: $A_\star(\tilde Q)=B_\star(\tilde Q^{\natural})$ and $A_\star(\tilde Q)=B_\star(\tilde Q)^{*}$. The plain product and the general quaternionic sesquilinear product have no such exchange, and their two planes are computed distinct in their subsections.

### The Four General Products: One Plane Through Two Conjugations

Fix a nonzero element of the cone, $\mathrm{Norm}(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=0$. Each of the four general products gives two planes for it, and the eight planes are related as follows.

**Theorem (the planes are read through the two conjugations).** Write $A_{\text{plain}},A_{*},A_{\natural},A_{\natural*}$ for the left annihilators of $\tilde Q$ in the plain, the general plain sesquilinear, the natural and the general quaternionic sesquilinear product. Then
$$ \boxed{\; A_{\natural}(\tilde Q)=A_{\text{plain}}(\tilde Q^{\natural}),\qquad A_{*}(\tilde Q)=A_{\text{plain}}(\tilde Q)^{*},\qquad A_{\natural*}(\tilde Q)=A_{\text{plain}}(\tilde Q^{\natural})^{*} \;}, $$
and the two sides coincide for the natural product and for the general plain sesquilinear product, while for the plain product and for the general quaternionic sesquilinear product they differ.

*Proof.* The first identity is $\tilde Q^{\natural}\tilde Q_1=0$ read as the plain product of $\tilde Q^{\natural}$ and $\tilde Q_1$. For the second, the substitution $\tilde Q_1=\tilde Q_2^{*}$ turns $\tilde Q\tilde Q_1^{*}=0$ into $\tilde Q\tilde Q_2=0$, and the Hermitian conjugation is a bijection, so the plane is the star-image of the plain plane; the third is the first and the second composed. The coincidences are the theorem of §*The Two One-Sided Annihilators*.

**Example.** Take $\tilde Q=e_t+i\vec e_x$, whose norm $\langle\cdot\rangle_{\natural}$ is $1-1=0$. The plain plane is
$$
A_{\text{plain}}(e_t+i\vec e_x)=\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z+i\vec e_y\},
$$
the general plain sesquilinear plane is the star-image of the first, $A_{*}(e_t+i\vec e_x)=\mathbb{C}\{\vec e_x+ie_t,\ \vec e_y+i\vec e_z\}$, which is the plane of §*$\mathrm{GPS}$, the general plain sesqualgebra*; the natural plane is $A_{\natural}(e_t+i\vec e_x)=A_{\text{plain}}(e_t-i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y+i\vec e_z\}$, which is the plane of §*$\mathrm{GQA}$, the general quaternionic algebra*; and the general quaternionic sesquilinear plane is $A_{\natural*}(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y-i\vec e_z\}$, the plane of §*$\mathrm{GQS}$, the general quaternionic sesqualgebra*. The four planes are the plain plane and its two conjugate images, and each one-sided plane of the four general products is read off the plain one.

## Summary

The annihilator of an element in a product is the set of partners that it kills on one side or the other; it is the solution set of the equation $\tilde Q\star\tilde Q_1=0$, and its dimension is the number of free complex parameters in that equation. The twelve products of the biquaternion space give twelve solutions, each written above with its case split and the generators of each set.

Five facts summarize the twelve structures.

- The two one-sided annihilators are equal in ten of the twelve structures. They differ in exactly two, the plain product and the general quaternionic sesquilinear product, and only at an element of norm zero. There they are two distinct planes that share the line $\mathbb{C}\tilde Q^{\natural}$ in the plain product and the line $\mathbb{C}\tilde Q^{*}$ in the general quaternionic sesquilinear product. In the plain product at $\vec e_x+i\vec e_y$, for example, the left annihilator is $\mathbb{C}\{\vec e_x+i\vec e_y,\ e_t+i\vec e_z\}$ and the right annihilator is $\mathbb{C}\{\vec e_x+i\vec e_y,\ e_t-i\vec e_z\}$.
- In two structures some element kills every partner. The two are the antisymmetric plain algebra and the antisymmetric quaternionic sesqualgebra, and the elements that kill every partner are exactly the scalar ones, the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$.
- In two structures the annihilator of every nonzero element is a hyperplane of dimension three. In the symmetric quaternionic algebra it is the hyperplane $Q_tQ_{1t}+(\vec Q,\vec Q_1)=0$, and in the symmetric plain sesqualgebra it is the hyperplane $Q_t\overline{Q_{1t}}+(\vec Q,\overline{\vec Q_1})=0$.
- In the two alternating structures every element lies in its own annihilator, because $\tilde Q\diamond\tilde Q=0$, and the two are the antisymmetric plain algebra and the antisymmetric quaternionic algebra. In the two conjugate-alternating structures, the antisymmetric plain sesqualgebra and the antisymmetric quaternionic sesqualgebra, the element lies in its own annihilator exactly when $\tilde Q\diamond\tilde Q$ vanishes, which is so at every element with real coefficients and can fail at an element with complex coefficients. In the other eight structures only some elements do.
- In the four general products an element of nonzero norm $\langle\cdot\rangle_{\natural}$ is invertible and its annihilator is $\{0\}$. At an element of norm $\langle\cdot\rangle_{\natural}$ zero the four planes are one plane read through the two conjugations, $A_{\natural}(\tilde Q)=A_{\text{plain}}(\tilde Q^{\natural})$, $A_{*}(\tilde Q)=A_{\text{plain}}(\tilde Q)^{*}$ and $A_{\natural*}(\tilde Q)=A_{\text{plain}}(\tilde Q^{\natural})^{*}$.

The single example that ties them together is $\tilde Q=e_t+i\vec e_x$, whose norm $\langle\cdot\rangle_{\natural}$ is $1-1=0$. Its plain plane is $\mathbb{C}\{e_t-i\vec e_x,\ \vec e_z+i\vec e_y\}$, its natural plane is $\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y+i\vec e_z\}$, its general plain sesquilinear plane is $\mathbb{C}\{\vec e_x+ie_t,\ \vec e_y+i\vec e_z\}$, and its general quaternionic sesquilinear plane is $\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y-i\vec e_z\}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | one of the twelve products of $\mathbb{B}$ |
| $\tilde Q\tilde Q_2$, $\tilde Q\tilde Q_2^{*}$, $\tilde Q^{\natural}\tilde Q_2$, $\tilde Q^{\natural}\tilde Q_2^{*}$ | the four general products |
| $A_\star(\tilde Q)$, $B_\star(\tilde Q)$ | the left and the right annihilator of $\tilde Q$ in the product $\star$, the kernels of $L_{\tilde Q}$ and $R_{\tilde Q}$ |
| $A_{\text{plain}},A_{*},A_{\natural},A_{\natural*}$ | the left annihilators in the plain, the general plain sesquilinear, the natural and the general quaternionic sesquilinear product |
| $A_{\text{plain}}(\tilde Q)=\{\tilde Q_2:\tilde Q\tilde Q_2=0\}$ | the kernel of the left multiplication in the plain product, $A_{\text{plain}}(\tilde Q)$ |
| $\mathbb{C}\{u,v\}$, $\mathbb{C}u$ | a complex plane and a complex line, given by their generators |
| $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the general quaternionic bilinear algebraic norm, also called the quaternionic norm $\mathrm{Norm}(\tilde Q)$; zero exactly on the cone, and **the deciding norm of every annihilator in this article** |
| $\langle\cdot\rangle$, $\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural}$, $\langle\cdot\rangle_{\natural*}$ | the four algebraic norms of the twelve products, carried in the pairs $(\mathrm{GPA},\mathrm{SPA})$, $(\mathrm{GPS},\mathrm{SPS})$, $(\mathrm{GQA},\mathrm{SQA})$, $(\mathrm{GQS},\mathrm{SQS})$; the four antisymmetrisations carry none |
| $\langle\tilde Q,\tilde Q_2\rangle_{\natural}=Q_tQ_{2t}+(\vec Q,\vec Q_2)$ | the general quaternionic bilinear form, the product of $\mathrm{SQA}$ up to $e_t$ |
| $\langle\tilde Q,\tilde Q_2\rangle_{*}=Q_t\overline{Q_{2t}}+(\vec Q,\overline{\vec Q_2})$ | the Hermitian form, the product of $\mathrm{SPS}$ up to $e_t$ |
| $\tilde Q^{\perp}$ | the hyperplane $\{\langle\tilde Q,\tilde Q_1\rangle_{\natural}=0\}$ or $\{\langle\tilde Q,\tilde Q_1\rangle_{*}=0\}$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$, $\mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures, read in the table of §*The Twelve Annihilators* |
| ${}^{*}$, ${}^{\natural}$ | the Hermitian conjugation, $\overline{Q_{1t}}e_t-\sum_{\mu\in\{x,y,z\}}\overline{Q_{1\mu}}\vec e_\mu$, and the natural conjugation, $Q_{1t}e_t-\vec Q_1$ |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |

## Further Reading

- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the cone, the twelve zero-divisor sets and the one-sided inverse equations.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the annihilator stated once for a general product.
- [The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](the-algebraic-structures-over-the-biquaternion-c-space.html), for the twelve names and their three-letter codes.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve products and their class-preserving exchange.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four algebraic norms $\langle\cdot\rangle$, $\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural}$, $\langle\cdot\rangle_{\natural*}$, the two products that carry each, and the norm $\langle\cdot\rangle_{\natural}$ that decides the annihilators.
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the kernels of the multiplications read in the matrix model.
- [Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space](annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.html), for the reading in the three companion structures of the quaternion space, where the elements that annihilate every partner are tabulated.

The owners of the twelve subsections, grouped by the article that carries them, are:

- [Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for $\mathrm{SPA}$, $\mathrm{APA}$, $\mathrm{SQA}$, $\mathrm{AQA}$, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{SQS}$ and $\mathrm{AQS}$.
- [Annihilators of the General Quaternionic Algebra](annihilators-of-the-general-quaternionic-algebra.html), for $\mathrm{GQA}$.
- [Annihilators of the General Plain Sesqualgebra](annihilators-of-the-general-plain-sesqualgebra.html), for $\mathrm{GPS}$.
- [Annihilators of the General Quaternionic Sesqualgebra](annihilators-of-the-general-quaternionic-sesqualgebra.html), for $\mathrm{GQS}$.
