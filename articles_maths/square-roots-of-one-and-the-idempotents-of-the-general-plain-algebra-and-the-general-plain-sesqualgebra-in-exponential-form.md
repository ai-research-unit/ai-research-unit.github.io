# __Square Roots of One and the Idempotents of the General Plain Algebra and the General Plain Sesqualgebra in Exponential Form__

## Introduction

The space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, which differ in one point alone: whether the coordinates of each of the two elements of the pair are used as they stand or taken from the conjugated element. Two of them leave the first element as it stands, and they are the subjects of this article. The **general plain algebra** is the space under the product $\tilde P\tilde Q$, the multiplication that makes $\mathbb{B}$ an associative unital $\mathbb{C}$-algebra. The **general plain sesqualgebra** is the same space under the product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, whose second slot conjugates. The two structures share the basis, the unit, the norm and the conjugations, and they differ in the single star of the second slot; they are the codes $\mathrm{GPA}$ and $\mathrm{GPS}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and they are compared point by point in *The General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared*.

This article re-reads two of their families in the **exponential form**. The first family is the square roots of one of a structure, the elements $\tilde\Xi$ with $\tilde\Xi\tilde\Xi=e_0$ in the algebra and $\tilde\Xi\star\tilde\Xi=e_0$ in the sesqualgebra; their classifications are *Square Roots of One and the Idempotents of the General Plain Algebra* and *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, and they are assumed here and not re-proved. The second family is the idempotents, which those roots carry through the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$. The vocabulary of the root, of the idempotent and of the halving map is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The results.** In the sesqualgebra every root of $+1$ is of the **unit-scalar form**

$$
\tilde\Xi=e^{i\theta}w,\qquad \theta\in\mathbb{R},\quad w\in\mathbb{H}\ \text{real},\quad \lvert w\rvert=1,
$$

one central scalar phase times one real unit quaternion; the exponential form is complete there, the family being the unitary group $U(\mathbb{B})\cong U(2)$, and the idempotents are the three families $0$, $e_0$ and $\tfrac12(e_0+i\hat u_{\mathrm n})$ over the real unit vectors $\hat u_{\mathrm n}$. In the algebra the same form covers the **Hermitian** roots alone, the central pair $\pm e_0$ and the purely imaginary family $\pm i\hat u_{\mathrm n}$ written $\pm i\vec n$ there; the four-real-parameter family of **non-trivial** roots is not of that form, and each of its members is a **hyperbolic** exponential times a Hermitian root,

$$
\tilde\Xi=e^{t\,i\hat u_{\mathrm b}}\,i\hat u_{\mathrm n},\qquad t\in\mathbb{R},\ t\neq0,\quad \hat u_{\mathrm b},\hat u_{\mathrm n}\ \text{real unit vectors with}\ \hat u_{\mathrm b}\perp\hat u_{\mathrm n} .
$$

So the exponential form is complete in the sesqualgebra and split in the algebra: one closed form in the sesqualgebra, two in the algebra. Beside these products, every root of $+1$ of the algebra is a **single exponential** of an idempotent, $\tilde\Xi=\exp(i\pi\tilde\Pi_-)$ with $\tilde\Pi_-=\tfrac12(e_0-\tilde\Xi)$, which the algebra shares with the sesqualgebra on the Hermitian roots alone.

**Owners and boundary.** This article owns the exponential *reading* of the two classifications and nothing else. The classifications are the two articles named above; the exponential of an element, its closed form and its kernel are *Biquaternion Elementary Functions*; the trichotomy of the exponential and the four factors of the polar word are *The Polar Element Representation of Biquaternions*; the unitary group is *The Unitary Group of the Biquaternion Algebra*; the isotropic idempotents and the zero divisors are *Zero Divisors of the General Plain Algebra* and *Zero Divisors of the General Plain Sesqualgebra*. The article is pure algebra: no distance, no limit and no derivative enters, and no physics is invoked. The exponential is used as the closed form of a one-parameter group, which is its elementary reading, and not as an analytic object.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, the relations $e_k^2=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and central scalar imaginary $i$ with $i^2=-1$. A general element is $\tilde Q=Q_0e_0+\vec Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_1e_1+Q_2e_2+Q_3e_3$; the scalar part is $\mathrm{Sc}(\tilde Q)=Q_0$ and the vector part is $\vec Q$.

The three conjugations are the **natural** one $\tilde Q^{\natural}=Q_0e_0-\vec Q$, the **coefficient** one $\bar{\tilde Q}=\sum_\mu\overline{Q_\mu}e_\mu$, and the **Hermitian** one $\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\overline{Q_0}e_0-\overline{\vec Q}$. The **central square** is $C(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^{2}$, defined by $\tilde Q\tilde Q^{\natural}=C(\tilde Q)e_0$, and the **norm** is the same central element, $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=C(\tilde Q)e_0$. The **Hermitian value** is $H(\tilde Q)=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}$, the general plain sesquilinear algebraic norm, read as the scalar part $\mathrm{Sc}(\tilde Q\tilde Q^{*})=H(\tilde Q)$. An element is **Hermitian** when $\tilde Q^{*}=\tilde Q$, that is when $Q_0$ is real and $\vec Q$ is purely imaginary.

The two products of the article are the general plain one $\tilde P\tilde Q$ and the general plain sesquilinear one $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The **halving map** is $\tilde\Xi\mapsto\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$, of inverse $\tilde\Xi=2\tilde\Pi-e_0$, and the two idempotents a root carries are $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ and $\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_0-\tilde\Xi)$.

An element of $\mathbb{B}$ is written in its **real halves** as

$$
\tilde\Xi=q_r+iq_i,\qquad q_r\in\mathbb{H},\quad q_i\in\mathbb{H}\ \text{real},
$$

with $q_r$ the real quaternion of the real parts of the coefficients and $q_i$ the real quaternion of the imaginary parts. A real quaternion $w$ is written $w=w_0e_0+\vec w$; it is **scalar** when $\vec w=0$ and **pure** when $w_0=0$. A **real unit vector** is a pure real quaternion $\hat u_{\mathrm n}$ with $(\hat u_{\mathrm n},\hat u_{\mathrm n})=1$, equivalently $\hat u_{\mathrm n}^2=-e_0$, and the real unit vector written $\hat u_{\mathrm b}$ is a second one, orthogonal to $\hat u_{\mathrm n}$ when the two appear together.

The real unit vector of the roots is written $\vec n$ in the algebra's article, the purely imaginary family there being $\pm i\vec n$ over the unit vectors $\vec n$, and $\hat u_{\mathrm n}$ in the sesqualgebra's, the Hermitian roots there being $i\hat u_{\mathrm n}$ over the unit vectors $\hat u_{\mathrm n}$. This article writes the root axis $\hat u_{\mathrm n}$ and the axis of the boost $\hat u_{\mathrm b}$, both unit pure glyphs whose subscripts name the role; it quotes $\vec n$ when the algebra's own statement is quoted. *The Polar Element Representation of Biquaternions* writes the axis of its rotor \hat u_{\mathrm r} and the axis of its boost \hat u_{\mathrm b}; the boost axis is written $\hat u_{\mathrm b}$ here, so that the letter $\hat u_{\mathrm n}$ keeps in this article the single meaning it has in the two root articles, and the polar tables are read with that one substitution.

## The Exponential and the Unit-Scalar Form

### The Exponential of the Algebra

The exponential is the series

$$
\exp(\tilde Q)=\sum_{m\ge0}\frac{\tilde Q^m}{m!},
$$

which converges in the finite-dimensional space $\mathbb{B}$ and is the exponential of *Biquaternion Elementary Functions*. Its closed form is read on the pair $(Q_0,\vec Q)$: with $B^2=(\vec Q,\vec Q)$ and the axis $\vec Q/B$, a root of $-1$,

$$
\exp(\tilde Q)=e^{Q_0}\Bigl(\cos B\,e_0+\sin B\,\frac{\vec Q}{B}\Bigr),\qquad B\neq0,
$$

$$
\exp(\tilde Q)=e^{Q_0}\bigl(e_0+\vec Q\bigr),\qquad B=0 .
$$

The exponential is never a zero divisor: $N(\exp(\tilde Q))=e^{2Q_0}e_0$, so its value is a unit. Every unit of $\mathbb{B}$ is the exponential of an element, and the kernel of the exponential is the set of the diagonalisable elements whose eigenvalues lie in $2\pi i\mathbb{Z}$.

### The Trichotomy

For a generator $\nu$ and a real parameter $\theta$ the sign of $\nu^2$ decides the character of the exponential, by the table of *The Polar Element Representation of Biquaternions*.

| case | $\nu^2$ | $\exp(\nu\theta)$ | what it produces here |
|---|---|---|---|
| trigonometric | $-e_0$ | $\cos\theta\,e_0+\nu\sin\theta$ | the **central phase**, at $\nu=i$, and the **rotor**, at $\nu$ a real unit vector |
| parabolic | $0$ | $e_0+\nu\theta$, the series truncating | nothing: the exponential of a nilpotent |
| hyperbolic | $+e_0$ | $\cosh\theta\,e_0+\nu\sinh\theta$ | the **boost**, at $\nu=i\hat u_{\mathrm b}$ (there written $i\hat u_{\mathrm n}$), and the **scale**, at $\nu=e_0$ |

All three rows are non-empty in $\mathbb{B}$. The central phase is the case $\nu=i$ and the rotor is the case $\nu$ a real unit vector; the boost is the case $\nu=i\hat u_{\mathrm b}$, a Hermitian element of square $+e_0$, and the scale is the case $\nu=e_0$, of exponential $e^{\theta}e_0$; the parabolic row contains the nilpotents, among them $\nu=e_1+ie_2$ with $\nu^2=0$ exactly, whose exponential truncates to $e_0+\nu$.

**Remark (the parabolic row produces no root of $+1$).** A generator of the parabolic row is a pure nilpotent $\nu$, that is $\nu^2=0$, and its exponential truncates to

$$
\exp(\nu)=e_0+\nu .
$$

In the algebra the square is $e_0+2\nu$, equal to $e_0$ only for $\nu=0$. In the sesqualgebra the square is $(e_0+\nu)(e_0+\nu^{*})$, of scalar part the Hermitian value $H(e_0+\nu)=1+H(\nu)$, and $H(\nu)=\sum_{k=1}^{3}\lvert\nu_k\rvert^{2}$ is positive for $\nu\neq0$; the scalar part of a root of $+1$ being one, the value $e_0$ is reached only for $\nu=0$. The parabolic row therefore produces no root of $+1$ in either structure.

### The Unit-Scalar Form and Its Two Halves

**Definition.** The **unit-scalar form** of $\mathbb{B}$ is the element

$$
e^{i\theta}w,\qquad \theta\in\mathbb{R},\quad w\in\mathbb{H}\ \text{real},
$$

the product of the central phase $e^{i\theta}=e^{\theta i}$ of the trigonometric row and the real quaternion $w$. Because $i$ is central the form is the two-term sum

$$
e^{i\theta}w=\cos\theta\,w+i\sin\theta\,w,
$$

so its real halves are read at once.

**Proposition (the two halves are dependent).** The real halves of $\tilde\Xi=e^{i\theta}w$ are

$$
q_r=\cos\theta\,w,\qquad q_i=\sin\theta\,w,
$$

two real quaternions linearly dependent over $\mathbb{R}$, both being multiples of $w$; when $\cos\theta\neq0$ the second is the multiple $q_i=\tan\theta\,q_r$ of the first, and when $\cos\theta=0$ the first vanishes. Conversely, if the two halves of a nonzero $\tilde\Xi=q_r+iq_i$ are linearly dependent, then $\tilde\Xi$ is of the form: if $q_r\neq0$ then $q_i=\lambda q_r$ with $\lambda\in\mathbb{R}$ and $\tilde\Xi=(1+i\lambda)q_r$, and writing $1+i\lambda=\sqrt{1+\lambda^{2}}\,e^{i\theta}$ with $\theta=\arctan\lambda$ and $w=\sqrt{1+\lambda^{2}}\,q_r$, a real quaternion, gives $\tilde\Xi=e^{i\theta}w$; if $q_r=0$ then $\tilde\Xi=iq_i=e^{i\pi/2}q_i$, of the same form. The unit-scalar form is therefore exactly the condition that the two real halves be linearly dependent over $\mathbb{R}$.

*Proof.* The first display is the definition expanded, since $e^{i\theta}=\cos\theta\,e_0+i\sin\theta\,e_0$ and $i$ is central, and the dependency is the display. The converse is the two cases above, and $w$ is real in both because $q_r$ and $q_i$ are. Every nonzero element with dependent halves is thus of the form, and no element of the form has independent halves unless $w=0$. The same reduction is the one of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, §*The Roots of One*, which separates the cases $\vec u\neq0$ and $\vec u=0$ in the same way.

**Proposition (the characteristic values of the form).** For a real quaternion $w$ of norm $\lvert w\rvert$ the unit-scalar form has

$$
C(e^{i\theta}w)=e^{2i\theta}\lvert w\rvert^{2},\qquad N(e^{i\theta}w)=e^{2i\theta}\lvert w\rvert^{2}e_0,
$$

and for $w$ of norm one the values are $C=e^{2i\theta}$ and $N=e^{2i\theta}e_0$, of modulus one and never zero: a unit-scalar element of unit norm is a unit of $\mathbb{B}$, and it is a zero divisor for no $\theta$.

*Proof.* The natural conjugation fixes $e^{i\theta}$ and sends $w$ to $w^{\natural}$, so $N(e^{i\theta}w)=e^{i\theta}w\,e^{i\theta}w^{\natural}=e^{2i\theta}ww^{\natural}=e^{2i\theta}\lvert w\rvert^{2}e_0$, and $C$ is its scalar coefficient. The reading $C=e^{2i\theta}$ at $\lvert w\rvert=1$ is the computation of the sesqualgebra's article.

## The Roots of One in Exponential Form

### The Sesqualgebra: the Root Set Is the Unit-Scalar Family

**Theorem (quoted).** In the general plain sesqualgebra the roots of $+1$ are exactly the elements of the unit-scalar form of real unit $w$,

$$
\tilde\Xi=e^{i\theta}w,\qquad \theta\in\mathbb{R},\quad w\in\mathbb{H}\ \text{real},\quad \lvert w\rvert=1,
$$

a single real four-parameter family $U(1)\cdot S^{3}$, which is the unitary group $U(\mathbb{B})\cong U(2)$; and no root of $+1$ is a zero divisor.

The theorem is *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, §*The Roots of One*, and the group reading is *The Unitary Group of the Biquaternion Algebra*. The exponential form is complete here: the family of the theorem and the unit-scalar form with $\lvert w\rvert=1$ are one and the same set, so the roots of $+1$ of the sesqualgebra are read off two factors, a central phase and a rotor.

The family contains the Hermitian roots of the algebra on the same two axes: the roots $\pm e_0$ at $\theta\in\{0,\pi\}$ and $w=\pm e_0$, and the purely imaginary roots $i\hat u_{\mathrm n}$ at $\theta=\pm\pi/2$ and $w=\hat u_{\mathrm n}$, the roots written $\tilde\Xi=\pm i\vec n$ in the algebra's article. It contains much more beside them, the whole sphere of the real unit quaternions at $\theta=0$ among the rest; and the non-trivial roots of the algebra lie in it at no phase. The parametrisation has kernel $\{(0,e_0),(\pi,-e_0)\}$ and is otherwise injective.

### The Algebra: What the Unit-Scalar Form Covers

**Theorem (the unit-scalar form in the algebra).** For a real unit quaternion $w$ and a real $\theta$ the element $e^{i\theta}w$ is a root of $+1$ in the general plain algebra exactly when $w$ is scalar or pure. Then

$$
e^{i\theta}w=\pm e_0\quad(\theta\in\{0,\pi\},\ w\ \text{scalar}),\qquad e^{i\theta}w=i\hat u_{\mathrm n}\quad(\theta=\pm\pi/2,\ w=\hat u_{\mathrm n}\ \text{pure unit}),
$$

so the unit-scalar form covers exactly the **Hermitian** roots of the algebra: the central pair and the purely imaginary family, and nothing beside them.

*Proof.* Write $w=w_0e_0+\vec w$ with $w_0\in\mathbb{R}$ and $\vec w$ real pure. By §*The Unit-Scalar Form and Its Two Halves* the scalar part of $\tilde\Xi=e^{i\theta}w$ is $\Xi_0=w_0e^{i\theta}$ and its vector part is $\vec\Xi=e^{i\theta}\vec w$. The plain square is $\tilde\Xi^2=\bigl(\Xi_0^{2}-(\vec\Xi,\vec\Xi)\bigr)e_0+2\Xi_0\vec\Xi$, so the vector equation of the root is $2w_0e^{2i\theta}\vec w=0$: the root requires $w_0=0$ or $\vec w=0$. For $w$ scalar, $w_0=\pm1$ and the scalar equation is $e^{2i\theta}=1$, whence $\theta\in\{0,\pi\}$ and the root $\pm e_0$. For $w$ pure, $(\vec w,\vec w)=\lvert w\rvert^{2}=1$ and the scalar equation is $-e^{2i\theta}=1$, whence $\theta=\pm\pi/2$ and the roots $\pm iw$, that is $i\hat u_{\mathrm n}$ over the real unit vectors $\hat u_{\mathrm n}$. A mixed $w$ gives no root. The Hermitian roots of the algebra are then exactly the central pair $\pm e_0$ and the family $i\hat u_{\mathrm n}$, and no others: the purely imaginary roots are Hermitian and are the only roots of $+1$ that are pure multiples of a real quaternion, by *Square Roots of One and the Idempotents of the General Plain Algebra*, while a non-trivial root is $\vec\xi+i\vec\xi'$ with the real $\vec\xi\neq0$, so its natural part is not real and the root is not Hermitian. The form covers the Hermitian roots and no other root.

The reading is the sharpest difference between the two structures. The same two factors, a central phase and a real unit quaternion, exhaust the root set of the sesqualgebra and produce only the two-real-parameter Hermitian part of the algebra's root set; the four-real-parameter family of the algebra's non-trivial roots is outside the form.

### The Algebra: the Non-Trivial Roots and the Hyperbolic Factor

**Theorem (the non-trivial roots in hyperbolic form).** The non-trivial roots of $+1$ in the general plain algebra are exactly the elements

$$
\tilde\Xi=e^{t\,i\hat u_{\mathrm b}}\,i\hat u_{\mathrm n},\qquad t\in\mathbb{R},\ t\neq0,\quad \hat u_{\mathrm b},\hat u_{\mathrm n}\ \text{real unit vectors with}\ \hat u_{\mathrm b}\perp\hat u_{\mathrm n} .
$$

Each has the real halves $\vec\xi=-\sinh t\,\hat u_{\mathrm b}\hat u_{\mathrm n}$ and $\vec\xi'=\cosh t\,\hat u_{\mathrm n}$ of the algebra's classification, and each has $C(\tilde\Xi)=-1$ and $N(\tilde\Xi)=-e_0$, the same two values as the purely imaginary roots. The form has four real parameters — the parameter $t$ and the two directions $\hat u_{\mathrm n}$ and $\hat u_{\mathrm b}$ — and it is the four-parameter family of the classification; the parameter may be taken positive, since the two pairs $(t,\hat u_{\mathrm b})$ and $(-t,-\hat u_{\mathrm b})$ give the same root, and the value $t=0$ is excluded because it gives the purely imaginary root $i\hat u_{\mathrm n}$ and not a non-trivial one.

*Proof.* Let $\tilde\Xi=e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$ with $\hat u_{\mathrm b}\perp\hat u_{\mathrm n}$ unit. Since $i$ is central and $\hat u_{\mathrm b}^2=\hat u_{\mathrm n}^2=-e_0$, with $\hat u_{\mathrm b}\hat u_{\mathrm n}+\hat u_{\mathrm n}\hat u_{\mathrm b}=0$ by the orthogonality,

$$
\tilde\Xi=\bigl(\cosh t\,e_0+i\sinh t\,\hat u_{\mathrm b}\bigr)i\hat u_{\mathrm n}=i\cosh t\,\hat u_{\mathrm n}-\sinh t\,\hat u_{\mathrm b}\hat u_{\mathrm n} .
$$

The product $\hat u_{\mathrm b}\hat u_{\mathrm n}$ of two orthogonal real unit vectors is a real unit vector, its scalar part vanishing and its square being $-e_0$; so $\tilde\Xi$ is $\vec\xi+i\vec\xi'$ with $\vec\xi=-\sinh t\,\hat u_{\mathrm b}\hat u_{\mathrm n}$ and $\vec\xi'=\cosh t\,\hat u_{\mathrm n}$, and the two halves are orthogonal, since $(\vec\xi,\vec\xi')=-\sinh t\cosh t\,(\hat u_{\mathrm b}\hat u_{\mathrm n},\hat u_{\mathrm n})=-\sinh t\cosh t\,\mathrm{Sc}\bigl((\hat u_{\mathrm b}\hat u_{\mathrm n})^{\natural}\hat u_{\mathrm n}\bigr)=-\sinh t\cosh t\,\mathrm{Sc}(\hat u_{\mathrm b})=0$. Their squares give

$$
\xi_1^{2}+\xi_2^{2}+\xi_3^{2}-(\xi'_1)^{2}-(\xi'_2)^{2}-(\xi'_3)^{2}=\sinh^{2}t-\cosh^{2}t=-1,
$$

so the two conditions of the classification hold and the element is a non-trivial root. Conversely, a non-trivial root is $\vec\xi+i\vec\xi'$ with the two conditions and $\vec\xi\neq0$; the imaginary half is nonzero there, so the conditions give $\vec\xi'=\cosh t\,\hat u_{\mathrm n}$ with one real $t>0$ and one real unit vector $\hat u_{\mathrm n}$, and then $\vec\xi=-\sinh t\,\hat u_{\mathrm b}\hat u_{\mathrm n}$ with $\hat u_{\mathrm b}=\vec\xi\hat u_{\mathrm n}/\sinh t$, a real unit vector orthogonal to $\hat u_{\mathrm n}$, since $\hat u_{\mathrm b}\hat u_{\mathrm n}=-\vec\xi/\sinh t$ is a real pure quaternion of norm one; hence $\tilde\Xi=e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$. For the two characteristic values, $\tilde\Xi^{\natural}=-i\cosh t\,\hat u_{\mathrm n}+\sinh t\,\hat u_{\mathrm b}\hat u_{\mathrm n}$, and $\hat u_{\mathrm b}\hat u_{\mathrm n}$ is a real unit vector of square $-e_0$, so

$$
\tilde\Xi\tilde\Xi^{\natural}=-\cosh^{2}t\,e_0+\sinh^{2}t\,e_0=-e_0,
$$

hence $C=-1$ and $N=-e_0$. The four parameters are the real $t$ and the directions of $\hat u_{\mathrm n}$ and of $\hat u_{\mathrm b}$ in the plane orthogonal to $\hat u_{\mathrm n}$.

**Remark (the two factors of the hyperbolic form do not commute).** The commutator of the two factors of the form is

$$
e^{t\,i\hat u_{\mathrm b}}\,i\hat u_{\mathrm n}-i\hat u_{\mathrm n}\,e^{t\,i\hat u_{\mathrm b}}=-2\sinh t\,\hat u_{\mathrm b}\hat u_{\mathrm n},
$$

of norm $2\lvert\sinh t\rvert$, so the two factors do not commute and the product is not the exponential of the sum of the two exponents. This is the caution of *The Polar Element Representation of Biquaternions* read on the root: a root of $+1$ of the algebra is a unit, hence has a logarithm, but the logarithm is not the sum $t\,i\hat u_{\mathrm b}+\log(i\hat u_{\mathrm n})$.

### The Two Root Sets in Exponential Form

| the structure | the family of the roots of $+1$ | exponential form | real dimension |
|---|---|---|---|
| $\mathrm{GPA}$, $\tilde\Xi\tilde\Xi=e_0$ | the central pair $\pm e_0$ | unit-scalar form, $w$ scalar, $\theta\in\{0,\pi\}$ | $0$ |
| $\mathrm{GPA}$ | the purely imaginary family $i\hat u_{\mathrm n}$ | unit-scalar form, $w$ pure unit, $\theta=\pm\pi/2$ | $2$ |
| $\mathrm{GPA}$ | the non-trivial roots | hyperbolic form $e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$, $t\neq0$, $\hat u_{\mathrm b}\perp\hat u_{\mathrm n}$ | $4$ |
| $\mathrm{GPS}$, $\tilde\Xi\tilde\Xi^{*}=e_0$ | the whole family $e^{i\theta}w$ | unit-scalar form, $w$ real unit, $\theta$ free | $4$ |

The first two rows of the algebra are the unit-scalar form, and the third is the hyperbolic form; the sesqualgebra is the unit-scalar form alone, and its family is not a union of three families but one four-parameter family, in which the trivial, purely imaginary and non-trivial parts of the algebra are not separated. That is the meaning of the split: the exponential form separates the algebra's roots into one trigonometric piece and one hyperbolic piece, and the sesqualgebra's root set is the trigonometric piece extended to every real unit quaternion.

### The Coordinate Form of the Families

The two forms of the article stand side by side in the coordinates $\tilde\Xi=(\Xi_0,\Xi_1,\Xi_2,\Xi_3)$ of the basis $e_0,e_1,e_2,e_3$.

| the family | the coordinate form | the exponential form | real dimension |
|---|---|---|---|
| the roots of $+1$ of $\mathrm{GPA}$, the central pair | $(\pm1,0,0,0)$ | $\pm e_0$ | $0$ |
| the roots of $+1$ of $\mathrm{GPA}$, the purely imaginary family | $(0,in_1,in_2,in_3)$, $n_1^2+n_2^2+n_3^2=1$ | $i\hat u_{\mathrm n}$ | $2$ |
| the roots of $+1$ of $\mathrm{GPA}$, the non-trivial family | $(0,\xi_1+i\xi'_1,\xi_2+i\xi'_2,\xi_3+i\xi'_3)$, $\sum_k\xi_k^{2}-\sum_k(\xi'_k)^{2}=-1$, $\sum_k\xi_k\xi'_k=0$, $\vec\xi\neq0$ | $e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$, $t\neq0$ | $4$ |
| the roots of $+1$ of $\mathrm{GPS}$ | $(e^{i\theta}w_0,e^{i\theta}w_1,e^{i\theta}w_2,e^{i\theta}w_3)$, $w$ real unit | $e^{i\theta}w$ | $4$ |

The first three rows are the coordinate form of *Square Roots of One and the Idempotents of the General Plain Algebra*, and the last is read on the family $e^{i\theta}w$ of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*; the exponential form is that coordinate form with the coordinates parametrised by the phase, the two directions and the rapidity.

The idempotents are read on the same coordinates, since the halving adds the unit to the scalar coordinate and halves every coordinate, $\tilde\Pi_\pm=\tfrac12(e_0\pm\tilde\Xi)$ having the coordinates $\bigl(\tfrac12(1\pm\Xi_0),\pm\tfrac12\Xi_1,\pm\tfrac12\Xi_2,\pm\tfrac12\Xi_3\bigr)$.

| the idempotent family | the coordinate form | the exponential form | real dimension |
|---|---|---|---|
| the trivial pair of $\mathrm{GPA}$ | $(1,0,0,0)$ and $(0,0,0,0)$ | $e_0$ and $0$ | $0$ |
| the Hermitian family of $\mathrm{GPA}$ | $\bigl(\tfrac12,\tfrac{i}{2}n_1,\tfrac{i}{2}n_2,\tfrac{i}{2}n_3\bigr)$, $n_1^2+n_2^2+n_3^2=1$ | $\tfrac12(e_0+i\hat u_{\mathrm n})$ | $2$ |
| the non-trivial family of $\mathrm{GPA}$ | $\bigl(\tfrac12,\tfrac{i}{2}\cosh t\,n_k-\tfrac12\sinh t\,(\hat u_{\mathrm b}\hat u_{\mathrm n})_k\bigr)$, $k=1,2,3$ | $\tfrac12(e_0+e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n})$, $t\neq0$, $\hat u_{\mathrm b}\perp\hat u_{\mathrm n}$ | $4$ |
| the idempotents of $\mathrm{GPS}$ | the trivial pair and $\bigl(\tfrac12,\tfrac{i}{2}n_1,\tfrac{i}{2}n_2,\tfrac{i}{2}n_3\bigr)$ | $0$, $e_0$ and $\tfrac12(e_0+i\hat u_{\mathrm n})$ | $2$ |

On the roots of vanishing scalar part, the purely imaginary and the non-trivial ones, the halving gives $\bigl(\tfrac12,\pm\tfrac12\Xi_1,\pm\tfrac12\Xi_2,\pm\tfrac12\Xi_3\bigr)$, the quoted value $\bigl(\tfrac12,\tfrac{i}{2}n_1,\tfrac{i}{2}n_2,\tfrac{i}{2}n_3\bigr)$ at $\tilde\Xi=i\hat u_{\mathrm n}$, and the trivial pair $\pm e_0$ gives the two remaining coordinates $(1,0,0,0)$ and $(0,0,0,0)$. In the non-trivial row, $(\hat u_{\mathrm b}\hat u_{\mathrm n})_k$ is the $k$-th real coordinate of the real unit vector $\hat u_{\mathrm b}\hat u_{\mathrm n}$, the third unit vector orthogonal to the two.

### The Idempotent Exponential Form of a Root

Every root of $+1$ of the algebra has a second exponential reading, in which it is a **single exponential of an idempotent**. For any root $\tilde\Xi\tilde\Xi=e_0$ put

$$
\tilde\Pi_-(\tilde\Xi) = \tfrac12(e_0-\tilde\Xi),
$$

the second element of the halving pair. It is idempotent,

$$
\tilde\Pi_-^2 = \tfrac14\bigl(e_0-2\tilde\Xi+\tilde\Xi^2\bigr) = \tfrac12(e_0-\tilde\Xi) = \tilde\Pi_- ,
$$

and since $i\pi$ is central and the exponential series of an idempotent truncates at the first power,

$$
\exp\bigl(i\pi\tilde\Pi_-\bigr) = e_0+\bigl(e^{i\pi}-1\bigr)\tilde\Pi_- = e_0-2\tilde\Pi_- = \tilde\Xi .
$$

So every root of $+1$ of the algebra is the exponential of $i\pi$ times an idempotent,

$$
\tilde\Xi = \exp\bigl(i\pi\tilde\Pi_-\bigr), \qquad \tilde\Pi_- = \tfrac12(e_0-\tilde\Xi), \qquad \tilde\Pi_-^2 = \tilde\Pi_- .
$$

The central pair sits at the two ends of the halving: $\tilde\Xi = e_0$ gives $\tilde\Pi_- = 0$ and $\exp(0) = e_0$, and $\tilde\Xi = -e_0$ gives $\tilde\Pi_- = e_0$ and $\exp(i\pi) = -e_0$. The exponential is not that of an idempotent itself but of $i\pi$ times an idempotent, so it does not collide with the remark of §*The Idempotents in Exponential Form*, §*The Halving Map* that no idempotent other than $e_0$ is an exponential.

The bridge to the two forms of this article is the **product of the last two factors** of the polar word of *The Polar Element Representation of Biquaternions* — the Hermitian boost $\tilde U_{\mathrm b}$ and the real rotor $\tilde u_{\mathrm r}$. At a root of $+1$ the element $-i\tilde\Xi$ is a root of $-e_0$, since $(-i\tilde\Xi)^2=-e_0$, and on the purely imaginary and the non-trivial roots it has unit norm and trivial phase, so that its polar decomposition is exactly that product,

$$
-i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r} , \qquad (\tilde U_{\mathrm b}\tilde u_{\mathrm r})^2 = -e_0 , \qquad \bigl\langle -i\tilde\Xi, -i\tilde\Xi\bigr\rangle_{\natural} = e_0 ,
$$

and the idempotent form expands into a central part and a two-factor part,

$$
\tilde\Xi = \exp\bigl(i\pi\tilde\Pi_-\bigr) = \exp\Bigl(\tfrac{i\pi}{2}e_0+\tfrac{\pi}{2}\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}\Bigr) = \exp\Bigl(i\pi\,\frac{e_0-i\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}}{2}\Bigr).
$$

In the other direction the halving idempotent and the product are recovered from each other by

$$
\tilde\Pi_- = \tfrac12\bigl(e_0-i\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr) , \qquad \tilde U_{\mathrm b}\tilde u_{\mathrm r} = i\,\bigl(2\tilde\Pi_--e_0\bigr) .
$$

In the hyperbolic form of this article the root is $\tilde\Xi = e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$, so the product of the last two factors is $-i\tilde\Xi = e^{t\,i\hat u_{\mathrm b}}\hat u_{\mathrm n}$: the boost $e^{t\,i\hat u_{\mathrm b}}$ multiplies the pure rotor $\hat u_{\mathrm n}$, and the constraint is the orthogonality of the two axes together with the purity of the rotor, which the hyperbolic form already carries. The Hermitian roots, $\pm e_0$ and $i\hat u_{\mathrm n}$, have a Hermitian halving element; the non-real one gives $\tilde\Pi_- = \tfrac12(e_0-i\hat u_{\mathrm n})$ and $\tilde\Xi = \exp\bigl(i\pi\tfrac{e_0-i\hat u_{\mathrm n}}{2}\bigr)$.

The reading is a third form of the root set of the algebra, beside the unit-scalar form and the hyperbolic form of the sections above: those two write a root as a product of two factors, while the idempotent form writes it as a single exponential, of exponent $i\pi\tilde\Pi_-$. The construction is the algebra's: it needs $\tilde\Xi^2=e_0$ in the plain product, where a root of the sesqualgebra has $\tilde\Xi\tilde\Xi^{*}=e_0$ instead, so in the sesqualgebra it covers the Hermitian roots alone, which the two structures share.

## The Idempotents in Exponential Form

### The Halving Map

The halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents of the plain product, of inverse $\tilde\Xi=2\tilde\Pi-e_0$, and a root $\tilde\Xi$ carries the complete orthogonal pair $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ and $\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_0-\tilde\Xi)=e_0-\tilde\Pi_+(\tilde\Xi)$, of sum $e_0$, of product $0$ and of difference the root. The map and its arithmetic are *Square Roots of One and the Idempotents of the General Plain Algebra*, §*The Correspondence With the Roots of One*. For every root other than $\pm e_0$ the idempotent is primitive, so the pair carries the Peirce decomposition of the algebra into four pieces of real dimension two each, *Ideals and Peirce Decomposition of the General Plain Algebra*; the roots of one are therefore the source of the idempotents and of that decomposition.

**Remark (an idempotent is read through the halving and not as an exponential).** No idempotent of the two structures other than $e_0$ is an exponential. The exponential is never a zero divisor, while every idempotent other than $0$ and $e_0$ is isotropic, $C=0$, hence a zero divisor; the origin is not a unit and is not in the image of the exponential either, since the image is the group of units. So the exponential form of an idempotent is the halving of an exponential-form root, $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$, and only the unit is an exponential itself, $e_0=\exp(0)$.

### The Sesqualgebra: a Two-Real-Parameter Family

**Theorem.** The idempotents of the general plain sesqualgebra are $0$, $e_0$, and the elements

$$
\tilde\Pi=\tfrac12\bigl(e_0+e^{i\pi/2}\hat u_{\mathrm n}\bigr)=\tfrac12\bigl(e_0+i\hat u_{\mathrm n}\bigr),\qquad \hat u_{\mathrm n}\ \text{a real unit vector},
$$

a real two-parameter family of rank-one Hermitian projections. The halving of a root $e^{i\theta}w$ is idempotent exactly when the root is Hermitian, that is exactly when $w$ is scalar or pure; the halving of a root with a mixed $w$ is not idempotent.

*Proof.* Let $\tilde\Xi=e^{i\theta}w$ be a root and $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$. Then $\tilde\Pi\star\tilde\Pi=\tfrac14(e_0+\tilde\Xi)(e_0+\tilde\Xi^{*})=\tfrac14\bigl(2e_0+\tilde\Xi+\tilde\Xi^{*}\bigr)$, since $\tilde\Xi\tilde\Xi^{*}=e_0$. This equals $\tfrac12(e_0+\tilde\Xi)$ exactly when $\tilde\Xi=\tilde\Xi^{*}$, that is when the root is Hermitian, and by §*The Unit-Scalar Form and Its Two Halves* that is exactly when $w$ is scalar or pure. The Hermitian roots are $\pm e_0$ and $i\hat u_{\mathrm n}$; the first two give the trivial idempotents $\tfrac12(e_0+e_0)=e_0$ and $\tfrac12(e_0-e_0)=0$, and the third gives $\tfrac12(e_0+i\hat u_{\mathrm n})$, of real dimension two. The classification is the theorem of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*.

The family is the set of the rank-one Hermitian idempotents of the matrix model $M_2(\mathbb{C})$, and it is the intersection of the two idempotent sets of the next table.

### The Algebra: Three Families

**Theorem.** The idempotents of the general plain algebra are the trivial pair $0$, $e_0$, the family

$$
\tilde\Pi=\tfrac12\bigl(e_0+i\hat u_{\mathrm n}\bigr),\qquad \hat u_{\mathrm n}\ \text{a real unit vector},
$$

of the Hermitian idempotents, and the family

$$
\tilde\Pi=\tfrac12\bigl(e_0+e^{t\,i\hat u_{\mathrm b}}\,i\hat u_{\mathrm n}\bigr),\qquad t\in\mathbb{R},\ t\neq0,\quad \hat u_{\mathrm b},\hat u_{\mathrm n}\ \text{real unit vectors with}\ \hat u_{\mathrm b}\perp\hat u_{\mathrm n},
$$

of the non-trivial idempotents, of real dimension four. Every idempotent other than the two trivial ones is isotropic, $C=0$, and is a zero divisor; the Hermitian family lies in the Hermitian subspace $\mathbb{M}_+$, and the non-trivial family lies in none of the remarkable subspaces.

*Proof.* By the halving map the idempotents are the elements $\tfrac12(e_0+\tilde\Xi)$ over the roots of $+1$, so the three families of §*The Two Root Sets in Exponential Form* give the three families here: $\pm e_0$ give $0$ and $e_0$, the purely imaginary roots give $\tfrac12(e_0+i\hat u_{\mathrm n})$, and the non-trivial roots give $\tfrac12(e_0+e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n})$ with $t\neq0$ and $\hat u_{\mathrm b}\perp\hat u_{\mathrm n}$. For the isotropic reading, write a non-trivial root as $\tilde\Xi=\vec\xi+i\vec\xi'$ with $\Xi_0=0$ and $(\vec\Xi,\vec\Xi)=-1$; the element $e_0+\tilde\Xi$ has scalar coefficient $1$ and vector coefficients $\Xi_k$, so

$$
C(\tilde\Pi)=\tfrac14\Bigl(1+\sum_{k=1}^{3}\Xi_k^{2}\Bigr)=\tfrac14\bigl(1+(\vec\Xi,\vec\Xi)\bigr)=0,
$$

and the same computation with $\tilde\Xi=i\hat u_{\mathrm n}$ gives the vanishing on the Hermitian family as well. A vanishing central square is the criterion of *Zero Divisors of the General Plain Algebra*, so every idempotent other than the two trivial ones is a zero divisor. The position in $\mathbb{M}_+$ of the Hermitian family is the projection reading of the algebra's article.

## Worked Examples

**The standard idempotent.** The root $\tilde\Xi=ie_3$ of the algebra and of the sesqualgebra is the unit-scalar form at $\theta=\pi/2$ and $w=e_3$, a pure real unit quaternion:

$$
\tilde\Xi=e^{i\pi/2}e_3=\cos\tfrac{\pi}{2}\,e_3+i\sin\tfrac{\pi}{2}\,e_3=ie_3,
$$

with $C(\tilde\Xi)=e^{i\pi}=-1$ and $N(\tilde\Xi)=-e_0$. Its pair is the standard one, $\tilde\Pi_+=\tfrac12(e_0+ie_3)$ and $\tilde\Pi_-=\tfrac12(e_0-ie_3)$, the two primitive orthogonal idempotents of $\mathbb{B}$, and both are idempotent in the algebra and in the sesqualgebra at once.

**A non-trivial root and its pair.** Take $\hat u_{\mathrm n}=e_1$, $\hat u_{\mathrm b}=e_3$, orthogonal real unit vectors, and $t=\ln 2$. Then $\cosh t=\tfrac54$, $\sinh t=\tfrac34$, and

$$
\tilde\Xi=e^{(\ln 2)i e_3}ie_1=\Bigl(\tfrac54\,e_0+i\tfrac34\,e_3\Bigr)ie_1=i\tfrac54\,e_1-\tfrac34\,e_2=-\tfrac34\,e_2+i\tfrac54\,e_1 .
$$

The real halves are $\vec\xi=-\tfrac34e_2$ and $\vec\xi'=\tfrac54e_1$, orthogonal, with $\tfrac{9}{16}-\tfrac{25}{16}=-1$, so the element is a non-trivial root of the algebra; it is not a root of the sesqualgebra, its sesquilinear square being $\tilde\Xi\tilde\Xi^{*}=\tfrac{17}{8}e_0+i\tfrac{15}{8}e_3$, and it is not of the unit-scalar form either, its two halves being linearly independent. Its two idempotents are $\tilde\Pi_\pm=\tfrac12(e_0\pm\tilde\Xi)$, of coordinates $\bigl(\tfrac12,\pm\tfrac58 i,\mp\tfrac38,0\bigr)$, both of vanishing central square, hence both zero divisors, and $\tilde\Pi_+\tilde\Pi_-=0$ with $\tilde\Pi_++\tilde\Pi_-=e_0$.

**A sesqualgebra root outside the algebra's root set.** Take $\theta=\pi/3$ and $w=\tfrac12(e_0+e_1+e_2+e_3)$, a real unit quaternion of mixed type. Then

$$
\tilde\Xi=e^{i\pi/3}w=\tfrac12\,w+i\tfrac{\sqrt3}{2}\,w=\tfrac14\bigl(e_0+e_1+e_2+e_3\bigr)+i\tfrac{\sqrt3}{4}\bigl(e_0+e_1+e_2+e_3\bigr),
$$

with $H(\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}=1$ and $C(\tilde\Xi)=e^{2i\pi/3}$. It is a root of the sesqualgebra, since $\tilde\Xi\tilde\Xi^{*}=e_0$, and it is not a root of the algebra: its two halves are linearly dependent and its $w$ is mixed, so the vector part of its plain square is $2\Xi_0\vec\Xi\neq0$. Its halving $\tfrac12(e_0+\tilde\Xi)$ is not idempotent in either product, by §*The Sesqualgebra: a Two-Real-Parameter Family*.

**The parabolic row on a unit.** The nilpotent $\nu=e_1+ie_2$ of the parabolic row has $\exp(\nu)=e_0+\nu=e_0+e_1+ie_2$, of norm $N=e_0$, hence a unit of the algebra; its plain square is $e_0+2\nu=e_0+2e_1+2ie_2\neq e_0$, so it is not a root of $+1$, and its sesquilinear square is $(e_0+\nu)(e_0+\nu^{*})=3e_0+2ie_2+2ie_3$, of scalar part $H(e_0+\nu)=3$, also not $e_0$. The example is the witness of the remark that the parabolic row produces no root of $+1$.

## The Two Structures Compared

| | $\mathrm{GPA}$, $\tilde P\tilde Q$ | $\mathrm{GPS}$, $\tilde P\tilde Q^{*}$ |
|---|---|---|
| the square | $\tilde\Xi^2=\bigl(\Xi_0^{2}-(\vec\Xi,\vec\Xi)\bigr)e_0+2\Xi_0\vec\Xi$ | $\tilde\Xi\tilde\Xi^{*}$, of scalar part $\sum_\mu\lvert\Xi_\mu\rvert^{2}$ |
| roots of $+1$, exponential form | unit-scalar form for the Hermitian roots, hyperbolic form $e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$ for the others | the unit-scalar form $e^{i\theta}w$, complete |
| the closed form is complete | no: two forms for one root set | yes: one form for the whole root set |
| real dimension of the root set | $0$, $2$ and $4$ on the three families | $4$ on the single family |
| is the root set a group | no: $ie_1$ and $ie_2$ are roots, their product $-e_3$ is not | yes: the unitary group $U(\mathbb{B})\cong U(2)$ |
| roots of $-1$ | non-empty: the elements $i\tilde\Xi$ | empty |
| roots of $0$ | the origin and the nilpotents, as $e_1+ie_2$ | the origin alone |
| idempotents | $0$, $e_0$, $\tfrac12(e_0+i\hat u_{\mathrm n})$, $\tfrac12(e_0+e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n})$ | $0$, $e_0$, $\tfrac12(e_0+i\hat u_{\mathrm n})$ |
| exponential form of the idempotents | the halving of the two forms | the halving of the Hermitian roots alone |

**Remark (the cause of the split).** The two products differ in the star of the second slot, and the star conjugates the second factor. The plain square of a pure element is $-\bigl(\vec\Xi,\vec\Xi\bigr)e_0$, an indefinite complex quantity, so the algebra reaches the values $+1$, $-1$ and $0$, and its roots of $+1$ carry both the compact directions of the trigonometric row and the non-compact directions of the hyperbolic row. The sesquilinear square has the scalar part $\sum_\mu\lvert\Xi_\mu\rvert^{2}$, a definite non-negative real number, so the sesqualgebra reaches the value $+1$ alone among the three, its roots of $+1$ lie in the compact part, and the hyperbolic row is not available to them. That is why the unit-scalar form is complete in the sesqualgebra and split in the algebra, and it is the same definiteness that makes the two structures differ at the other central values.

## Summary

The roots of $+1$ of the general plain sesqualgebra are exactly the elements of the unit-scalar form $\tilde\Xi=e^{i\theta}w$ over the real unit quaternions $w$, a single real four-parameter family, the unitary group $U(\mathbb{B})\cong U(2)$; the idempotents are $0$, $e_0$ and $\tfrac12(e_0+i\hat u_{\mathrm n})$ over the real unit vectors $\hat u_{\mathrm n}$. The roots of $+1$ of the general plain algebra are covered by that form on their Hermitian part alone, the central pair $\pm e_0$ and the purely imaginary family $i\hat u_{\mathrm n}$, and their four-real-parameter non-trivial part is instead the hyperbolic form $\tilde\Xi=e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$ with $t\neq0$ over the orthogonal real unit vectors $\hat u_{\mathrm b},\hat u_{\mathrm n}$, each such root being a boost of the polar representation applied to a Hermitian root, of characteristic values $C=-1$ and $N=-e_0$. The idempotents of the algebra are the two trivial ones and the halvings of the two forms; every idempotent other than the two trivial ones is isotropic and a zero divisor, and no idempotent other than $e_0$ is an exponential, so the idempotents are read through the halving and not as exponentials. The exponential form is complete in the sesqualgebra and split in the algebra, and the split is the indefiniteness of the plain square against the definiteness of the sesquilinear one. Each root of $+1$ of the algebra has, beside the two forms above, the idempotent exponential form $\tilde\Xi = \exp(i\pi\tilde\Pi_-)$ built on the halving idempotent $\tilde\Pi_- = \tfrac12(e_0-\tilde\Xi)$, with the product of the last two polar factors read from the root, $-i\tilde\Xi$, carrying the hyperbolic form on the non-central roots, $-i\tilde\Xi = e^{t\,i\hat u_{\mathrm b}}\hat u_{\mathrm n}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^{i\theta}w$, $\theta\in\mathbb{R}$, $w\in\mathbb{H}$ real | the unit-scalar form, the product of the central phase and a real quaternion |
| $q_r$, $q_i$, $\tilde\Xi=q_r+iq_i$ | the two real halves of an element; the unit-scalar form has the dependent halves $\cos\theta\,w$ and $\sin\theta\,w$ |
| $\hat u_{\mathrm n}$ | a real unit vector, $\hat u_{\mathrm n}^2=-e_0$; the axis of the Hermitian root $i\hat u_{\mathrm n}$ and of the projections; written $\vec n$ in the algebra's article |
| $\hat u_{\mathrm b}$ | a real unit vector, the axis of the boost $e^{t\,i\hat u_{\mathrm b}}$ of the hyperbolic form, orthogonal to $\hat u_{\mathrm n}$ |
| $t$ | the real parameter of the hyperbolic form, nonzero on the non-trivial roots |
| $e^{t\,i\hat u_{\mathrm b}}i\hat u_{\mathrm n}$ | the hyperbolic form of the non-trivial roots of $+1$ of the algebra, $C=-1$, $N=-e_0$ |
| $\exp(\tilde Q)=e^{Q_0}\bigl(\cos B\,e_0+\sin B\,\tfrac{\vec Q}{B}\bigr)$ | the closed form of the exponential, $B^2=(\vec Q,\vec Q)$, quoted from *Biquaternion Elementary Functions*, whose axis $\vec Q/B$ is written $\hat u_{\mathrm n}$ there |
| trigonometric, parabolic, hyperbolic | the three rows of the trichotomy, $\nu^2=-e_0$, $0$, $+e_0$ |
| $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_0\pm\tilde\Xi)$ | the two idempotents of a root, complete and orthogonal, of difference the root |
| $-i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the product of the last two factors of the polar word, read from a root of $+1$, a unit-norm root of $-e_0$ |
| $\exp(i\pi\tilde\Pi_-)$ | the idempotent exponential form of a root of $+1$, the exponential of $i\pi$ times the halving idempotent |
| $C$, $H$, $N$ | the central square $\sum_\mu Q_\mu^{2}$, the Hermitian value $\sum_\mu\lvert Q_\mu\rvert^{2}$, the general plain sesquilinear algebraic norm, and the norm $C\,e_0$ |

## Further Reading

- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra.md`), for the classification of the roots of $+1$ and of the idempotents of the algebra, which this article re-reads and does not reprove
- *Square Roots of One and the Idempotents of the General Plain Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra.md`), for the same classification in the sesqualgebra, where the root set is the family $e^{i\theta}w$ and the Hermitian roots are the $i\hat u_{\mathrm n}$
- *Biquaternion Elementary Functions* (`articles_maths/biquaternion-elementary-functions.md`), for the exponential, its closed form, its kernel, its norm and the logarithm that inverts it off the zero divisors
- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the trichotomy of the exponential, the four factors of the polar word and the two cautions of the exponential reading
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the group structure of the roots of $+1$ of the sesqualgebra
- *The General Plain Algebra and the General Plain Sesqualgebra of Biquaternions Compared* (`articles_maths/the-general-plain-algebra-and-the-general-plain-sesqualgebra-of-biquaternions-compared.md`), for the point-by-point comparison of the two structures that this article reads in one column
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the isotropic idempotents and the zero divisors that exclude the idempotents from the image of the exponential
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the root of a central value, the idempotent and the halving map
- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), the companion of this article in the operator group, for the four adjoints that the four forms of the same space produce
