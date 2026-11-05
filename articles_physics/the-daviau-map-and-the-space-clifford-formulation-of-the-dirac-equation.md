# __The Daviau Map and the Space Clifford Formulation of the Dirac Equation__

## Introduction

Daviau writes the Dirac equation as one equation for a general element of the biquaternion algebra. The formulation is called the space Clifford formulation. This article reads it in the corpus's conventions, and it is the third of the three equivalent rewritings of Dirac theory that the corpus records, beside the matrix formulation of *The Dirac Equation in Biquaternionic Form* and the spacetime-algebra formulation of *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*. The equivalence of the three is the subject of a short paper of Fauser, whose statements this article transcribes.

**One algebra, not two.** The source builds its algebra on three vectors of three-dimensional Euclidean space. In the corpus those three vectors are the Hermitian units $i\vec e_x$, $i\vec e_y$, $i\vec e_z$: each squares to $+e_t$, any two anticommute, and the three generate the biquaternion algebra $\mathbb{B}$ (§*The Three Space Vectors and the Dictionary*). No second algebra is introduced, and no second multiplication is fixed.

**The equation.** For a general element $\tilde\Psi$ of $\mathbb{B}$ the equation is

$$
\boxed{\;\mathfrak D\,\tilde\Psi\,(-\vec e_x)=m\,\overline{\tilde\Psi}+q\,\tilde A\,\tilde\Psi\;}
$$

with the elements $\mathfrak D$ and $\tilde A$ of §*The Daviau Equation*. The gradient multiplies on the left, the fixed bivector $-\vec e_x$ on the right, and the mass term is the complex conjugation of the field.

**What the article shows.** Three things, and each is exact. The eight real functions of the source's field are the eight real coordinates of an element of $\mathbb{B}$, and the assignment carries no free choice (§*The Daviau Map*). The star conjugation of the source is the corpus's complex conjugation $\bar{\cdot}$, and not the Hermitian conjugation ${}^{*}$; this is the article's main algebraic point (§*The Star Conjugation*). The equation is two-sided, but its right factor is a fixed bivector and not the chirality, which places it with the corpus's chiral pair and not with Kravchenko's equation (§*The Two Equations the Corpus Carries*).

**The name.** The source calls its algebra a Clifford algebra, and the article keeps that name for the formulation because it is the name of the object described. The field itself is written as an element of $\mathbb{B}$ throughout, and no carrier is introduced for it.

## The Three Space Vectors and the Dictionary

**The three vectors.** The source takes three vectors of three-dimensional Euclidean space with

$$
(i\vec e_j)(i\vec e_k)+(i\vec e_k)(i\vec e_j)=2\delta_{jk}\,e_t .
$$

This is a derived form. It follows from the multiplication table of the units (*Algebra and Element Conventions*, §*The Algebra and Its Basis*) read on the three Hermitian units. At $j=k$ it reads $(i\vec e_k)^2=e_t$, since $i$ is central and $\vec e_k^2=-e_t$:

$$
(i\vec e_k)^2=i^2\vec e_k^2=(-1)(-e_t)=e_t .
$$

Two distinct space vectors anticommute, since two distinct quaternion units do.

**The pseudoscalar is the central imaginary.** The product of the three vectors is one element, and it is the scalar imaginary of the algebra,

$$
(i\vec e_x)(i\vec e_y)(i\vec e_z)=i^3\,\vec e_x\vec e_y\vec e_z=i^3(-e_t)=(-i)(-e_t)=i ,
$$

using $\vec e_x\vec e_y=\vec e_z$, $\vec e_z\vec e_z=-e_t$ and $i^3=-i$. That element is central, $i\tilde\Psi=\tilde\Psi i$, and its square is $-e_t$. So the pseudoscalar of the source and the central imaginary of the corpus are one element, and the source's algebra, read over the real field, is the whole algebra $\mathbb{B}$.

**The eight real units.** The four units of the coefficient basis together with their $i$-multiples are eight real elements,

$$
e_t,\qquad i\vec e_x,\ i\vec e_y,\ i\vec e_z,\qquad \vec e_x,\ \vec e_y,\ \vec e_z,\qquad i ,
$$

and they are a real basis of $\mathbb{B}$: the algebra has real dimension eight, and the eight displayed are linearly independent. The first four square to $+e_t$ and the last four to $-e_t$.

**The dictionary.** The source's four kinds of element are four kinds in the corpus, and the table is the whole dictionary:

| the formulation | the corpus's element | square |
|---|---|---|
| the identity | $e_t$ | $+e_t$ |
| the three space vectors | $i\vec e_x$, $i\vec e_y$, $i\vec e_z$ | $+e_t$ |
| the three products of two space vectors | $-\vec e_x$, $-\vec e_y$, $-\vec e_z$ | $-e_t$ |
| the pseudoscalar | $i$ | $-e_t$ |

**Derived form (the products of two).** The product of two space vectors is minus a quaternion unit, and the three products are the three quaternion units with the minus sign:

$$
(i\vec e_x)(i\vec e_y)=-\vec e_z,\qquad (i\vec e_y)(i\vec e_z)=-\vec e_x,\qquad (i\vec e_z)(i\vec e_x)=-\vec e_y .
$$

Each is $i$ times a space vector as well, $i\,(i\vec e_k)=-\vec e_k$, and that is the line that pairs each space vector with one quaternion unit.

**The dictionary is a reading.** It carries one algebra into two spellings, and it compares no two algebras. The corpus's matrix model of $\mathbb{B}$ is fixed once, in *Matrix Representations Conventions*, and its arrays are not used here: every statement below is a statement about elements and their products.

**The two parities.** The source reads its eight units in a parity of its own, and the spacetime reading gives another. In the formulation the three space vectors and the pseudoscalar are odd, while the identity and the three products of two are even. In the spacetime reading the same three space directions are carried by $\vec e_x$, $\vec e_y$, $\vec e_z$, which are even there. The two readings agree on the three quaternion units and disagree on the three Hermitian ones, and the corpus keeps them apart (*Biquaternion Versors and the Orthogonal Group*).

## The Daviau Map

**The eight real functions.** The source writes its field as four complex components carrying eight real functions $a,b,c,d,e,f,g,h$. The eight enter through four complex combinations,

$$
u=a+ih,\qquad v=f+ib,\qquad w=c+ig,\qquad t=d+ie ,
$$

and the four entries of its array are $\chi_1=u+w$, $\chi_3=t-v$, $\chi_2=t+v$, $\chi_4=u-w$. The corpus's field $\tilde\Psi$ carries eight real functions too, one in $\mathbb H_{\mathbb B}$ and one in $i\mathbb H_{\mathbb B}$ for each of the four directions, and the Daviau map is the assignment of the eight of the source to the eight real units of §*The Three Space Vectors and the Dictionary*.

**Derived form (the expansion).** Read back through the corpus's matrix model, the four entries give

$$
\boxed{\;\tilde\Psi=a\,e_t+d\,i\vec e_x+b\,i\vec e_y+c\,i\vec e_z-e\,\vec e_x+f\,\vec e_y-g\,\vec e_z+h\,i\;}
$$

with the coefficients $(a,d,b,c,-e,f,-g,h)$ on the units $(e_t,\,i\vec e_x,\,i\vec e_y,\,i\vec e_z,\,\vec e_x,\,\vec e_y,\,\vec e_z,\,i)$.

*Proof.* Substitute the four complex combinations into the four entries and read the eight real functions against the eight units. The computation was carried out symbolically on the eight parameters and gives the coefficients displayed. The source prints the coefficient of $i$ with the opposite sign in one place; the sign above is the one the substitution gives, and the one the star of the next section requires.

**The map is a reading, not a change of object.** The eight real functions are the same eight in both spellings. What the map supplies is the unit each one multiplies, and that is a datum of the algebra: the eight units are fixed by the coefficient basis, and no further choice enters.

**Remark (onto the whole algebra).** The element ranges over all of $\mathbb{B}$: its eight coefficients are free, and the eight units are a real basis. The spacetime-algebra formulation works in the algebra of four spacetime vectors and puts its field in the even part of that algebra; the present formulation works in the algebra of three space vectors and puts its field on all of it. The two carriers are of real dimension eight in both cases, so the difference is the algebra and not the size.

**Remark (the corpus's field).** The eight real functions of the source are the eight real parameters of the corpus's field. The identification is exact at the level of real vector spaces, and it is the same dimension count that makes the spacetime-algebra field an element.

## The Star Conjugation

**The map.** The star of the source is real-linear, involutive and multiplicative, and it reverses the phase: for a complex $\lambda$, the star of $\lambda\tilde\Psi$ is $\bar\lambda$ times the star of $\tilde\Psi$. It is therefore an algebra automorphism that reverses the phase. It is not the identity, it is not the quaternion conjugation, and it is not the Hermitian conjugation of the algebra.

**Notation.** The source writes the star with an asterisk. This article writes it $\overline{\cdot}$, because it is the corpus's complex conjugation; the corpus's ${}^{*}$ is a different map (§*It is not the Hermitian conjugation*).

**Its values on the eight real units.** Recomputed from the source's formula, the star fixes the four units $e_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$ and negates the four $i$, $i\vec e_x$, $i\vec e_y$, $i\vec e_z$:

| unit | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ | $i$ | $i\vec e_x$ | $i\vec e_y$ | $i\vec e_z$ |
|---|---|---|---|---|---|---|---|---|
| the star | $+1$ | $+1$ | $+1$ | $+1$ | $-1$ | $-1$ | $-1$ | $-1$ |

**Proposition (the star is the complex conjugation).** The complex conjugation of the corpus fixes each $e_\mu$ and negates each $i e_\mu$ (*Algebra and Element Conventions*, §*The Conjugations*). On the eight real units the two maps agree, and both are real-linear; hence they are one map. Daviau's star is the corpus's $\bar{\cdot}$.

*Proof.* A real-linear map is determined by its values on a real basis. The eight units are a real basis, and the values agree on all eight.

**Why the source's formula gives these values.** The source writes the star as the conjugation of its array by one of its units, composed with the entrywise conjugation. That unit is the image of $i\vec e_y$, and the computation on the eight units gives the table above. It was verified symbolically on the eight units and on a hundred general elements.

**It is not the Hermitian conjugation.** The corpus's ${}^{*}$ negates the three vector units and fixes their $i$-multiples. The star does the opposite on those six units. The two agree on $e_t$ and on $i$ and differ everywhere else, so a display that reads the star as ${}^{*}$ is wrong on six of the eight units. The corpus already records that the entrywise conjugation of an array is not the image of any involution of the algebra (*Algebra and Element Conventions*); the star is the involution that is the image, and the unit the source writes on each side is the whole of the correction.

**Remark (the star is outer).** The star sends the central $i$ to $-i$. An inner automorphism of an algebra fixes the centre, and the centre of $\mathbb{B}$ is the complex line of $e_t$, so no element conjugates the star into itself. Enlarging the algebra does not help: $i$ remains central in every algebra that contains $\mathbb{B}$, and no inner automorphism of any of them moves it. What carries the star is its conjugate-linearity.

**Remark (no multiplication implements it).** A multiplication by a fixed element, on the left or on the right, is complex-linear: it sends $i\tilde\Psi$ to $i$ times the image. The star is conjugate-linear. Hence neither a left multiplication nor a right multiplication is the star, whatever the fixed element.

## The Daviau Equation

**Definition.** With $\tilde\Psi$ a general element and $\mathfrak D$, $\tilde A$ the elements below, the equation is

$$
\boxed{\;\mathfrak D\,\tilde\Psi\,(-\vec e_x)=m\,\overline{\tilde\Psi}+q\,\tilde A\,\tilde\Psi\;}
$$

with

$$
\mathfrak D=e_t\frac{\partial}{\partial Q_t}+i\vec e_y\frac{\partial}{\partial Q_x}+i\vec e_z\frac{\partial}{\partial Q_y}+i\vec e_x\frac{\partial}{\partial Q_z},
\qquad
\tilde A=A_t\,e_t+A_x\,i\vec e_y+A_y\,i\vec e_z+A_z\,i\vec e_x .
$$

The derivatives are the four coordinate derivatives of the corpus (*Operator and Calculus Conventions*, §*The Gradient*), the coordinates are $Q_t,Q_x,Q_y,Q_z$, and on the material sector $Q_t=ict'$.

**The terms, and the side of each.** The gradient $\mathfrak D$ multiplies on the left. The fixed bivector $-\vec e_x$ multiplies on the right, with the same value for every element and at every point. The mass term is the complex conjugation of the field, real-linear and conjugate-linear over $\mathbb{C}$, with the real central coefficient $m$. The coupling is the left multiplication by the potential, and it is the minimal coupling of *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*.

**Derived form (the gradient, term by term).** The three space derivatives carry the three Hermitian units in the cyclic order $i\vec e_y$, $i\vec e_z$, $i\vec e_x$ attached to $\partial/\partial Q_x$, $\partial/\partial Q_y$, $\partial/\partial Q_z$, and the time derivative carries $e_t$. The corpus's gradient carries the four coefficient units in the order $e_t,\vec e_x,\vec e_y,\vec e_z$ (*Operator and Calculus Conventions*, §*The Gradient*). The two differ twice: by the factor $i$ on the space part, and by the cyclic relabelling of the three directions.

**Proposition (the equation is a Dirac equation).** The field carries the eight real functions of the Dirac field (§*The Daviau Map*). The mass term is linear in the field, real and central. The coupling is the left multiplication by the potential. The equation is the Dirac equation written on the algebra, and its content is the content of the matrix formulation, term for term.

**Remark (the right factor and the two parities).** The right factor is the pseudoscalar times the first space vector,

$$
i\,(i\vec e_x)=-\vec e_x ,
$$

so it is minus a quaternion unit. It is even in both parities of §*The Three Space Vectors and the Dictionary*: in the formulation it is the product of the pseudoscalar with a space vector, and in the spacetime reading it is minus a quaternion unit, which is a bivector. The two readings agree on it, and they disagree on the three space vectors that the gradient carries.

## The Two Equations the Corpus Carries

The corpus carries two Dirac equations, and the Daviau equation is a **third form that must be placed against both**, not identified with either. The two are distinguished by which side the operator acts on, and they carry different pieces of physics: chirality on the one-sided equation, the mass direction on the two-sided one.

**The one-sided equation, and chirality.** The corpus's own equation is the chiral pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad \tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R ,
$$

in which the gradient multiplies on the left in each line and the mass pairs the two values of the subscript. Chirality here is not an extra operator: it is the split of the field into its L part and its R part, and the mass is what mixes the two. The operator is one-sided, and the two lines are the two values.

**The two-sided equation, and the mass direction.** Kravchenko's equation is a single equation on $\mathbb{B}$, written $\mathcal NF=0$, with

$$
\mathcal NF=\Bigl(i\frac{\partial}{\partial t'}+D_3\Bigr)F-mi\,\overline{F}\,\vec e_z,\qquad
D_3=\sum_{k\in\{x,y,z\}}\vec e_k\frac{\partial}{\partial Q_k},
$$

where $t'$ is the physical time, related to the corpus's coordinate by $Q_t=ict'$ on the material sector. The time derivative and the spatial gradient multiply on the left, the mass multiplies on the right by the fixed direction $\vec e_z$, and the conjugation supplies the conjugate-linear part. This is the two-sided equation of the corpus: two sides, one field, no split into two values.

**Daviau's equation: two-sided, with a fixed right bivector and a conjugate-linear mass.** Daviau's equation is two-sided as well, but its right factor is the fixed bivector $-\vec e_x$ and its mass is the conjugation. It is the space-formulation face of the chiral equation, not a rewriting of Kravchenko's. The word "two-sided" does not identify the two: it says only that a right multiplication is present, and it leaves open which element multiplies and what the mass term is.

| | Daviau equation | Corpus chiral pair | Kravchenko's equation |
|---|---|---|---|
| Equation | $\mathfrak D\tilde\Psi(-\vec e_x)=m\overline{\tilde\Psi}+q\tilde A\tilde\Psi$ | $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | $\mathcal NF=0$ |
| Multiplication | left by $\mathfrak D$, right by $-\vec e_x$ | left by $\tilde\nabla$ and by $\tilde\nabla^{\natural}$ | left by $i\partial/\partial t'$ and by $D_3$, right by $\vec e_z$ |
| Field | $\tilde\Psi\in\mathbb{B}$, a general element | $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$ | $F\in\mathbb{B}$ |
| Mass | $m\overline{\tilde\Psi}$, conjugate-linear | the pairing of the two values | $-mi\overline{F}\vec e_z$ |
| Chirality | the field carries both values; the right factor is a bivector | the two equations are the two values | the right factor is the fixed direction $\vec e_z$ |
| Role in the corpus | the space formulation | the corpus's formulation | the dictionary and the Cauchy theory |

The table separates the three. The Daviau equation and the chiral pair are the two this article compares; Kravchenko's column is recorded so that the word "two-sided" does not identify the two. The chiral pair and Kravchenko's equation are themselves related by the dictionary of *Canonical Quantization of the Biquaternion Dirac Field*, but they are different equations with mass terms of different kinds, and Daviau's equation belongs with the chiral pair, not with Kravchenko's.

## The Equivalence with the Spacetime Algebra Formulation

The other formulation writes the Dirac equation for a field of the algebra of four spacetime vectors, with the gradient multiplying on the left, a fixed right multiplier on the gradient terms, and a mass that is a right multiplication by the time vector rather than a conjugation. That last point is the one the comparison has to reconcile, because Daviau's mass is the conjugation.

**The comparison equation.** Fauser writes it with the three space vectors of that formulation multiplying the space derivatives, the pseudoscalar on the right of each derivative term, and the mass as minus the conjugation. In the corpus's elements the three space vectors of that formulation are the three quaternion units, and its pseudoscalar is the same $i$:

$$
\frac{\partial}{\partial Q_t}\tilde\Psi\,(i\vec e_z)
+\sum_{k\in\{x,y,z\}}\vec e_k\frac{\partial}{\partial Q_k}\tilde\Psi\,(i\vec e_z)
=-m\,\overline{\tilde\Psi}+q\Bigl(A_t+\sum_{k\in\{x,y,z\}}A_k\vec e_k\Bigr)\tilde\Psi .
$$

The time derivative carries no space vector in either formulation, and that is what puts the two equations in the same shape.

**Statement (the equivalence).** Daviau's formulation and the spacetime formulation are equivalent. The relabelling $z$ that carries the three space directions of one to those of the other is the cycle

$$
z(\vec e_x)=\vec e_z,\qquad z(\vec e_z)=\vec e_y,\qquad z(\vec e_y)=\vec e_x,
$$

with $z(e_t)=e_t$ and $z(i)=i$. It extends to an automorphism of $\mathbb{B}$: it permutes the three vector units cyclically, so it preserves $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$; it satisfies $z^3=\mathrm{id}$ and $z^{-1}=z^2$; and it commutes with the complex conjugation, because it fixes $i$ and permutes the units with real coefficients. Applying $z^{-1}$ to the spacetime equation and flipping the sign of the mass yields the Daviau equation, and conversely $z$ and the reverse flip recover the other. The two formulations differ, therefore, only by the sign of the mass, the cyclic relabelling of the three space directions, and the star.

*Proof sketch (transcription of Fauser's argument).* The two equations are written term by term, the images of the four kinds of element are matched with the Daviau gradient and potential, and the two fields are identified by $z^{-1}$. The mass signs are opposite because the two equations put the mass in different slots: a right multiplication by the time vector there, the conjugation here. The star is the same conjugation in both, and $z$ carries it to itself, $z(\overline{\tilde\Psi})=\overline{z(\tilde\Psi)}$. The three operations are read off from the two displayed equations.

**What the equivalence says and does not say.** It says that the space formulation is not a different theory from the spacetime formulation, but the same theory written in the smaller algebra with a permuted space basis and the opposite mass sign. The dictionary between the corpus's own conventions and either formulation is the one of §*The Three Space Vectors and the Dictionary*; the equivalence then makes the three corpus formulations — matrix, spacetime algebra, space vectors — one formulation read three ways. It does not say which interpretation is physical, and it supplies no prediction, in keeping with the status of every equivalent rewriting in this series.

**Remark (the significance of the star).** That the two formulations are related by the star is the point of the equivalence being nontrivial. Were the star the identity, the two equations would differ only by a basis relabelling and a mass sign, and the equivalence would be trivial. The star is a genuine automorphism of the algebra, the corpus's complex conjugation in its sector-cutting role, and the equivalence asserts that this automorphism, together with a cyclic relabelling, is the whole of the difference between the two pictures.

## The Right Action and the Bi-module Reading

The equation multiplies the field on the left, through the gradient and the coupling, and on the right, through the fixed bivector, at the same time. The two multiplications commute, because the algebra is associative: $\mathfrak D\bigl(\tilde\Psi(-\vec e_x)\bigr)=(\mathfrak D\tilde\Psi)(-\vec e_x)$. Fauser reads this as an action of the algebra on itself on both sides at once. The corpus develops that interpretation in *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, where the two actions are exhibited as the two commuting regular representations inside the endomorphism algebra, and where it is shown that the enveloping algebra $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}^{\mathrm{opp}}$ is the natural home of the pair.

The physical point the corpus records is that the left-versus-right question of *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* is not, at the algebraic level, a choice between two theories. Daviau's equation uses both sides at once, and it is a Dirac equation. What the two sides say is that both multiplications are available and that they commute; what they do not say is which one carries which physical degree of freedom. Fauser's further caution, recorded in the paper, is that attempts to identify the right multiplication with the iso-spin degree of freedom are not warranted by the algebra alone. The corpus records the caution and does not pursue it here.

## Open Questions

1. **Chirality.** The field is a general element, and it carries both values of the subscript. Whether the right multiplication by $-\vec e_x$, composed with the conjugation, agrees with the corpus's chirality — the cell $-iR_{\vec e_z}$ of the axis-free frame — is not answered by the equation. The corpus's *The Reflection and the Rotation in Biquaternionic Form* records that the algebra of three space vectors does not single out a chirality by itself; the cell belongs to a frame.

2. **The odd element.** The right factor is even in both parities. The elements that change parity between the two readings are the three space vectors, odd in the formulation and even in the spacetime reading. Which parity is the physical one, and does the corpus's sector split select it?

3. **The four options of Parra.** Daviau's equation is one of four inequivalent forms of the real Dirac equation recorded by Parra. Which option is it, and how do the other three read in the corpus's conventions? This is the subject of the companion article *Parra's Four Options of the Dirac Equation and the Discrete Symmetries*.

4. **The conjugation and the corpus's real structures.** The star is the corpus's complex conjugation $\bar{\cdot}$. The corpus's other antilinear structure is $\flat=-{}^{*}$, the algebra's real structure, used for the retired antilinear mass. Are the two related by the identification of §*The Three Space Vectors and the Dictionary*, and does the mass term $m\overline{\tilde\Psi}$ have an interpretation as a pairing with a conjugate in the sense of *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*?

5. **Empirical contact.** None is claimed. The formulation is an equivalent rewriting, and the question, as everywhere, is whether it makes a structural fact of the framework easier to see, not whether it predicts anything new.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

No gamma symbol is used in the body of this article; the five appear here for reference, as cells of the full operator algebra. They are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$. The first is the odd cell of the Dirac adjoint, the $\beta$ of the Hamiltonian frame; the last is the chirality cell.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The formulation writes the Dirac equation as one equation for a general element $\tilde\Psi$ of $\mathbb{B}$: a cyclically permuted gradient, a potential in the same basis, a fixed right bivector and a conjugate-linear mass. The three space vectors of the source are the Hermitian units $i\vec e_x$, $i\vec e_y$, $i\vec e_z$; their product is the central imaginary $i$; and the eight real functions of the source's field are the eight real coordinates of $\tilde\Psi$ on the real basis $e_t$, $i\vec e_k$, $\vec e_k$, $i$. The map is exact and carries no free choice.

The star of the source is the corpus's complex conjugation $\bar{\cdot}$, not the Hermitian conjugation ${}^{*}$. On the eight real units it fixes $e_t,\vec e_x,\vec e_y,\vec e_z$ and negates $i,i\vec e_x,i\vec e_y,i\vec e_z$, which is the definition of the complex conjugation. It is outer, and no multiplication by a fixed element implements it. This is the article's main algebraic point, and it is exact.

The equation is two-sided: the gradient and the coupling multiply on the left, the fixed bivector $-\vec e_x$ on the right. It is not the corpus's two-sided equation, because its right factor is a fixed bivector and not Kravchenko's mass direction, and because its mass is the conjugation. It is the space-formulation face of the chiral pair.

The formulation is an equivalent rewriting and carries no new physics. Its value is the dictionary, which is exact, and the three places it assigns: the space directions are the Hermitian units, the mass is the complex conjugation, and the right action is a fixed bivector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $i\vec e_x$, $i\vec e_y$, $i\vec e_z$ | The three space vectors of the formulation; squares $+e_t$, pairwise anticommuting |
| $i$ | The pseudoscalar of the formulation; the corpus's central imaginary |
| $e_t$, $i\vec e_k$, $\vec e_k$, $i$ | The eight real units the map uses |
| $\tilde\Psi$ | The field, a general element of $\mathbb{B}$ |
| $a,\dots,h$ | The eight real functions of the field |
| $\tilde\Psi=a\,e_t+d\,i\vec e_x+b\,i\vec e_y+c\,i\vec e_z-e\,\vec e_x+f\,\vec e_y-g\,\vec e_z+h\,i$ | The Daviau map, on the eight real units |
| $\overline{\tilde\Psi}$ | The star of the source: the corpus's complex conjugation, not ${}^{*}$ |
| $\mathfrak D=e_t\partial/\partial Q_t+i\vec e_y\partial/\partial Q_x+i\vec e_z\partial/\partial Q_y+i\vec e_x\partial/\partial Q_z$ | The cyclically permuted gradient |
| $\tilde A=A_t\,e_t+A_x\,i\vec e_y+A_y\,i\vec e_z+A_z\,i\vec e_x$ | The potential in the same basis |
| $\mathfrak D\tilde\Psi(-\vec e_x)=m\overline{\tilde\Psi}+q\tilde A\tilde\Psi$ | The Daviau equation |
| $-\vec e_x$ | The fixed right factor; a bivector, even in both parities |
| $z$ | The cyclic relabelling of the three space directions, $z^3=\mathrm{id}$ |
| $\mathbb{B}$ | The biquaternion algebra; the algebra of the formulation |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The corpus's gradient and its quaternion conjugate |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, for the map, the star, the equivalence and the four options; the source of this article.
- C. Daviau, "Équation de Dirac et algèbre de Clifford," *Annales de la Fondation Louis de Broglie*, for the space Clifford formulation in its original form.
- D. Hestenes, *Space–Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra formulation that the equivalence compares against.
- B. Fauser, "Isospin from Spin by Compositeness," arXiv:hep-th/9908015, for the alternative to the iso-spin interpretation of the right action.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html), [Element and Operator Representations: The Three Actions](element-and-operator-representations-the-three-actions.html), [The Reflection and the Rotation in Biquaternionic Form](the-reflection-and-the-rotation-in-biquaternionic-form.html), [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), and [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html).
