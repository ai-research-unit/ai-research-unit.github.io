# __Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra__

## Introduction

The central value $+1$ and the idempotents are the two faces of one subject in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$: a **root of one** is an element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = e_t$, an **idempotent** is an element $\tilde\Pi$ with $\tilde\Pi\star\tilde\Pi = \tilde\Pi$, and both are read from the square of the same multiplication, the **general quaternionic sesquilinear product**

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*} ,
$$

whose rule, scalar–vector form and table are *Introduction to the General Quaternionic Sesqualgebra*, and whose place among the four general products is *The Four General Products and Their Relations*. A root of a central value and an idempotent are notions of a **product** and not of an algebra: the root of $\lambda$ is defined for a general product in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §6, and the idempotent there as well. The article treats the roots of one first and the idempotents after, and it reads both from the square identity $\tilde Q_2\star\tilde Q_2 = (\overline{\tilde Q}_2\tilde Q_2)^{\natural}$ of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*.

**What the article does not do.** The roots of the central value $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*; the roots of a **general** element are *Square Roots of a General Element in the General Quaternionic Sesqualgebra*, and the central value is the special case of that problem. The roots of $-1$ are **not** a subject of this article; they are quoted in one short paragraph at the end of §*The Roots of One*, they are used by no other passage, and the idempotent part rests on the roots of $+1$ alone. The zero divisors are *Zero Divisors of the General Quaternionic Sesqualgebra*, the criterion of invertibility of the plain algebra that the article uses is *Norm and Invertibility in the General Quaternionic Sesqualgebra*, and the four idempotent sets of the four general products are compared in *The Four General Products and Their Relations* §*The Squares, the Idempotents and the Roots*.

**The results.** In the general quaternionic sesquilinear product the square reduces to $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$, so a root of $\lambda$ exists only for real $\lambda$, and for real $\lambda$ the nonzero roots are the family $\tilde\Xi = c(\vec u+it)$ with $(t^2-1)\lvert c\rvert^2 = \lambda$, of real dimension four, together with the central circle $\lvert a\rvert^2 = \lambda$ when $\lambda>0$. The value $+1$ takes the slopes $\lvert t\rvert>1$, with $\lvert c\rvert^2 = 1/(t^2-1)$, beside the central circle, and contains $e_t$ and $i$; every root of one is a unit of the plain algebra. The idempotents are exactly the two trivial elements $0$ and $e_t$ together with the two-parameter family $\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ over the real vectors $\vec u$ with $(\vec u,\vec u)=1$; every nontrivial idempotent has central square $1$, so it is a unit of the plain algebra with inverse its own natural conjugate $-\tfrac12e_t-\tfrac{\sqrt3}{2}\vec u$, and it lies outside the Hermitian subspace, being neither Hermitian nor skew-Hermitian. The four general products carry four different idempotent sets, and only this one has nontrivial idempotents that are units of the plain algebra; the idempotents of the sibling sesquilinear product are isotropic here, each of them square-zero. Each section below states its result first and then proves it.

## The Reduction of the Root Equation

**The square of a root reduces to $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$, so the equation $\tilde\Xi\star\tilde\Xi = \lambda e_t$ is the plain equation $\overline{\tilde\Xi}\tilde\Xi = \lambda e_t$ and forces $\lambda$ real; on coordinates the equation is the system $\xi_t^{2}+\xi'^{2}_t-\lvert\vec\xi\rvert^{2}-\lvert\vec\xi'\rvert^{2} = \lambda$, $\xi_t\vec\xi+\xi'_t\vec\xi' = 0$, $\vec\xi\times\vec\xi' = 0$.**

**Proposition (the central square of a root).** For every $\tilde\Xi$,

$$
\tilde\Xi\star\tilde\Xi = \bigl(\overline{\tilde\Xi}\,\tilde\Xi\bigr)^{\natural} ,
$$

so $\tilde\Xi$ is a root of $\lambda$ if and only if $\overline{\tilde\Xi}\tilde\Xi = \lambda e_t$; in particular the equation $\tilde\Xi\star\tilde\Xi = \lambda e_t$ forces $\lambda\in\mathbb{R}$.

**Proof.** The identity is the one of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, proved on the coordinates. Its scalar part is the **Krein form** $\mathrm{Sc}(\overline{\tilde\Xi}\tilde\Xi) = \sum_\mu \varepsilon_\mu\lvert \Xi_\mu\rvert^2$ with $\varepsilon = (1,-1,-1,-1)$, a real number; the scalar part of the left side is therefore real, and the scalar part of $\lambda e_t$ is $\lambda$, whence $\lambda\in\mathbb{R}$.

**Proposition (the coordinate system).** Write $\tilde\Xi = a+\vec q$ with $a = \xi_t+i\xi'_t$, $\xi_t,\xi'_t\in\mathbb{R}$, and $\vec q = \vec\xi+i\vec\xi'$, $\vec\xi,\vec\xi'\in\mathbb{R}^3$. Then $\tilde\Xi\star\tilde\Xi = \lambda e_t$ if and only if

$$
\xi_t^2+\xi'^2_t-\lvert\vec\xi\rvert^2-\lvert\vec\xi'\rvert^2 = \lambda , \qquad \xi_t\vec\xi+\xi'_t\vec\xi' = 0 , \qquad \vec\xi\times\vec\xi' = 0 .
$$

**Proof.** The plain product $\overline{\tilde\Xi}\tilde\Xi = (\overline{a}+\overline{\vec q})(a+\vec q)$ has scalar part $\xi_t^2+\xi'^2_t-\lvert\vec\xi\rvert^2-\lvert\vec\xi'\rvert^2$; its vector part $\overline{a}\vec q+a\overline{\vec q}+\overline{\vec q}\times\vec q$ is $2(\xi_t\vec\xi+\xi'_t\vec\xi')+2i\,\vec\xi\times\vec\xi'$, a real vector plus $i$ times a real vector, since $\overline{a}\vec q+a\overline{\vec q} = 2(\xi_t\vec\xi+\xi'_t\vec\xi')$ and $\overline{\vec q}\times\vec q = (\vec\xi-i\vec\xi')\times(\vec\xi+i\vec\xi') = 2i\,\vec\xi\times\vec\xi'$. Setting the three parts equal to those of $\lambda e_t$ gives the system; the same computation at $\lambda = 0$ is the square-zero equation of *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.

## The Root Set of a Central Value

**A central value $\lambda$ has a root exactly when $\lambda$ is real, and then the nonzero roots are exactly the family $\tilde\Xi = c(\vec u+it)$ with $c\in\mathbb{C}^{*}$, $\lvert\vec u\rvert = 1$, $t\in\mathbb{R}$ and $(t^2-1)\lvert c\rvert^{2} = \lambda$, of real dimension four for $\lambda\neq0$, together with the central circle $\lvert a\rvert^{2} = \lambda$ when $\lambda>0$; the value $\lambda = 0$ is not pursued here, its roots being the square-zero family of *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.**

**Theorem (the roots of a central value).** Let $\lambda\in\mathbb{C}$. The value $\lambda$ has a root in $\star$ if and only if $\lambda\in\mathbb{R}$, and then the nonzero roots are exactly

$$
\boxed{\; \tilde\Xi = c\bigl(\vec u + it\bigr) , \qquad c\in\mathbb{C}^{*} , \quad \vec u\in\mathbb{R}^3 , \quad \sum_{\mu\in\{x,y,z\}}u_\mu^2 = 1 , \quad t\in\mathbb{R} , \quad (t^2-1)\lvert c\rvert^2 = \lambda \;},
$$

together with, when $\lambda>0$, the **central circle** of the scalar roots $\tilde\Xi = ae_t$ with $\lvert a\rvert^2 = \lambda$.

**Proof.** Let $\tilde\Xi = a+\vec q$ satisfy the coordinate system. The equation $\vec\xi\times\vec\xi' = 0$ makes the real vectors $\vec\xi$ and $\vec\xi'$ parallel. When $\vec q = 0$ the system reduces to $\lvert a\rvert^2 = \lambda$, so $\lambda>0$ and $a$ runs over the circle $\lvert a\rvert^2 = \lambda$; the value $\lambda = 0$ gives $a = 0$, which is not a root because a root is nonzero. When $\vec q \neq 0$ one writes $\vec q = c\vec u$ with $c\in\mathbb{C}^{*}$ and $\vec u$ a real unit vector, and the equation $\xi_t\vec\xi+\xi'_t\vec\xi' = 0$ becomes $\operatorname{Re}(\overline{a}c) = 0$; when $a \neq 0$ this says $c = ita$ with $t\in\mathbb{R}$, and when $a = 0$ the same relation holds with the parameter $t = 0$, the first equation giving $\lvert c\rvert^2 = -\lambda$. Substituting $a = itc$ into the first equation gives $(t^2-1)\lvert c\rvert^2 = \lambda$, and the parametrization $a = itc$, $\vec q = c\vec u$ is $\tilde\Xi = c(\vec u+it)$. The family is well parametrized: for $\lambda\neq0$ the modulus $\lvert c\rvert$ is determined by $t$ through the displayed equation, while the argument of $c$ and the direction $\vec u$ are free.

**Corollary (the shape of the root set and its dimension).** For $\lambda\neq0$ the root set is a real four-dimensional family, $t$ of one real parameter, the argument of $c$ of one and the direction $\vec u$ of two, with $\lvert c\rvert$ determined by $t$; for $\lambda>0$ it carries in addition the real one-dimensional central circle; and at $\lambda = 0$ the equation $(t^2-1)\lvert c\rvert^2 = 0$ gives $t = \pm1$, so the family is $c(\vec u\pm i)$, the square-zero set of *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.

**Proof.** The parameter count is the one stated, and the value $\lambda = 0$ is read in the cited article.

**Corollary (the central square of a root).** A root of the real value $\lambda$ in the parametrization $\tilde\Xi = c(\vec u+it)$ has central square

$$
C(\tilde\Xi) = c^2\,(1-t^2) ,
$$

and a scalar root has $C(ae_t) = a^2$.

**Proof.** The central square of $c(\vec u+it)$ is $c^2$ times the sum of the squares of the four coordinates of $\vec u+it$, which is $\sum_{\mu\in\{x,y,z\}}u_\mu^2 + (it)^2 = 1-t^2$; for the scalar root it is $a^2$. The value vanishes exactly at $\lambda = 0$, the square-zero condition of *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.

## The Roots of One

**The roots of $+1$ are the central circle $\lvert a\rvert^{2} = 1$ together with the family $\lvert t\rvert>1$ with $\lvert c\rvert^{2} = 1/(t^{2}-1)$ and $\lvert\vec u\rvert = 1$; the elements $e_t$ and $i$ are roots, no root of one is square-zero, and every root of one is a unit of the plain algebra.**

**Theorem (the roots of one).** The roots of $+1$ in $\star$ are exactly the central circle $\lvert a\rvert^2 = 1$ together with the family

$$
\boxed{\; \tilde\Xi = c\bigl(\vec u + it\bigr) , \qquad c\in\mathbb{C}^{*} , \quad \lvert t\rvert>1 , \quad \lvert c\rvert^2 = \frac{1}{t^2-1} , \qquad \lvert\vec u\rvert = 1 \;},
$$

a real four-dimensional family beside the circle; the elements $e_t$ and $i$ are roots, and no root of $+1$ is square-zero.

**Proof.** The value is positive, so the central circle is present and is read off the case $\vec q = 0$; the family is $(t^2-1)\lvert c\rvert^2 = 1$, with $t^2>1$ and $\lvert c\rvert^2 = 1/(t^2-1)$. The elements $e_t$ and $i$ are the scalar roots of modulus one. A square-zero element would give $\lambda = 0$, so it is not a root of $+1$.

**Corollary (the roots of one are units of the plain algebra).** Every root of $+1$ has central square $C(\tilde\Xi)\neq0$: $C = c^2(1-t^2)$ with $t^2>1$ on the family, and $C = a^2$ with $\lvert a\rvert^2 = 1$ on the circle. Hence every root of one is a **unit of the plain algebra**, and none is a zero divisor.

**Proof.** The formula is the corollary of §*The Root Set of a Central Value*. On the family the real factor $t^2-1$ is positive, and on the circle $\lvert a\rvert^2 = 1$, so $C(\tilde\Xi)\neq0$ throughout. The criterion of invertibility of the plain algebra is $C\neq0$ (*Norm and Invertibility in the General Quaternionic Sesqualgebra*), and a nonzero element of central square $0$ is a zero divisor (*Zero Divisors of the General Quaternionic Sesqualgebra*).

**The value $-1$.** Multiplication by the central imaginary does not produce the roots of $-1$ from the roots of $+1$: the product is conjugate-linear in its second slot, so $(i\tilde\Xi)\star(i\tilde\Xi) = \lvert i\rvert^{2}\,\tilde\Xi\star\tilde\Xi = \tilde\Xi\star\tilde\Xi$ for every $\tilde\Xi$, and the value is unchanged rather than flipped. The roots of $-1$ are read from the same formula at $\lambda = -1$: they are the elements $\tilde\Xi = c(\vec u+it)$ with $\lvert t\rvert<1$ and $\lvert c\rvert^2 = 1/(1-t^2)$, a set of the same real dimension four, with no central circle and no pure scalar; the basis vectors $\vec e_x$, $\vec e_y$, $\vec e_z$ are roots, so the set is non-empty, and every one of its elements is a unit of the plain algebra. This is the negative sign of the family and nothing else.

## The Idempotent Equation

**An element $\tilde\Pi$ is idempotent exactly when $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{\natural}$, equivalently when the coordinates satisfy $Q_{2t}\in\mathbb{R}$, $Q_{2t} = \lvert Q_{2t}\rvert^{2}-\sum_{\mu\in\{x,y,z\}}\lvert Q_{2,\mu}\rvert^{2}$, $(2Q_{2t}+1)\vec a = 0$ and $\vec a\times\vec b = -\tfrac12\vec b$ for $\vec Q_2 = \vec a+i\vec b$.**

### The Criterion

**Definition.** An element $\tilde\Pi$ is **idempotent** for the multiplication when $\tilde\Pi \star \tilde\Pi = \tilde\Pi$.

**Proposition (the criterion).** An element $\tilde Q_2$ is idempotent if and only if

$$
\overline{\tilde Q}_2\,\tilde Q_2 = \tilde Q_2^{\natural} .
$$

**Proof.** The equation $\tilde Q_2 \star \tilde Q_2 = \tilde Q_2$ reads $\tilde Q_2^{\natural}\tilde Q_2^{*} = \tilde Q_2$. The map ${}^{\natural}$ is an involution and an anti-automorphism of the plain product, and $(\tilde Q_2^{*})^{\natural} = \overline{\tilde Q}_2$ because the two conjugations commute and ${}^{*} = \overline{\cdot} \circ {}^{\natural}$. Applying ${}^{\natural}$ to the equation therefore gives

$$
\bigl(\tilde Q_2^{\natural}\tilde Q_2^{*}\bigr)^{\natural}
= (\tilde Q_2^{*})^{\natural}\,(\tilde Q_2^{\natural})^{\natural}
= \overline{\tilde Q}_2\,\tilde Q_2 = \tilde Q_2^{\natural} ,
$$

which is the criterion. Conversely, applying ${}^{\natural}$ to the criterion returns the original equation, so the two are equivalent.

The criterion is the form in which the equation is read on the coordinates, since the left-hand side is a plain product and the right-hand side a conjugation, and it is the form used in *Square Roots of a General Element in the General Quaternionic Sesqualgebra*.

### The Equation on the Coordinates

**Proposition (the coordinate equations).** Write $\tilde Q_2 = Q_{2t} + \vec Q_2$ with $\vec Q_2 = \vec a + i\vec b$, where $\vec a$ and $\vec b$ are vectors with real coefficients. Then $\tilde Q_2$ is idempotent if and only if

$$
Q_{2t} \in \mathbb{R} , \qquad Q_{2t} = \lvert Q_{2t}\rvert^{2} - \sum_{\mu\in\{x,y,z\}}\lvert Q_{2,\mu}\rvert^{2} , \qquad (2Q_{2t} + 1)\vec a = 0 , \qquad \vec a \times \vec b = -\tfrac12 \vec b .
$$

**Proof.** The left-hand side of the criterion is the plain product of $\overline{\tilde Q}_2 = \overline{Q_{2t}} + \overline{\vec Q_2}$ and $\tilde Q_2 = Q_{2t} + \vec Q_2$, whose scalar–vector form is that of *The Four General Products and Their Relations*,

$$
\overline{\tilde Q}_2\,\tilde Q_2 = \overline{Q_{2t}}Q_{2t} - (\overline{\vec Q_2},\vec Q_2) + \overline{Q_{2t}}\vec Q_2 + Q_{2t}\overline{\vec Q_2} + \overline{\vec Q_2}\times\vec Q_2 ,
$$

the dot and cross products being the general plain bilinear ones. The right-hand side is $\tilde Q_2^{\natural} = Q_{2t} - \vec Q_2$. Equating scalar parts gives $Q_{2t} = \lvert Q_{2t}\rvert^{2} - \sum_{k}\lvert Q_{2,\mu}\rvert^{2}$, which exhibits $Q_{2t}$ as the difference of two real numbers and hence real; writing $Q_{2t} = u \in \mathbb{R}$ and $\vec Q_2 = \vec a + i\vec b$, the same equation is the second displayed relation. Equating vector parts gives $\overline{Q_{2t}}\vec Q_2 + Q_{2t}\overline{\vec Q_2} + \overline{\vec Q_2}\times\vec Q_2 = -\vec Q_2$, that is

$$
u(\vec Q_2 + \overline{\vec Q_2}) + \overline{\vec Q_2}\times\vec Q_2 = -\vec Q_2 ,
$$

using $Q_{2t} = u$ real. Now $\vec Q_2 + \overline{\vec Q_2} = 2\vec a$ and $\overline{\vec Q_2}\times\vec Q_2 = (\vec a - i\vec b)\times(\vec a + i\vec b) = 2i\,\vec a\times\vec b$, the two real cross terms cancelling and the two mixed terms doubling. Substituting and separating the real and the imaginary coefficients of the vector equation gives $2u\vec a = -\vec a$ and $2\vec a\times\vec b = -\vec b$, which are the last two displayed relations.

The two vector relations are of different kinds: the first constrains $\vec a$ alone, the second couples $\vec a$ and $\vec b$ through the cross product.

## The Classification of the Idempotents

**The idempotents are exactly $0$, $e_t$ and the family $\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ with $\vec u$ a real unit vector of the vector subspace and $(\vec u,\vec u)=1$; the two trivial idempotents have vanishing vector part, and every nontrivial idempotent has central square $1$ and is a unit of the plain algebra with inverse $-\tfrac12e_t-\tfrac{\sqrt3}{2}\vec u$.**

### The Two Trivial Idempotents

**Proposition.** The elements $0$ and $e_t$ are idempotent, and they are the only idempotents with vanishing vector part.

**Proof.** Directly, $0 \star 0 = 0$ and $e_t \star e_t = e_t^{\natural}e_t^{*} = e_t$. Conversely let $\tilde Q_2 = Q_{2t} e_t$ be a scalar element, so that $\vec a = \vec b = 0$. The coordinate equations reduce to $Q_{2t} \in \mathbb{R}$ and $Q_{2t} = Q_{2t}^{2}$, whose solutions are $Q_{2t} = 0$ and $Q_{2t} = 1$.

### The Family

**Theorem (the classification).** The idempotents of the multiplication are exactly

$$
\boxed{\; 0 , \qquad e_t , \qquad\text{and}\qquad \tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u , \qquad \vec u\in\mathrm{Vect}(\mathbb{B})_{\mathbb{R}} , \qquad (\vec u,\vec u)=1 \;}.
$$

**Proof.** Let $\tilde Q_2$ be idempotent and write $\tilde Q_2 = u + \vec a + i\vec b$ as above. The proof splits on whether the real vector $\vec a$ vanishes.

Suppose first that $\vec a \neq 0$. The relation $(2u+1)\vec a = 0$ forces $u = -\tfrac12$. The relation $\vec a\times\vec b = -\tfrac12\vec b$ says that $\vec b$ lies in the kernel of the operator $\vec w\mapsto\vec a\times\vec w+\tfrac12\vec w$, that is, that $\vec b$ is a kernel vector of $L_{\vec a} + \tfrac12 I$ with $L_{\vec a}(\vec w) = \vec a\times\vec w$. The operator $L_{\vec a}$ is antisymmetric with respect to the real definite structure, since $(\vec a\times\vec w,\vec y) = -(\vec w,\vec a\times\vec y)$; an antisymmetric real operator has purely imaginary spectrum, together with the eigenvalue $0$, so $L_{\vec a} + \tfrac12 I$ has spectrum $\{ \tfrac12 \} \cup \{ \tfrac12 \pm i\lvert \vec a\rvert \}$, which does not contain $0$. Hence $L_{\vec a} + \tfrac12 I$ is invertible and $\vec b = 0$. The coordinate equation $u = u^{2} - \lvert\vec Q_2\rvert^{2}$ then gives $\lvert\vec Q_2\rvert^{2} = u^{2} - u = \tfrac14 + \tfrac12 = \tfrac34$, that is $(\vec Q_2,\vec Q_2) = \tfrac34$ for $\vec Q_2 = \vec a$, so the idempotent is $\tilde\Pi(\vec u)$ with the real unit vector $\vec u = \tfrac{2}{\sqrt3}\vec Q_2$; this is the family.

Suppose next that $\vec a = 0$. The relation $(2u+1)\vec a = 0$ is vacuous, and the relation $\vec a\times\vec b = -\tfrac12\vec b$ reads $\vec b = 0$. Then $\vec Q_2 = 0$ and the coordinate equation gives $u = u^{2}$, that is $u = 0$ or $u = 1$. These are the two trivial idempotents.

**Remark.** The theorem classifies the idempotents of the whole algebra. The group article *Introduction to the General Quaternionic Sesqualgebra* states the classification on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the coefficients are real and the criterion reads $\tilde Q_2^{2} = \tilde Q_2^{\natural}$; the two statements agree, and every nontrivial idempotent lies in that subspace, since the family has real coordinates. No idempotent has a nonzero imaginary part of the scalar coordinate and none has a non-real component in the vector coordinates.

## The Idempotents and the Roots of One

**The idempotents are not the roots of one halved: the map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ carries the roots of $+1$ to idempotents only at the two trivial roots $\pm e_t$, and the candidate inverse $2\tilde\Pi-e_t = -2e_t+\sqrt{3}\vec u$ of a nontrivial idempotent has square $e_t+4\sqrt{3}\vec u$, not $e_t$.**

In a product with a two-sided unit the **halving map** $\tilde\Pi = \tfrac12(e_t+\tilde\Xi)$ and its inverse $\tilde\Xi = 2\tilde\Pi-e_t$ carry the roots of $+1$ onto the idempotents, because $\tilde\Xi^{2} = e_t$ exactly when $\tilde\Pi^{2} = \tilde\Pi$. This product has **no unit** (*The Two One-Sided Actions and the Absence of a Unit*), and the map fails here; the two sets are different and are read independently.

**Proposition (the halving map fails).** Let $\tilde\Xi$ be a root of $+1$ and put $\tilde\Pi = \tfrac12(e_t+\tilde\Xi)$. Then $\tilde\Pi$ is idempotent if and only if $\tilde\Xi = e_t$ or $\tilde\Xi = -e_t$, giving $\tilde\Pi = e_t$ and $\tilde\Pi = 0$; for every other root of one the halved element is not idempotent.

**Proof.** With $\tilde\Xi\star\tilde\Xi = e_t$,

$$
\tilde\Pi\star\tilde\Pi = \tfrac14\,(e_t+\tilde\Xi)^{\natural}(e_t+\tilde\Xi)^{*}
= \tfrac14\bigl(e_t + \tilde\Xi^{\natural} + \tilde\Xi^{*} + \tilde\Xi^{\natural}\tilde\Xi^{*}\bigr)
= \tfrac12 e_t + \tfrac14\bigl(\tilde\Xi^{\natural} + \tilde\Xi^{*}\bigr) ,
$$

using $\tilde\Xi^{\natural}\tilde\Xi^{*} = \tilde\Xi\star\tilde\Xi = e_t$. The equation $\tilde\Pi\star\tilde\Pi = \tilde\Pi = \tfrac12e_t+\tfrac12\tilde\Xi$ is therefore $\tilde\Xi^{\natural}+\tilde\Xi^{*} = 2\tilde\Xi$. Writing $\tilde\Xi = x+\vec v$, this is $\bar x - \vec v + x - \overline{\vec v} = 2x + 2\vec v$, that is $(\bar x - x) - (\vec v + \overline{\vec v}) = 2\vec v$. The scalar part gives $x\in\mathbb{R}$ and the vector part gives $\vec v + \overline{\vec v} + 2\vec v = 0$; writing $\vec v = \vec a+i\vec b$ this is $4\vec a + 2i\vec b = 0$, so $\vec a = \vec b = 0$ and $\vec v = 0$. The root $\tilde\Xi$ is then the real scalar $x$ with $x^{2} = 1$, that is $x = \pm1$.

**Proposition (the candidate inverse is not a root).** For the nontrivial idempotent $\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ the element $\tilde\Xi = 2\tilde\Pi(\vec u)-e_t = -2e_t+\sqrt{3}\vec u$ has

$$
\tilde\Xi\star\tilde\Xi = e_t + 4\sqrt{3}\vec u ,
$$

which is not $e_t$ for $\vec u\neq0$.

**Proof.** The element is real, so $\tilde\Xi^{\natural} = \tilde\Xi^{*} = -2e_t-\sqrt{3}\vec u$ and $\tilde\Xi\star\tilde\Xi = \tilde\Xi^{\natural}\tilde\Xi^{*} = (-2e_t-\sqrt{3}\vec u)^{2} = 4e_t + 4\sqrt{3}\vec u + 3\vec u^{2}$. Since $\vec u^{2} = -(\vec u,\vec u)e_t = -e_t$, this is $4e_t+4\sqrt{3}\vec u-3e_t = e_t+4\sqrt{3}\vec u$.

**Remark.** The two sets therefore differ, and they meet only at $e_t$: an element that is both a root of one and an idempotent satisfies $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ and $\tilde\Pi\star\tilde\Pi = e_t$, so $\tilde\Pi = e_t$; the element $0$ is an idempotent but is excluded from the roots, which are nonzero by definition. The idempotent part of the article rests on the idempotent equation alone, and the roots of $-1$ play no part in it.

## The Central Square of an Idempotent, and the Units

**Every nontrivial idempotent has central square $1$, hence is a unit of the plain algebra with inverse its own natural conjugate $-\tfrac12e_t-\tfrac{\sqrt3}{2}\vec u$; the two trivial idempotents have central squares $C(0) = 0$ and $C(e_t) = 1$.**

**Proposition.** Every nontrivial idempotent has central square $1$,

$$
C\bigl(\tilde\Pi(\vec u)\bigr) = \tfrac14 + \tfrac34(\vec u,\vec u) = 1 ,
$$

and hence is a unit of the plain algebra, with inverse its own natural conjugate, $\tilde\Pi(\vec u)^{-1} = \tilde\Pi(\vec u)^{\natural} = -\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u$. The two trivial idempotents have central squares $C(0) = 0$ and $C(e_t) = 1$.

**Proof.** The central square of $\tilde\Pi(\vec u)$ is $\lvert-\tfrac12\rvert^{2} + \tfrac34(\vec u,\vec u) = \tfrac14 + \tfrac34 = 1$. An element of central square $1$ is a unit of the plain algebra because $\tilde Q_1\tilde Q_1^{\natural} = C(\tilde Q_1)e_t = e_t$, and $\tilde\Pi(\vec u)^{\natural} = -\tfrac12e_t - \tfrac{\sqrt3}{2}\vec u$ by the linearity of ${}^{\natural}$. The values for $0$ and $e_t$ are immediate.

The proposition is the sharpest difference of this multiplication from its three companions. Among the four general products, only this one has a nontrivial idempotent, and the nontrivial idempotents of the other three are degenerate in a way the central square detects: they are zero divisors.

**Remark (which unit, and which algebra).** The word **unit** in this section and in the summaries is the unit of the **plain algebra** $\tilde Q_1\tilde Q_2$ and never the unit of the multiplication $\star$: the multiplication $\star$ has **no unit at all**, its two actions of $e_t$ being the star $\tilde Q_2\star e_t = \tilde Q_2^{\natural}$ and the natural conjugation $e_t\star\tilde Q_2 = \tilde Q_2^{*}$ (*The Two One-Sided Actions and the Absence of a Unit*). The element $\tilde\Pi(\vec u)^{-1} = -\tfrac12e_t-\tfrac{\sqrt3}{2}\vec u$ is the inverse of $\tilde\Pi(\vec u)$ in the plain algebra, $\tilde\Pi\tilde\Pi^{-1} = e_t$, and it is an inverse in no sense of the multiplication $\star$, which has no inverse because it has no unit. The corrected claim is therefore the one of *Norm and Invertibility in the General Quaternionic Sesqualgebra*: the nontrivial idempotents of the block are units of the plain algebra, and the block has no unit.

## The Idempotents of the Other Multiplications

**The four general products have four different idempotent sets: the plain product and the sibling sesquilinear product have infinite families of nontrivial idempotents that are zero divisors, the sibling bilinear product has only $0$ and $e_t$, and only this product has nontrivial idempotents that are units of the plain algebra.**

### The Idempotents of the Plain Product

The idempotents of the plain product $\tilde Q_1\tilde Q_2$ are the idempotents of the algebra, classified in *Idempotents of the General Plain Algebra*: the elements $\tfrac12(e_t + \tilde\Xi)$ with $\tilde\Xi$ a **root of one of the plain algebra**, $\tilde\Xi\tilde\Xi = e_t$, with the two trivial idempotents at the two trivial roots $\tilde\Xi = \pm e_t$. They fall into the Hermitian family, where $\tilde\Xi=i\vec u$ with $\vec u$ a real unit vector, and the non-Hermitian family, where it is not.

**Proposition.** Every nontrivial idempotent of the plain product is a zero divisor and is not a unit.

**Proof.** Let $\tilde\Pi = \tfrac12(e_t + \tilde\Xi)$ with $\tilde\Xi\tilde\Xi = e_t$, and write $\tilde\Xi = \xi_t + \vec v$ with $\xi_t$ the scalar part and $\vec v$ the vector part. The equation $\tilde\Xi\tilde\Xi = e_t$ reads $\xi_t^{2} - (\vec v,\vec v) = 1$ and $2\xi_t\vec v = 0$. Either $\xi_t\neq0$, when $\vec v = 0$ and $\xi_t = \pm1$, giving the two trivial idempotents; or $\xi_t = 0$ and $(\vec v,\vec v) = -1$. In the second case the central square of $\tilde\Pi$ is

$$
C(\tilde\Pi) = \tfrac14\bigl(e_t + \tilde\Xi + \tilde\Xi^{\natural} + C(\tilde\Xi)e_t\bigr)
= \tfrac14\bigl(1 + 2\xi_t + C(\tilde\Xi)\bigr) = \tfrac14\bigl(1 + 0 - 1\bigr) = 0 ,
$$

since $C(\tilde\Xi) = \xi_t^{2}+(\vec v,\vec v) = -1$, and $\tilde\Xi+\tilde\Xi^{\natural} = 2\xi_t = 0$. The element is nonzero of central square $0$, so by the criterion of *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors* it is a zero divisor and not a unit of the plain algebra. The witness $\tilde\Xi=i\vec u$ has $\xi_t = 0$ and $(\vec v,\vec v) = -(\vec u,\vec u) = -1$, so every Hermitian idempotent of the algebra is a nontrivial example.

**Remark.** The family $\tfrac12(e_t+\tilde\Xi)$ is the exact opposite of the family of this article: it is infinite and it consists entirely of zero divisors, whereas the family of this article is infinite and consists entirely of units of the plain algebra. The plain product and this one have their nontrivial idempotents disjoint, and the difference is carried by the sign of the vector contribution to the central square.

### The Idempotents of the Sibling Sesquilinear Product

The sibling general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ is the derived operation of the algebra with its star conjugation (*Introduction to the General Plain Sesqualgebra*). Its idempotents are exactly the Hermitian idempotents of the algebra,

$$
\tilde\Pi_+(\tilde\Xi) = \tfrac12\bigl(e_t + \tilde\Xi\bigr) , \qquad \vec u \in \mathbb{R}^{3} , \quad \lvert\vec u\rvert = 1 ,
$$

the pure states of *Idempotents of the General Plain Algebra*.

**Proposition.** Every nontrivial idempotent of the sibling sesquilinear product is isotropic for this multiplication,

$$
\tilde\Pi_+(\tilde\Xi) \star \tilde\Pi_+(\tilde\Xi) = 0 .
$$

**Proof.** Let $\tilde H = \tfrac12(e_t + \tilde\Xi)$ with $\vec u$ a real unit vector; it is Hermitian, $\tilde H^{*} = \tilde H$, and its coordinates are $H_t = \tfrac12$, $H_\mu = \tfrac{i}{2}u_\mu$. Its central square is $C(\tilde H) = \tfrac14 - \tfrac14\sum_{\mu\in\{x,y,z\}}u_\mu^{2} = 0$, as for the plain product. For a Hermitian element $\overline{\tilde H} = \tilde H^{\natural}$, and $\tilde H\star\tilde H = (\overline{\tilde H}\tilde H)^{\natural}$ by the square identity of *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*; here the direct computation is available: $\tilde H \star \tilde H = \tilde H^{\natural}\tilde H^{*} = \tilde H^{\natural}\tilde H = C(\tilde H)e_t = 0$, the $\natural$-product of an element with its conjugate being the central scalar $C(\tilde H)e_t$ (*Introduction to the General Quaternionic Algebra* §*The Square and the Elements It Distinguishes*).

**Remark.** The sibling's idempotents are therefore not idempotents here, and they fail in the strongest possible way: their square in the multiplication vanishes. The two families of idempotents are the two fixed points of the same involution rule read in the two sesquilinear products, and the insertion of the natural conjugation in the first slot transposes them into square-zero elements.

### The Idempotents of the Sibling Bilinear Product

The sibling general quaternionic bilinear product $\tilde Q_1^{\natural}\tilde Q_2$ has the two trivial idempotents alone,

$$
\tilde Q_2 \star \tilde Q_2 = \tilde Q_2 \iff \tilde Q_2 = 0 \ \text{or}\ \tilde Q_2 = e_t ,
$$

because its square is the central scalar $\bigl(\sum_\mu Q_{2,\mu}^{2}\bigr)e_t$ (*Introduction to the General Quaternionic Algebra* §*The Square and the Elements It Distinguishes*). This is the smallest idempotent set of the four, and it is the one that agrees with the second row of the comparison table.

### The Comparison

**Theorem (the four idempotent sets).** The four general products have four different idempotent sets, and only the fourth has nontrivial idempotents that are units of the plain algebra:

| product | idempotents | nontrivial idempotents are |
|---|---|---|
| $\tilde Q_1\tilde Q_2$ | $0$, $e_t$, and $\tfrac12(e_t + \tilde\Xi)$ for a root of one $\tilde\Xi$ of the plain algebra | zero divisors |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $0$ and $e_t$ | none |
| $\tilde Q_1\tilde Q_2^{*}$ | $0$, $e_t$, and the Hermitian idempotents $\tfrac12(e_t + \tilde\Xi)$ | zero divisors |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $0$, $e_t$, and the family $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ with $(\vec u,\vec u)=1$ | units of the plain algebra, of central square $1$ |

**Proof.** The four rows are the propositions above and the statement of the classification theorem; the last column is the central-square computation for each family, $C = 0$ for the nontrivial idempotents of the plain and of the sibling sesquilinear product and $C = 1$ for the family. The table is the idempotent row of *The Four General Products and Their Relations* §*The Squares, the Idempotents and the Roots*, read with the central square attached to each entry.

**Remark.** The table is the reason the idempotent problem is the sharpest of the four element problems. The zero divisors are one set for all four general products (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*), and the square-zero elements are already two different problems for the four; but the idempotents are four sets, no two of which agree beyond $0$ and $e_t$, and the fourth alone is a family of units of the plain algebra.

## The Family of Idempotents

**The family is the sphere of radius $\tfrac{\sqrt3}{2}$ centred at $-\tfrac12e_t$ in the real vector subspace, written $\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ over the real unit vectors $\vec u$, a two-parameter family whose six coordinate-axial members are $-\tfrac12e_t\pm\tfrac{\sqrt3}{2}\vec e_\mu$; the group of unit quaternions acts transitively on it by conjugation.**

### The Parametrisation

The family of idempotents is the image of the set $(\vec u,\vec u)=1$ in the real three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})_{\mathbb{R}}$ under the map $\vec u\mapsto-\tfrac12 e_t+\tfrac{\sqrt3}{2}\vec u$. Writing $\vec u = u_x\vec e_x+u_y\vec e_y+u_z\vec e_z$ with **real** coefficients $u_\mu$, the constraint is the single real quadratic equation

$$
u_x^2+u_y^2+u_z^2=1 ,
$$

so every nontrivial idempotent is

$$
\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u , \qquad u_x^2+u_y^2+u_z^2=1 .
$$

The three coordinate-axial idempotents are the elements with $\vec u$ along one basis vector:

$$
-\tfrac12 e_t \pm \tfrac{\sqrt3}{2} \vec e_x , \qquad -\tfrac12 e_t \pm \tfrac{\sqrt3}{2} \vec e_y , \qquad -\tfrac12 e_t \pm \tfrac{\sqrt3}{2} \vec e_z .
$$

They are the six intersection points of the family with the coordinate axes, and they are the simplest nonrational elements of the family.

### Worked Elements

**Example.** Let $\tilde\Pi = -\tfrac12 e_t + \tfrac{\sqrt3}{2} \vec e_x$. Its square in the plain product is

$$
\tilde\Pi^{2} = \Bigl(\tfrac14 - \tfrac34\Bigr) e_t + 2\cdot\Bigl(-\tfrac12\Bigr)\cdot\tfrac{\sqrt3}{2} \vec e_x = -\tfrac12 e_t - \tfrac{\sqrt3}{2} \vec e_x = \tilde\Pi^{\natural} ,
$$

and $\tilde\Pi^{2} = -\tfrac12 e_t - \tfrac{\sqrt3}{2} \vec e_x$ is not $\tilde\Pi$, so the element is not idempotent for the plain product. For the multiplication of this article it is: the coordinates are real, so $\overline{\tilde\Pi} = \tilde\Pi$ and the criterion reads $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{2} = \tilde\Pi^{\natural}$, which is satisfied. Directly, $\tilde\Pi \star \tilde\Pi = \tilde\Pi^{\natural}\tilde\Pi^{*} = \bigl(\tilde\Pi^{\natural}\bigr)^{2} = \tilde\Pi$, since $\tilde\Pi^{*} = \tilde\Pi^{\natural}$ for a real element and the square of the natural conjugate returns the element. Its central square is $C = \tfrac14 + \tfrac34 = 1$.

**Example.** Let $\tilde\Pi = -\tfrac12 e_t + \tfrac{\sqrt3}{2}\vec u$ with $\vec u = \tfrac{3}{5}\vec e_x + \tfrac{4}{5}\vec e_y$ a real unit vector. Then $\tilde\Pi^{2} = \tilde\Pi^{\natural} = -\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u$, and the same reading shows the idempotence. The example is the general one: idempotence depends only on $\vec u$ and not on the choice of the two transversal directions.

### The Automorphisms of the Family

**Proposition.** The group of unit quaternions acts transitively on the family of idempotents by conjugation.

**Proof.** Let $\tilde U$ be a unit of the quaternion subspace, $\tilde U \in \mathbb{H}_{\mathbb{B}}$ with $C(\tilde U) = 1$; conjugation by $\tilde U$ in the quaternion division algebra is a real orthogonal map $\rho$ of the real vector subspace. Conjugation is a $\mathbb{C}$-algebra automorphism of the plain product, it commutes with both conjugations ${}^{\natural}$ and ${}^{*}$, and it therefore commutes with the multiplication $\star$ by the rule $\tilde U(\tilde Q_1 \star \tilde Q_2)\tilde U^{-1} = (\tilde U\tilde Q_1\tilde U^{-1}) \star (\tilde U\tilde Q_2\tilde U^{-1})$. Reading this on the criterion shows that it preserves the idempotent set and maps $\tilde\Pi(\vec u)$ to $\tilde\Pi(\rho\vec u)$. Since these real orthogonal maps act transitively on the set $(\vec u,\vec u)=1$, the action on the idempotent family is transitive.

**Remark.** The idempotent family is therefore a single class under the action of the unit quaternions, and the linear maps of the real vector subspace preserving the form $(\vec u,\vec u)$ are the structure group of the action. The two trivial idempotents are the fixed elements of the action, since a $\mathbb{C}$-algebra automorphism fixes $0$ and $e_t$.

## The Hermitian Subspace and the Family

**A nontrivial idempotent is neither Hermitian nor skew-Hermitian, $\tilde\Pi(\vec u)^{*}=-\tfrac12e_t-\tfrac{\sqrt3}{2}\vec u\neq\pm\tilde\Pi(\vec u)$ for $\vec u\neq0$, so the family lies in the quaternion subspace and outside the Hermitian subspace.**

The family lies in the quaternion subspace and outside the Hermitian subspace, and this is worth isolating because it is the source of the contrast with the sibling product.

**Proposition.** A nontrivial idempotent is not Hermitian,

$$
\tilde\Pi(\vec u)^{*} = -\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u \neq -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u = \tilde\Pi(\vec u)
$$

for $\vec u \neq 0$, and it is not skew-Hermitian either.

**Proof.** The element $\tilde\Pi(\vec u)$ has real coordinates, so $\overline{\tilde\Pi(\vec u)} = \tilde\Pi(\vec u)$ and $\tilde\Pi(\vec u)^{*} = \tilde\Pi(\vec u)^{\natural} = -\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u$. This differs from $\tilde\Pi(\vec u)$ exactly when $\vec u \neq 0$, and it differs from $-\tilde\Pi(\vec u) = \tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u$ because the scalar coordinates $\pm\tfrac12$ do not vanish.

**Remark.** The Hermitian subspace $\mathbb{M}_{+}$ is where the sibling product finds its idempotents and where this product finds none beyond the centre; the family of this product is cut out of the quaternion subspace instead, the fixed space of the other conjugation. This is the element-theoretic form of the fact that the two products differ by which slot carries the conjugation, and it is developed into the reading of the two halves in *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*.

**Remark (the complementary spherical family, and the absence of complementation).** The two infinite families are **complementary** in the following sense and in no other. The sibling product's idempotents are the **Hermitian spherical family** $\tilde\Pi_+(\tilde\Xi) = \tfrac12(e_t+\tilde\Xi)$ over the real unit vectors $\vec u$, and they are exactly the elements of the square-zero family of this product with scalar part $\tfrac12$: for such an element $\overline{\tilde\Pi_1}\tilde\Pi_1 = C(\tilde\Pi_1)e_t = 0$, so $\tilde\Pi_1 \star \tilde\Pi_1 = 0$; the idempotents of this product are the elements $-\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ with $(\vec u,\vec u)=1$, of scalar part $-\tfrac12$. The two families are therefore on the two signs of the scalar part and neither is a translate or a conjugate of the other. There is **no nontrivial complementation**: the relations $\tilde\Pi \star \tilde\Pi_2 = 0$ and $\tilde\Pi+\tilde\Pi_2 = e_t$ hold, in either order, for the trivial pair $\{\tilde\Pi,\tilde\Pi_2\} = \{e_t,0\}$ and for no other pair of idempotents. Indeed two nontrivial idempotents both have scalar part $-\tfrac12$, so their sum has scalar part $-1$ and not $1$; on the vector parts the relation would read $\tfrac{\sqrt3}{2}(\vec u + \vec u') = 2e_t$, impossible since $\vec u$ and $\vec u'$ lie in the real vector subspace and their sum has no scalar part. The block has no unit and is not associative either, so the complementation and the Peirce decomposition of the plain product are not available to it, and the absence is one of the specificities recorded in *The Specificities of the General Quaternionic Sesqualgebra*.

## Summary

The roots of $+1$ and the idempotents of the general quaternionic sesquilinear product $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$ are read from the identity $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$, whose scalar part is the Krein form $\sum_\mu\varepsilon_\mu\lvert \Xi_\mu\rvert^2$ with $\varepsilon = (1,-1,-1,-1)$.

A root of the central value $\lambda$ exists only for real $\lambda$, and for real $\lambda$ the nonzero roots are the family $\tilde\Xi = c(\vec u+it)$ with $(t^2-1)\lvert c\rvert^2 = \lambda$, of real dimension four, together with the central circle $\lvert a\rvert^2 = \lambda$ when $\lambda>0$. The value $+1$ takes the slopes $\lvert t\rvert>1$, with $\lvert c\rvert^2 = 1/(t^2-1)$, beside the central circle, and contains $e_t$ and $i$; the central square of a root is $C(\tilde\Xi) = c^{2}(1-t^{2})$, so every root of one is a unit of the plain algebra. The roots of $-1$ are the negative sign of the same formula: $\lvert t\rvert<1$ with $\lvert c\rvert^2 = 1/(1-t^2)$, they contain $\vec e_x,\vec e_y,\vec e_z$, they are non-empty, and they are not obtained by multiplying the roots of one by the central imaginary. The three central classes are **not** the plain classes of the same name: in the plain algebra the roots of $-1$ are the imaginary units, the roots of $+1$ the involutions that halve to the idempotents, and the roots of $0$ the pure isotropic cone, while here the roots of $0$ are the non-pure family and the roots of $+1$ are not the idempotent parameters; the comparison is the row of *The Four General Products and Their Relations*.

The idempotents are the solutions of $\overline{\tilde Q}_2\tilde Q_2 = \tilde Q_2^{\natural}$, equivalently of the four coordinate equations $Q_{2t} = u \in \mathbb{R}$, $u = u^{2} - \lvert\vec Q_2\rvert^{2}$, $(2u+1)\vec a = 0$ and $\vec a\times\vec b = -\tfrac12\vec b$ for $\vec Q_2 = \vec a + i\vec b$. Their list is the two trivial idempotents $0$ and $e_t$ together with the family

$$
\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u , \qquad \vec u\in\mathrm{Vect}(\mathbb{B})_{\mathbb{R}} , \qquad (\vec u,\vec u)=1 ,
$$

and each nontrivial idempotent has central square $1$, so that it is a unit of the plain algebra with inverse its own natural conjugate $-\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u$. The family is a single class under the action of the unit quaternions of the quaternion subspace, and it lies outside the Hermitian subspace, since a nontrivial idempotent is neither Hermitian nor skew-Hermitian. The idempotents are not the roots of one halved: the halving map carries the roots of one to idempotents only at the two trivial roots $\pm e_t$, and the two sets meet at $e_t$ alone. The idempotent sets of the four general products are four different sets: the plain product and the sibling sesquilinear product have infinite families of zero divisors, the sibling bilinear product has only the two trivial idempotents, and this product alone has a family of units of the plain algebra. The idempotents of the sibling sesquilinear product are isotropic for this multiplication, each of them having square zero, so the two infinite families are disjoint beyond $0$ and $e_t$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product |
| $\tilde\Xi$ | a root, $\tilde\Xi \star \tilde\Xi = \lambda e_t$ |
| root of one | a nonzero $\tilde\Xi$ with $\tilde\Xi \star \tilde\Xi = e_t$ |
| $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$ | the reduction of the square |
| $\sum_\mu\varepsilon_\mu\lvert \Xi_\mu\rvert^2$, $\varepsilon = (1,-1,-1,-1)$ | the Krein form, the scalar part of $\overline{\tilde\Xi}\tilde\Xi$ |
| $c(\vec u+it)$, $(t^2-1)\lvert c\rvert^2 = \lambda$ | the root family, $\lvert\vec u\rvert = 1$ |
| central circle, $\lvert a\rvert^2 = \lambda$ | the scalar roots, present only for $\lambda>0$ |
| $C(\tilde\Xi) = c^2(1-t^2)$ | the central square of a root |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi \star \tilde\Pi = \tilde\Pi$ |
| $\overline{\tilde Q}_2\tilde Q_2 = \tilde Q_2^{\natural}$ | the criterion for idempotence |
| $Q_{2t} = u \in \mathbb{R}$, $u = u^{2} - \lvert\vec Q_2\rvert^{2}$ | the scalar coordinate equations |
| $(2u+1)\vec a = 0$, $\vec a\times\vec b = -\tfrac12\vec b$ | the vector coordinate equations, $\vec Q_2 = \vec a + i\vec b$ |
| $\tilde\Pi(\vec u) = -\tfrac12e_t+\tfrac{\sqrt3}{2}\vec u$ | a nontrivial idempotent |
| $\vec u\in\mathrm{Vect}(\mathbb{B})_{\mathbb{R}}$, $(\vec u,\vec u)=1$ | the parameter and its constraint: a two-dimensional family |
| $C(\tilde\Pi(\vec u)) = 1$ | every nontrivial idempotent is a unit of the plain algebra |
| $\tilde\Pi(\vec u)^{-1} = \tilde\Pi(\vec u)^{\natural} = -\tfrac12 e_t - \tfrac{\sqrt3}{2}\vec u$ | the inverse of a nontrivial idempotent |
| $\tilde\Pi_+(\tilde\Xi) = \tfrac12(e_t + \tilde\Xi)$ | the idempotents of the sibling sesquilinear product, isotropic here |
| $\rho$ | the real orthogonal map of the vector subspace induced by conjugation by a unit quaternion |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the root of a central value and the idempotent, stated once for a general product.
- [Square Roots of a General Element in the Quaternion Algebra](square-roots-of-a-general-element-in-the-quaternion-algebra.html), for the plain reading of the three values, against which the roots of one are compared.
- [Square Roots of a General Element in the General Quaternionic Sesqualgebra](square-roots-of-a-general-element-in-the-general-quaternionic-sesqualgebra.html), for the general square-root problem of which the central value is the special case.
- [Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra](square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-sesqualgebra.html), for the roots of $0$, the square-zero family $c(\vec u\pm i)$.
- [Square Roots of One and the Idempotents of the Quaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.html), for the idempotents of the algebra and the Hermitian family.
- [Zero Divisors of the General Quaternionic Sesqualgebra](zero-divisors-of-the-general-quaternionic-sesqualgebra.html), for the zero-divisor cone and the criterion used on the roots of one and on the idempotents of the other products.
- [Norm and Invertibility in the General Quaternionic Sesqualgebra](norm-and-invertibility-in-the-general-quaternionic-sesqualgebra.html), for the plain criterion of invertibility $C\neq0$.
- [The Two One-Sided Actions and the Absence of a Unit](the-two-one-sided-actions-and-the-absence-of-a-unit.html), for the absence of a unit that makes the halving map fail.
- [The Square of the General Quaternionic Sesquilinear Product and the Two Halves](the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.html), for the identity $\tilde\Xi\star\tilde\Xi = (\overline{\tilde\Xi}\tilde\Xi)^{\natural}$ and the Krein scalar part.
- [The Four General Products and Their Relations](the-four-general-products-and-their-relations.html), for the definition of the four products and their scalar parts.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation and the article format.
