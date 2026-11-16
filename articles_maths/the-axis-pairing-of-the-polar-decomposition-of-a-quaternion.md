# __The Axis Pairing of the Polar Decomposition of a Quaternion__

## Introduction

The polar word of a quaternion is $\tilde q=r\tilde u_{\mathrm r}$, a positive scale and a versor. The **axis pairing** reads the same word with the exponent transported onto a named axis: for a unit pure quaternion $\nu$, the element is written
$$
\tilde q=\tilde u_{\mathrm r}\,(a+b\nu),\qquad a,b\in\mathbb{R},
$$
where $a+b\nu$ lies in the plane $\mathbb{R}\oplus\mathbb{R}\nu$ that $\nu$ spans with the unit, and $\tilde u_{\mathrm r}$ is a versor. The two real slots $a$ and $b$ carry the scale and the transported angle, and the versor carries the part of the element that the axis does not see.

The article proves the existence of the word for every element and every axis, identifies the pair $(a,b)$ with the normalised projection of the element onto the plane of the axis, and proves uniqueness under a single normalisation of the versor. The uniqueness fails exactly on the hyperplane $\nu^{\perp}$ orthogonal to the axis, and the real axis is the worst case of that failure: there the word is the same for every axis, so that no axis is recorded at all. The planes $\mathbb{R}\oplus\mathbb{R}\nu$ are the Cartan subalgebras of the algebra, and the pairing is the real case of the groupings of the biquaternion block, where the axis is a root of $-e_t$ and the word has four factors instead of two.

The forms of the word that this one is compared with are the modulus-unit form of [Modulus–Unit Polar Decomposition of Quaternions](modulus-unit-polar-decomposition-of-quaternions.html), the rational chart of [Rational-Chart Polar Decomposition of Quaternions](rational-chart-polar-decomposition-of-quaternions.html) and the exponential of [Exponential Polar Decomposition of Quaternions](exponential-polar-decomposition-of-quaternions.html).

## The Axis and Its Plane

**Definition.** A real unit axis is a unit vector $\nu\in\operatorname{Vect}(\mathbb{H})$, that is $\nu^2=-e_t$. Its plane is
$$
\mathbb{C}_\nu=\mathbb{R}\oplus\mathbb{R}\nu=\{a+b\nu:\ a,b\in\mathbb{R}\}.
$$

**Proposition (the plane is a copy of the complex numbers).** $\mathbb{C}_\nu$ is a subalgebra of $\mathbb{H}$ isomorphic to $\mathbb{C}$, commutative, of real dimension two, with unit $e_t$; the element $\nu$ plays the role of $i$; and the conjugation of $\mathbb{H}$ restricts to the conjugation of the plane, $a+b\nu\mapsto a-b\nu$.

*Proof.* The product of two elements of the plane is $aa'-bb'\nu^2+(ab'+a'b)\nu=(aa'-bb')+(ab'+a'b)\nu$, which is in the plane; the algebra is the quotient $\mathbb{R}[t]/(t^2+1)$; and the conjugation sends $\nu$ to $-\nu$ and fixes the reals. Verified on the products.

**Proposition (the maximal commutative subalgebras).** The commutative subalgebras of $\mathbb{H}$ containing $e_t$ are the real line and the planes $\mathbb{C}_\nu$; the planes are maximal, and two of them meet in the real line.

*Proof.* Let $A$ be commutative and contain $e_t$, and let $\tilde u\in A$ be non-real. Then every element of $A$ commutes with $\tilde u$, so $A$ is contained in the centraliser of $\tilde u$, which is $\mathbb{C}_{\vec u/\lvert\vec u\rvert}$ by the centraliser theorem of the algebra. Two distinct planes meet in the elements that commute with both, which are the reals. Verified on the basis.

**Remark (the axes are the Cartan subalgebras).** The planes $\mathbb{C}_\nu$ are the Cartan subalgebras of the algebra read as a real Lie algebra under the commutator: they are the maximal toral subalgebras, one for each point of the projective plane of the axes, since $\nu$ and $-\nu$ give the same plane. **The axis of the pairing is the choice of a Cartan subalgebra, and the pairing is the statement that every element is a versor times a normalised element of the chosen Cartan subalgebra.**

## The Word on an Axis

**Theorem (existence).** For every unit axis $\nu$ and every $\tilde q$ there are a versor $\tilde u_{\mathrm r}$ and reals $a,b$ with $a^2+b^2=N(\tilde q)$ such that $\tilde q=\tilde u_{\mathrm r}(a+b\nu)$.

*Proof.* Choose any pair $(a,b)$ on the circle of radius $\lvert\tilde q\rvert$ and put $\tilde u_{\mathrm r}=\tilde q(a+b\nu)^{-1}$; then $N(\tilde u_{\mathrm r})=N(\tilde q)/(a^2+b^2)=1$, so $\tilde u_{\mathrm r}$ is a versor, and the product returns $\tilde q$. Verified on random elements and axes.

**Remark (the circle of words).** The words over a fixed element and a fixed axis form a free circle orbit: if $\tilde q=\tilde u_{\mathrm r}(a+b\nu)$ then for every real $\phi$
$$
\tilde q=\bigl(\tilde u_{\mathrm r}e^{\phi\nu}\bigr)\bigl(e^{-\phi\nu}(a+b\nu)\bigr),
$$
and the two factors are again a versor and an element of the plane. So the pairing is not a factorisation until a normalisation is chosen, and the choice of the normalisation is the real content of the construction.

**Theorem (uniqueness with the normalisation).** Let $\tilde q\notin\nu^{\perp}$, that is $\tilde q\not\equiv0$ modulo the hyperplane orthogonal to the axis. Then there is exactly one word with
$$
\langle\vec u_{\mathrm r},\nu\rangle=0,\qquad u_{{\mathrm r}t}>0 ,
$$
and in it
$$
a=\frac{\lvert\tilde q\rvert\,q_t}{\sqrt{q_t^2+\langle\vec q,\nu\rangle^2}},\qquad b=\frac{\lvert\tilde q\rvert\,\langle\vec q,\nu\rangle}{\sqrt{q_t^2+\langle\vec q,\nu\rangle^2}}.
$$

*Proof.* Existence is the construction of the formula: put $\mathrm{den}=\sqrt{q_t^2+\langle\vec q,\nu\rangle^2}$ and $f=a+b\nu=\lvert\tilde q\rvert(q_t+\langle\vec q,\nu\rangle\nu)/\mathrm{den}$, which is invertible in the plane, and $\tilde u_{\mathrm r}=\tilde q f^{-1}$, a versor; the scalar part of $\tilde u_{\mathrm r}$ is $\lvert\tilde q\rvert^{-1}\mathrm{Sc}(\tilde q f^{\natural})$, and the computation of the scalar part and of the component along $\nu$ gives $u_{{\mathrm r}t}=\mathrm{den}/\lvert\tilde q\rvert>0$ and $\langle\vec u_{\mathrm r},\nu\rangle=0$. For uniqueness, let two normalised words be given; then $\tilde u_{\mathrm r}^{-1}\tilde u_{\mathrm r}'=(a+b\nu)(a'+b'\nu)^{-1}=e^{\phi\nu}$ for some $\phi$, since the quotient of two elements of the plane is invertible in the plane. The component of the vector part of $\tilde u_{\mathrm r}'=\tilde u_{\mathrm r}e^{\phi\nu}$ along $\nu$ is $\sin\phi\,u_{{\mathrm r}t}$, which vanishes only for $\phi\in\{0,\pi\}$, and the condition $u_{{\mathrm r}t}'>0$ gives $u_{{\mathrm r}t}\cos\phi>0$, hence $\phi=0$. Verified on $2000$ random elements: the constructed word satisfies all four conditions, and the two conditions cut the circle to one point.

**Corollary (the pair is the normalised projection).** Let $\pi_\nu(\tilde q)=q_te_t+\langle\vec q,\nu\rangle\nu$ be the orthogonal projection of $\tilde q$ onto the plane of the axis. Then
$$
\tilde q=\tilde u_{\mathrm r}\,\lvert\tilde q\rvert\,\widehat{\pi_\nu(\tilde q)},
\qquad \widehat{\pi_\nu(\tilde q)}=\frac{\pi_\nu(\tilde q)}{\lvert\pi_\nu(\tilde q)\rvert},
$$
with $\tilde u_{\mathrm r}$ the versor of the theorem; so the word is the modulus times the normalised projection, corrected by a versor.

*Proof.* The pair of the theorem is $a+b\nu=\lvert\tilde q\rvert\pi_\nu(\tilde q)/\lvert\pi_\nu(\tilde q)\rvert$ in the basis $(e_t,\nu)$, and $\lvert\pi_\nu(\tilde q)\rvert=\mathrm{den}$. Verified numerically.

## The Two Slots Read the Scale and the Angle

**Theorem (the readings).** In the normalised word, the modulus of the pair is the scale of the element and the argument of the pair is the angle of the element in the plane of the axis:
$$
\sqrt{a^2+b^2}=\lvert\tilde q\rvert,\qquad \tan\theta_\nu=\frac{b}{a}=\frac{\langle\vec q,\nu\rangle}{q_t},
$$
where $\theta_\nu$ is the transported angle, the angle of $\pi_\nu(\tilde q)$ in the plane measured from the real line.

*Proof.* The first is $a^2+b^2=N(\tilde q)$; the second is the ratio of the two formulas of the theorem. The angle of the projection is by definition $\arctan$ of the ratio of its two coordinates. Verified on the four coordinate axes.

**Proposition (the transport of the angle).** The angle of the exponential form of $\tilde q$ is $\arctan\bigl(\lvert\vec q\rvert/q_t\bigr)$, and the transported angle is the same formula with the modulus of the vector part replaced by its component along the axis. So the transport replaces $\lvert\vec q\rvert$ by $\langle\vec q,\nu\rangle$ and leaves everything else unchanged.

*Proof.* In the modulus-unit form $\tilde q=r(\cos\theta+\sin\theta\,\vec m)$ with $\vec m$ the unit direction of the vector part, so $\tan\theta=\lvert\vec q\rvert/q_t$; the transported formula is the ratio of the two slots. Verified numerically on general elements.

**Remark (what the two slots are).** $a$ measures the scalar part of the element in the units of the projection, and $b$ measures the component of the vector part along the axis in the same units; the modulus of the pair is the modulus of the element, the argument is the angle in the plane, and the orthogonal complement is entirely absorbed by the versor. **Two real numbers and one versor: the two numbers are the coordinates of the projection, and the versor is the whole of the rest.**

## The Failure on the Real Axis

**Proposition (the degenerate hyperplane).** The normalised word exists and is unique exactly on $\mathbb{H}\setminus\nu^{\perp}$, where $\nu^{\perp}=\{\tilde q:\ q_t=0,\ \langle\vec q,\nu\rangle=0\}$ is a hyperplane of dimension three containing the real axis; on $\nu^{\perp}$ the words form a free circle and the normalisation does not select one.

*Proof.* On $\nu^{\perp}$ the projection $\pi_\nu(\tilde q)$ vanishes, the pair $(a,b)$ is the zero pair and cannot be used to divide; equivalently, every word on the hyperplane has $u_{{\mathrm r}t}=0$, so the condition $u_{{\mathrm r}t}>0$ is empty. Verified on the hyperplane.

**Corollary (the real axis).** On the real axis the word is $(a,b)=(\pm\lvert\lambda\rvert,0)$ with $\tilde u_{\mathrm r}=\pm e_t$, for every axis: the axis is not recorded and the two slots carry no angle.

*Proof.* A real element has $\vec q=0$, hence $\pi_\nu=0$; the words are $\tilde q=\tilde u_{\mathrm r}(a+b\nu)$ with an arbitrary $\tilde u_{\mathrm r}$, and the choice $\tilde u_{\mathrm r}=e_t$ gives $a=\lambda$, $b=0$. Verified for the four axes.

**Remark (the verdict on the failure).** The failure is not a failure of the decomposition of the element: it is a failure of the *transport*, because the transport reads the component of the vector part along the axis, and on the hyperplane there is no such component to read. **The real axis is the worst case: it lies in every hyperplane $\nu^{\perp}$, so the axis pairing of a real number is the same word for every axis and carries no information about it.**

## Worked Examples on the Four Axes

**Example (the axis $\nu=\vec e_x$).** Take $\tilde q=1+2\vec e_x+\tfrac12\vec e_y-\vec e_z$, with $q_t=1$, $\lvert\vec q\rvert^2=4+\tfrac14+1=\tfrac{21}4$ and $\lvert\tilde q\rvert=\tfrac52$. The component along the axis is $2$, so $\mathrm{den}=\sqrt{1+4}=\sqrt5$ and
$$
a=\frac{5}{2\sqrt5}=\frac{\sqrt5}{2},\qquad b=\frac{5}{\sqrt5}=\sqrt5 .
$$
So $a+b\nu=\tfrac{\sqrt5}2(1+2\vec e_x)$ and $\tilde u_{\mathrm r}=\tilde q(a+b\nu)^{-1}$, of norm one, with $\langle\vec u_{\mathrm r},\vec e_x\rangle=0$ and positive scalar part.

**Example (the same element on the axis $\vec e_y$).** The component along $\vec e_y$ is $\tfrac12$, so $\mathrm{den}=\sqrt{1+\tfrac14}=\tfrac{\sqrt5}{2}$ and
$$
a=\frac{\tfrac52\cdot1}{\tfrac{\sqrt5}{2}}=\sqrt5,\qquad b=\frac{\tfrac52\cdot\tfrac12}{\tfrac{\sqrt5}{2}}=\frac{\sqrt5}{2},
$$
so $a^2+b^2=5+\tfrac54=\tfrac{25}{4}$, the square of the scale. The pair is different from the pair of the previous example; only the modulus is the same. Verified on the four coordinate axes.

**Remark (what the examples show).** The scale is the invariant of the pairing, the angle is read on the pair, and the pair changes with the axis as the projection changes; the versor absorbs the difference. **The axis pairing is a family of words indexed by the projective plane of the axes, all with the same first slot read as a modulus, and the family is the family of the Cartan subalgebras.**

## The Three Pairings of the Biquaternion Block

**Remark (the complex case).** In the biquaternion block the polar word has four factors — the positive scale, the central phase, the Hermitian boost and the real rotor — and the groupings of the four give exactly three pairings: the Hamilton root pairing, which groups the scale with the phase and the boost with the rotor, the quaternion pairing, which groups the scale with the rotor, and the Cartan Hermitian pairing, which groups the scale with the boost. Each reads the unit part of the word through an axis, which is a root of $-e_t$ in the first and a Hermitian direction in the third.

**Remark (the real case as the Hamilton pairing).** Over $\mathbb{R}$ the central phase is trivial, so the four factors collapse to two and the three groupings collapse to one: the scale with the versor. The role of the axis is played by the root of $-e_t$ that the element carries, that is by the direction $\nu$ of the plane in which the projection is read. **The axis pairing is the real form of the Hamilton root pairing: the axis is the root, the two slots are the modulus and the transported angle of the root's exponential, and the versor is the part of the word that the root does not see.** The three complex pairings are [The Hamilton Root Pairing of the Polar Decomposition on the N-Regular Sector](the-hamilton-root-pairing-of-the-polar-decomposition-on-the-n-regular-sector.html), [The Quaternion Pairing of the Polar Decomposition on the N-Regular Sector](the-quaternion-pairing-of-the-polar-decomposition-on-the-n-regular-sector.html) and [The Cartan Hermitian Pairing of the Polar Decomposition on the N-Regular Sector](the-cartan-hermitian-pairing-of-the-polar-decomposition-on-the-n-regular-sector.html).

## The Comparison of the Three Forms of the Word

| | modulus-unit | rational chart | exponential | axis pairing |
|---|---|---|---|---|
| word | $r\tilde u_{\mathrm r}$ | $r\,u(v)$ | $r\exp(\theta\vec m)$ | $\tilde u_{\mathrm r}(a+b\nu)$ |
| real slots | $r>0$ | the three coordinates of $v$ | $r$ and $\theta$ | $a,b$ |
| unit factor | any versor | any versor | $\exp(\theta\vec m)$ | the versor orthogonal to the axis |
| domain | all | $\mathbb{H}\setminus(-\infty,0]$ | $\mathbb{H}\setminus(-\infty,0]$ | $\mathbb{H}\setminus\nu^{\perp}$ |
| uniqueness | yes, both factors | yes, both factors | off the real axis | off the hyperplane |
| the axis | absent | absent | carried by $\vec m$ | named in advance |

**Remark (the price of each form).** The modulus-unit form is total, unique and carries no axis; the rational chart is total on a cut plane, unique, and rational in both directions; the exponential names the axis of the element and is unique off the real axis; the axis pairing names the axis in advance and is unique off a hyperplane. **The four forms are the four ways of spending the two degrees of freedom of the versor: two scalars, three rational coordinates, a scalar and an angle, or a scalar and a slot pair.**

## Summary

For a unit axis $\nu$, the plane $\mathbb{C}_\nu=\mathbb{R}\oplus\mathbb{R}\nu$ is a copy of the complex numbers, a maximal commutative subalgebra, and a Cartan subalgebra of the algebra.

Every element is a versor times an element of the plane, and the words over a fixed element form a free circle orbit; the normalisation $\langle\vec u_{\mathrm r},\nu\rangle=0$ with positive scalar part selects exactly one word off the hyperplane $\nu^{\perp}$.

In the selected word the pair is the normalised projection of the element onto the plane, $a+b\nu=\lvert\tilde q\rvert\widehat{\pi_\nu(\tilde q)}$, and the two slots read the scale $\sqrt{a^2+b^2}=\lvert\tilde q\rvert$ and the transported angle $\tan\theta_\nu=\langle\vec q,\nu\rangle/q_t$.

On the hyperplane $\nu^{\perp}$, which contains the real axis, the normalisation degenerates and the word is not unique; on the real axis every axis gives the same word and no axis is recorded.

The pairing is the real form of the Hamilton root pairing of the biquaternion block, and it is compared with the modulus-unit, rational-chart and exponential forms of the same word.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\nu$ | a real unit axis, $\nu^2=-e_t$ |
| $\mathbb{C}_\nu$ | the plane $\mathbb{R}\oplus\mathbb{R}\nu$ |
| $\pi_\nu(\tilde q)$ | the orthogonal projection $q_te_t+\langle\vec q,\nu\rangle\nu$ |
| $a,b$ | the two real slots, the coordinates in the plane |
| $\theta_\nu$ | the transported angle, $\arctan(b/a)$ |
| $\tilde u_{\mathrm r}$ | the versor of the word |
| $\nu^{\perp}$ | the hyperplane on which the pairing degenerates |

## Further Reading

- [Modulus–Unit Polar Decomposition of Quaternions](modulus-unit-polar-decomposition-of-quaternions.html), [Rational-Chart Polar Decomposition of Quaternions](rational-chart-polar-decomposition-of-quaternions.html) and [Exponential Polar Decomposition of Quaternions](exponential-polar-decomposition-of-quaternions.html) for the three forms compared here.
- [Decompositions Along the Remarkable Subspaces of the Quaternions](decompositions-along-the-remarkable-subspaces-of-the-quaternions.html) for the axis decomposition of the algebra.
- [Quaternion Automorphisms and Derivations](quaternion-automorphisms-and-derivations.html) for the centralisers and the Cartan subalgebras.
- [The Hamilton Root Pairing of the Polar Decomposition on the N-Regular Sector](the-hamilton-root-pairing-of-the-polar-decomposition-on-the-n-regular-sector.html) for the complex counterpart of this pairing.
