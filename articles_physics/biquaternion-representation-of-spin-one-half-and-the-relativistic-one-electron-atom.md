# __Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom__

## Introduction

**The article records one external source.** Alejandro Arias Jiménez, *Biquaternion representation of the spin one half and it's application on the relativistic one electron atom*, arXiv:2403.02344v1 [quant-ph], 28 February 2024, Department of Physics, Universidad de las Américas Puebla. It is a short student preprint with no peer review indicated, and its derivations are treated here as claims to be checked, not as results to be quoted.

**Its programme is stated in its abstract.** Represent the spin-$\tfrac12$ particle by complex quaternions, pass to $2\times2$ arrays "in order to obtain the Pauli matrices", determine with that representation the states, the rotation operators and the total-angular-momentum function, and use it to solve the relativistic hydrogen atom, arriving at a probability function. The closing outlook proposes the quaternion form as a computational saving over arrays and lists extensions to quantum-computing mathematics, particle physics, statistical mechanics, atomic physics and the two-electron atom.

**Two objects of the source are the reason it is recorded.** The first is an explicit exchange of the Pauli arrays for elements of the quaternion algebra. The second is a **quaternion-space form of the relativistic one-electron wave function**, which the corpus's article on the Dirac–Coulomb problem names as absent from the corpus. The first is defective in a way that can be stated exactly. The second is a transcription and not a derivation.

**The apparatus is the corpus's and is named, not restated.** The element, its units and its four conjugations are those of *Algebra and Element Conventions*; the products and the forms are those of *Product and Form Conventions*; the two norms, the Hermitian form and the Born weight are those of *Norm and Pairing Conventions* and of *Spin-1/2 Quantum Physics in Biquaternionic Form*; the spin operators and the pure states are those of *Angular Momentum and Spin in Biquaternionic Form*; the rotors are those of *Biquaternion Rotations and Lorentz Transformations*; the radial Dirac–Coulomb problem is that of *The Hydrogen Atom in Biquaternionic Form — The Relativistic Case*; and the complex-linear map from the algebra to the two-by-two arrays is $\mathsf{M}_2$ of *Matrix Representations Conventions*, §*The $2\times2$ Pauli Representation*. No symbol of those files is defined here.

**Two identifiers of the source are kept.** The coefficient labels $q_1 := q_x$ and $q_3 := q_z$, and the source's square of an element, $|q|^2 = \sum_\mu\lvert q_\mu\rvert^2$. That square is the corpus's Hermitian norm $H$ and not the algebra norm $\langle\cdot\rangle_{\natural}$; the difference is used below and is not a notational one.

**The body of the article prints no array.** The assignment the source quotes is described by its entries and by what it does to the two components, because in that section the array is the object of the sentence. The one place where the older formulation is written out is §*The Legacy Pauli Gamma Formulation*, which this article keeps as the record.

**The findings, stated before the detail.**

- The assignment the source proposes, its equation (8), gives the identity and the three arrays the source calls the Pauli arrays on the four elements it lists, and it does nothing else: it does not respect the central scalar, it does not preserve products and it loses elements, so it is not the representation it is claimed to be. The classical assignment it invokes is a different one, and that one is multiplicative on the real quaternions and not on the complex ones.
- The spin operators and the two states are correct: the angular-momentum algebra and the six eigenvalue equations hold. Read in the corpus's algebra, the two states are of different kinds. The up state divided by $\sqrt2$ is its own square and is a pure state along $\vec e_x$; the down state divided by $\sqrt2$ squares to zero. The source's square is $1$ on both, and the algebra norm vanishes on both.
- The rotation operators are unit-norm elements and the action $D^{*}S_kD$ is correct on the three axes. The single printed formula for the rotated components does not say which pair belongs to which axis; recomputed, the plus sign belongs to $(j,k)=(z,y)$ about $x$, $(x,z)$ about $y$ and $(y,x)$ about $z$, the reverse pairing carries the opposite sign, and the component along the axis is invariant.
- The two states are orthonormal in the Hermitian form and not in the product, where $q_\pm^{*}q_\pm = e_t - i\vec e_x$ is a zero divisor rather than $e_t$. The source's probability example is that Hermitian pairing, used before it is named.
- The relativistic one-electron atom is the standard radial Dirac–Coulomb problem re-expressed. The system, the wave function and the density are the standard ones. The spectrum is printed **without the square on the ratio**; with the ratio squared it is the Sommerfeld–Dirac formula and it reproduces the exact ground-state value, which the printed form does not.
- The source's section on the eight-parameter algebra puts one parameter in two coefficients and another in none, so the correspondence printed there cannot be one-to-one.

## The Proposed $2\times2$ Transformation

### The Assignment and Its Four Values

**The source assigns a $2\times2$ complex array to an element**, its equation (8), on $q = q_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$: the first row is $(q_t + iq_1,\ q_y + iq_3)$ and the second is $(\overline{q_y} - i\overline{q_3},\ q_t + i\overline{q_1})$, with $q_1 := q_x$ and $q_3 := q_z$ the source's labels. The source's star on a coefficient is the complex conjugation of that scalar and is written with an overbar here, so $(iq_3)^{*} = -i\overline{q_3}$ and $(iq_1)^{*} = -i\overline{q_1}$, since $i^{*} = -i$. The second row is printed in the source in unsimplified form, and the entries above are the simplified ones.

**The four values the source reads off are exact.** Recomputed on those four elements, they reproduce the four arrays to zero error. They are stated by what the assignment does to the two components of the pair it acts on, because the array is the object here and its entries are the four numbers just written.

| $q$ | what $A(q)$ does to the two components | the source's label for the array |
|---|---|---|
| $e_t$ | $(a,b)\longmapsto(a,b)$ | none |
| $-i\vec e_x$ | $(a,b)\longmapsto(a,-b)$ | $z$ |
| $-i\vec e_y$ | $(a,b)\longmapsto(-ib,ia)$ | $y$ |
| $-i\vec e_z$ | $(a,b)\longmapsto(b,a)$ | $x$ |

**The table fixes the source's own labelling.** Its $x$-array is the value at $-i\vec e_z$, its $y$-array the value at $-i\vec e_y$ and its $z$-array the value at $-i\vec e_x$: $x$ and $z$ are exchanged and $y$ is fixed, so the source's $x$-component belongs to $\vec e_z$ and its $z$-component to $\vec e_x$. (The source's own list of the four operators misprints the second entry; the table above is what its evaluations give.)

**The rest of the source's physics is built on this assignment.** It is therefore worth asking of it the three properties an assignment to arrays must have: that it respect the complex scalars, that it preserve products, and that it lose nothing.

### The Assignment Does Not Respect the Complex Scalars

**Statement.** $A(iq)$ is not $iA(q)$ in general, so the assignment is not a map of the complex algebra.

**Witness.** At $q = \vec e_y$ the entry $(2,1)$ is $-i$ in $A(i\vec e_y)$ and $+i$ in $iA(\vec e_y)$, so $A(i\vec e_y) \neq A(i)A(\vec e_y)$: the failure is at the central scalar itself. The central imaginary is a scalar of $\mathbb{B}$, and an assignment that reverses it at one element cannot be multiplicative.

### The Assignment Does Not Preserve Products

**Statement.** $A(qp)$ is not $A(q)A(p)$ in general.

**Proof by counterexample.** $A(\vec e_x)$ is $i$ times the identity, $A(\vec e_y)$ interchanges the two components, and $\vec e_x\vec e_y = \vec e_z$. Computed directly, $A(\vec e_x)A(\vec e_y)$ and $A(\vec e_z)$ differ in the entry $(2,1)$, which is $+i$ in the product and $-i$ in the image. On a hundred random pairs of complex elements the largest entrywise discrepancy between $A(qp)$ and $A(q)A(p)$ is of the order of $10^1$, the size of the entries themselves; on a hundred random pairs of real elements it is of the same order. The failure is therefore not an artefact of the complex coefficients, and no algebraic statement may be carried through the assignment.

### The Assignment Loses Elements

**Statement.** The kernel of $A$ has real dimension three.

**Proof.** The vanishing of $A(q)$ is the vanishing of the two entries $q_t + iq_1$ and $q_y + iq_3$ together with that of the diagonal entry $q_t + i\overline{q_1}$. The first two give $q_t = -iq_1$ and $q_y = -iq_3$; the third then reads $i(\overline{q_x} - q_x) = 0$, that is, $q_x$ real. The solutions are $q_x = x$ real, $q_t = -ix$, and $q_z$ an arbitrary complex number with $q_y = -iq_3$, which is a real three-dimensional space,

$$
\boxed{\;\ker A = \mathrm{span}_\mathbb{R}\left\{-ie_t + \vec e_x,\ -i\vec e_y + \vec e_z,\ \vec e_y + i\vec e_z\right\}\;}.
$$

**The kernel contains the source's down state.** The last generator spans, over $\mathbb{C}$, the whole complex line through $-\vec e_y - i\vec e_z$; the source's state $q_- = (-\vec e_y - i\vec e_z)/\sqrt2$ is a complex multiple of it, and $A(q_-) = 0$ was confirmed on a hundred random complex multiples. So the assignment does not merely fail to preserve products: it annihilates one of the two states the source uses, and with it every other element of that line. What the source's table exhibits is an assignment that agrees with a representation on four chosen elements, not a representation.

### The Classical Assignment, and the Corpus's Map

**The assignment the source attributes to Kravchenko and Shapiro is a different one.** That assignment carries $q = z + w\vec e_y$ to the array whose first row is $(z,w)$ and whose second row is $(-\bar w,\bar z)$, with $z = q_t + iq_1$ and $w = q_y + iq_3$, the complex structure being left multiplication by $\vec e_x$. The corpus carries it in *The $M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation*, with another choice of the splitting, as the array form of the real-quaternion subspace.

**Three things are true of it, and each was checked.**

- It is multiplicative on the real quaternions: a hundred random pairs give a largest discrepancy of $10^{-15}$, machine precision.
- It is **not** multiplicative on the complex ones: a hundred random pairs give a discrepancy of the order of $10^1$. The reason is structural and not accidental: the entries $-\bar w$ and $\bar z$ use complex conjugation, which is antilinear, and an antilinear operation cannot commute with the central $i$ of a complex-linear product. The classical form is an array over $\mathbb{C}$ of the real quaternions, not of $\mathbb{B}$.
- The source's assignment is not this one. In the $z,w$ notation the source's lower-left entry is $+\bar w$ where the classical form has $-\bar w$, and its lower-right entry is $q_t + i\overline{q_1}$ where the classical form has $\bar z$. The source displays the classical form in the compact notation and then expands it into a different array.

**The corpus's map is the complex-linear one, and it is multiplicative on $\mathbb{B}$ to machine precision.** It is $\mathsf{M}_2$ of *Matrix Representations Conventions*, §*The $2\times2$ Pauli Representation*, where its four values on the units are fixed; it is named here only where a comparison needs it, and nothing below is derived through it.

**The two assignments agree on the four elements up to a relabelling of the three spatial units.** The array the source assigns to $-i\vec e_x$ is the corpus's image of $i\vec e_z$, the array it assigns to $-i\vec e_y$ is the image of $i\vec e_y$, and the array it assigns to $-i\vec e_z$ is the image of $i\vec e_x$. So $x$ and $z$ are exchanged and $y$ is fixed, which is the relabelling the table of the four values already shows.

**The substitution of the hydrogen section carries the same relabelling.** The source writes $\alpha_r = -i\vec e_y$ and $\beta = -i\vec e_x$, consistent with its own table; the corpus's units that give the same two arrays are $i\vec e_y$ and $i\vec e_z$. A reader who applies the corpus's map to the source's two elements therefore lands on the negatives of the two arrays the source intends, with one axis exchanged. The mismatch is a convention mismatch and not an error of the source, which is self-consistent with its own table throughout.

## The Spin Operators and the States

### The Operators

**The source's spin operators are its equations (9)–(11)**,

$$
S_x = \frac{\hbar}{2}(-i\vec e_z), \qquad S_y = \frac{\hbar}{2}(-i\vec e_y), \qquad S_z = \frac{\hbar}{2}(-i\vec e_x).
$$

**Their commutation relations were recomputed and hold exactly.** $[S_x,S_y] = i\hbar S_z$, $[S_y,S_z] = i\hbar S_x$ and $[S_z,S_x] = i\hbar S_y$, with no residual term. So the three elements satisfy the angular-momentum algebra of spin $\tfrac12$ in the algebra's own product, and that part of the source needs no correction.

**The corpus's operators are $\tilde S_k = \tfrac{\hbar}{2}i\vec e_k$, and the source's are the corpus's in another labelling**: $S_x = -\tilde S_3$, $S_y = -\tilde S_2$ and $S_z = -\tilde S_1$. The two triples are equal as algebras and different as identifications of the three directions, and the exchange is the one the table of the four values shows. Neither is wrong; what the page does not say is which of the two it uses.

### The States

**The source's states are its equations (12) and (13)**,

$$
q_+ = \frac{1}{\sqrt2}\left(e_t - i\vec e_x\right), \qquad q_- = \frac{1}{\sqrt2}\left(-\vec e_y - i\vec e_z\right).
$$

**All six eigenvalue equations were recomputed and hold.**

| | $q_+$ | $q_-$ |
|---|---|---|
| $S_x$ | $+\tfrac{\hbar}{2}q_-$ | $+\tfrac{\hbar}{2}q_+$ |
| $S_y$ | $+i\tfrac{\hbar}{2}q_-$ | $-i\tfrac{\hbar}{2}q_+$ |
| $S_z$ | $+\tfrac{\hbar}{2}q_+$ | $-\tfrac{\hbar}{2}q_-$ |

**The entry worth pausing on is the one for $S_x$ on $q_-$.** The source displays that product and reads off $q_+$ with the positive sign, and that is what direct multiplication gives; the sign is right and the flipped sign would be wrong. The four orthogonality and normalisation statements that follow in the source were also recomputed: $q_+^{*}q_- = 0$, and the source's square is $1$ on both states. Its duals are $q_\pm^{*}$: $q_+^{*} = q_+$, since $q_+$ is Hermitian, while $q_-^{*} = \tfrac{1}{\sqrt2}\left(\vec e_y - i\vec e_z\right)$, which is neither $q_-$ nor $-q_-$, and which fails as a dual in the product, where $q_+^{*}q_+ = q_-^{*}q_- = e_t - i\vec e_x$ is the zero divisor computed below.

### The Two States as Elements

**The source's square is the corpus's Hermitian norm.** $|q|^2 = \sum_\mu\lvert q_\mu\rvert^2$ is the diagonal of the Hermitian form of *Norm and Pairing Conventions*, $H$, and it is $1$ on both states. The algebra norm is $0$ on both:

$$
\boxed{\;\langle q_+\rangle_{\natural} = 0, \qquad \langle q_-\rangle_{\natural} = 0\;}.
$$

**Both are zero divisors**, and the source itself expects this where it says that in the complex quaternions "there are certain objects called zero divisors" and that the inverse is lost. The consequence for the interpretation of the two states is sharper than the source draws. Dividing each by $\sqrt2$ gives an element of the algebra, and the two elements so obtained are of different kinds.

| element | $H$ | $\langle\cdot\rangle_{\natural}$ | divided by $\sqrt2$ | under squaring |
|---|---|---|---|---|
| $q_+$ | $1$ | $0$ | $\tfrac12\left(e_t - i\vec e_x\right)$ | its own square, Hermitian, scalar part $\tfrac12$ |
| $q_-$ | $1$ | $0$ | $\tfrac12\left(-\vec e_y - i\vec e_z\right)$ | zero |

**The first of the two is a pure state and the second is not.** $\tfrac12(e_t - i\vec e_x)$ is Hermitian and equal to its own square, so by *Spin-1/2 Quantum Physics in Biquaternionic Form* it is a pure state, and by the operators above it is the state of eigenvalue $-\tfrac{\hbar}{2}$ of the corpus's $\tilde S_x$. The element $\tfrac12(-\vec e_y - i\vec e_z)$ squares to zero, and the two products between them are $\tfrac12(-\vec e_y - i\vec e_z)\cdot\tfrac12(e_t - i\vec e_x) = \tfrac12(-\vec e_y - i\vec e_z)$ and $\tfrac12(e_t - i\vec e_x)\cdot\tfrac12(-\vec e_y - i\vec e_z) = 0$. The complementary pure state along $\vec e_x$ is $\tfrac12(e_t + i\vec e_x)$.

**So the source's up state is a pure state up to the factor $\sqrt2$, and its down state is not an element of that kind at all.** The source's square cannot see the difference, since it is $1$ on both, and the algebra norm cannot see it either, since it is $0$ on both; the difference is visible only in the square. The source calls the first of the two its up state because its own $S_z$ is $-\tilde S_x$, so the state of eigenvalue $-\tfrac{\hbar}{2}$ of $\tilde S_x$ is the state of eigenvalue $+\tfrac{\hbar}{2}$ of its own $S_z$.

## The Rotation Operators

**The source writes $D^\dagger$ for the conjugate, and the corpus writes $D^{*}$ for the Hermitian conjugate of an element**, the dagger being reserved for operators. The source's rotation operator and its conjugate are

$$
D(n,\theta) = e_t\cos\frac{\theta}{2} - i\left(q_p\cdot n\right)\sin\frac{\theta}{2},
\qquad
D^{*}(n,\theta) = e_t\cos\frac{\theta}{2} + i\left(q_p\cdot n\right)\sin\frac{\theta}{2},
$$

with $q_p$ the source's spin vector, whose component along the axis $n$ is $q_p\cdot n=-i(\vec e\cdot n)$ — the unit-spin vector times $-i$, not $\vec e\cdot n$ itself. Since $-i(-i)=i^2=-1$, the general formula reduces to

$$
D(n,\theta)=e_t\cos\frac{\theta}{2}-(\vec e\cdot n)\sin\frac{\theta}{2},
\qquad
D^{*}(n,\theta)=e_t\cos\frac{\theta}{2}+(\vec e\cdot n)\sin\frac{\theta}{2}.
$$

**For the three axes the source's (14)–(16) read**

$$
\begin{aligned}
D(x,\theta) &= e_t\cos\frac{\theta}{2}-\vec e_z\sin\frac{\theta}{2},\\
D(y,\theta) &= e_t\cos\frac{\theta}{2}-\vec e_y\sin\frac{\theta}{2},\\
D(z,\theta) &= e_t\cos\frac{\theta}{2}-\vec e_x\sin\frac{\theta}{2}.
\end{aligned}
$$

**They are unit-norm elements**: $D^{*}D = e_t$ was recomputed for each axis and holds exactly, so the corpus's rotor theory applies to them unchanged.

**For the source's $x$-axis, whose unit is $\vec e_z$, the action is**

$$
\boxed{\;
\begin{aligned}
D^{*} S_xD &= S_x,\\
D^{*} S_yD &= \cos\theta\,S_y-\sin\theta\,S_z,\\
D^{*} S_zD &= \cos\theta\,S_z+\sin\theta\,S_y.
\end{aligned}\;}
$$

**The component along the axis is invariant and the two transverse components rotate into one another** in the standard sense; the two remaining axes give the two remaining rotations of the same pattern. The source collects all three into the single formula (17),

$$
D^{*}(n_a,\theta)S_jD(n_a,\theta)=\frac{\hbar}{2}\left(q_j\cos\theta+q_k\sin\theta\right),
$$

where $q_j=-i\vec e_j$. The source does not state which pair belongs to which axis, so as printed the formula is under-determined: the plus sign belongs to $(j,k)=(z,y)$ about $x$, $(x,z)$ about $y$ and $(y,x)$ about $z$, the reverse pairing carries the opposite sign, and the component along the axis is not covered by the pattern at all.

## The Raising and Lowering Operators

**The source prints $S_+ = \tfrac12(S_x + iS_y)$ and $S_- = \tfrac12(S_x - iS_y)$**; with its own $S_x,S_y$ from (9)–(10) the factor $\tfrac12$ is spurious, and the values it prints in (18)–(19) are those of $S_x\pm iS_y$ with $\hbar=1$. Indeed, using $i(-i)=+1$,

$$
S_+ = S_x+iS_y = \frac{\hbar}{2}\left(-i\vec e_z+\vec e_y\right)=\frac{\hbar}{2}\left(\vec e_y-i\vec e_z\right),
$$

$$
S_- = S_x-iS_y = \frac{\hbar}{2}\left(-i\vec e_z-\vec e_y\right)=\frac{\hbar}{2}\left(-\vec e_y-i\vec e_z\right),
$$

so in units $\hbar=1$ the two elements are

$$
S_+=\tfrac12\left(\vec e_y-i\vec e_z\right),\qquad S_-=\tfrac12\left(-\vec e_y-i\vec e_z\right),
$$

which were recomputed. **The raising and lowering behaviour is correct**: $S_+q_- = q_+$, $S_+q_+ = 0$, $S_-q_- = 0$ and $S_-q_+ = q_-$, all verified.

**Two remarks belong to the notation.** The first is that the source's statement that the two operators are obtained from one another by conjugation is correct: the identity $S_- = S_+^{*}$ holds, and the negative form $S_- = -S_+^{*}$ fails. The second is an overload: the symbols $q_+$ and $q_-$ denote the two **states** in the source's (12)–(13) and the two **operators** in its (18)–(19), and these are different elements — the states are $\sqrt2$ times a pure state and a square-zero element, the operators are pure vectors with no scalar part. The coincidence is not accidental, since the state $q_-$ is $\sqrt2$ times the operator $S_-$, but a reader who carries a symbol across the two uses will be carrying the wrong element.

## The Angular Element

**The source's equation (20) encodes the angular factor as one element.** Its two coefficients are defined beside that equation as the radicals $C_{l1}=\sqrt{l\pm m_j+\tfrac12}$ and $C_{l2}=\sqrt{l\mp m_j+\tfrac12}$, and its equation (25) calls the $C_n$ the Clebsch–Gordan coefficients of the case; the prefactor is $1/\sqrt2$ where the standard harmonic carries $1/\sqrt{2l+1}$, so on normalised harmonics the source's angular element has squared norm $(2l+1)/2$ rather than $1$. With $C_1$ and $C_2$ left as the source's two numbers, the encoding is the single element

$$
\frac{1}{\sqrt2}\left(C_1Y_l^{s_{\mathrm{tot},z}-\frac12}e_t - iC_1Y_l^{s_{\mathrm{tot},z}-\frac12}\vec e_x - C_2Y_l^{s_{\mathrm{tot},z}+\frac12}\vec e_y - iC_2Y_l^{s_{\mathrm{tot},z}+\frac12}\vec e_z\right),
$$

**that is, on any values of the two harmonics,**

$$
C_1Y_l^{s_{\mathrm{tot},z}-\frac12}\,q_+ + C_2Y_l^{s_{\mathrm{tot},z}+\frac12}\,q_- ,
$$

the expansion of the angular element in the source's own two states, with the two components of the pair as its coefficients. So the encoding is faithful and its convention is the same one the states of the previous sections are written in.

**The two sides of the page are one element and its expansion.** The object on the left is an element of $\mathbb{B}$ and the object on the right is the same element written as two multiples of the two fixed elements; in the corpus the two sides are the same object, so nothing is identified that was not already one object: the ordered pair is a writing of an element, and not a second space.

**The probability example that closes the section is the measurement of the down state on the $l = 2$ harmonic**, $y = C_1Y_2^1q_+ + C_2Y_2^2q_-$ with $C_1 = \sqrt{2/5}$ and $C_2 = \sqrt{1/5}$, and the source's result is $\tfrac15\lvert Y_2^2\rvert^2$. **The two states are orthonormal in the Hermitian form**: $\langle q_p,q_q\rangle_{*} = \delta_{pq}$ was verified on the four pairs. The full products are not the identity element, however: $q_+^{*}q_+ = q_-^{*}q_- = e_t - i\vec e_x$ is a zero divisor, so the source's dual is a dual only at the level of the scalar part. **That scalar part is the Hermitian pairing of *Norm and Pairing Conventions*, and the source's example is that pairing used before it is named**: the value is $\mathrm{Sc}\left(q_-^{*}y\right) = C_2Y_2^2$, checked on a hundred random harmonic amplitudes, whence the squared modulus $\tfrac15\lvert Y_2^2\rvert^2$. The source's "orthogonality and normalisation", in other words, are true statements about the Hermitian form and not about the product, which is the same distinction the corpus's Born rule draws.

## The Relativistic One-Electron Atom

### The Source's Route

**The source's section 1 solves the problem by the standard matrix route and states the answer; its section 6 re-solves it in the quaternion representation.** In the radial equation the two arrays of the matrix route are replaced by the two elements $\alpha_r = -i\vec e_y$ and $\beta = -i\vec e_x$, and the radial function is written as one element,

$$
R(r) = \frac{1}{r}\left(F(r)\left(e_t - i\vec e_x\right) + G(r)\left(-\vec e_y - i\vec e_z\right)\right),
$$

whose two fixed elements are, up to the factor $\sqrt2$, the two states of the previous sections: the pair $(F,G)$ is encoded exactly as the two parts of the angular element were, $R = \tfrac{\sqrt2}{r}(Fq_+ + Gq_-)$. So the radial reduction is a reduction to the two parts $F$ and $G$, and the object encoded is one element of $\mathbb{B}$, not a four-part object. Expanding the equation in the two fixed elements separates it into the two coupled first-order equations

$$
\begin{aligned}
-c\hbar\frac{dG}{dr} - \frac{c\hbar k}{r}G + mc^2F - \frac{z\hbar ca_0}{r}F &= EF,\\
c\hbar\frac{dF}{dr} - \frac{c\hbar k}{r}F - mc^2G - \frac{z\hbar ca_0}{r}G &= EG.
\end{aligned}
$$

**which is the same pair the source's matrix route prints**, $k$ the Dirac–Coulomb quantum number and $za_0$ the Coulomb coupling in units of $\hbar c$. The two displays were compared entrywise and are the same system; the system itself is the standard radial Dirac–Coulomb one, its $1/r$ terms, mass terms and coupling being those of the textbook problem in the source's conventions.

**Its closed-form solution is given by the source as Laguerre polynomials** in $\rho = Cr$ with $C = \sqrt{m^2c^4 - E^2}/(\hbar c)$ and $s = \sqrt{k^2 - z^2a_0^2}$, and its wave function is the pair of angular elements multiplied by $F(\rho)$ and $G(\rho)$, written first as an ordered pair and then as the single element of its equations (25) and (26), with the dual in (27). The scalar part of $\tilde{Ξ}^{\mathrm{spn}*}\tilde{Ξ}^{\mathrm{spn}}$, its (28), is $1/r^2$ times the sum of the squared moduli of the two angular parts with $F^2$ and $G^2$ attached. Its (29) integrates that density over the angular variables, and the density is

$$
\begin{aligned}
\rho(\theta,\theta^{\mathrm{azm}})=\frac{1}{r^2}\Bigl(&C_1^2\left\lvert Y_k^{s_{\mathrm{tot},z}-\frac12}\right\rvert^2F(r)^2
+C_2^2\left\lvert Y_k^{s_{\mathrm{tot},z}+\frac12}\right\rvert^2F(r)^2\\
&+C_3^2\left\lvert Y_{-k}^{s_{\mathrm{tot},z}-\frac12}\right\rvert^2G(r)^2
+C_4^2\left\lvert Y_{-k}^{s_{\mathrm{tot},z}+\frac12}\right\rvert^2G(r)^2\Bigr),
\end{aligned}
$$

**The volume probability is $\int_0^\infty r^2\,dr\int_{S^2}\rho\,d\Omega$**, the $r^2$ of the measure cancelling the $1/r^2$, and the angular factor alone is $\int_{S^2}\rho\,d\Omega$. The source prints the limits $-a$ to $a$ against $d\Omega$, and those limits are radial while the measure is angular, so the printed integral is not a probability as it stands. Apart from this measure slip the density is the standard one for the two-part radial solution. (The source calls this probability $\rho$, the same letter it uses for the radial variable $\rho = Cr$ in the closed forms; the collision is the source's, and the two are kept apart here by context.)

**The structure of (28) and (29) was checked against (25) and (26)** and is consistent with them, with one slip of the source's: the $C_3$ term of (28) is printed without the $G^2$ that its counterpart in (29) carries and that the expansion of (25) requires, and the display above restores it. The source writes the squares of the harmonics as $Y^2$ and defines them as $Y^{*}Y$, which is the $\lvert Y\rvert^2$ used here.

**The closed forms of $F(\rho)$ and $G(\rho)$ were not independently recomputed**: the radicals and the Laguerre arguments do not survive extraction from the source's file in a form that can be transcribed without guesswork, and a half-guessed formula is worse than a recorded one. They are recorded as printed and marked unverified.

### The Spectrum as Printed

**The source's energies are printed as**

$$
E_{\mathrm{printed}} = mc^2\left(1 + \frac{za_0}{n - |k| + \sqrt{k^2 - z^2a_0^2}}\right)^{-1/2},
$$

**in which the square on the ratio is absent.** The standard Sommerfeld–Dirac formula squares the whole ratio,

$$
E = mc^2\left(1 + \left(\frac{za_0}{n - |k| + \sqrt{k^2 - z^2a_0^2}}\right)^2\right)^{-1/2}
= mc^2\left(1 + \frac{z^2a_0^2}{\left(n - |k| + \sqrt{k^2 - z^2a_0^2}\right)^2}\right)^{-1/2},
$$

**and the difference is not cosmetic.** At $n = 1$, $|k| = 1$ the exact Dirac–Coulomb ground state is $E = mc^2\sqrt{1 - z^2a_0^2}$, and the two forms compare as follows:

| $za_0$ | printed | with the ratio squared | exact $\sqrt{1-z^2a_0^2}$ |
|---|---|---|---|
| $0.1$ | $0.95324433$ | $0.99498744$ | $0.99498744$ |
| $0.2$ | $0.91130629$ | $0.97979590$ | $0.97979590$ |
| $0.5$ | $0.79622522$ | $0.86602540$ | $0.86602540$ |

**The restored form agrees with the exact ground state to every digit displayed**, at each coupling, and the printed form does not. The missing operation is the square on the ratio; the denominator's square under the root, $k^2 - z^2a_0^2$, is already correct in the source, so the slip is in the ratio and not an extraction artefact. Nothing else in the source's spectrum is at issue.

### What This Is and What It Is Not

**The source's quaternion wave function is the standard radial Dirac–Coulomb solution, re-encoded**: the same system, the same Laguerre functions, the same angular harmonics, written as one element instead of an ordered pair. The article on the Dirac–Coulomb problem in this corpus records that the exact bound-state solution is the standard radial Dirac–Coulomb one, that what the corpus does not supply is the radial Dirac–Coulomb solution **inside the algebra** — the derivation, not the transcription — and that the transcription is what this article's source supplies.

**The source's result is the transcription and not the derivation**: a reproduction, in the algebra's notation, of the standard solution. It is a transcription, and the source itself says so, obtaining the quaternion form from the matrix solution of its section 1 and then rewriting it. It is therefore recorded here as the transcription that fills the corpus's notation gap at the level of notation, and **not** as the algebra-level derivation that article says is absent. The difference is not pedantic: a derivation inside the algebra would produce the radial system and its solution from the algebra's own Dirac equation, with the mass term and the coupling as the corpus's equation carries them; a transcription produces them from the matrix problem and then relabels. What the source demonstrates is that the relabelling can be carried out and that the results agree; what it does not demonstrate is that the algebra produces them.

**The second thing the source supplies in this neighbourhood is the pair of substitutions $\alpha_r = -i\vec e_y$, $\beta = -i\vec e_x$** inside the quaternion radial equation, that is, an explicit statement of which elements carry the Dirac operator in a Coulomb computation. Because the substitution is made through the source's own table and not through a multiplicative map, its result is safe only as long as the source's labelling is kept; the corpus's pair for the same two arrays is $i\vec e_y$ and $i\vec e_z$, as noted above. This is a small point of bookkeeping that the source leaves open and a reader must close.

## The Two Closing Sections of the Source

**Two short sections close the source's physics.** The first represents the algebra spanned by the identity and the three arrays the source calls the Pauli arrays. Its eight parameters $q_t,\dots,q_7$ are assigned to the eight basis elements, and the assignment is then rewritten in the quaternion space as

$$
q = \left(q_t - iq_7\right)e_t - \left(iq_1 + q_4\right)\vec e_x - \left(iq_2 + q_5\right)\vec e_y - \left(iq_3 + q_7\right)\vec e_z ,
$$

its equation (30). **As printed, the parameter $q_7$ appears in two coefficients and the parameter $q_6$ in none**, so the displayed correspondence cannot be a bijection between the eight parameters and the four complex coefficients. Recorded as printed and not repaired here. The same section represents "the Hodge operator" by the element $-ie_t$, its equation (31), a statement whose symbol $\varepsilon$ is not defined anywhere in the source and whose content cannot be recovered from the page; it is recorded as printed and nothing is built on it.

**The second short section writes four $4\times4$ arrays in element form and attributes the representation to Silvis (2010)**; that attribution is the only place in this corpus where Silvis is named. Two things are visible on the page without any reconstruction. The first array, with $1,1,-1,-1$ on its diagonal, is sent to the two diagonal places both carrying $e_t$, which is the identity: the second of the two is printed with $e_t$ where the minus of the $4\times4$ array should stand, so that as printed the image of that array is the identity and not the pair $(e_t,-e_t)$. The three places off the diagonal are printed with $-i\vec e_x$ above and $i\vec e_x$ below, and the same with $\vec e_z$ and with $\vec e_y$.

**The corpus's side of the same correspondence is in *Matrix Representations Conventions*, §*The Legacy Pauli Gamma Formulation***, in the mostly-minus convention: a timelike generator off the diagonal with $e_t$ in both places, and three spacelike generators off the diagonal with $i\vec e_k$ above and $-i\vec e_k$ below. The two sets differ in two ways and agree in the algebra: the source's first array is diagonal where the corpus's timelike generator is off-diagonal, and the source's three spacelike places are the negatives of the corpus's, a sign that flips all three odd elements at once and therefore leaves every product unchanged. Which elements carry which axes is again the source's own table.

## What Is Verified and What Is Not

- The four values of the source's table, exactly.
- The failure of the assignment on the central scalar, and its failure of multiplicativity on complex and on real elements, with the explicit counterexample $\vec e_x, \vec e_y$.
- The kernel of the assignment, its three real generators, and the annihilation of the source's down state and of its complex line.
- The multiplicativity of the classical assignment on the real quaternions and its failure on the complex ones; the multiplicativity of the corpus's map on the complex ones.
- The commutation relations of the three spin operators, exactly.
- The six eigenvalue equations, including the sign of $S_xq_-$.
- Orthogonality and normalisation of the two states in both norms, the two conjugates $q_\pm^{*}$, the square of $\tfrac12(e_t - i\vec e_x)$, the vanishing square of $\tfrac12(-\vec e_y - i\vec e_z)$, the two products between them, and the Hermiticity of the first.
- The two ladder operators, their action on the two states, and the conjugation $S_- = S_+^{*}$.
- Unitarity of the three rotation operators and their action on the three spin operators.
- The identity of the source's equation (20) with the expansion in its own two states, and the squared norm $(2l+1)/2$ of the source's angular element at three values of $l$.
- The Hermitian pairing $\langle q_p,q_q\rangle_{*} = \delta_{pq}$, the zero-divisor values of the full products, and the source's $l = 2$ probability example against a hundred random harmonic amplitudes.
- The identity of the two printed radial systems, and the consistency of (28) and (29) with (25) and (26) apart from the missing $G^2$ of the $C_3$ term of (28) and the angular measure corrected to $S^2$.
- The spectrum with the ratio squared against the exact ground-state value, at three couplings.

**The following are recorded from the source and were not verified**: the closed forms of $F(\rho)$ and $G(\rho)$ and their Laguerre arguments; the two transformations the source uses to pass between its elements and the ordered pairs, whose displayed forms do not extract cleanly; the intermediate reduction from the radial equation to the two coupled equations, whose printed terms carry the $1/r$ of the definition of $R$ and the $c$ of the derivative in a bookkeeping that does not close on the page; the Hodge-operator statement (31); and the four $4\times4$ arrays of the last section, which are compared to the corpus's dictionary by their labels only.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}^{\mathrm{spn}}=a\tilde{Ξ}^{\mathrm{spn}}$ and $R_b\tilde{Ξ}^{\mathrm{spn}}=\tilde{Ξ}^{\mathrm{spn}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

**The two Dirac equations.** The corpus carries two forms of one dynamics, and the difference between them is where the second chirality slot sits. In units $\hbar=c=1$, with the biquaternionic gradient $\tilde\nabla=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$ and its conjugate $\tilde\nabla^{\natural}$, the **one-sided** form is the chiral pair

$$
\tilde\nabla\tilde{Ξ}^{\mathrm{spn}}_R=m\tilde{Ξ}^{\mathrm{spn}}_L,\qquad
\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{spn}}_L=m\tilde{Ξ}^{\mathrm{spn}}_R,
$$

two fields, both equations acting from the left, the chirality carried by the two fields and exchanged by $\natural$. The **two-sided** form writes a single field and puts the second slot on the right of the algebra element,

$$
\left(i\frac{\partial}{\partial t'}+D_3\right)F-mi\,\overline{F}\,\vec e_z=0,
\qquad
D_3=\sum_k\vec e_k\frac{\partial}{\partial Q_k},
$$

with the derivative acting from the left, the bar the antilinear entry, and $\vec e_z$ multiplying from the right after the conjugation. The two are one operator read from two sides: since $i\partial/\partial t'=-\partial/\partial Q_t$ in these units, the free part is $-\tilde\nabla^{\natural}$, and the equation reads

$$
\tilde\nabla^{\natural}F=m\left(-i\overline{F}\vec e_z\right),
$$

which is the second member of the pair with its left field read as $-i\overline{F}\vec e_z$: a conjugation and a fixed direction, nothing else. That is what the right multiplier carries — the second chirality slot, which the one-sided form holds in a second field, the two-sided form holds in the side of the action. The dictionary is recorded in *The Dirac Equation in Biquaternionic Form*. The chirality cell is $\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

**The source's assignment is not a representation.** Its equation (8) gives the identity and the three arrays the source calls the Pauli arrays on four elements, and it fails on everything else: it does not respect the central scalar, it does not preserve products, and its kernel is three real dimensions wide and contains the source's own down state. The classical assignment it invokes is a different one, and that one is multiplicative on the real quaternions and not on the complex ones. The corpus's map is the complex-linear one, and it is multiplicative on the algebra.

**Everything the source builds on the states is correct and can be read in the corpus's algebra.** The three spin operators satisfy the angular-momentum algebra, the six eigenvalue equations hold, the rotation operators are unit-norm elements that act correctly, and the ladder operators raise and lower. The corpus's reading differs from the source's in two places. The labelling of the three directions is the corpus's with $x$ and $z$ exchanged and a sign. And the two states are of different kinds: the up state divided by $\sqrt2$ is a pure state along $\vec e_x$, the down state divided by $\sqrt2$ squares to zero.

**The two states are orthonormal in the Hermitian form and not in the product.** The source's square is that form's norm and is $1$ on both; the algebra norm is $0$ on both; the product of either with its own conjugate is the zero divisor $e_t - i\vec e_x$. The source's probability example is the Hermitian pairing, used before it is named.

**The hydrogen atom is the standard radial Dirac–Coulomb problem re-expressed.** The system, the angular element, the density and the closed forms are the standard ones, and the source obtains them from its matrix solution and then relabels them. That makes the result the transcription of the corpus's notation gap and not the closure of its mathematical gap, and it is recorded as such. The spectrum carries one error: the square on the ratio is missing, and with it restored the formula is the Sommerfeld–Dirac one and reproduces the exact ground-state value.

**The older formulation appears once, in §*The Legacy Pauli Gamma Formulation*.** The body of the article writes no array, no cell and no Pauli or gamma symbol: the assignment of the source is described by its entries and by what it does to the two components, and every other statement of the body is a statement about elements of the algebra and about their products.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra of the corpus, the algebra of every element of this article |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | The units, in the naming of *Algebra and Element Conventions* |
| ${}^{*}$, ${}^{\natural}$, $\bar{\ }$ | The Hermitian, natural and coefficient conjugations, as those conventions fix them |
| $\mathrm{Sc}$, $H$, $\langle\cdot\rangle_{\natural}$ | The scalar part, the Hermitian norm and the algebra norm of *Norm and Pairing Conventions* |
| $\langle\cdot,\cdot\rangle_{*}$ | The Hermitian form of *Norm and Pairing Conventions* |
| $\mathsf{M}_2$ | The corpus's complex-linear map to the two-by-two arrays; named here, restated nowhere |
| $A(q)$ | The source's assignment, its equation (8); not complex-linear, not multiplicative, not injective |
| $\ker A$ | $\mathrm{span}_\mathbb{R}\{-ie_t + \vec e_x,\ -i\vec e_y + \vec e_z,\ \vec e_y + i\vec e_z\}$, containing the down-state line |
| $z, w$ | $z = q_t + iq_1$ and $w = q_y + iq_3$ in the classical assignment $q = z + w\vec e_y$ |
| $\lvert q\rvert^2 = \sum_\mu\lvert q_\mu\rvert^2$ | The source's square, the Hermitian norm $H$; $1$ on both states |
| $q_1, q_3$ | The source's coefficient labels, $q_x$ and $q_z$ |
| $S_x, S_y, S_z$ | The source's spin operators; equal to $-\tilde S_3, -\tilde S_2, -\tilde S_1$ |
| $\tilde S_k = \tfrac{\hbar}{2}i\vec e_k$ | The corpus's spin operators |
| $q_+ = \tfrac{1}{\sqrt2}(e_t - i\vec e_x)$, $q_- = \tfrac{1}{\sqrt2}(-\vec e_y - i\vec e_z)$ | The source's two states |
| $\tfrac12(e_t \pm i\vec e_x)$ | The two pure states along $\vec e_x$; the minus member is $q_+/\sqrt2$ |
| $\tfrac12(-\vec e_y - i\vec e_z)$ | The square-zero element $q_-/\sqrt2$ |
| $D(n,\theta) = e_t\cos\frac{\theta}{2} - i(q_p\cdot n)\sin\frac{\theta}{2}$, $q_p\cdot n=-i(\vec e\cdot n)$ | The source's rotation operator; a unit-norm element |
| $S_\pm = S_x \pm iS_y$ | The source's ladder operators; $S_- = S_+^{*}$ |
| $Y_l^{s_{\mathrm{tot},z}\pm\frac12}$, $C_1, \dots, C_4$ | The angular harmonics and the source's coefficients, the radicals $C_{l1},C_{l2}$ beside its (20), called Clebsch–Gordan in its (25) |
| $\sqrt2\,q_+ = e_t - i\vec e_x$, $\sqrt2\,q_- = -\vec e_y - i\vec e_z$ | The two fixed elements in which the radial pair $(F,G)$ is borne |
| $F(r), G(r)$ | Radial functions; closed forms recorded, not verified |
| $k$, $za_0$, $a_0$, $\rho = Cr$, $s$ | Dirac–Coulomb quantum number, Coulomb coupling, its constant, radial variable and exponent |
| $E$ | Energy; the source's formula printed without the square on the ratio |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Alejandro Arias Jiménez, "Biquaternion representation of the spin one half and it's application on the relativistic one electron atom," arXiv:2403.02344v1 [quant-ph] (28 February 2024), Universidad de las Américas Puebla, the source recorded here.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics*, Pitman Research Notes in Mathematics 351 (Addison-Wesley Longman, 1996), for the $2\times2$ matrix form $\left(\begin{smallmatrix}z&w\\-\bar w&\bar z\end{smallmatrix}\right)$ of the real quaternions and the quaternionic function theory built on it.
- V. V. Kravchenko, *Applied Quaternionic Analysis*, Research and Exposition in Mathematics 28 (Heldermann, 2003), for the quaternionic Dirac operators and potentials that the source's last sections approach from the matrix side.
- Maurits H. Silvis, *A quaternion formulation of the Dirac equation*, Centre for Theoretical Physics, University of Groningen (2010), for the matrix representation that the source's final section records.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the complex-quaternion algebra, its conjugations, its norm and its zero divisors, cited as the source's own reference.
- J. J. Sakurai and E. D. Commins, *Modern Quantum Mechanics*, revised edition (Addison-Wesley, 1995), for the Pauli-matrix formalism of spin one half, the source's own reference for the operators and states.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the standard radial Dirac–Coulomb system, its Laguerre solutions and the Sommerfeld–Dirac spectrum against which the source's result is compared.
- H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957), for the exact Dirac–Coulomb spectrum and the two-electron problem the source names as its next step.
- Companion articles: [Spin-1/2 Quantum Physics in Biquaternionic Form](spin-1-2-quantum-physics-in-biquaternionic-form.html); [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html); [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html); [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [Conventions of the Matrix Models](matrix-representations-conventions.html); [Element and Operator Representations: The Three Actions](element-and-operator-representations-the-three-actions.html); [The $M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation](../articles_maths/m2c-h-standard-representation.html); [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html).
