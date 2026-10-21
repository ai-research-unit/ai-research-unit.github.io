# __The Quaternion Pairing of the Polar Element Representation of Biquaternions__

## Introduction

Every biquaternion of non-vanishing norm is the ordered product of a positive real scale, a central phase and two unit factors,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
= r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) .
$$

| # | factor | name | exponent | root | range | real dimension | action | stable subspaces |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | — | — | $r \in \mathbb{R}$, $r>0$ | $1$ | $\tilde Q\mapsto r^{2}\tilde Q$ | $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ |
| 2 | $\exp(i\alpha)$ | central phase | $i\alpha$ | $i$ | $\alpha \in \left(-\frac{\pi}{2},\frac{\pi}{2}\right]$ | $1$ | $\tilde Q\mapsto \exp(i\alpha)\tilde Q$ | $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ |
| 3 | $\tilde U_{\mathrm b} = \exp\bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\bigr)$ | boost | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $i\vec u_{\mathrm b}$ | $\psi \ge0$, $\vec u_{\mathrm b}\in\mathcal{A}$ | $3$ | $\tilde Q\mapsto \tilde U_{\mathrm b}\tilde Q\tilde U_{\mathrm b}^{*}$ | $\mathbb{M}_+$, $\mathbb{M}_-$ |
| 4 | $\tilde u_{\mathrm r} = \exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | rotor | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\vec u_{\mathrm r}$ | $\theta \in [0,2\pi]$, $\vec u_{\mathrm r}\in\mathcal{A}$ | $3$ | $\tilde Q\mapsto \tilde u_{\mathrm r}\tilde Q\tilde u_{\mathrm r}^{-1}$ | $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ |

The action column records the operation by which the factor acts on the algebra. For the scale, the boost and the rotor this is the sandwich by the factor in view, that is the dilation $\tilde Q\mapsto r^{2}\tilde Q$, the congruence $\tilde Q\mapsto\tilde U_{\mathrm b}\tilde Q\tilde U_{\mathrm b}^{*}$ and the conjugation $\tilde Q\mapsto\tilde u_{\mathrm r}\tilde Q\tilde u_{\mathrm r}^{-1}$. The phase is central and its sandwich is the identity, so its row records multiplication by the scalar, the only action under which it is not in the kernel; this is the one row that departs from the sandwich convention of *The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces*, where the phase would list every subspace because it acts trivially. The scale preserves $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$. The phase preserves $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ and no other: on a real form the factor $\exp(i\alpha)$ turns a real part into an imaginary one. The boost preserves $\mathbb{M}_+$ and $\mathbb{M}_-$ and no other. The rotor preserves $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$: conjugation by a real unit quaternion is an automorphism of $\mathbb{B}$ commuting with the three conjugations, so it carries each of the six into itself. Parameters are generic; at the identity value of a parameter the factor is $e_t$ and preserves every subspace. Two-sided multiplication by the rotor, $\tilde Q\mapsto\tilde u_{\mathrm r}\tilde Q\tilde u_{\mathrm r}$, is a different action and is not used: under it the rotor preserves only $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, while under conjugation it preserves all six.

This is the polar word of *The Polar Element Representation of Biquaternions*. It is recalled in full because the pairing below regroups exactly these four factors. The scale $r$ is a positive real and the phase $\exp(i\alpha)$ is central, with $\alpha$ real. The last two factors are the **boost** $\tilde U_{\mathrm b}$ and the **rotor** $\tilde u_{\mathrm r}$, with axes $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ the unit real pure quaternions of the axis sphere $\mathcal{A}$ of the reference article, $\psi\ge0$ the rapidity and $\theta\in[0,2\pi]$ the rotation angle. The boost is Hermitian positive and of unit norm, and the rotor is a unit real quaternion, hence also of unit norm. The four factors are unique. They can be grouped in pairs in exactly three ways, and the three pairings of the series regroup the same four factors. What differs is where the brackets fall, and what each bracketed pair is then recognised to be.

**The quaternion pairing** is the grouping that joins the scale to the rotor and the phase to the boost, and writes the element with a real quaternion modulus $\tilde q$ and a real quaternion angle $\tilde\Psi$:

$$
\tilde{Q} = \tilde q\,\exp(i\tilde\Psi), \qquad \tilde q = r\,\tilde u_{\mathrm r}, \qquad \exp(i\tilde\Psi) = \exp(i\alpha)\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r} .
$$

The fourth factor of the table, the rotor $\tilde u_{\mathrm r}$, is moved to the left, past the central phase, next to the scale, and the boost is conjugated by it so that the two non-central factors can stand together on the right as one exponential. The modulus $\tilde q = r\tilde u_{\mathrm r}$ is a real quaternion, and the angle is the real quaternion $\tilde\Psi = \alpha+\theta_{\mathrm b}\vec u_{\mathrm b}'$, with $\theta_{\mathrm b} = \psi/2$ half the rapidity and $\vec u_{\mathrm b}' = \tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ the boost axis rotated by the rotor. The element is thus determined by the two real quaternions $\tilde q$ and $\tilde\Psi$. The split itself is made by the real quaternion part $\tilde q_r$ of the element, which the construction has to invert. The pairing is not named for the complex numbers. Its only complex object is the central phase, and $\mathbb{C}$ has a polar representation of its own in *Complex Polar Element Representation*; the older name *complex representation* invited a confusion that the name here avoids. One reading of the first factor is worth stating at the outset: written $\tilde q = r\tilde u_{\mathrm r}$, the modulus $\tilde q$ is the polar representation of an ordinary quaternion in the sense of *Quaternion Polar Element Representation*, with the same two factors and the same symbols. The pairing therefore carries the polar word of the quaternion algebra as its first factor, and only the second factor leaves that algebra.

The pairing is **partial**: its modulus is a composite object, the product of the scale and the rotor, and the pairing as constructed is available only where that object can be read from the parts of the element. The other partial pairing, the Hamilton one, groups the scale with the phase and the boost with the rotor; the third grouping, in which the scale joins the boost and the phase joins the rotor, is not partial and is *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions*.

**The approach.** The article states the pairing, its construction from the parts of the element, the identity that the two readings give the same real quaternion, the reading of its first factor as the polar representation of the ordinary quaternions, its domain, and the two senses in which a partial pairing holds; it then compares the pairing with the Hamilton pairing, records the degenerate limits and the behaviour under the three conjugations, and closes with four worked examples. It takes the construction of the four factors from *The Polar Element Representation of Biquaternions* and does not re-derive it. No physics is invoked.

**The result, in one sentence.** Writing $\tilde{Q} = \tilde q_r+i\tilde q_i$ with real quaternion parts $\tilde q_r,\tilde q_i$, the element is the product $\tilde q\exp(i\tilde\Psi)$ of the quaternion modulus $\tilde q = \tilde q_r(\cos\tilde\Psi)^{-1}$ and the quaternion angle $\tan\tilde\Psi = \tilde q_r^{-1}\tilde q_i$ whenever $\tilde q_r$ is invertible and the biquaternion norm does not vanish; the two factors are the polar word's scale-times-rotor and the exponential of its central phase and its rotor-conjugated boost.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_x\vec e_y = \vec e_z$ and the central scalar imaginary $i$, $i^2 = -1$. An element is $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu = Q_te_t+\vec Q$ with $\vec Q = \sum_{k=1}^{3}Q_k\vec e_k$ and $Q_\mu\in\mathbb{C}$, and its real and imaginary quaternion parts are $\tilde q_r,\tilde q_i\in\mathbb{H}$ under $\tilde{Q} = \tilde q_r+i\tilde q_i$; the quaternion subspace is $\mathbb{H}_{\mathbb{B}}$. The quaternion conjugation is $\tilde{Q}^{\natural} = Q_te_t-\vec Q$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \overline{Q_t}e_t+\overline{\vec Q}$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, the two operations commuting. The norm is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}$, and the domain of the polar representation is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. The symbols $r$, $\exp(i\alpha)$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$, $\Rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ and the subspaces $\mathbb{M}_\pm$, $\mathrm{Sp}(1)$ are those of *The Polar Element Representation of Biquaternions*. The quaternion modulus is $\tilde q$ and the quaternion angle is $\tilde\Psi$, with $\theta_{\mathrm b} = \psi/2$ half the rapidity and $\vec u_{\mathrm b}'$ the boost axis rotated by the rotor.

## The Quaternion Pairing

### The Pairing

The quaternion pairing is the pairing of the scale with the rotor against the phase with the boost:

$$
\tilde{Q} = \tilde q\,\exp(i\tilde\Psi), \qquad \tilde q = r\,\tilde u_{\mathrm r}, \qquad \exp(i\tilde\Psi) = \exp(i\alpha)\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r} .
$$

The modulus is a real quaternion, of norm $\langle \tilde q,\tilde q\rangle_{\natural} = r^2$, and the exponential is central in its phase but not in its boost: the boost has been conjugated by the rotor, so that it can stand to the right of the modulus in the canonical order. Writing the conjugated boost as

$$
\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \cosh\theta_{\mathrm b}\,e_t + i\sinh\theta_{\mathrm b}\,\vec u_{\mathrm b}', \qquad \theta_{\mathrm b} = \frac{\psi}{2},
$$

with $\psi$ the rapidity of $\tilde U_{\mathrm b}$ and $\vec u_{\mathrm b}'$ its axis rotated by the rotor, the exponent is

$$
\tilde\Psi = \alpha + \theta_{\mathrm b}\,\vec u_{\mathrm b}' ,
$$

a real quaternion with scalar part $\alpha$ and pure quaternion part $\theta_{\mathrm b}\vec u_{\mathrm b}'$. This is the arrangement in which the pairing is stated: its $\tilde\Psi$ has a scalar part and a pure part, and the two travel together.

### The Statement

The pairing is stated as follows. Write $\tilde{Q} = \tilde q_r + i\tilde q_i$ with $\tilde q_r,\tilde q_i\in\mathbb{H}$ the real and imaginary quaternion parts, suppose $\tilde q_r \neq 0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$, put $\tan\tilde\Psi = \tilde q_r^{-1}\tilde q_i$ and $\tilde q = \tilde q_r(\cos\tilde\Psi)^{-1}$. Then $\tilde{Q} = \tilde q\exp(i\tilde\Psi)$ with $\tilde q$ and $\tilde\Psi$ real quaternions. The verification is the computation $\tilde q\exp(i\tilde\Psi) = \tilde q_r(\cos\tilde\Psi)^{-1}(\cos\tilde\Psi+i\sin\tilde\Psi) = \tilde q_r + i\tilde q_r\tan\tilde\Psi = \tilde q_r+i\tilde q_i$, in which the two trigonometric factors commute because they are functions of the single quaternion $\tilde\Psi$.

### The Modulus Is a Real Quaternion

The modulus $\tilde q = r\tilde u_{\mathrm r}$ of the pairing is exactly the modulus $\tilde q_r(\cos\tilde\Psi)^{-1}$ of the construction from the element's parts. The identity is not a coincidence of two constructions; it follows from the polar representation. Since $\tilde q = r\tilde u_{\mathrm r}$ is a real quaternion and $\exp(i\tilde\Psi)$ is an exponential of the central imaginary, the real quaternion part of $\tilde{Q} = \tilde q\exp(i\tilde\Psi)$ is

$$
\tilde q_r = \tilde q\,\frac{\exp(i\tilde\Psi)+\exp(-i\tilde\Psi)}{2} = \tilde q\cos\tilde\Psi ,
$$

because the complex conjugation of $\exp(i\tilde\Psi)$ is $\exp(-i\tilde\Psi)$ and the modulus $\tilde q = r\tilde u_{\mathrm r}$ is fixed by it. Hence $\tilde q = \tilde q_r(\cos\tilde\Psi)^{-1}$, which is the construction formula. The identity is therefore the equality of the modulus of the pairing with the modulus of the construction, not an agreement of two independent constructions.

### The First Factor Is the Polar Form of an Ordinary Quaternion

The modulus $\tilde q = r\tilde u_{\mathrm r}$ is not a new object. Read inside the ordinary quaternions $\mathbb{H}$, it is exactly the polar representation

$$
\tilde q = r\,\tilde u_{\mathrm r}, \qquad r\in\mathbb{R}, \quad r>0, \qquad \langle\tilde u_{\mathrm r}\rangle_{\natural} = 1 ,
$$

of *Quaternion Polar Element Representation*: the same two factors, the same modulus $r = \sqrt{\langle \tilde q,\tilde q\rangle_{\natural}}$ and the same unit factor $\tilde u_{\mathrm r}$, a point of $\mathrm{Sp}(1)$. The quaternion pairing therefore reads

$$
\tilde{Q} = \bigl(r\,\tilde u_{\mathrm r}\bigr)\,\exp(i\tilde\Psi) ,
$$

the polar form of an ordinary quaternion followed by the exponential of a real quaternion; only the second factor is not an ordinary quaternion, its coefficients being complex. The first factor needs no construction: it is read from the polar word, with no part of the element to invert.

The companion article also gives these two factors in exponential form: its unit factor is $\exp(\mu\tfrac{\theta}{2})$ whenever $\vec q_{a,\mathrm r}\neq0$, with

$$
\mu = \frac{\vec q_{a,\mathrm r}}{\lvert\vec q_{a,\mathrm r}\rvert} , \qquad \theta = 2\arccos\bigl(\mathrm{Sc}\,\tilde u_{\mathrm r}\bigr)\in(0,2\pi) ,
$$

the rotation angle, twice the angle of the unit factor; so the first factor of the pairing is the two-exponential word of the companion article,

$$
\tilde q = \exp(\ln r)\,\exp\Bigl(\mu\frac{\theta}{2}\Bigr) .
$$

The polar word of the smaller algebra thus sits inside the biquaternion word as its modulus, and the nested word has the properties that the second factor lacks. Its two factors are a positive real and a unit element, so the decomposition is unique and needs no construction and no choice of branch. It is fixed by complex conjugation, $\bar{\tilde q} = \tilde q$. And it is closed under the other two conjugations in the same shape, $\tilde q^{\natural} = r\tilde u_{\mathrm r}^{\natural}$ and $\tilde q^{*} = r\tilde u_{\mathrm r}^{\natural}$, again the polar representation of an ordinary quaternion with the same modulus $r$ and the conjugated unit factor.

The correspondence is a correspondence of objects, not of names: the modulus of the pairing is the ordinary quaternion written in the two-factor form of the companion article, while the Hamilton modulus is the complex scalar $\Rho = r\exp(i\alpha)$, an object of the centre. This is one of the two senses, independent of domain, in which the two named pairings are complementary; the other is recorded in the section on the conjugations below.

### The Domain

The construction from the element's parts needs $\tilde q_r^{-1}$, so the pairing, as constructed from the parts, is available on

$$
\left\{\tilde{Q} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0 \ \text{ and } \ \tilde q_r\neq0\right\},
$$

the condition $\tilde q_r\neq0$ being equivalent to the invertibility of the real quaternion part because $\mathbb{H}$ is a division algebra.

The two conditions are again independent, and the second is met or missed independently of the first: the element $i\vec e_x+i\vec e_y$ has $N = -2\neq0$, so it is invertible, while its real quaternion part vanishes, so the construction fails on it; and the element $1+\vec e_x+i\vec e_y$ has $\tilde q_r = 1+\vec e_x \neq 0$ but no Hamilton representation, so the two domains are not nested. Within its domain the representation is unique up to the replacement $\tilde\Psi\mapsto\tilde\Psi+\pi$ with the sign of $\tilde q$ adjusted, which is the branch ambiguity of the tangent.

### The Pairing Without the Construction

A remark is in order, because it separates two distinct statements. The pairing $\tilde{Q} = (r\tilde u_{\mathrm r})\exp(i\tilde\Psi)$ is a grouping of the four factors of the polar representation, and the four factors exist whenever $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. Hence the **factorisation** of $\tilde{Q}$ as a real quaternion times an exponential of the central imaginary exists on the whole complement of the null cone, while the **construction** of it from the real quaternion part needs $\tilde q_r$ invertible. On the element $i\vec e_x+i\vec e_y$ the pairing gives

$$
i\vec e_x+i\vec e_y = \left(\vec e_x+\vec e_y\right)\,\exp\!\left(i\frac{\pi}{2}\right),
$$

with modulus $\vec e_x+\vec e_y$, which is a real quaternion, and exponent $\pi/2$, which is real: the factorisation holds, and the construction formula $\tan\tilde\Psi = \tilde q_r^{-1}\tilde q_i$ is what fails, since $\tilde q_r = 0$ has no inverse. The distinction between the factorisation and the construction is recorded here because the domain of a partial representation is a statement about the construction, and the pairing is what shows it to be a grouping of the four factors.

## The Domain Comparison

### The Table

| representation | modulus | second factor | available when | condition on the element |
|---|---|---|---|---|
| Hamilton | $\Rho = r\exp(i\alpha)$, complex scalar | $\exp(\vec\Xi\Theta) = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $(\vec Q,\vec Q)\neq0$ and $N\neq0$ | the vector part is non-null |
| quaternion pairing | $\tilde q = r\tilde u_{\mathrm r}$, real quaternion | $\exp(i\tilde\Psi) = \exp(i\alpha)\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\tilde q_r\neq0$ and $N\neq0$ for the construction; $N\neq0$ for the pairing | the real quaternion part is invertible |
| polar representation | four factors | four factors | $N\neq0$ | none beyond invertibility |

The third pairing, the Cartan pairing, is available whenever $N\neq0$, the full domain of the polar representation; it is not partial and is treated in *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions*.

### The Inclusions and the Counterexamples

The domains are not nested. The Hamilton and quaternion domains overlap without containing each other, and both are contained in the domain of the polar representation. The following elements separate the cases, and each is computed in the examples below.

| element | $N$ | $(\vec Q,\vec Q)$ | $\tilde q_r$ | Hamilton | quaternion |
|---|---|---|---|---|---|
| $(1+i)e_t+\vec e_x+2\vec e_y$ | $5+2i$ | $5$ | $1+\vec e_x+2\vec e_y$ | yes | yes |
| $1+\vec e_x+i\vec e_y$ | $1$ | $0$ | $1+\vec e_x$ | no | yes |
| $i\vec e_x+i\vec e_y$ | $-2$ | $-2$ | $0$ | yes | no |
| $i$ | $-1$ | $0$ | $0$ | no | no |

The first line is the generic case, in which both partial representations are available and give two different groupings of the same four factors. The second line separates the Hamilton pairing from the quaternion one: the element is invertible and has an invertible real part, but its vector part is null, so no axis exists. The third line separates the quaternion pairing from the Hamilton one: the vector part is non-null and the real part vanishes. The fourth line, the scalar imaginary, fails the two conditions simultaneously and lies outside both partial representations; it is nevertheless an invertible element, and the polar representation is $i = 1\cdot \exp(i\pi/2)\cdot e_t\cdot e_t$.

The complement of the null cone is the union of the two domains together with the nonzero purely imaginary complex scalars, and these scalars are exactly the elements that the Hamilton and quaternion pairings miss between them. The reason is elementary: $\tilde q_r = 0$ means that every coefficient is purely imaginary, $Q_\mu = ib_\mu$ with $b_\mu\in\mathbb{R}$, and then

$$
(\vec Q,\vec Q) = \sum_{k=1}^{3}(ib_k)^2 = -\sum_{k=1}^{3}b_k^2 \leq 0 ,
$$

a negative real that vanishes only when $b_1 = b_2 = b_3 = 0$. So the two conditions fail together only on $\tilde{Q} = ib_0e_t$, $b_0\neq0$. Each such element lies in the domain of the polar representation, with $r = |b_0|$ and $\alpha = \pi/2$, the sign of $b_0$ being carried by the rotor; and it has an ordinary complex polar form $ib_0 = |b_0|\exp(\pm i\pi/2)$, which the quaternion pairing reproduces only in the degenerate sense of the section on the degenerate limits below.

### Why the Four-Factor Form Is the Reference

Two properties of the polar representation explain its role as the reference of the series, and neither is shared by the partial representations.

**Its domain is the largest.** The only obstruction is the vanishing of the biquaternion norm, which is the vanishing of the determinant of the matrix image. The partial representations fail on additional sets, and each failure is a failure to construct the pairing from a part of the element: the Hamilton axis cannot be normalised when the vector part is null, and the quaternion modulus cannot be constructed from $\tilde q_r$ when $\tilde q_r$ is not invertible.

**Its modulus separates into a scale and a phase.** The Hamilton representation calls the complex number $\Rho = r\exp(i\alpha)$ the modulus, and one of its two constituents, $r$, is a positive real and the other, $\exp(i\alpha)$, is central. The quaternion pairing calls the real quaternion $r\tilde u_{\mathrm r}$ the modulus, one factor of which is a positive real and the other a rotation. In each case a positive real scale is entangled with a non-scalar factor, and only the four-factor representation exhibits the scale by itself.

## Behaviour Under the Three Conjugations

The algebra has three nontrivial conjugations: quaternion conjugation ${}^{\natural}$, the anti-automorphism fixing the centre $\mathbb{C}_{\mathbb{B}}$; complex conjugation $\bar{\cdot}$, the automorphism conjugating every coefficient; and Hermitian conjugation ${}^{*} = {}^{\natural}\circ\bar{\cdot}$, the two operations commuting because one acts on the coefficients and the other on the units. The three act on the quaternion pairing below as a computation rather than as a contrast of styles; their action on the Hamilton data is computed in *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions*, and the contrast between the two is what the closing subsection records.

### The Quaternion Data

In $\tilde{Q} = \tilde q\exp(i\tilde\Psi)$ the modulus $\tilde q$ and the angle $\tilde\Psi$ are real quaternions, so $\bar{\tilde q} = \tilde q$ and $\bar{\tilde\Psi} = \tilde\Psi$, while $\tilde q^{\natural}\neq \tilde q$ and $\tilde\Psi^{\natural}\neq\tilde\Psi$ in general; the two factors need not commute, and it is this that makes the quaternion pairing the less symmetric of the two under conjugation.

**Complex conjugation.** Since $\bar{\cdot}$ is an automorphism fixing $\tilde q$ and $\tilde\Psi$ and conjugating the scalar imaginary,

$$
\bar{\tilde{Q}} = \tilde q\exp(-i\tilde\Psi) :
$$

the modulus and the angle are both unchanged and only the sign of the exponent changes. Equivalently, the canonical angle of $\bar{\tilde{Q}}$ is $-\tilde\Psi$, because the real and imaginary quaternion parts of $\bar{\tilde{Q}}$ are $(\tilde q_r,-\tilde q_i)$, whence $\tan\tilde\Psi(\bar{\tilde{Q}}) = \tilde q_r^{-1}(-\tilde q_i) = -\tan\tilde\Psi$.

**Quaternion conjugation.** Since ${}^{\natural}$ is an anti-automorphism, the two factors exchange order:

$$
(\tilde{Q})^{\natural} = \exp(i\tilde\Psi^{\natural})\,\tilde q^{\natural} ,
$$

which is not the canonical shape, the modulus of the quaternion pairing being the left factor. Recovering the canonical shape requires the parts of the conjugated element, and the result is not the conjugate angle in general. The parts of $(\tilde{Q})^{\natural}$ are $(\tilde q_r^{\natural},\tilde q_i^{\natural})$, so its angle $\tilde\Psi'$ satisfies

$$
\tan\tilde\Psi' = (\tilde q_r^{\natural})^{-1}\tilde q_i^{\natural} , \qquad\text{whereas}\qquad (\tan\tilde\Psi)^{\natural} = \tilde q_i^{\natural}(\tilde q_r^{\natural})^{-1} ,
$$

and the two agree exactly when $\tilde q_r^{\natural}$ and $\tilde q_i^{\natural}$ commute, equivalently when $\tilde q_r$ and $\tilde q_i$ commute. The commuting case is exact and the non-commuting case is genuinely different: the element

$$
\tilde{Q} = (1+\vec e_x) + i(\vec e_x+\vec e_y), \qquad \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 2i, \qquad \tilde q_r = 1+\vec e_x\ \text{invertible} ,
$$

has $\tan\tilde\Psi = \tfrac12(1+\vec e_x+\vec e_y-\vec e_z)$, conjugate $\tfrac12(1-\vec e_x-\vec e_y+\vec e_z)$, and angle of the conjugated element $\tan\tilde\Psi' = \tfrac12(1-\vec e_x-\vec e_y-\vec e_z)$; the two differ in the $\vec e_z$ coefficient alone, the commutator being $\tilde q_r\tilde q_i-\tilde q_i\tilde q_r = 2\vec e_z$.

**Hermitian conjugation.** Combining the two, $\tilde{Q}^{*} = \exp(-i\tilde\Psi^{\natural})\,\tilde q^{\natural}$, again with the factors in the reversed order.

### What the Comparison Shows

The two named representations are distinguished by conjugation as sharply as by domain. For the Hamilton representation all three conjugations act on the parameters, ${}^{\natural}$ reversing the axis, $\bar{\cdot}$ conjugating the three parameters and ${}^{*}$ doing both, and the representation is closed under every one of them, the computation being in *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions*. For the quaternion pairing, complex conjugation touches only the scalar imaginary of the exponent, while quaternion conjugation and Hermitian conjugation exchange the order of the two factors, and quaternion conjugation carries the canonical angle to the quaternion conjugate of the angle only when the two quaternion parts of the element commute. A statement about a biquaternion and its conjugates is therefore cheapest in the representation whose conjugation action it needs, and this is a second sense, independent of domain, in which the Hamilton and quaternion pairings are complementary.

## The Two Degenerate Limits

Two exact statements identify which classical polar form each named pairing generalises. Both are cases in which the element lies in a proper subalgebra of $\mathbb{B}$.

**A real quaternion.** If all four coefficients of $\tilde{Q}$ are real and the vector part is nonzero then $\tilde{Q}\in\mathbb{H}_{\mathbb{B}}$, the biquaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu q_\mu^2$ is a positive real, and with the principal branch of the square root

$$
\Rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}} \in \mathbb{R}_{>0}, \qquad \cos\Theta = \frac{q_t}{\Rho}\in[-1,1], \qquad \sin\Theta = \frac{|\vec q|}{\Rho}\in[0,1] ,
$$

so both the modulus and the angle are real and $\vec\Xi = \vec q/|\vec q|$ is a unit pure real quaternion. The Hamilton representation is then the quaternion polar representation of the companion article *Quaternion Polar Element Representation*, in the two forms that article gives it: the two-factor form $\tilde q = r\tilde u_{\mathrm r}$ with $r = \Rho$ and $\tilde u_{\mathrm r} = \exp(\vec\Xi\Theta)$, and the exponential form $\exp(\ln r)\exp(\mu\tfrac{\theta}{2})$ with $\mu = \vec\Xi$ and $\theta = 2\Theta$, the companion's $\theta$ being twice the angle of the unit factor, which is $\Theta$ here. The identification is exact rather than asymptotic. The quaternion pairing is available on the same elements and is degenerate there: $\tilde q_i = 0$, hence $\tan\tilde\Psi = 0$, $\tilde\Psi = 0$ and $\tilde q = \tilde q_r = \tilde{Q}$, the element itself in the two-factor form $\tilde q = r\tilde u_{\mathrm r}$ of the same article, with $r = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ and $\tilde u_{\mathrm r} = \tilde{Q}/r$; the second factor is trivial. In this limit the two named pairings are two readings of the same two-factor word of the companion article: the quaternion pairing gives the word itself, with its second factor trivial, and the Hamilton pairing gives the exponential form of its unit factor.

**A complex scalar.** If $\tilde{Q} = ze_t$ with $z\in\mathbb{C}$ and $\operatorname{Re}z\neq0$ then the vector part vanishes, so $B = 0$ and the Hamilton representation is unavailable, while the quaternion pairing gives

$$
\tilde q_r = (\operatorname{Re}z)e_t, \qquad \tilde q_i = (\operatorname{Im}z)e_t, \qquad \tan\tilde\Psi = \frac{\operatorname{Im}z}{\operatorname{Re}z}\,e_t, \qquad \tilde q = \frac{\operatorname{Re}z}{\cos\tilde\Psi}\,e_t = |z|\,e_t ,
$$

so that $\tilde\Psi = (\arg z)e_t$ is a scalar and $\tilde{Q} = |z|\exp\!\big(i(\arg z)e_t\big)$: the quaternion pairing reduces to the ordinary complex polar form of $\mathbb{C}$, with the central scalar imaginary of the algebra in the role of the scalar imaginary of $\mathbb{C}$ and the quaternion modulus collapsed to a scalar.

The two limits are disjoint, and together they are the reason the two named pairings are complementary rather than competing: the Hamilton representation is the one that carries the quaternion polar form into the biquaternions, and the quaternion pairing is the one that carries the complex polar form.

## Worked Examples

### The Generic Element

Take $\tilde{Q} = (1+i)e_t+\vec e_x+2\vec e_y$, the generic element of the table above. Its polar representation, computed in the companion article, is

$$
r = 2.320595787, \quad \alpha = 0.190253189, \quad \tilde U_{\mathrm b} = 1.072349609\,e_t - 0.173166789\,i\,\vec e_x - 0.346333577\,i\,\vec e_y, \quad \tilde u_{\mathrm r} = 0.470592172\,e_t+0.394599292\,\vec e_x+0.789198585\,\vec e_y .
$$

*The regrouping.* The modulus is the real quaternion

$$
\tilde q = r\tilde u_{\mathrm r} = 1.092054\,e_t + 0.915705\,\vec e_x + 1.831411\,\vec e_y ,
$$

matching the modulus $\tilde q_r(\cos\tilde\Psi)^{-1}$ of the construction with $\tilde q_r = 1+\vec e_x+2\vec e_y$, and the exponent is

$$
\tilde\Psi = \alpha + \frac{\psi}{2}\vec u_{\mathrm b}' = 0.190253 - 0.169108\,\vec e_x - 0.338216\,\vec e_y ,
$$

where $\psi = 0.756273220$ is the rapidity of $\tilde U_{\mathrm b}$ and $\vec u_{\mathrm b}' = -(1,2,0)/\sqrt5$ is its axis, unchanged by the rotor because the rotor's axis is parallel to it.

The two partial regroupings of the same four factors are therefore displayed on one element, the Hamilton regrouping of it being computed in *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions*, and their moduli are visibly different objects: a complex scalar and a real quaternion. The third pairing, the Cartan pairing, groups the four factors differently again and is treated in *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions*.

### The Element with a Null Vector Part

Take $\tilde{Q} = 1+\vec e_x+i\vec e_y$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 1+1+i^2 = 1$ and $(\vec Q,\vec Q) = 1+i^2 = 0$, so the Hamilton representation does not exist: $B = 0$ and the axis is undefined. The quaternion pairing does exist, with

$$
r = 1, \qquad \alpha = 0, \qquad \tilde U_{\mathrm b} = 1.414213562\,e_t + 0.707106781\,i\,\vec e_y + 0.707106781\,i\,\vec e_z, \qquad \tilde u_{\mathrm r} = 0.707106781\left(e_t+\vec e_x\right) ,
$$

so that the quaternion modulus is $\tilde q = \tilde u_{\mathrm r} = 0.707106781(e_t+\vec e_x)$. The modulus computed from the parts, $\tilde q_r(\cos\tilde\Psi)^{-1}$, is the same quaternion, and this equality is the identity proved in the section on the pairing above; the element is also the non-scalar example of that section.

### The Element with a Vanishing Real Part

Take $\tilde{Q} = i\vec e_x+i\vec e_y$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -2$ and $\tilde q_r = 0$, so the construction of the quaternion pairing from the element's parts fails. The polar representation gives

$$
r = \sqrt{2}, \qquad \alpha = \frac{\pi}{2}, \qquad \tilde U_{\mathrm b} = e_t, \qquad \tilde u_{\mathrm r} = \frac{\vec e_x+\vec e_y}{\sqrt{2}} ,
$$

so the Hamilton representation exists, with $B = \sqrt{-2} = i\sqrt{2}$, axis $\vec\Xi = (\vec e_x+\vec e_y)/\sqrt2$, $\Rho = i\sqrt2$, $\cos\Theta = 0$ and $\sin\Theta = 1$:

$$
\tilde{Q} = i\sqrt{2}\,\exp\!\left(\frac{\vec e_x+\vec e_y}{\sqrt2}\frac{\pi}{2}\right) .
$$

The quaternion pairing, on the other hand, exists with modulus $r\tilde u_{\mathrm r} = \vec e_x+\vec e_y$ and exponent $\tilde\Psi = \alpha = \pi/2$, as recorded above. The example therefore exhibits both the failure of the construction and the existence of the factorisation.

### The Scalar Imaginary

Take $\tilde{Q} = i$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -1$, so the element is invertible and the polar representation is $i = 1\cdot \exp(i\pi/2)\cdot e_t\cdot e_t$: the scale is one and the boost and the rotor are trivial. Both partial constructions fail, since $\vec Q = 0$ and $\tilde q_r = 0$; the element is nevertheless in the domain of the polar representation, and the Cartan pairing, which needs only $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$, is available as $i = e_t\cdot i$. The example is the clearest single illustration of the difference between having a representation and being able to construct one from the element's parts.


## Summary

The polar representation of a biquaternion has four factors, so it has exactly three pairings. The quaternion pairing is the one that groups the scale with the rotor into the quaternion modulus $\tilde q = r\tilde u_{\mathrm r}$ and the phase with the rotor-conjugated boost into the exponential $\exp(i\tilde\Psi)$, both factors real quaternions. The construction reads the pairing off the parts of the element, $\tan\tilde\Psi = \tilde q_r^{-1}\tilde q_i$ and $\tilde q = \tilde q_r(\cos\tilde\Psi)^{-1}$, and the identity $\tilde q = \tilde q_r(\cos\tilde\Psi)^{-1}$ is what ties the construction to the polar grouping, the two readings giving the same real quaternion $r\tilde u_{\mathrm r}$. That modulus is the polar representation $\tilde q = r\tilde u_{\mathrm r}$ of the ordinary quaternions of *Quaternion Polar Element Representation*, so the pairing carries the whole two-factor word of the quaternion algebra as its first factor, while the second factor, the exponential of a real quaternion, is the part of the pairing that is not an ordinary quaternion.

The construction needs the real quaternion part invertible; the pairing needs only $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$. The gap between the two is the difference between the factorisation, which the four factors provide on the complement of the null cone, and the construction, which needs the inverse of a part. The Hamilton pairing needs the vector part non-null, and the two domains are not nested: the complement of the null cone is their union together with the nonzero purely imaginary complex scalars, which are exactly the elements in neither.

Under the three conjugations the modulus and the angle of the pairing are unchanged by complex conjugation, which flips the scalar imaginary of the exponent and nothing else, while quaternion conjugation and Hermitian conjugation exchange the order of the two factors, and the canonical angle of the conjugate is the quaternion conjugate of the angle exactly when the two quaternion parts of the element commute. In the degenerate limits a non-scalar real quaternion gives a modulus alone, where the Hamilton pairing is the quaternion polar representation, and a complex scalar with nonzero real part gives the ordinary complex polar form of $\mathbb{C}$; the Hamilton pairing carries the quaternion polar form into the biquaternions, and the quaternion pairing carries the complex polar form.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar representation, four factors |
| $r$, $\exp(i\alpha)$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$ | scale, central phase, Hermitian positive boost, unit real quaternion rotor, with $\tilde u_{\mathrm r}\in\mathrm{Sp}(1)$ |
| $\Rho = r\exp(i\alpha) = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$ | the complex modulus of the four-factor representation, which is the Hamilton modulus |
| $\vec Q = Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part of $\tilde{Q}$ |
| $(\vec Q,\vec Q) = Q_x^2+Q_y^2+Q_z^2$ | the general plain bilinear square of the vector part |
| $\tilde q_r$, $\tilde q_i$ | the real and imaginary quaternion parts of $\tilde{Q}$ |
| $\vec\Xi$, $\Theta$ | Hamilton axis, parallel to $\vec Q$, and complex angle |
| $B = \sqrt{(\vec Q,\vec Q)}$ | the length of the vector part, the Hamilton axis being $\vec Q/B$ |
| $\tilde q$ | quaternion modulus, the real quaternion $r\tilde u_{\mathrm r}$ |
| $\tilde q = r\tilde u_{\mathrm r}$ | the polar representation of the ordinary quaternions, which the modulus $\tilde q$ is |
| $\tilde\Psi = \alpha+\theta_{\mathrm b}\vec u_{\mathrm b}'$ | quaternion angle, a real quaternion |
| $\theta_{\mathrm b} = \psi/2$, $\vec u_{\mathrm b}'$ | half the boost rapidity, and the rotor-rotated boost axis |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | quaternion, complex and Hermitian conjugation |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the four factors, the modulus $\Rho = \sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}$, the domain, and §*The Procedure in Practice* of that article for the procedure itself, the factors in the coordinates of $\tilde{Q}$ and the exponents with their positions.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the Hamilton grouping, its complex modulus and its non-central root of $-1$, the exponential of the element, the non-uniqueness of its parameters, and the reading of the same word at the roots of one.
- *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$* (`articles_maths/the-biquaternion-algebra-as-a-vector-space-over-c-and-r.md`), for the real, complex and quaternionic coordinate systems and the convention $Q_\mu = q_\mu+iq'_\mu$ used in the derivation above.
- *Biquaternion Elementary Functions* (`articles_maths/biquaternion-elementary-functions.md`), for the exponential and the logarithm of which the second factor of the pairing is built, and which carry the branch ambiguity of the construction.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), for the null cone on which all four representations fail.
- *Quaternion Polar Element Representation* (`articles_maths/quaternion-polar-element-representation.md`), for the polar representation $\tilde q = r\tilde u_{\mathrm r}$ of the ordinary quaternions, which is the first factor of the pairing, for its exponential form $\exp(\ln r)\exp(\mu\tfrac{\theta}{2})$, which the Hamilton representation generalises, and for the degenerate limit in which the two-factor form is read on the element itself.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the third pairing of the four factors, its Hermitian and anti-Hermitian exponent split, its full domain and its identification with the matrix polar decomposition.
- *Complex Polar Element Representation* (`articles_maths/complex-polar-element-representation.md`) and *Split-Complex Polar Element Representation* (`articles_maths/split-complex-polar-element-representation.md`), for the two-dimensional members of the series and the rule of the exponential $\exp(\nu\theta)$ that the factors of these pairings are built from.
