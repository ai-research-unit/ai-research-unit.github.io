# __The Fourier Transform and the Proca Equation in Biquaternionic Form__

## Introduction

**The Proca subject is already three articles deep, and each of them counts something different.** *The Proca Equation: Massive Spin 1 in Biquaternionic Form* writes the equation, derives the Lorenz condition, and counts three real polarisation directions at each wave number. *Degenerate Solutions of the Biquaternionic Proca Equation* classifies the field values at which the potential loses its causal character. *Wave–Particle Duality and the Count of Degrees of Freedom* counts the rank of left multiplication by $i\tilde K_\Phi$ on the vector part and reads three off the light cone and two on it. **None of the three counts the rank of the Proca operator itself**, and that is the number this article computes.

**The operator's symbol is a four-by-four matrix, and it is the first in the corpus whose rank moves.** The Klein–Gordon symbol is one scalar, the Schrödinger symbol is one affine scalar, and the Dirac symbol is a two-by-two matrix whose rank is two wherever it does not vanish. The Proca symbol has rank four off the mass shell and rank one on it. **Three numbers follow from that single fact** — four off, one on, three in the kernel — and they are the whole of the article's content.

**The determinant is a product of two factors with different multiplicities, and the multiplicities are the physics.** In the four-component reading the symbol is $\sigma^\mu{}_\nu=(k^{2}-k_m^{2})\delta^\mu{}_\nu-k^\mu k_\nu$, whose determinant is $-k_m^{2}(k^{2}-k_m^{2})^{3}$. The cubic factor is the three polarisations of the parent's count; the single factor $-k_m^{2}$ is the longitudinal direction, and it does not vanish on the shell. **The mass is what keeps one direction out of the kernel**, and it is why the count is three and not two.

**The rank is the same for the massive and the massless field, and the difference is one membership.** On the mass shell the kernel is the Lorenz plane, three-dimensional, in both cases. The massless field's kernel contains one more direction than the Lorenz plane does — the wave number itself — and that direction is the gauge orbit. So the two fields have the same kernel dimension and different propagating counts, and the difference is whether $k^\mu$ is annihilated. **That is the frequency-space form of "the Lorenz condition is implied here and chosen there"**, and it is checked to machine precision.

**The massless limit is a failure of invertibility and not a discontinuity of the spectrum.** As $k_m\to0$ the determinant does not merely acquire a new zero: it vanishes at every wave number, so the symbol is invertible nowhere in the limit. The parent's discontinuous degrees-of-freedom count and the Stueckelberg device are the position-space faces of this one fact.

**The symbol is even in the four-wave-number, and that evenness is a structural slot.** $\sigma(-\tilde K_\Phi)=\sigma(\tilde K_\Phi)$, exactly, and the same holds for the Klein–Gordon scalar; the Dirac symbol is odd and the Schrödinger symbol is neither. The polar companion reads the evenness as the absence of a central bracket, and the variational companion reads it as the two-valued inversion of the symbol in the frequency. **The three articles of this set are three registers of one matrix.**

**The denial is stated plainly.** The transform acts on $\mathbb{B}$-valued functions and returns $\mathbb{B}$-valued functions; no material-sector field is carried to an informational-sector one. **There is no new solution and no new equation**; the equation, the Lorenz condition and the polarisations are the parents', and what is added is the rank, the multiplicity and the membership.

## Conventions

The algebra and the units are those of *Algebra and Element Conventions*, the gradient and the d'Alembertian those of *Operator and Calculus Conventions*, the four products those of *Product and Form Conventions*, the two forms those of *Norm and Pairing Conventions*, the units and the material time those of *Physics Units and Common Elements Conventions*, and the sector bookkeeping those of *Mirror Biquaternions and the Phy–Psy Switch*. The transform is the one of *Derivatives, Fields and Transforms*, whose symbol rule is quoted in derived form and not re-derived:

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi ,
\qquad
\Box_\Phi\longmapsto-\langle\tilde K_\Phi\rangle_\natural=k^{2} ,
\qquad
\tilde K_\Phi=ik_t'e_t+\vec k_\Phi ,
\qquad
k_t'=\frac{\omega}{c},
\qquad
k^{2}=k_t'^{2}-\vec k_\Phi^{2}.
$$

**The potential and its Lorenz form.** The potential is $\tilde A_\Phi=i\,a_t'e_t+\vec A$ with $a_t'$ and $\vec A$ real, and on a mode its two invariants are the four-vector $(a_t',\vec a)$ and the divergence. Write

$$
[kA]:=k_t'a_t'-\vec k_\Phi\cdot\vec a ,
$$

the material contraction of the four-wave-number with the amplitude, so that $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ has symbol $-i[kA]$ on a mode. **$[kA]$ is the Lorenz form of the amplitude**, and the sign is the one the parent's plane-wave section fixes: it finds $\mathrm{Sc}(i\tilde P_\Phi^{\natural}\tilde A_{\Phi,0})=-\frac{\omega}{c}A_t+i\vec k_\Phi\cdot\vec a$, which is $i[kA]$ with $A_t=i a_t'$.

**The symbol of the Proca operator, in the four-component reading.** The parent's component equation is $\partial_\mu F_{\mu\nu}=-k_m^{2}A_\nu$ with $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, and its symbol is the matrix

$$
(\sigma A)_\mu=\bigl(k^{2}-k_m^{2}\bigr)A_\mu-k_\mu\,[kA] ,
$$

so that the equation of motion on a mode is $\sigma A=0$. **The first term is the Klein–Gordon symbol acting on each component; the second is the rank-one piece that the Lorenz form subtracts**, and the whole article is the study of the competition between them. The biquaternion letter for the same object is $k^{2}-k_m^{2}$ less the image of $\tilde\nabla_\Phi\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\,\cdot)$, and §*The Symbol* states it once in each register.

**The overall sign is a convention and the multiplicities are not.** The corpus's series convention gives $\Box_\Phi\mapsto k^{2}$; the mostly-minus convention gives the negative. Every statement below is about a determinant's factors, a rank, or a membership, and none of the three changes under an overall sign. The sign is fixed once here and not renegotiated.

**The three denials, stated once.** First, the transform carries $\mathbb{B}$-valued functions to $\mathbb{B}$-valued functions and never exchanges sectors. Second, a symbol exists only where the coefficients are constant, which the free equation satisfies identically. Third, a Legendre transform between a field and its conjugate momentum grants no Fourier reading, and nothing below is one.

## The Symbol

**In the algebra the symbol is one number less one rank-one element.** The Proca operator is $\tilde\nabla_\Phi\,\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\,\cdot\bigr)-k_m^{2}$, and the composition of the gradient with its conjugate is $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box_\Phi$, a central scalar operator. The two pieces that compose it have the images

$$
\tilde\nabla_\Phi\,\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\,\cdot\bigr)\longmapsto-i\tilde K_\Phi\,[kA] ,
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\longmapsto-\langle\tilde K_\Phi\rangle_\natural=k^{2} ,
$$

so the symbol is $k^{2}-k_m^{2}$ less the rank-one piece $-i\tilde K_\Phi[kA]$, whose component reading is the $-k_\mu[kA]$ of the display below. **The first piece is central and the second is not**: a central scalar alone would give four equal eigenvalues and four equal directions, and the rank-one part is what breaks the four into three and one.

**In components the same matrix is displayed once and used throughout.** With the four-vector amplitude $(a_t',\vec a)$ and the four-wave-number $(k_t',\vec k_\Phi)$,

$$
\sigma=\bigl(k^{2}-k_m^{2}\bigr)\delta^\mu{}_\nu-k^\mu k_\nu ,
\qquad
k^\mu=\bigl(k_t',-\kappa_x,-\kappa_y,-\kappa_z\bigr) ,
\qquad
k_\nu=\bigl(k_t',\kappa_x,\kappa_y,\kappa_z\bigr) ,
$$

which is the display the parents use when they contract every pair with $\delta_{\mu\nu}$ and put the metric into $A_0=i a_t'$. **The matrix is real and symmetric in the material metric, so its eigenvectors are orthogonal and its eigenvalues real**, and no spectral question beyond linear algebra arises anywhere in the article.

**The field strength's symbol carries no mass, and that is where the mass sits.** $\tilde F$ has symbol the antisymmetric part of $i\tilde K_\Phi^{\natural}\tilde A$, whose components are $i(k_\mu a_\nu-k_\nu a_\mu)$ up to the polarisation normalisation of the parents. The mass enters the equation only through the $-k_m^{2}\delta$ term, so **the mass is the identity on the amplitude space**. That sentence is what §*The Kernel Is the Lorenz Plane* measures and what the variational companion uses.

## The Determinant and the Two Multiplicities

**The determinant is the product of the two factors, and its verification is exact.** Writing $m^{2}:=k^{2}-k_m^{2}$ for the repeated eigenvalue,

$$
\boxed{\;\det\sigma=-k_m^{2}\bigl(k^{2}-k_m^{2}\bigr)^{3}\;}
$$

with the eigenvalue list $\{m^{2},m^{2},m^{2},-k_m^{2}\}$. The check is direct evaluation of the determinant against the closed form, and it agrees to the printed digits:

| $k_t'$ | $k^{2}-k_m^{2}$ | eigenvalues | $\det\sigma$ | $-k_m^{2}(k^{2}-k_m^{2})^{3}$ |
| --- | --- | --- | --- | --- |
| $0.5$ | $-0.38$ | $\{-0.49,-0.38,-0.38,-0.38\}$ | $+2.68872800\times10^{-2}$ | $+2.68872800\times10^{-2}$ |
| $\sqrt{0.63}$ | $0$ | $\{-0.49,0,0,0\}$ | $0$ | $0$ |
| $1.6$ | $+1.93$ | $\{-0.49,1.93,1.93,1.93\}$ | $-3.52263793$ | $-3.52263793$ |

The wave vector is $\vec k_\Phi=(0.3,0.2,0.1)$ throughout and $k_m=0.7$, so $k_m^{2}=0.49$ and $\vec k_\Phi^{2}=0.14$.

**The cubic factor is the three polarisations and the linear factor is the longitudinal direction.** A matrix whose eigenvalues are $\{m^{2},m^{2},m^{2},-k_m^{2}\}$ says exactly that: three directions scale with the Klein–Gordon symbol and one does not. **The parent's "four components minus one constraint leaves three" is this multiplicity**, and what the article adds is that the factor the constraint removes is the linear one.

**The vanishing of the determinant is one condition and it is the mass shell.** $\det\sigma=0$ requires $k^{2}=k_m^{2}$, since $k_m\neq0$; the second factor is a constant and never vanishes for a massive field. **So the symbol is singular on one surface and nowhere else**, and the surface is the dispersion relation the parent derives by substitution. The two derivations agree and neither needs the other: the parent's is a dispersion, this one is a singularity.

**The multiplicities survive at $k_m=0$ only as a limit, and the limit is degenerate.** Setting $k_m=0$ makes the linear factor vanish identically, so the determinant is zero for every $k$ and the multiplicity structure collapses: what was a three-fold surface becomes a four-fold identity. **§*The Massless Limit Is a Failure of Invertibility* is that collapse read as a physical statement**, and it is why the massless theory is not the continuous endpoint of the massive one.

## The Rank, On and Off the Shell

**Off the shell the symbol is invertible and the kernel is empty.** At $k_t'=1$, $\vec k_\Phi=(0.3,0.2,0.1)$ and $k_m=0.7$ the singular values are $\{0.948946,\,0.37,\,0.37,\,0.191054\}$, so the rank is four and $\dim\ker\sigma=0$. **The smallest singular value is $0.191$, not small**: the symbol is comfortably invertible, and the propagator exists with no gauge ambiguity to fix.

**On the shell the rank is one.** At $k_t'=\sqrt{0.63}$ the singular values are $\{0.77,0,0,0\}$, so the rank is one and the kernel is three-dimensional. **The one surviving direction is the wave number itself**, and the three annihilated directions span the Lorenz plane. The two statements are one computation:

$$
\sigma k^\mu=-k_m^{2}k^\mu ,
\qquad
\sigma A=0\iff[kA]=0\ \text{and}\ k^{2}=k_m^{2},
$$

the first checked to $1.1\times10^{-16}$ on the shell, the second being the eigenvalue statement read as a kernel.

**The rank is a number the corpus has not yet reported for this operator.** *Wave–Particle Duality and the Count of Degrees of Freedom* reports the rank of a different map, and §*The Count, and the Two Ranks in the Corpus* sets the two side by side. **The two ranks answer different questions, and their agreement on the number three is a check rather than a duplication.**

**Off the shell nothing propagates, and that is the same statement as the dispersion relation.** The rank-four case says that $\sigma A=0$ has only the trivial solution away from $k^{2}=k_m^{2}$. **A non-zero amplitude at an off-shell wave number does not solve the equation at all**, which is the frequency-space form of the dispersion's being an equation rather than a branch choice.

## The Kernel Is the Lorenz Plane

**The kernel is three-dimensional and every vector in it satisfies the Lorenz condition.** The three null vectors of the symbol at $k_t'=\sqrt{0.63}$ give

$$
[kA]=+3.08\times10^{-17},\qquad -1.72\times10^{-17},\qquad +2.88\times10^{-17},
$$

each of unit length and each annihilated to $9\times10^{-17}$. **The kernel is the Lorenz plane**, and it is the same plane that the parent's §*The Lorenz Condition on a Plane Wave* identifies by fixing $A_t=i(c/\omega)\vec k_\Phi\cdot\vec a$.

**The two derivations of the plane are independent and they coincide.** The parent differentiates the equation, takes the scalar part, and finds $k_m^{2}S=0$. The transform reads the symbol's kernel and finds the same plane. **One is a divergence and the other is a null space**, and their agreement is the reason the constraint is not an extra condition imposed on the amplitude: it is the set of directions the operator does not see.

**The fourth direction is not annihilated, and its eigenvalue is the mass.** The wave number itself is an eigenvector with eigenvalue $-k_m^{2}$, verified to $1.1\times10^{-16}$. **So the amplitude along $k^\mu$ is not removed by the operator; it is multiplied by $-k_m^{2}$**, and the equation sets it to zero only through its coupling to the transverse part. That is what "the longitudinal mode is physical for a massive field" means in the symbol's language, and it is the exact counterpart of the massless case, where the same direction is annihilated outright.

**The polarisation count is read off the kernel and not off the rank.** Three annihilated directions and one amplified direction, and the amplified one is the direction whose removal would leave two. **The count is the kernel's dimension**, and §*The Count, and the Two Ranks in the Corpus* shows that the same sentence gives two for the massless field once the gauge orbit is subtracted.

## The Count, and the Two Ranks in the Corpus

**Two matrices, two ranks, one word.** The corpus counts degrees of freedom twice, and the two computations must be distinguished once and then never confused:

| | dof-count article | this article |
| --- | --- | --- |
| map | left multiplication by $i\tilde K_\Phi$ | the Proca symbol $\sigma^\mu{}_\nu$ |
| domain and codomain | vector part, $3\to4$ | four-vector, $4\to4$ |
| off the shell / off the cone | rank $3$ | rank $4$ |
| on the shell / on the cone | rank $2$ | rank $1$ |
| what moves | one direction joins the kernel on the cone | the whole transverse plane joins the kernel |

**The first column's rank counts how many field strengths the gradient can produce; the second counts how many amplitudes the equation leaves free.** Both report three propagating directions for the massive field, from different numbers, and the agreement is the check that neither computation has lost a factor.

**The massless column is where the two computations separate visibly.** For $k_m=0$ the symbol has rank three off the cone and one on it, and the count follows from one formula applied four times:

| field | surface | rank | $\dim\ker$ | $k^\mu$ in kernel | gauge orbit | count |
| --- | --- | --- | --- | --- | --- | --- |
| Proca | $k^{2}=k_m^{2}$ | $1$ | $3$ | no | $0$ | $3$ |
| Proca | $k^{2}\neq k_m^{2}$ | $4$ | $0$ | — | — | $0$ |
| Maxwell | $k^{2}=0$ | $1$ | $3$ | yes | $1$ | $2$ |
| Maxwell | $k^{2}\neq0$ | $3$ | $1$ | yes | $1$ | $0$ |

**Read the fourth column: it is the whole difference between the two theories.** The two fields have the same rank on their respective surfaces and the same kernel dimension, and they differ in whether the wave number belongs to the kernel. **The mass's entire effect on the rank structure is one membership**, and everything the parent says about gauge freedom follows from it.

**The count is the kernel's dimension minus the gauge orbit's dimension inside it.** For the Proca field on the shell that is $3-0=3$; for the Maxwell field on the cone it is $3-1=2$. **The formula is the corpus's, and the article uses it four times rather than asserting the answers separately**, because a count derived once from one formula cannot drift between the rows.

## The Massless Limit Is a Failure of Invertibility

**Setting the mass to zero removes the symbol's invertibility everywhere at once.** The determinant's linear factor is $-k_m^{2}$, so at $k_m=0$ the determinant vanishes identically. The approach is smooth in the numbers and singular in the structure:

| $k_m$ | $\lvert\det\sigma\rvert$ | $s_{\min}/s_{\max}$ | rank |
| --- | --- | --- | --- |
| $0.7$ | $2.083$ | $2.002\times10^{-1}$ | $4$ |
| $0.3$ | $0.7418$ | $3.403\times10^{-2}$ | $4$ |
| $0.1$ | $9.261\times10^{-2}$ | $3.704\times10^{-3}$ | $4$ |
| $0.03$ | $8.444\times10^{-3}$ | $3.325\times10^{-4}$ | $4$ |
| $0$ | $2.947\times10^{-15}$ | $1.089\times10^{-16}$ | $3$ |

The wave number is fixed at $k_t'=1.5$ with $\vec k_\Phi=(0.3,0.2,0.1)$, so no entry is near its own shell: $k^{2}-k_m^{2}$ runs from $2.035$ at $k_m=0.7$ to $2.11$ at $k_m=0$, and the determinant falls by twelve orders of magnitude while that factor moves by four per cent. **The fall is entirely the linear factor.**

**The limit is therefore not a limit of symbols.** Every $k_m>0$ gives an invertible symbol off the shell and a propagator with one pole on it. At $k_m=0$ there is no invertible point, the propagator is not defined as an inverse, and the gauge orbit appears. **That is the frequency-space form of the parent's statement that no sequence of Proca fields converges to a Maxwell field with a smooth third state**, and it is why the Stueckelberg device has to add a field rather than perturb one.

**The ratio $s_{\min}/s_{\max}$ is the quantitative version of the same statement.** It falls by fifteen orders of magnitude across the table while the rank stays four, which is the numerical signature of a matrix approaching singularity along a fixed direction: the direction is the longitudinal one, its eigenvalue is $-k_m^{2}$, and the approach is linear in $k_m^{2}$.

## The Symbol Is Even

**The Proca symbol is even in the four-wave-number, exactly.** $\sigma(-\tilde K_\Phi)=\sigma(\tilde K_\Phi)$ to machine precision, $0.00\times10^{0}$ in the largest entry difference, because both terms are quadratic: $k^{2}$ is a square and $k^\mu k_\nu$ is a product of two. **The Klein–Gordon scalar is even for the same reason, the Dirac symbol is odd, and the Schrödinger symbol is neither.**

**The parity is a slot and not a coincidence.** The gradient's symbol is $i\tilde K_\Phi$ and the Proca operator is second order, so its symbol is quadratic in that symbol; an operator of even order in a first-order symbol is even. **The evenness is therefore the statement that the Proca operator is second order**, and it is the property the polar companion turns into the absence of a central bracket and the variational companion turns into a two-valued inversion.

**Two consequences are used by the sibling articles and derived here.** First, the frequency roots come in the pair $\pm\sqrt{\vec k_\Phi^{2}+k_m^{2}}$, so the inversion of $\sigma=0$ for $\omega$ is two-valued and the particle–antiparticle pairing is the reflection $k_t'\mapsto-k_t'$. Second, the symbol cannot distinguish the sign of the energy, so no statement about a preferred sign can be a statement about the symbol. **Both are properties of an even quadratic form and neither is a property of the Proca equation in particular.**

**What the parity does not say is anything about the amplitude's sign.** The evenness is in the wave number and not in the amplitude. The amplitude's sign is the branch of the polar chart, and the two are independent. **The article states them as two because they are two.**

## Limits

**The constant-coefficient licence bounds every statement here.** The symbol is a matrix of numbers only where the coefficients are constant, which the free equation satisfies. With a connection the symbol is a matrix of operators, and the coupled companion treats that case; nothing here anticipates it.

**The rank is a count of amplitude directions and not of states.** That a direction is a state is the corpus's identification, imported by *Wave–Particle Duality and the Count of Degrees of Freedom* at its §*Limits*, and the article does not re-argue it. **What is proved here is the rank and the kernel; what is imported is the reading.**

**The four-component reading is a reading.** The Proca equation is one biquaternion equation for one element, and the four-vector is the component display that the parents use throughout. The symbol's rank is the same in the algebra and in components because the two carriers have the same real dimension, and the article claims no more than that.

**The denial, once more.** No sector is exchanged at any step. The symbol is a matrix multiplying an amplitude, the kernel is a subspace of amplitudes, and the count is a dimension. **None of the three is a statement about $\mathbb{B}_\Phi$ and $\mathbb{B}_\Psi$.**

## Open Questions

**Whether the cubic multiplicity has a reading that is not the imported one is open.** The cubic factor counts the directions the symbol scales equally, and the corpus reads those as the three polarisations. Whether the multiplicity can be identified with the count *without* the identification of a direction with a state — that is, whether the algebra alone supplies the reading — is not settled here, and the article records the import rather than hiding it.

**Whether the massless limit has a symbol at all is open.** The limit's symbol is identically zero, so the limit of the operators is not the operator of a limit theory. The Stueckelberg form is one way to make a limiting family, and whether it is the only one is the parent's question; nothing above bears on it.

**The spin-one content is not located in the symbol.** The angular-momentum current's vector-index part is the variational parent's subject, and the symbol's eigenvalues carry no spin label. Whether the eigenvalue $-k_m^{2}$ and the longitudinal polarisation are the same object under a rotation is a question the article raises and does not answer.

## Summary

The Proca operator's symbol, in the four-component reading, is $\sigma^\mu{}_\nu=(k^{2}-k_m^{2})\delta^\mu{}_\nu-k^\mu k_\nu$ with $k^{2}=k_t'^{2}-\vec k_\Phi^{2}$ and $k_t'=\omega/c$. Its eigenvalues are $\{k^{2}-k_m^{2},k^{2}-k_m^{2},k^{2}-k_m^{2},-k_m^{2}\}$ and its determinant is $-k_m^{2}(k^{2}-k_m^{2})^{3}$, verified against direct evaluation at $k_t'=0.5$, $\sqrt{0.63}$ and $1.6$ with $k_m=0.7$.

Off the mass shell the rank is four, the kernel is empty, and the symbol is invertible with smallest singular value $0.191$. On the shell the rank is one, the kernel is three-dimensional, and it is the Lorenz plane: the three null vectors satisfy $[kA]=0$ to $3\times10^{-17}$. The wave number itself is an eigenvector with eigenvalue $-k_m^{2}$, verified to $1.1\times10^{-16}$, so the longitudinal amplitude is multiplied rather than annihilated. **That is why the massive field has three polarisations and not two.**

The count is the kernel's dimension minus the gauge orbit's dimension inside it: $3-0=3$ for the Proca field on the shell and $3-1=2$ for the Maxwell field on the cone. **The two fields have the same rank and the same kernel dimension and differ in one membership** — whether $k^\mu$ is annihilated. That single fact is the frequency-space form of "the Lorenz condition is implied here and chosen there".

The massless limit is a failure of invertibility: $\lvert\det\sigma\rvert$ falls from $2.083$ to $2.9\times10^{-15}$ as $k_m$ goes from $0.7$ to $0$ at a wave number four per cent from its own shell, which is the linear factor's vanishing and nothing else. The symbol is even in the wave number to machine precision, and that evenness is the second order of the operator — read by the polar companion as an absent bracket and by the variational companion as a two-valued inversion.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$ | The four-wave number; $k_t'=\omega/c$ |
| $k^{2}=k_t'^{2}-\vec k_\Phi^{2}$ | The interval in wave numbers; the Klein–Gordon symbol |
| $k_m=mc/\hbar$ | The mass wave number; $k_m^{2}=0.49$ at $k_m=0.7$ |
| $\tilde A_\Phi=i\,a_t'e_t+\vec A$ | The potential; $(a_t',\vec a)$ its four-vector amplitude |
| $[kA]=k_t'a_t'-\vec k_\Phi\cdot\vec a$ | The Lorenz form of the amplitude; symbol of $S$ up to $-i$ |
| $\sigma^\mu{}_\nu=(k^{2}-k_m^{2})\delta^\mu{}_\nu-k^\mu k_\nu$ | The Proca symbol |
| $\{m^{2},m^{2},m^{2},-k_m^{2}\}$, $m^{2}=k^{2}-k_m^{2}$ | The eigenvalues; three transverse, one longitudinal |
| $\det\sigma=-k_m^{2}(k^{2}-k_m^{2})^{3}$ | The determinant; multiplicities $1$ and $3$ |
| rank $4$ / rank $1$ | Off the shell / on the shell |
| $L_{i\tilde K_\Phi}$ | Left multiplication by the gradient's symbol on the vector part; the dof-count article's map |

## Further Reading

- *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the equation, the Lorenz condition, the plane waves and the count of three polarisations.
- *Degenerate Solutions of the Biquaternionic Proca Equation*, for the lightlike set of the potential and the two cones.
- *Wave–Particle Duality and the Count of Degrees of Freedom*, for the rank of the gradient on the vector part and for the import of the reading.
- *The Fourier Transform and the Proca Equation in Biquaternionic Polar Variables*, for the same matrix read in the word and for the absent bracket.
- *The Fourier Transform, the Variational Principle and the Proca Equation in Biquaternionic Form*, for the quadratic form whose stationarity is $\sigma A=0$ and for the longitudinal coefficient.
- *The Fourier Transform and the Coupled Proca Equation in Biquaternionic Form*, for the symbol with a connection, where a curvature term joins the translation.
- *The Spin-One Fluid of the Biquaternion Proca Field*, for the Lorenz condition as the field's own continuity equation.
- *Derivatives, Fields and Transforms*, for the symbol rule and the transform's conventions.
- *Operator and Calculus Conventions*, for $\partial/\partial R_t=-i\,\partial/\partial r_t'$ and the sign of the d'Alembertian.
- A. Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the equation and the constraint.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 3, for the massive vector propagator and its longitudinal residue.
- S. Weinberg, *The Quantum Theory of Fields*, Volume I (Cambridge University Press, 1995), Chapter 5, for the counting of polarisations by constraint.
