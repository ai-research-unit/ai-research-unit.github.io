# __Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form__

## Introduction

Charge conjugation is the discrete operation that exchanges a particle with its antiparticle. On the biquaternion algebra it is written on the element, $Q^{\mathrm c}=-e_y\bar Qe_y$: the coefficient conjugation, followed by a two-sided product by a fixed product of units. The companion article *The CPT Theorem in Biquaternionic Form* builds the same operation and finds that its internal factor is the single spatial unit $-e_y$, which is anti-Hermitian, so it lies in the material sector $\mathbb{M}_-$ and not in the Hermitian one $\mathbb{M}_+$. The present article asks the question that computation cannot answer: **when is $C$ trivial?** A symmetry that acts as the identity on the algebra exchanges nothing there; the class of particles on which charge conjugation acts trivially has a name — the **truly neutral** particles — and a place in physics: the photon, the $Z$ boson, and the neutral mesons $\pi^0$, $\eta$, $\phi$.

The classification of the algebra literature answers the question with a single algebraic datum. The field of the article is valued in a module, and a module has a **division ring** of scalars, which is $\mathbb{R}$, $\mathbb{H}$ or $\mathbb{C}$ and nothing else. Over a real division ring the fixed product that implements the conjugation is central, so the conjugation reduces to the coefficient conjugation and exchanges no two states. Over a quaternionic division ring it is a genuine product of units and exchanges an element with a distinct partner; over the complex one it relates the module to its conjugate. The division ring, in other words, is what decides whether a particle can be its own antiparticle. (The literature writes the operation with a star on the element; here the star is reserved for the Hermitian conjugation of the corpus, and the bar is the coefficient conjugation.)

The article is organised as follows. A first section writes the conjugation on the algebra and fixes the two values of the subscript. A second states the division-ring trichotomy. A third reads the trichotomy as the three classes of particles, and a fourth places the three classes in the biquaternion algebra. A fifth separates what the framework supplies from what it transcribes. The article closes with the open questions, the legacy section on the gamma formulation, and the summary.

- Companion article *The CPT Theorem in Biquaternionic Form*, for the explicit form of the conjugation and for the classification of the discrete operations.
- The mathematics articles *Division Rings*, *Central Simple Algebras and the Brauer Group* and *The Brauer Wall Group and the Eightfold Way*, for the division ring as an isomorphism invariant of a real or complex algebra.
- Companion article *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*, for reality conditions and real structures on the algebra.
- Companion articles *The Neutron in Biquaternionic Form* and *The Proton in Biquaternionic Form*, for the two charge states of one isospin doublet.

## The Conjugation of the Algebra

The three discrete operations $P$, $T$ and $PT$ act on each graded piece of the algebra by a sign. Charge conjugation is not of that kind, and two features separate it from them. It is **conjugate-linear**: it contains the coefficient conjugation and it reverses the scalar, so that

$$
(\lambda Q)^{\mathrm c}=\bar\lambda\,Q^{\mathrm c},
$$

which no untwisted operation does. And it preserves products,

$$
(QX)^{\mathrm c}=Q^{\mathrm c}X^{\mathrm c},
$$

so it is an automorphism of the algebra read over the reals and only a semilinear map over the complex numbers. The reversal of the scalar is what the name *pseudoautomorphism* records.

The fixed product supplies the rest. On this algebra it is $-e_y$, whose square is $-e_t$. Written on an element, the conjugation is

$$
Q^{\mathrm c}=-e_y\,\bar Q\,e_y .
$$

That is a derived form: the coefficient conjugation, followed by the two-sided product by the fixed product. The two factors are one object used twice, and the product is fixed only up to a nonzero scalar, so the only freedom in the operation is the choice of that scalar, exactly as the companion article's verification found.

**The multiplier alone.** The two-sided product by the fixed product is written out,

$$
Q\mapsto-e_y\,Q\,e_y ,
$$

It is linear, it is an automorphism, and its square is the identity: the two factors multiply to $e_y^2=-e_t$ on the left and on the right, and the two signs cancel. The conjugation is that multiplier preceded by the coefficient conjugation, and the two behave differently on the two values of the subscript.

### The Two Values of the Subscript

An element is written $Q=Q_L+Q_R$. The part $Q_L$ is the part of value $L$, the minus one, and $Q_R$ the part of value $R$, the plus one. That is the whole definition, and the values are exactly two. Every element is a sum of one part of each, only the zero element has both parts zero, a product takes the value of its right factor, and left multiplication keeps the value.

**The conjugation keeps the value.** The fixed product is a single spatial unit, and it changes the value on its own. The coefficient conjugation changes the value too, since it conjugates the frame's phase $i$ and leaves the direction $\vec e_z$ alone. The two changes cancel, so the conjugation carries an $L$ element to an $L$ element. The older reading took the fixed product's own exchange for a flip of the value; the flip is the fixed product's, and not the operation's.

That is also the physics: $C$ carries a left-handed particle to a left-handed antiparticle, and it is $CP$ that exchanges the two values. The companion article composes the multiplier with a module conjugation of its own rather than with the coefficient conjugation, so the two accounts differ on which side of the algebra the operation moves; the operation on the element is the one written here.

**The two squares.** The conjugation squares to the identity: the coefficient conjugation is applied twice and the multiplier is applied twice, and each pair returns its argument.

$$
(Q^{\mathrm c})^{\mathrm c}=Q .
$$

The one-sided form, the right multiplication by $e_x$, has order four: its square is minus the argument, $Q\mapsto Qe_x\mapsto Qe_xe_x=-Q$, and its fourth power returns the argument. The two signs come from the two units: the two-sided product uses $-e_y$ twice on each side, so its square is $e_y^4=+e_t$, and the one-sided product uses $e_x$ twice, so its square is $e_x^2=-e_t$.

**The two lines.** The free equation of the series has two lines, one for each value of the subscript; the pair is fixed in *Operator and Calculus Conventions*, §*The Pair Operator*, and is not restated here. The conjugation keeps the value, so it carries a field of one line to a field of the same line; that a solution is carried to a solution is the companion article's explicit verification.

## The Division-Ring Trichotomy

The classification is a theorem of the algebra literature and is transcribed here. The field is valued in a module, and the module has a **division ring** of scalars. Only three occur, and the form of the fixed product follows the ring:

| the division ring | the fixed product | the conjugation |
|---|---|---|
| $\mathbb{R}$ | central | the coefficient conjugation alone; no state is carried to a distinct one |
| $\mathbb{H}$ | a product of units, not central | the particle is interchanged with a distinct partner |
| $\mathbb{C}$ | a product of units | the module is related to its conjugate |

**One test decides the case: whether the fixed product is central.** When it is, the inner automorphism it defines is the identity, the conjugation is the coefficient conjugation alone, and it fixes every element pointwise. When it is not, the inner automorphism is genuine, and an element outside its fixed set is carried to a different one.

**The three rings are not three forms of one algebra.** The two real ones name subalgebras of the biquaternion algebra, and the complex one names the algebra itself read over $\mathbb{C}$.

### The Three Cases

**Real division ring.** The scalars are $\mathbb{R}$. The fixed product is central and the conjugation is the coefficient conjugation, so every element of the real form is its own conjugate. The particles are their own antiparticles in the strongest sense — not a neutral particle equal to its conjugate, but a particle on which the conjugation exchanges nothing. A real form may still carry the sign $-1$; for a boson that sign is the charge-conjugation parity, $-1$ for the photon and the $\phi$ and $+1$ for the $\pi^0$ and the $\eta$, and it does not make the antiparticle a distinct state.

**Quaternionic division ring.** The scalars are $\mathbb{H}$. The fixed product is a product of units and is not central. The conjugation acts inside the real form and exchanges an element with a distinct one: the state is its own conjugate only up to a distinct partner. This is the neutral case.

**Complex division ring.** The scalars are $\mathbb{C}$. The conjugation relates the module to its conjugate. The two charge states $\pm1$ are the two members of the conjugate pair, and the conjugation maps one to the other. No state of the pair is its own antiparticle. This is the charged case.

## The Meaning of the Square

The square of the operation is the identity on the algebra, and two signs are in circulation in the literature. The section separates what the division ring fixes from what the representation fixes.

**What the division ring fixes.** Only the form of the fixed product: central, or not. It fixes no sign on a state. Over a real division ring the conjugation is the coefficient conjugation and its square is the identity for that reason; over the other two the square is the identity because the fixed product is used twice and its square is central. In neither case does the division ring supply a minus sign.

**The one-sided square.** The right multiplication by $e_x$ squares to minus the argument, because $e_x^2=-e_t$. A minus sign at the level of a single one-sided action therefore comes from the square of the unit, and it belongs to that reading and not to the division ring. The minus sign the older presentation reports on a single chiral half is a statement of this kind, and it is not restated here: the object that carries it is a Pauli array, and no array is an element of this algebra.

**The two-sided square.** The multiplier and the conjugation square to the identity, because the fixed product enters twice on each side and its square is the central $-e_t$. On the algebra, therefore, the conjugation is an involution, $(Q^{\mathrm c})^{\mathrm c}=Q$, which is the standard statement for a Dirac field. The pair, and not one side of it, is what the algebra carries, and the two readings do not conflict: one is one-sided and the other two-sided.

The corpus meets both signs elsewhere: the Euclidean charge conjugation of *The Spectral Triple of the Biquaternion Algebra* is a cell that squares to $-I_4$, and the real structure of *Bosonization in Biquaternionic Form* is an involution. The moral for the classification is that the sign of a square belongs to the representation and not to the division ring, and that neither sign changes the class of a particle.

## The Three Classes of Particles

The physics uses the trichotomy, not the other way round. Three classes of particle are distinguished by the charge states they carry, and the classes are exactly the three division rings.

**Charged particles.** Electron, proton, muon, the charged $W$ bosons, the charged mesons: at least one of their charge states is non-zero, $Ϙ=\pm1$. The two states $\pm1$ are related by the conjugation and they are distinct, so neither state is its own antiparticle. This is the case of the complex division ring.

**Neutral particles.** Neutron, neutrino, the neutral kaon $K^0$: a charge state $Ϙ=0$ but a non-vanishing field. The particle is neutral — the conjugation carries it to a state of the same charge, $Ϙ=0$ — but that state is still distinct from it, and it has its own name, the antiparticle. This is the case of the quaternionic division ring.

**Truly neutral particles.** Photon, $Z$ boson, $\pi^0$, $\eta$, $\phi$: a charge state $Ϙ=0$ and a field that is its own antiparticle at the level of states, not only of charges. The diagram $Z$ decays to an electron-positron pair, so its fields couple to charge, and its self-conjugacy is not the statement that it carries no charge; it is the statement that the conjugation is trivial on the module that carries it. This is the case of the real division ring.

### The Dictionary

| the notion | the framework's image |
|---|---|
| a particle | a state, an element of the module that carries the field |
| its antiparticle | the state obtained by the conjugation |
| a charge state | $Ϙ=\pm1$ for the two members of a conjugate pair, $0$ for a neutral state |
| the charge-conjugation parity | $\pm1$, the sign of the conjugation on a truly neutral state |
| truly neutral | the conjugation acts trivially on the module |

The dictionary is coarse and it is adequate. It says what the division ring is for: a particle can be its own antiparticle exactly when the module that carries it does not notice the conjugation, and that is exactly the case of the real division ring.

**The criterion is the division ring, not the reality of the Lorentz field.** The Dirac field of $\mathrm{Spin}^{+}(1,3)$ is quaternionic for the electron as much as for the neutron, so the field alone does not separate the classes. What separates them is the ring of scalars of the module that carries it. Two particles with the same kind of field can therefore sit in different classes, and two with different fields can sit in the same one; the class is a property of the module and not of the representation.

**The elimination is complete for fermions and carries no information for neutral bosons.** A Dirac field is neutral exactly when the conjugation is trivial on its module, and the division ring decides that. For a real boson field the conjugation acts on the field without acting on a charge, so the division-ring criterion returns the real ring and adds nothing to the statement that the field is real.

## The Biquaternion Reading

The biquaternion algebra has two readings, and the trichotomy uses both. Read over $\mathbb{C}$, its scalars are $\mathbb{C}$, so the division ring of the module is $\mathbb{C}$: the charged case, by the table itself. Read as a **real** algebra, it carries two real subalgebras of real dimension four, and they carry the other two cases.

- **The coefficient conjugation** fixes the subspace of real coefficients, $\mathbb{H}_{\mathbb{B}}$. That subspace is a division ring isomorphic to $\mathbb{H}$, so a module over it has $\mathbb{H}$ for division ring: the neutral case.
- **The charge conjugation** fixes the elements whose time and $y$ coefficients are real and whose $x$ and $z$ coefficients are imaginary. That set is a real subalgebra of real dimension four; it is not a division ring, since the two nonzero elements $\tfrac12(e_t+i\vec e_x)$ and $\tfrac12(e_t-i\vec e_x)$ multiply to zero; and its scalars are $\mathbb{R}$: the truly neutral case.

**The third subalgebra is read off the conjugation.** It is written here as a fixed set and not by naming its basis, because the conjugation is the datum the article is about and the subalgebra is what that datum leaves alone. The two real forms are the two conjugations the algebra carries, one for each.

### The Axis Is a Property of the Basis

A display that singles out a direction does so through its basis, and the test is a property of the basis alone: an operator is diagonal when each basis element is carried into a multiple of itself.

- In the coefficient basis the diagonal cells are the four squares, $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$, $\vec e_z\vec e_z$. The set is unchanged by any permutation of the three spatial units, because the four squares name the four directions and nothing else.
- In a frame built on a declared direction $\vec u$ the diagonal cells are four others: $e_te_t$, $e_t\vec u$, $\vec u\,e_t$, $\vec u\vec u$. The declared direction appears twice, time appears twice, and the other two spatial units appear in none. The set changes when the units are permuted, and it is written with $\vec u$ so that no axis is privileged by the notation.

That is the whole of the axis. The change from one display to the other is the conjugation by $C_{\Pi}$, which keeps the trace, the determinant, the spectrum, the rank and every product; the four diagonal cells are not among the things it keeps, and no argument of this article depends on which of the two displays is written.

### Choosing the Algebra

The three cases are realised by the choice of the module the field is valued in.

- **Charged fields** are carried by the algebra itself, read over $\mathbb{C}$. Their conjugation is the conjugate-linear map of the first section, and it relates the field to its conjugate.
- **Neutral fields** are carried by the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, which is a division ring. Their conjugation is the non-trivial exchange of a particle with a distinct partner.
- **Truly neutral fields** are carried by the fixed set of the conjugation. On it the conjugation is the identity, and the field is its own antiparticle, with the sign $\pm1$ allowed as a parity.

The interpretation is not a derivation, and it adds no field content. Its value is that it locates the three charge classes in the same algebra: the complex algebra carries the charged case, and its two real subalgebras of real dimension four carry the two neutral cases. The photon article's finding that the free photon is a real, self-conjugate field is the case of the real division ring; the neutron article's finding that the neutron is neutral but distinguishable from the antineutron is the case of the quaternionic one.

## What the Framework Establishes, Transcribes, and Does Not

### Established, and recomputed

Each statement below is a computation and not an analogy.

- **The conjugation on the element.** $Q^{\mathrm c}=-e_y\bar Qe_y$ is conjugate-linear, preserves products, and squares to the identity.
- **The multiplier and the values.** The two-sided product $-e_yQe_y$ exchanges the two values of the subscript, the coefficient conjugation exchanges them as well, and the conjugation keeps them.
- **The two signs.** The one-sided form is the right multiplication by $e_x$ and its square is minus the argument; the two-sided product squares to the identity. The sign is the square of the unit.
- **The two fixed sets.** The fixed set of the coefficient conjugation is the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$; the fixed set of the conjugation is a real subalgebra of real dimension four that is not a division ring.

### Transcribed, not derived

- **The classification theorem.** The form of the fixed product is governed by the division ring of the module, and the three division rings give the three cases. The theorem is the algebra literature's, and the article organises the charge classes by it.
- **The physical identifications.** The assignments — charged for the complex ring, neutral for the quaternionic one, truly neutral for the real one — are the standard reading of the classification. Their translation into the framework's presentation is the present article's contribution; the physics itself is not.
- **The biquaternion realisation.** That the algebra is complex with $\mathbb{C}_{\mathbb{B}}$ for centre, and that it carries a real-quaternion subspace and a real subalgebra of real type, is the corpus's own structure. Reading the three classes through those subalgebras is the article's organisation, not a theorem the algebra forces.

### Gap, left visible

- **The conjugation is not intrinsic.** The operation needs the fixed product, and the fixed product is fixed only up to a scalar. The construction therefore does not derive the existence of charge conjugation from the division ring; it uses the division ring to classify a conjugation that is put in by hand.
- **No intrinsic form of the conjugation inside the algebra.** The conjugation is the coefficient conjugation composed with the multiplier, and the multiplier is outside the Hermitian sector. A reading in which the operation were intrinsic to the algebra would need an element that the algebra supplies, and there is none.
- **The dictionary between classes and division rings is structural, not functorial.** It says that the modules over the three rings realise the three cases. It does not give a map from a given state to its division ring.

## Open Questions

**Is the neutrality of a field always the statement that its module is fixed by one of the two conjugations?** The neutron's neutrality is the quaternionic ring, which here is the statement that the module is fixed by the coefficient conjugation. The photon's self-conjugacy is the real ring, the statement that it is fixed by the charge conjugation. Whether every neutral field is of one of the two kinds, or whether a third kind exists that the division-ring classification does not see, is not settled by the theorem.

**The conjugation and massive neutral fermions.** A Majorana field is neutral but carries mass. In the framework, the mass term couples the two values of the subscript, and the conjugation keeps them, so a Majorana mass and a Dirac mass are distinguished by which values the mass term joins. The companion computation stops at the free field, and the massive case is not done.

**The charge-conjugation parity of truly neutral particles.** The $\pi^0$ has $C=+1$ and the $\phi$ has $C=-1$ despite both being $Ϙ=0$. In the algebra the sign is a sign of the fixed set — the identity on the module up to $\pm1$ — and where such a sign comes from is open.

**The two squares in higher-spin fields.** A one-sided action squares to minus the argument and a two-sided one to the argument itself. The corpus's higher-spin fields live in tensor powers of the algebra. Whether the distinction survives the tensor power, or whether the sign changes with the spin, is a test: take the two squares on a two-fold tensor power and compare.

**Coupling to gauge fields.** A gauge field adds a connection to the field, and the conjugated field is charged under the conjugated connection. In the real-division-ring case a connection and its conjugate are the same connection; in the other two they are not. The consequence for the classification is that a truly neutral field can carry no charge under a connection that its own conjugate does not share, which is a constraint on which fields can be truly neutral in a gauged theory. The constraint is known in the physics and is not derived here.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

This section is the only place in the article where the gamma matrices appear. They are not a different algebra and no formula above needs them: they are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, and each gamma *is* one of the five frame cells, the factor $i$ included, so the dictionary below carries no extra phase.

With $L_a\psi=a\psi$ and $R_b\psi=\psi b$, the dictionary is:

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

The first and the last collapse to one-sided multipliers, $\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}$ and $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$, because $L_{e_t}^{\mathrm{pau}}$ is the identity. The charge-conjugation cell of the article is the same frame read in the spatial direction:

$$
\eta_C=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=i\gamma_2,
$$

In the axis-free display:

$$
\eta_C=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=i\gamma_2,
$$

and the chirality cell is:

$$
\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}=\gamma_5.
$$

The same identities in the axis-free display:

$$
\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}=\gamma_5.
$$

The dictionary is complex-linear. Over $\mathbb{R}$ it splits into two real forms: the products of $\gamma_0,\dots,\gamma_3$ satisfy the $\mathrm{Cl}_{1,3}$ relations and span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, while the sixteen two-sided cells $L_aR_b$ span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

The central grading $\chi$ is a different object from $\gamma_5$. It is $\chi=i\tilde\Xi_{\mathrm{ad}}$, where $\tilde\Xi_{\mathrm{ad}}$ is the adjoined central root of $-1$, with $\tilde\Xi_{\mathrm{ad}}^{2}=-e_t$, so that $\chi^{2}=e_t$; it is also the difference $e_+-e_-$ of the two central idempotents. On the Dirac module it is represented by $\gamma_5$, and it is not $\Gamma$.

For translation from the gamma literature, with $\epsilon_{0123}=+1$ and $\varepsilon=(1,-1,-1,-1)$:

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
\qquad \varepsilon=(1,-1,-1,-1),$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

No identity in this list is used in the body of the article. They are recorded so that a formula written in the gamma frame can be translated into the cells, and they are the only place in the article where gamma symbols occur.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Charge conjugation is the conjugate-linear map $Q^{\mathrm c}=-e_y\bar Qe_y$ of the biquaternion algebra: the coefficient conjugation, followed by the two-sided product by a fixed product of units. It preserves products and reverses the scalar. The multiplier alone, $-e_yQe_y$, exchanges the two values of the subscript; the coefficient conjugation exchanges them as well, so the conjugation keeps them; and the conjugation is an involution. The one-sided form is the right multiplication by $e_x$, whose square is $-e_t$, that is, minus the argument; the sign of that square is the square of the unit, not a property of the division ring.

The three charge classes are the three division rings of the module. Over $\mathbb{R}$ the fixed product is central, the conjugation is the coefficient conjugation, and no element of the module moves: the truly neutral particles, at $Ϙ=\bar0$, with the parity $-1$ for the photon and the $\phi$ and $+1$ for the $\pi^0$ and the $\eta$. Over $\mathbb{H}$ the fixed product is not central and an element is carried to a distinct partner: the neutral particles, at $Ϙ=0$, the neutron among them. Over $\mathbb{C}$ the conjugation relates the module to its conjugate: the charged particles, at $Ϙ=\pm1$.

The biquaternion algebra read over $\mathbb{C}$ has $\mathbb{C}$ for scalars, so its division ring is $\mathbb{C}$: the charged case, by the table itself. Its two real subalgebras of real dimension four carry the other two cases: the real-coefficient subspace $\mathbb{H}_{\mathbb{B}}\cong\mathbb{H}$ is the fixed set of the coefficient conjugation and carries the neutral case, and the fixed set of the charge conjugation is a real subalgebra of real type and carries the truly neutral case. The division ring therefore places the three classes in one algebra: the photon's self-conjugacy is the case of the real ring, the neutron's neutrality the case of the quaternionic one, and the charged fields are the complex algebra itself. What is transcribed is the classification and the physical assignments; what is recomputed here is the conjugation on the element, its two squares, and the two fixed sets.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; complex dimension four, complex centre $\mathbb{C}_{\mathbb{B}}$ |
| $\mathbb{R}$, $\mathbb{H}$, $\mathbb{C}$ | The three division rings a module can carry; one per charge class |
| $Q^{\mathrm c}=-e_y\bar Qe_y$ | Charge conjugation on the element; $\bar{\cdot}$ is the coefficient conjugation |
| $-e_y$ | The fixed product; its square is $-e_t$, and it is fixed only up to a scalar |
| $Q\mapsto-e_yQe_y$ | The two-sided multiplier; exchanges the two values of the subscript; its square is the identity |
| $Q\mapsto Qe_x$ | The one-sided form; its square is $-e_t$, its order is four |
| $Q_L$, $Q_R$ | The two values of the subscript, the minus one and the plus one |
| $\tilde\Psi_L$, $\tilde\Psi_R$ | The two lines of the free equation, one per value |
| $\mathbb{H}_{\mathbb{B}}\subset\mathbb{B}$ | Real-quaternion subspace, $\cong\mathbb{H}$; fixed set of the coefficient conjugation |
| the fixed set of $Q^{\mathrm c}$ | Time and $y$ real, $x$ and $z$ imaginary; a real subalgebra of real dimension four, not a division ring |
| $Ϙ=\pm1,0,\bar{0}$ | Charged (either sign), neutral, truly neutral charge states |
| $C_{\Pi}$ | The change of display; keeps trace, determinant, spectrum, rank and products |
| $\mathrm{pau}$, $\mathrm{axf}$ | The labels of the two displays of an array |
| $\gamma_\mu$, $\Gamma=\gamma_5$ | The frame cells of the closing section; they appear only in *The Legacy Pauli Gamma Formulation* |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- B. L. van der Waerden, *Group Theory and Quantum Mechanics* (Springer, 1974), and R. Brauer and H. Weyl, "Spinors in $n$ dimensions," *American Journal of Mathematics* **57** (1935) 425–449, for spinors over the division rings $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$.
- M. F. Atiyah, R. Bott and A. Shapiro, "Clifford modules," *Topology* **3** (1964) 3–38, for the classification of real and complex Clifford algebras and their division rings.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the intrinsic order-two maps and the pseudoautomorphism of a Clifford algebra.
- P. K. Rashevskii, "The theory of spinors," *Uspekhi Matematicheskikh Nauk* **10** (1955) 3–110 (*American Mathematical Society Translations* (2) **6** (1957) 1–110), for the classification of the fundamental automorphisms.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the division-ring trichotomy of the charge-conjugation pseudoautomorphism and the charged, neutral and truly neutral classes.
- Companion articles: [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html); [The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form](the-spin-charge-hilbert-space-and-the-su3-supermultiplets-in-biquaternionic-form.html); [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html); [The Neutron in Biquaternionic Form](the-neutron-in-biquaternionic-form.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*; *Clifford Algebra Representation*; *The Brauer Wall Group and the Eightfold Way*.
