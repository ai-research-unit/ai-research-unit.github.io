# __Conventions of the Norms and the Pairings__

## Introduction

These are the conventions of the norms and of the pairings. The norm of a form is the form at its two equal arguments, so the four norms are fixed with the four forms; the article assumes the products and the forms of *Conventions of the Products and the Forms* and the base of *Conventions in the Biquaternion Universe*.

The order follows the reading. The four norms are named by one letter each, with two arities; the qualified words regular and degenerate are fixed; the unitary convention fixes what norm one means in each layer and separates it from the star-unitary condition. The polar word follows, with its four factors and its domain, the two norms it is read against, the four objects called a boost, the four-momentum, the trace and the normalised state, and the three pairings with their non-nested domains.

The article states conventions only; the existence and uniqueness of the word are proved in *The Polar Decomposition of a N-Regular Biquaternion*, and the pairings in *The Polar Decomposition and Its Three Pairings*.

## The Four Algebraic Norms and the Unitary Convention

**The definition of a norm.** The norm of a form is that form read at its two equal arguments,

$$
\mathrm{Norm}(\tilde{Q}) = \mathrm{Form}(\tilde{Q},\tilde{Q}) ,
$$

and the convention is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand, and the four forms above and the four norms below are its instances.

**Bars around a complex element are the ordinary complex modulus.** For $Q=q+iq'$,

$$
\lvert Q\rvert=\sqrt{Q\bar Q}=\sqrt{q^2+q'^2},
$$

a real and non-negative number. The bars are the modulus and not a bracket of the layer: the algebraic norms keep their bracket, $\langle Q\rangle=Q^2$ and $\langle Q\rangle_{*}=Q\bar Q$. The same bars apply to a complex coefficient of a biquaternion, $\lvert Q_\mu\rvert=\sqrt{q_\mu^2+{q'_\mu}^2}$; over $\mathbb{C}$ the square of the modulus is the Hermitian norm, $\lvert Q\rvert^2=\langle Q\rangle_{*}$.

**The argument of a complex element is written $\arg Q_t$.** For $Q_t\neq0$ it is the angle of the polar form,

$$
Q_t=\lvert Q_t\rvert\,e^{i\arg Q_t},
$$

defined modulo $2\pi$; the branch is stated where the argument is used, and the principal argument in $(-\pi,\pi]$ is written $\operatorname{Arg}Q_t$. The same letter applies to a complex coefficient of a biquaternion, $\arg Q_\mu$, with $\lvert Q_\mu\rvert$ the modulus above.

**The four algebraic norms.** Each pair gives one norm, the diagonal of its form. **One bracket, two arities:** the bracket names the form when it carries two arguments and the algebraic norm when it carries one, so the plain bracket is the form $\langle\tilde{Q}_1,\tilde{Q}_2\rangle = \mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ and the norm $\langle\tilde{Q}\rangle = \langle\tilde{Q},\tilde{Q}\rangle$, and the same holds for the Hermitian, the quaternionic and the Krein. Read with one argument, the value lies in $\mathbb{C}$ for the two bilinear norms and in $\mathbb{R}$ for the two sesquilinear norms, because a sesquilinear form has a real diagonal. The four names are those of the four forms with *norm* in place of *form*:

| bracket | form | letter | algebraic norm | value | realified signature | role |
|---|---|---|---|---|---|---|
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle=\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ | plain | $P$ | $Q_t^2-Q_x^2-Q_y^2-Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | complex cone |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}=\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$ | quaternionic | $N$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | $\mathbb{C}$ | $(4,4)$ | multiplicative; zero-divisor cone |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$ | Hermitian | $H$ | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(8,0)$ | definite; topology |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}=\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2^{*})$ | Krein | $K$ | $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$ | $\mathbb{R}$ | $(2,6)$ | indefinite |

**One letter, two arities.** The four also carry one letter each, $P$ for the plain, $N$ for the quaternionic, $H$ for the Hermitian and $K$ for the Krein, the letter naming the form with two arguments and the algebraic norm with one: $P(\tilde{Q}_1,\tilde{Q}_2)$ is the plain form and $P(\tilde{Q})$ the plain norm, and the same holds for the other three. The plain norm is written $P$ and not $B$, because $B$ is the complex modulus of the vector part, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. The letters and the four qualified notions of a regular and a degenerate biquaternion are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*.

The quaternionic norm is the determinant in the $2\times2$ image and is the multiplicative one, vanishing exactly on the zero-divisor cone; the Hermitian norm is the definite one and carries the topology. The signature column is that of the realified form on the eight real parameters; on the material sector the restrictions are those stated above. Read on one argument the four are the plain norm, the Hermitian norm, the quaternionic norm and the Krein norm. The other sense of the word, the **topological norm**, is the square root of the definite one, $\lVert\tilde{Q}\rVert_E = \bigl(\langle\tilde{Q}\rangle_{*}\bigr)^{1/2}$, and it is *The Norm Defined by a Form*. The four products, their forms and their norms go together, one to a row:

| Product | Form | Letter | Norm |
|---|---|---|---|
| the general plain bilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | $P$ | the plain norm $\langle\tilde{Q}\rangle$ |
| the general quaternionic bilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | $N$ | the quaternionic norm $\langle\tilde{Q}\rangle_{\natural}$ |
| the general plain sesquilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | $H$ | the Hermitian norm $\langle\tilde{Q}\rangle_{*}$ |
| the general quaternionic sesquilinear | $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}$ | $K$ | the Krein norm $\langle\tilde{Q}\rangle_{\natural*}$ |

**The qualified regular and the qualified degenerate.** For a letter $\Phi$ of the four, a biquaternion is **$\Phi$-regular** when $\Phi(\tilde{Q})\neq0$ and **$\Phi$-degenerate** when $\Phi(\tilde{Q})=0$. Only $N$ decides invertibility: $\{N=0\}$ is the origin together with the zero divisors, so $N$-regular is the unit group and $N$-degenerate the non-units. $P$-degenerate and $K$-degenerate contain units, $P(e_t+\vec e_x)=K(e_t+\vec e_x)=0$ with $N(e_t+\vec e_x)=2$, and $H$-degenerate is the origin alone. The unqualified *regular* is the spectral one, $B^{2}\neq0$, of *The Spectrum*, so the letter is never omitted.

### The Unitary Convention

**The convention is the unit-element convention, and the heading keeps its old name because the corpus cites it by that name.** The glyphs $U$, $\tilde u$ and $\tilde U$, in the three cases of the case rule, mark an element of **norm one**; for the biquaternion algebra that norm is $N$ and only $N$. It does not mark a $*$-unitary element: the $*$-unitary condition is a different condition, stated at the end of the section.

A unit element carries its own glyph, the **$u$** in the two cases, beside the root $\tilde\Xi$, the idempotent $\tilde\Pi$ and the nilpotent $\tilde\nu$, as in the mathematical corpus (§*The Unitary Convention* of *Conventions of the Norms and the Unitary Convention*): the letter $u$ is reserved for a unit element, and a general element is $\tilde q$ or $\tilde Q$. **The exponential is written $\exp(\cdot)$**, never $e^{\cdot}$, the letter $e$ being the base $e_t,\vec e_x,\vec e_y,\vec e_z$.

**"Norm one" is fixed layer by layer.** The glyph names no set by itself. The layers used in the physics are these, and the norm of each is the one in the table:

| Layer | Glyph | The norm | The condition | The norm-one elements |
|---|---|---|---|---|
| $\mathbb{C}$ | $U$ | $\lvert Q\rvert=(Q\bar Q)^{1/2}$, the modulus | $\lvert Q\rvert=1$ | $\mathrm{U}(1)=S^{1}$ |
| $\mathbb{H}$, quaternion | $\tilde u$ | $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | $\langle\tilde q\rangle_{\natural}=1$ | $Sp(1)=S^{3}=\mathrm{SU}(2)$ |
| $\mathbb{H}_{\mathrm{s}}$, split-quaternion | $\tilde u$ | $\langle\tilde q\rangle_{\natural}$ | $\langle\tilde q\rangle_{\natural}=1$ | $\mathrm{SL}_{2}(\mathbb{R})$ |
| $\mathbb{B}$, biquaternion | $\tilde U$ | $\langle\tilde Q\rangle_{\natural}$ and no other | $\langle\tilde Q\rangle_{\natural}=e_t$ | $\mathbb{B}^{\times}_{1}\cong\mathrm{SL}(2,\mathbb{C})$ |

The real, split-complex, dual, reduced-biquaternion and split-biquaternion layers are tabulated in *Conventions of the Norms and the Unitary Convention*, §*The Unitary Convention*. In the quaternion layer the level set is $Sp(1)=\{\tilde u\in\mathbb{H}:\tilde u\tilde u^{\natural}=e_t\}=S^{3}=\mathrm{SU}(2)$, and **the rotors are these elements**: an orientation rotor, of norm $e_t$, is a unit real quaternion and is written $\tilde u$.

**For the biquaternion layer the norm is $N$ and no other.** The glyph $\tilde U$ is the $N$-norm-one element,

$$
\mathbb{B}^{\times}_{1}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=e_t\}\cong\mathrm{SL}(2,\mathbb{C}),
$$

and the other three norms of the layer are not unit-element conditions. Their level sets are named for completeness and carry no glyph:

| Letter | Norm | The level set | What it is | Defines $\tilde U$ |
|---|---|---|---|---|
| $P$ | $\langle\tilde Q\rangle$ | $Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}=e_t$ | the complex hyperboloid of the plain norm | no |
| $N$ | $\langle\tilde Q\rangle_{\natural}$ | $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=e_t$ | $\mathbb{B}^{\times}_{1}$, the norm-one units | **yes** |
| $H$ | $\langle\tilde Q\rangle_{*}$ | $\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2}=1$ | the unit sphere of the Hermitian norm | no |
| $K$ | $\langle\tilde Q\rangle_{\natural*}$ | $\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2}=1$ | the indefinite level set of the Krein norm | no |

**Only $N$ decides invertibility**, which is the reason it is the norm of the glyph: $\{N=0\}$ is the origin together with the zero divisors, while the other three degenerate sets contain units. The phrase "the norm in view" belongs to the polar decompositions, where the author names the norm in the text and takes its level set; it is not a licence to read one glyph under four norms.

**$*$-Unitary is not norm one.** The $*$-unitary group is

$$
\mathrm{U}(\mathbb{B})=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}\cong\mathrm{U}(2)=S^{1}\cdot S^{3},
$$

of real dimension four, written upright because it is a group. Its elements are **$*$-unitary elements**, not unit elements, and the two conditions are independent:

- neither set contains the other: $\mathrm{U}(2)\cap\mathrm{SL}(2,\mathbb{C})=\mathrm{SU}(2)=S^{3}$, the unit quaternions;
- the Hermitian level set $\{H=1\}$ contains $\mathrm{U}(2)$ strictly, since it is the unit sphere of $\mathbb{R}^{8}$ of dimension seven and $\mathrm{U}(2)$ has dimension four;
- the $N$-norm-one set $\mathbb{B}^{\times}_{1}$ does not contain $\mathrm{U}(2)$, because $\mathrm{U}(2)\not\subset\mathrm{SL}(2,\mathbb{C})$.

A boost is a unit element and is not $*$-unitary: $\tilde U_{\mathrm b}$ is $N$-norm one and $\tilde U_{\mathrm b}^{*}\tilde U_{\mathrm b}\neq e_t$. A $*$-unitary element whose determinant is not one is $*$-unitary and is not a unit element. The glyph asserts the first and never the second; an article that needs a $*$-unitary element states $\tilde Q^{*}\tilde Q=e_t$ on it.

**The norm and the group condition exist only where their involution does**: the bar alone over $\mathbb{C}$ and the split-complex numbers, the natural sign alone over $\mathbb{H}$ and the split-quaternions, all four marks over $\mathbb{B}$ and the split-biquaternions.

**The case rule splits the glyph**, as for the elements: $\tilde U$ in the biquaternion and split-biquaternion layers, $\tilde u$ in the quaternion and split-quaternion ones, $U$ in the complex, split-complex, dual and reduced biquaternion ones. The pure case carries the arrow, $\vec u$ and $\vec U$.

**The coordinates carry the letter of the unit element**: in $\mathbb{B}$ it is $\tilde U = U_te_t + U_x\vec e_x + U_y\vec e_y + U_z\vec e_z$ with $U_\mu = u_\mu + iu'_\mu$ and vector part $\vec U = \vec u + i\vec u'$; in $\mathbb{H}$ it is $\tilde u = u_te_t + u_x\vec e_x + u_y\vec e_y + u_z\vec e_z$ with real $u_\mu$. **A coordinate carries the label of its direction**, as the base does: the scalar coordinate is $U_t$ and the vector coordinates are $U_x, U_y, U_z$, and likewise $u_t, u_x, u_y, u_z$ for the quaternion-layer element $\tilde u$; a role label is written in the upright roman where the statement names a role. **It is allowed to add subscripts when several unit elements are used**, $\tilde U_1, \tilde U_2$.

**The letter $u$ names a unit element and nothing else.** A velocity, a speed, a Lorentz factor and a rapidity are never written $u$ or $U$: the letter of a motion is $v$, and the four-velocity is the element $\tilde V$. A $*$-unitary group is written $\mathrm{U}(1)$, $SU(2)$, $SU(3)$, and its Lie algebra in the upright roman, $\mathrm{u}(1)$, $\mathrm{su}(2)$, $\mathrm{su}(3)$.

**The boost is a unit element, not a letter.** The boost of rapidity $\psi$ along the unit $\vec u_{\mathrm b}$ is
$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},
$$
a Hermitian element of norm one; it carries the glyph $\tilde U$ of every unit element. It is the **frame rotor**; the four-vector factor $\mathcal B=\tilde U_{\mathrm b}^{-2}$ is a different object, and §*The Polar Word and the Three Pairings* separates the four objects called a boost. Where an infinitesimal generator is needed it is read from the exponential as the pure element $\tfrac12 i\vec u_{\mathrm b}$, and the Lorentz brackets are written on the pure elements $\tfrac12\vec e_k$ and $\tfrac12 i\vec e_k$. No letter $K$ is introduced for the Lorentz boost.

## The Polar Word and the Three Pairings

The series writes one polar word and reads it in three bracketings. The word, its factors and the three readings are fixed here once: the polar-decomposition articles of the *Biquaternions* category prove the statements and the physics articles interpret them, but all of them use these symbols with these meanings.

### The Word and Its Factors

**The domain.** The word exists on the complement of the zero-divisor cone, $\langle\tilde Q\rangle_{\natural}\neq0$, and on no larger set. The existence and uniqueness are those of *The Polar Decomposition of a N-Regular Biquaternion*.

**The word.** Every element off the cone is the ordered product

$$
\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad r>0,\qquad \alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}],\qquad \psi_w\ge0,\qquad \theta\in[0,2\pi],
$$

with the factors of the table. The order is forced: the scale and the phase are central, the Hermitian positive boost stands on the left of the real rotor, and the rotor is what remains after the Hermitian part is divided out.

| # | factor | glyph | range | type | action on the algebra |
| --- | --- | --- | --- | --- | --- |
| 1 | scale | $r$ | $r>0$ | real central scalar | dilation by $r^2$ |
| 2 | central phase | $\exp(i\alpha)$ | $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | central unit | scalar multiplication |
| 3 | boost | $\tilde U_{\mathrm b}(\psi_w)=\cosh\frac{\psi_w}{2}e_t+i\sinh\frac{\psi_w}{2}\vec u_{\mathrm b}$ | $\psi_w\ge0$, $\vec u_{\mathrm b}$ a unit real vector | Hermitian positive, $\det=1$ | congruence $X\mapsto\tilde U_{\mathrm b}(\psi_w)X\tilde U_{\mathrm b}(\psi_w)^{*}$ |
| 4 | rotor | $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\vec u_{\mathrm r}$ a unit real vector | real unit quaternion | conjugation $X\mapsto\tilde u_{\mathrm r}X\tilde u_{\mathrm r}^{*}$ |

**The word is not the exponential.** The four factors are a section of the word map, not of the exponential map; the two coincide only when the exponents commute. The defect is the Baker–Campbell–Hausdorff term, and it is recorded in *The Exponential Word and Its Boundary*.

### The Two Norms of the Word

The modulus is the square root of the **quaternionic** norm, and it is not the square root of the Hermitian norm. The two norms measure different things, and the corpus uses both.

| bracket | name | value | role in the word |
| --- | --- | --- | --- |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | quaternionic norm | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, complex | the modulus, $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ on the principal branch; multiplicative; vanishing is the cone |
| $\langle\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | Hermitian norm | $\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$, real and non-negative | the total size; it carries the topology and never enters the existence condition of the word |

**Two warnings.** First, a square root of the Hermitian norm is the **topological norm**, not the polar modulus: the polar modulus is complex and the topological norm is real, so the two are not interchangeable. Second, the polar articles write $E^2=\sum_\mu\lvert Q_\mu\rvert^2$ for the Hermitian norm. That $E$ is not the physical energy: for a four-momentum it is $m^2c^2\cosh 2\psi$ in the notation below, not $m^2c^4\cosh^2\psi$. A formula that needs the energy takes it from the four-momentum, not from this $E^2$.

### The Four Objects Called a Boost

Four different objects carry the word *boost*, and the factor of two between them is the most common error in the corpus. They are separated here once. The kinematic rapidity is $\psi$; the word's parameter is $\psi_w$.

| object | glyph | formula | exponent angle | what it is |
| --- | --- | --- | --- | --- |
| frame rotor | $\tilde U_{\mathrm b}(\psi)$ | $\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | $\psi/2$ | the Lorentz rotor; its congruence is the boost of rapidity $\psi$; linear in the spinor |
| four-vector factor | $\mathcal B=\tilde U_{\mathrm b}(\psi)^{-2}$ | $\cosh\psi\,e_t-i\sinh\psi\,\vec u_{\mathrm b}$ | $-\psi$ | the inverse square of the frame rotor; the factor a four-vector element carries |
| generator | $\tfrac12 i\psi\vec u_{\mathrm b}$ | — | — | the Hermitian element whose exponential is $\tilde U_{\mathrm b}(\psi)$ |
| rapidities | $\psi,\ \psi_w$ | real, $\psi\ge0$ | — | $\psi$ kinematic; $\psi_w=2\psi$ for a four-vector element, whose word axis is opposite the frame axis |

The fourth factor of the word, $\tilde u_{\mathrm r}$, is a rotation and not a boost. The word *boost* alone is not a name: a statement must say whether it means the frame rotor, the four-vector factor, the generator or a rapidity. In the word table the letter $\vec u_{\mathrm b}$ names the axis of the word's factor; for a transformation it coincides with the frame axis, and for a four-vector it is opposite it.

**Linear and bilinear.** The frame rotor acts on a spinor by left multiplication, $\chi\mapsto\tilde U_{\mathrm b}(\psi)\chi$, and on a four-vector by the congruence $X\mapsto\tilde U_{\mathrm b}(\psi)X\tilde U_{\mathrm b}(\psi)^{*}$. A four-vector is bilinear in the spinor, so the factor that the four-vector element itself carries is the inverse square, $\mathcal B=\tilde U_{\mathrm b}(\psi)^{-2}=e^{-i\psi\vec u_{\mathrm b}}$: the same boost, read twice. The word stores the boost in the frame rotor and deposits it twice in the four-vector; its parameter is $\psi_w=2\psi$.

### The Four-Momentum

Let $\tilde P=i(E/c)e_t+\vec p$ with $E=mc^2\cosh\psi$ and $\vec p=mc\sinh\psi\,\hat p$, so that $\psi$ is the kinematic rapidity. Then

$$
\tilde P=imc\,\mathcal B,\qquad \mathcal B=e^{-i\psi\hat p},\qquad \Rho=imc,\qquad \Theta=-i\psi,\qquad \vec U=\hat p,
$$

with $B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}=\lvert\vec p\rvert$, and the eigenvalues are

$$
\lambda_\pm=Q_t\pm iB=imc\,e^{\pm\psi}=\Rho\,e^{\pm i\Theta}.
$$

The word's parameter here is $\psi_w=2\psi$, and the third factor of the word is $\mathcal B$, whose axis is $-\hat p$. The frame rotor $\tilde U_{\mathrm b}(\psi)$ has the axis $+\hat p$.

**Three errors to avoid.** Writing $\Theta=+i\psi$ swaps the two eigenvalues. Writing $\psi$ for the word parameter when the element is a four-vector halves the word's rapidity, because $\psi_w=2\psi$. Taking the frame rotor $\tilde U_{\mathrm b}(\psi)$ for the four-vector factor gives $imc\,\tilde U_{\mathrm b}(\psi)$, a four-vector of rapidity $\psi/2$. The Hamilton axis $\vec U=\vec Q/B$ points along the momentum; the word's axis in $\mathcal B$ points opposite it, because $\mathcal B=e^{-i\psi\hat p}$ is a boost of rapidity $\psi$ about $-\hat p$.

### The Trace and the Normalised State

The trace is the trace of the $2\times2$ image and nothing else,

$$
\operatorname{Tr}\tilde Q=\operatorname{Tr}\mathsf M_2(\tilde Q)=2\,\mathrm{Sc}\,\tilde Q=2Q_t.
$$

The factor $2$ is forced by $\mathsf M_2(e_t)=I_2$ and cannot be divided out. It cancels in every ratio, and the Born weight is a ratio:

$$
p=\frac{\langle\tilde{Ϛ},\tilde H\rangle_{*}}{\langle\tilde{Ϛ},e_t\rangle_{*}}=\frac{\operatorname{Tr}(\tilde{Ϛ}\tilde H)}{\operatorname{Tr}\tilde{Ϛ}},
\qquad \operatorname{Tr}\tilde{Ϛ}=1\iff\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12 .
$$

A normalised state therefore has trace one; the factor $2$ belongs in the definition of the trace and cancels in the probability. Dropping it from the trace or inserting it in the ratio are the two opposite mistakes.

### The Domains of the Three Pairings

The three pairings are three bracketings of the same word, and their domains differ. The table records the condition for the **factorisation** and the condition for the **construction**, which are not the same statement.

| pairing | factorisation | factorisation exists | construction exists | witness of failure |
| --- | --- | --- | --- | --- |
| word | $r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ | same | any element of the cone |
| quaternion | $\tilde q\,e^{i\tilde\Psi}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ | $\tilde q_r\neq0$ (on this domain) | $i\vec e_x+i\vec e_y$: $\langle\tilde Q\rangle_{\natural}=-2$ but $\tilde q_r=0$ |
| Hamilton | $\Rho\,e^{\vec U\Theta}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ | same | $e_t+\vec e_x+i\vec e_y$: $\langle\tilde Q\rangle_{\natural}=1$ but $\langle\vec Q,\vec Q\rangle_{\natural}=0$ |
| Cartan | $\tilde Q_H\tilde Q_0$ | $\langle\tilde Q\rangle_{\natural}\neq0$ | same | $e_t+i\vec e_x$: on the cone; the generalized form gives a partial isometry |

**The domains are not nested.** The quaternion construction fails at $\tilde q_r=0$; the Hamilton pairing fails when the vector part is null; the Cartan pairing is the widest and is total off the cone. The generalized polar decomposition extends the Cartan pairing to the cone with a partial isometry, and it is *The Polar Decomposition of a Biquaternion*.

**The tangent equation on the domain of the word.** The equation $\tan\tilde\Psi=\tilde q_r^{-1}\tilde q_i$ fails to have a real solution in exactly one case, when $\tilde q_r^{-1}\tilde q_i$ is a unit pure quaternion. That case forces $\langle\tilde Q\rangle_{\natural}=0$: writing $\tilde q_i=\tilde q_rT$ with $T$ a unit pure quaternion makes the real inner product of $\tilde q_r$ and $\tilde q_i$ vanish and their norms equal, so the difference of the squared norms and the cross term both vanish. On the complement of the cone, therefore, the construction exists exactly when $\tilde q_r\neq0$. The condition $\tilde q_r\neq0$ alone is not sufficient on the whole algebra: $e_t+i\vec e_x$ has $\tilde q_r=e_t$ and lies on the cone, where the word does not exist. The article's "exactly" is correct on the word's domain; its claim that the set $\{\tilde q_r\neq0\}$ lies inside that domain is not.

## Summary

Each form has a norm, and each norm takes one letter, $P$, $N$, $H$ or $K$, used with two arguments for the form and with one for the norm. Regular and degenerate are qualified by the letter, because only the $N$ pair gives the unit partition, and the unqualified word regular is spectral. Norm one is fixed layer by layer by the unitary convention, and for the biquaternion layer it is $N$ and no other; the star-unitary condition is a different condition, and only $N$ decides invertibility. The letter $u$ names a unit element and nothing else.

The polar word is $\tilde Q=r\,e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ on the complement of the zero-divisor cone. It is a section of the word map, not of the exponential. The modulus is the square root of the quaternionic norm, not of the Hermitian one; the Hermitian norm is the topological norm and never enters the existence condition. Four objects carry the word *boost*, and the factor of two between the frame rotor and the four-vector factor is the most common error in the corpus; for a four-momentum $\Rho=imc$, $\Theta=-i\psi$ and the word parameter is $\psi_w=2\psi$.

The trace is the trace of the $2\times2$ image, $\operatorname{Tr}\tilde Q=2Q_t$, and the factor two is forced and cancels in the Born ratio; a normalised state has trace one. The three pairings are three bracketings of one word, and their domains are not nested: the quaternion construction can fail where the word exists, the Hamilton pairing can fail where both exist, and the Cartan pairing is the widest off the cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$, $N$, $H$, $K$ | The four norms, the diagonals of the plain, quaternionic, Hermitian and Krein forms |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ | The biquaternion norm, the multiplicative one; its zero set is the zero-divisor cone |
| $H(\tilde Q)=\mathrm{Sc}(\tilde Q\tilde Q^{*})$ | The Hermitian norm, real and non-negative |
| $\Phi$-regular, $\Phi$-degenerate | $\Phi(\tilde Q)\neq0$ and $\Phi(\tilde Q)=0$; only the $N$ pair is the unit partition |
| $\Rho,\Theta,\vec U,B$ | The Hamilton data of the polar word; $\Rho=imc$, $\Theta=-i\psi$, $\vec U=\hat p$, $B=\lvert\vec p\rvert$ for a four-momentum |
| $\psi$, $\psi_w$ | The kinematic rapidity and the word parameter, $\psi_w=2\psi$ for a four-vector |
| $\tilde U_{\mathrm b}$, $\mathcal B$ | The frame rotor and the four-vector factor $\mathcal B=\tilde U_{\mathrm b}^{-2}$ |
| $\operatorname{Tr}\tilde Q=2Q_t$ | The trace of the $2\times2$ image; a normalised state has trace one |
| $p=\operatorname{Tr}(\tilde{Ϛ}\tilde H)/\operatorname{Tr}\tilde{Ϛ}$ | The Born weight, a ratio in which the factor two cancels |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](conventions-of-the-products-and-the-forms.html), for the four forms whose diagonals are these norms.
- [Conventions of the Representations](conventions-of-the-representations.html), for the $2\times2$ image whose trace is used here.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the domains and the proofs.
- [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the existence and uniqueness of the word.
