# __The Foldy–Wouthuysen Transformation in Biquaternionic Form__

## Introduction

The Dirac equation describes particles and antiparticles on the same footing, and its solutions mix the two. The Foldy–Wouthuysen (FW) transformation, introduced by Leslie Foldy and Siegfried Wouthuysen in 1950, is the $*$-unitary transformation that separates them. It diagonalises the Dirac Hamiltonian: one part of the field becomes the positive-frequency (particle) sector and the other the negative-frequency (antiparticle) sector. In doing so it produces the systematic expansion of the relativistic Hamiltonian in powers of $1/c$ whose leading terms are the Schrödinger and Pauli Hamiltonians. The non-relativistic reductions of this corpus are built on it, and the companion articles on the electron and on the hydrogen atom presuppose it.

The transformation is worth a biquaternion article for a structural reason. The biquaternionic Dirac equation is a **pair**: the mass couples $\tilde{Ξ}_{\mathrm{sp},L}$ to $\tilde{Ξ}_{\mathrm{sp},R}$, and the two parts are the two components that the subscripts name, under the reading fixed in *Special Element Conventions*, §*The Chirality Convention*. The FW transformation, by contrast, separates **positive from negative frequency**, and the two pieces into which it splits the field are not the two components of the pair. The article therefore keeps two splits apart. The **subscript split** is the one the mass exchanges, and in it the biquaternion pair is written. The **frame split** is the one fixed by the right multiplication of the field by $i\vec e_x$, in which the FW transformation works and the mass term is a multiple of that multiplication. Conflating the two is the standard way to misread either, and making the distinction explicit is the biquaternion content of the transformation.

**Two Dirac equations.** The corpus carries two, and they must not be read as one. The equation used here is the **one-sided** chiral pair of *Operator and Calculus Conventions*, in which the gradient acts by left multiplication and the mass couples the $L$ part of the field to the $R$ part. The **two-sided** equation is Kravchenko's, in which the time derivative and the spatial gradient act from the left, the mass acts by right multiplication through $\vec e_z$, and a componentwise conjugation supplies the antilinear part (*The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*). The two are related by Kravchenko's dictionary, a change of variable with a conjugation in the mass term, and describe the same physics in different representations. The Hamiltonian form is read off the one-sided pair, so the transformation below is stated for that pair; the two-sided equation is the same dynamics in the representation in which the analytic machinery acts. What the transformation diagonalises in either reading is the frame grading; what it leaves alone is the subscript.

The scope is the transformation itself: its generator, its free-particle closed form, the mean position operator it defines, and the interpretation of all this in the algebra. The quantised field, the Fock space and the fermionic path integral belong to the companion category *Biquaternion Quantum Fields*, and the relativistic qubit and the informational interpretation to the subcategory *focus on informational aspects*. The Pauli equation itself, and the detailed non-relativistic expansion including the Darwin and spin–orbit terms, are worked through in the companion exercise *Exercise: The Non-Relativistic Limit and the Pauli Equation* and are only summarised here.

**Conventions.** Every derivative in this article is the biquaternionic gradient of *Operator and Calculus Conventions*,

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial R_\mu},
\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial R_\mu},
\qquad
\varepsilon=(1,-1,-1,-1),
$$

with $e_t$ the identity of the algebra and $e_x,e_y,e_z$ the three pure units, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_x\vec e_y=-\vec e_y\vec e_x=\vec e_z$ and cyclic, so that $\vec e_j\vec e_\eta=-\delta_{j\eta}e_t+\epsilon_{j\eta l}\vec e_l$. Its norm is the d'Alembertian

$$
\Box=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla=\frac{\partial^2}{\partial R_t^2}+\Delta_Q ,
$$

and on the material sector, where $Q_t=i r'_t$, the two gradients and the norm read

$$
\tilde\nabla_{\Phi}=-i\,e_t\frac{\partial}{\partial r'_t}+D_3,
\qquad
(\tilde\nabla_\Phi)^{\natural}=-i\,e_t\frac{\partial}{\partial r'_t}-D_3,
\qquad
\Box\big|_{\mathbb{B}_{\Phi}}=\Delta_Q-\frac{\partial^2}{\partial {r'_t}^2},
\qquad
D_3=\sum_\eta\vec e_\eta\frac{\partial}{\partial q_\eta}.
$$

Minimal coupling shifts each derivative, $\partial/\partial R_\mu\to\partial/\partial R_\mu-\frac{iϙA_{\mu}}{\hbar}$, so the pure part becomes $D_3^A=\sum_\eta\vec e_\eta(\partial/\partial q_\eta-\frac{iϙA_{\eta}}{\hbar})$, and $\sum_\eta\vec e_\eta\pi_\eta=-i\,\hbar\,D_{3}^{A}$ with $\pi_\eta=p_\eta-ϙA_\eta$ and $p_\eta=-i\,\hbar\partial/\partial q_\eta$. The charge is $ϙ$ and the four-potential is $A_\mu=(A_0,-\vec A)$.

**The two involutions.** The reduction needs two right multiplications of the algebra, written by position. The **mass grading** and the **chirality** are

$$
\beta F=iF\vec e_x,
\qquad
\Gamma F=-iF\vec e_z=iF\omega,
\qquad
\omega=-\vec e_z,
\qquad
\omega^2=-e_t,
$$

with $\omega$ the pseudoscalar of the frame; the $i$ in front of $\omega$ is the central scalar of the algebra and not $\omega$. Both square to the identity, $\beta^2=\Gamma^2=e_t$; they anticommute, $\beta\Gamma=-\Gamma\beta$; and both commute with the gradient, which acts on the other side. The side is position: the chirality acts as $F\mapsto-iF\vec e_z$, and the left action $F\mapsto-i\vec e_zF$ is a different element, never used here. Every operator in this article is an action on the field and its side is written out: the gradient, its pure part $D_3$ and multiplication by a scalar act on the left, $\beta$ and $\Gamma$ act on the right, and the kinetic operator $O$, the generators $S_1$ and $S_2$, the free-particle involution $A$ and the mean position $X_\eta$ act on both sides, with both elements displayed wherever they appear.

**The equation.** The pair is

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$

both gradients acting from the left, with no right multiplication and no conjugation in it. The source's own equation of the transformation is a one-field equation whose operator is the gradient read with two frame factors attached, one on each side; translated once into these conventions the operator is $\tilde\nabla_\Phi$. Its square is the d'Alembertian in the source's frame factors, while the gradient's square is not scalar, so wherever a scalar square of the derivative is needed the article uses the norm $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box$. No one-field first-order equation with a mass is written anywhere below.

## The Dirac Hamiltonian and the Odd/Even Split

The FW transformation is best stated for the Hamiltonian form of the Dirac equation. The pair, read on the Dirac module $\Delta=\mathbb B$, is the equation of motion

$$i\,\hbar\,c\frac{\partial  F}{\partial  r'_t}=HF,
\qquad
HF=\beta mc^2F+OF+ϙA_0F,
\qquad
OF=c\sum_\eta\vec e_\eta\pi_kF\vec e_z=c\,(\vec\pi F)\vec e_z .
$$

The mass term is the grading itself multiplied by the mass, and the kinetic term is the pure part of the gauged gradient followed by the chirality's own right multiplication; that last factor is what makes $O$ carry the opposite sign on the two components of the pair, which is the sign the pair gives them. The relations used below are five:

$$
\beta^2=e_t,
\qquad
\beta O=-O\beta,
\qquad
\beta\,ϙA_0=ϙA_0\,\beta,
\qquad
O=O^{\dagger},
\qquad
\beta=\beta^{\dagger},
$$

so that $O$ is odd, $ϙA_0$ is even, and $H$ is Hermitian. At zero potential $H^2=m^2c^4+O^2$, and the free $O^2=c^2\vec p^2$, so the eigenvalues are $\pm\sqrt{m^2c^4+c^2\vec p^2}$, which is the mass shell of the pair. With a field $O^2/c^2=\vec\pi^2-i\,\hbar\,ϙ\,\vec B$, so the two branches are split by the Zeeman term, computed below. The square is scalar because $\beta$ anticommutes with $O$ and because the pure units multiply as $\vec e_j\vec e_\eta=-\delta_{j\eta}e_t+\epsilon_{j\eta l}\vec e_l$, the antisymmetric part of which cancels between the two orderings of a mixed derivative.

The Hamiltonian splits into an **even** part and an **odd** part,

$$
H=\beta mc^2+\underbrace{c\,(\vec\pi F)\vec e_z}_{\textstyle O}+\underbrace{ϙA_0}_{\textstyle\mathcal{E}},
$$

where even and odd are defined by conjugation with the mass grading,

$$
\beta\mathcal{E}\beta=+\mathcal{E},
\qquad
\beta O\beta=-O .
$$

The odd part $O$ is what exchanges the $+1$ and $-1$ parts of the mass grading, and hence what makes the positive- and negative-frequency sectors talk to each other. The FW transformation is the $*$-unitary transformation that removes $O$ order by order.

It is important to say at once which split this is, because several $\mathbb{Z}/2$'s are in play. Conjugation by the mass grading defines the **frame grading**, the large/small split of the Foldy–Wouthuysen transformation; it is a frame-dependent split and not one of the algebra's own gradings. It is **not** the split by the conjugation $\natural$: the kinetic operator $O$ is frame-odd and yet Hermitian, hence in $\mathbb{B}_{\Psi}$, so "odd" is not another word for "anti-Hermitian". The parity of *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form* is a third thing again.

Nor is the frame grading the subscript. The basis operator is the right multiplication $\Gamma F=-iF\vec e_z$ (*Special Element Conventions*, §*The Chirality Convention*), and it anticommutes with $\beta$; the anticommutation is a property of the pair of basis operators and is not what makes the operator a chirality. The parent article states the value as a label and computes no operator (*The Dirac Equation in Biquaternionic Form*, §*The Subscript and the Two Parts*). The central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, the difference of the two central idempotents, is a different object and defines a different split, and must not be read as this one (*Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*). The chirality is a right multiplication, an element of the algebra and not an array. The mass term is even under the frame grading, and it exchanges the $L$ part and the $R$ part: a reader who identifies "odd" with "value-changing" will misread the transformation the whole way through.

**The Hamiltonian as one factor of the grading.** The identification of $O$ as the frame-odd part is visible in the algebra. Since $\beta^2=e_t$, the kinetic operator is the grading applied to $\beta O$,

$$
O=\beta(\beta O),
\qquad
\beta O=c\sum_\eta\vec e_\eta\pi_\eta(\cdot)\vec e_y ,
$$

and $\beta O$ is the same two-sided action as $O$, with $\vec e_y$ in place of $\vec e_z$. The Hamiltonian is therefore the mass grading applied to a bracket of two pieces, $H=\beta\bigl(mc^2+\beta O\bigr)$, one even and one odd: the mass is frame-even, and $\beta O$ is frame-odd. Multiplying the even piece by the grading leaves it even; multiplying the odd piece gives back $O$ itself. After the transformation the Hamiltonian is the grading times the energy alone, so the frame-odd piece is gone from it, and that is the algebraic content of the diagonalisation.

## The Transformation and Its Generator

Let $U=\exp(iS)$, with $S=S_1+S_2+\cdots$ Hermitian so that $U$ is $*$-unitary. The letter $S$ is the FW generator here, as in the literature. The transformed Hamiltonian is

$$
H_2=UHU^\dagger-i\,\hbar\,U\frac{\partial}{\partial  r'_t}U^\dagger ,
$$

where the second term vanishes for a time-independent $S$. Since $H=\beta mc^2+O+\mathcal{E}$, the idea is to choose $S$ so that the large commutator $i[S_1,\beta mc^2]$ equals $-O$ at leading order, cancelling the odd part and leaving an even remainder of order $1/c^2$.

Expanding,

$$
UHU^\dagger=H+i[S,H]+\frac{i^2}{2!}[S,[S,H]]+\cdots ,
$$

the condition $i[S_1,\beta mc^2]=-O$ is satisfied by

$$
\boxed{\;
S_1=-\frac{i}{2\,m\,c^{2}}\,\beta O,
\qquad
S_1F=\frac{1}{2\,m\,c}\sum_\eta\vec e_\eta\pi_kF\vec e_y
\;}
$$

because $-i$ times the $i$ of $\beta$ is $+1$:

$$
-\frac{i}{2\,m\,c^{2}}\,\beta\bigl(c\vec\pi F\vec e_z\bigr)
=-\frac{i\cdot i}{2mc}\,\vec\pi F\vec e_y
=\frac{1}{2\,m\,c}\,\vec\pi F\vec e_y .
$$

Indeed $[S_1,\beta]=\frac{i}{mc^2}O$, because the right multiplication by $\vec e_y$ gives $[\vec e_\eta(\cdot)\vec e_y,\beta]=2i\vec e_\eta(\cdot)\vec e_z$ term by term, whence $i[S_1,\beta mc^2]=-O$. The remaining term is evaluated with the same anticommutation:

$$
i[S_1,O]=\frac{\beta O^2}{mc^2},
$$

because $[\beta O,O]=2\beta O^2$ when $O$ is odd.

The second-order term of the expansion is of the same magnitude and supplies the factor $\frac12$. At this order $[S_1,H]=iO+\cdots$, whence

$$
-\frac{1}{2}[S_1,[S_1,H]]=-\frac{i}{2}[S_1,O]=-\frac{i}{2}\cdot\Bigl(-\frac{i}{mc^2}\Bigr)\beta O^2
=\frac{i\cdot i}{2mc^2}\beta O^2
=-\frac{\beta O^2}{2mc^2},
$$

using $i\cdot i=-1$ once more. Collecting, the first-order term $+\beta O^2/(mc^2)$ and this one combine to the half, and the transformed Hamiltonian at this order is

$$
\boxed{\;
H_2=\beta mc^2+\mathcal{E}+\frac{\beta O^2}{2mc^2}+O_1+\cdots
\;}
$$

The odd remainder is fixed by the same commutator, applied to the potential rather than to the mass:

$$
O_1=i[S_1,\mathcal{E}]=\frac{\beta}{2mc^2}\,[O,\mathcal{E}],
$$

which is odd, since $[O,\mathcal{E}]$ is odd and $\beta$ is even, and of relative order $v^2/c^2$ compared with $O$. It is removed by the second generator

$$
S_2=-\frac{i}{2\,m\,c^{2}}\beta O_1 ,
$$

odd like $S_1$, and by the same computation as for $S_1$, with $O_1$ in place of $O$, it gives $i[S_2,\beta mc^2]=-O_1$. Every generator is odd under the grading for the same reason: it enters the transformed Hamiltonian only through the commutator with $\beta mc^2$, and only an odd generator produces an odd term there. The price of the second step is a new odd remainder $O_2$, smaller by two powers of $v/c$, which the next generator removes in turn. Explicitly, $[O,\mathcal{E}]F=i\,\hbar\,c\,ϙ\,\vec E\,F\,\vec e_{z}$ and

$$
S_2F=\frac{\hbar\,ϙ}{4\,c^{3}\,m^{2}}\,(\vec EF)\vec e_z ,
$$

odd, as every generator is. For the free particle $O=c\vec p$, $\mathcal{E}=0$, so $O_1=0$ and $O^2=c^2\vec p^2$; then $O^2/(2mc^2)=\vec p^2/(2m)$ and

$$
H_2=\beta\Bigl(mc^2+\frac{\vec p^{2}}{2\,m}-\frac{\vec p^4}{8m^3c^2}+\cdots\Bigr),
$$

whose first two terms are the free-particle Schrödinger Hamiltonian on the $+1$ part of the mass grading and its negative on the $-1$ part, and whose $\vec p^4$ term is the first relativistic correction to the kinetic energy. The expansion is in powers of $(\vec p/mc)^2$, i.e. in $v^2/c^2$; the residual odd terms are smaller by two powers of $v/c$.

The generator has a transparent physical meaning in the algebra. The operator $\beta O$ is the piece of the Hamiltonian that exchanges the $+1$ and $-1$ parts of the mass grading. The generator $S_1=-\frac{i}{2\,m\,c^{2}}\beta O$ is proportional to it, and it anticommutes with $\beta$: the generator is frame-odd, and the transformation it generates does not leave the grading fixed. It is the rotation whose angle measures how much mixing of the two frequency parts the kinetic term produces. For a slowly moving particle the angle is small and the transformation is close to the identity; in the ultra-relativistic regime the expansion breaks down, which is the signal that the non-relativistic separation is no longer meaningful.

It is worth recording why one generator is not enough. With $U=e^{iS_1}$ taken exactly, the odd remainder $O_1$ survives: the leading generator removes the leading odd term and nothing more. The generator is a series, $S=S_1+S_2+\cdots$, and each term removes one order. The free particle is the exception, and the next section is about it: there the series terminates and a single closed-form exponential does the whole job at once.

### The Second Transformation and the Iteration

The odd remainder of the first step is $O_1$, of relative order $v^2/c^2$ compared with $O$. The same algorithm applied to it removes it, with the generator displayed above, and leaves a new odd remainder of relative order $v^4/c^4$; call that one $O_2$, and continue. The procedure iterates: at each stage the odd part of the next order is conjugated away by a generator proportional to it, and the new odd residual is two powers of $v/c$ smaller. The resulting expansion of the transformed Hamiltonian is the systematic $1/c$ expansion of the Dirac theory, and its convergence criterion is the physically transparent one,

$$
\frac{|\vec\pi|}{mc}\ll1 ,
$$

i.e. particle momenta small compared with $mc$. The criterion is usually quoted as $v\ll c$, and that is right as a limit and wrong as an equality: the two quantities are not proportional, and $\lvert\vec\pi\rvert=mc$ is $v=c/\sqrt{2}$, not $v\to c$, since $v/c=\lvert\vec\pi\rvert/\sqrt{\vec\pi^{2}+m^{2}c^{2}}$. The radius of the free binomial series is that point and not the whole of $v<c$. When the criterion fails the iteration still exists term by term but no longer converges to a useful separation: the notion of a particle part is momentum-dependent and becomes meaningless in the ultra-relativistic regime.

Two features of the iteration are worth keeping in view. First, the transformation is **asymptotic, not exact**, unless the theory is free, or the background has a special symmetry: the series is what the non-relativistic limit means. Second, the even terms are not unique as operators until the ordering of the non-commuting factors is fixed — $\vec E$ and $\vec\pi$ do not commute, so the spin term and the kinetic term do not either, and only the Hermitian, symmetrised combination is physical. The biquaternion framework reads the first feature as the statement that the frame grading is only approximately aligned with the dynamics, and the second as the statement that the kinetic operator multiplies the field on both sides, so it is the field's own non-commutativity that the ordering ambiguity expresses.

## The Free Particle in Closed Form

For the free particle the transformation can be written exactly, and the exact form is the cleanest check that the expansion above is right. With $\vec u_p$ the unit vector along $\vec p$ and

$$
AF=i\vec u_pF\vec e_y,
\qquad
A^2=-e_t,
\qquad
\beta A=-A\beta,
\qquad
\theta=\arctan\frac{|\vec p|}{mc},
$$

the $*$-unitary

$$
U=\cos\frac{\theta}{2}+A\sin\frac{\theta}{2}=\exp(A\theta/2)
$$

brings the Hamiltonian to diagonal form. The verification is short. Since $\beta A=-A\beta$, conjugation by $U$ acts as

$$
U\beta U^\dagger=\beta\exp(-A\theta),
$$

while $A$ commutes with $U$ and is unchanged. Writing

$$
H=\beta mc^2+c|\vec p|\,\beta A=\beta\,(mc^2+c|\vec p|A),
$$

where $c|\vec p|\,\beta A=c\sum_\eta\vec e_\eta p_\eta(\cdot)\vec e_z=O$ follows from $p_\eta=|\vec p|u_\eta$ and $\beta A=\sum_\eta\vec e_\eta u_\eta(\cdot)\vec e_z$, one has

$$
H=\beta E(\cos\theta+A\sin\theta)=\beta E\exp(A\theta),
$$

with

$$
E=\sqrt{\vec p^2c^2+m^2c^4},
\qquad
\cos\theta=\frac{mc^2}{E},
\qquad
\sin\theta=\frac{c|\vec p|}{E},
$$

and $\exp(A\theta)=\cos\theta+A\sin\theta$ because $A^2=-e_t$. Therefore

$$
\begin{aligned}
UHU^\dagger
&=\exp(A\theta/2)\,\beta E\exp(A\theta)\exp(-A\theta/2)\\
&=\beta E\exp(-A\theta/2)\exp(A\theta)\exp(-A\theta/2)\\
&=\beta E,
\end{aligned}
$$

that is, $UHU^\dagger=\beta\sqrt{\vec p^2c^2+m^2c^4}$ exactly. In this language the exact generator is $S=S_1\,\theta/\tan\theta$, since $S_1=-\tfrac{i}{2}A\tan\theta$ and $iS=\tfrac{1}{2}A\theta$; it reduces to $S_1$ as $\theta\to0$; the factor $\theta/\tan\theta\le1$ is the whole of the relativistic correction to the non-relativistic generator. The $+1$ part of $\beta$ is the relativistic energy $+E$, the $-1$ part is $-E$, and the odd part has been removed to all orders. The leading expansion of the closed form reproduces the result of the previous section:

$$
\beta E=\beta\Bigl(mc^2+\frac{\vec p^{2}}{2\,m}-\frac{\vec p^4}{8m^3c^2}+\cdots\Bigr),
$$

the $\vec p^4$ term being the first relativistic correction to the kinetic energy. The closed form was checked numerically: with $\tan\theta=|\vec p|/(mc)$ and $U=\cos(\theta/2)+A\sin(\theta/2)$, the identity $UHU^\dagger=\beta E$ holds to machine precision, at the $10^{-15}$ level for a generic three-momentum and every value of $|\vec p|/(mc)$ tested.

**The exact form is not a differential operator.** That the identity holds exactly is a statement about the algebra, not about locality. The symbol of $\beta\sqrt{\vec p^{2}c^{2}+m^{2}c^{4}}$ is $\sqrt{k^{2}c^{2}+m^{2}c^{4}}$, which is not a polynomial in $k$ at any order, so the operator is of infinite order: written in position space it has a kernel that does not vanish off the diagonal. In one dimension the kernel is elementary,

$$
\mathcal{K}(x)=\int\!\frac{dp}{2\pi\hbar}\;\sqrt{p^{2}c^{2}+m^{2}c^{4}}\;e^{ipx/\hbar}=-\dfrac{m\,c^{2}K_{1}(k_m\lvert x\rvert)}{\pi\lvert x\rvert},
$$

non-zero at every $x\neq0$ and decaying only over the reduced Compton wavelength $\dfrac{1}{k_m}$. The closed form separates the distributional part with $\frac{1}{\pi}\int_0^{\infty}k\cos(kx)\,dk=-\frac{1}{\pi x^{2}}$, what remains being conditionally convergent, and the integral was checked against it to twenty-five digits at $k_m\lvert x\rvert=0.5,1,2,3$. In three dimensions the kernel is more singular at coincidence rather than less, the difference $\sqrt{p^{2}c^{2}+m^{2}c^{4}}-pc$ falling off only as $\dfrac{m^{2}c^{3}}{2\,p}$, whose angular integral diverges. The transformation therefore trades one property for another: the Dirac Hamiltonian is local and not block-diagonal, its exact Foldy–Wouthuysen image is block-diagonal and not local, and only the truncated polynomial $\beta mc^{2}+\beta\vec p^{2}/(2m)$ is both. Locality belongs to the two ends of the chain, not to the middle. Nothing here contradicts the closed form above; it says what the closed form costs. The mean position operator below is the same non-locality read on the coordinate instead of on the Hamiltonian, since the operator that is blind to the trembling cannot itself be a multiplication by $\vec x$.

## The Mean Position Operator

The transformation does more than diagonalise the Hamiltonian: it also changes which operator plays the role of position. Write the position as the material vector $\vec q=\sum_\eta Q_\eta\vec e_\eta$, with $Q_\eta$ the operator of multiplication by the coordinate. In the transformed frame that multiplication is the coordinate, so the operator carrying it back to the original frame is obtained by conjugating with $U^\dagger$, not with $U$:

$$
\vec X=U^\dagger\vec q\,U=\vec q-i[S_1,\vec q]-\frac{1}{2}[S_1,[S_1,\vec q]]+\cdots .
$$

The direction of the conjugation is the content of the definition. The other ordering, $U\vec q\,U^\dagger$, is the original coordinate read in the transformed frame, and it keeps the trembling; $U^\dagger\vec q\,U$ is the coordinate whose image in the transformed frame is plain multiplication.

The correction to each component is fixed by one commutator with the momentum. Since the right multiplication by $\vec e_y$ commutes with multiplication by a coordinate and $[\pi_\eta,Q_\eta]=-i\,\hbar$,

$$
[S_1,Q_\eta]F=-\frac{i}{2\,k_m}\,\vec e_\eta F\vec e_y,
\qquad
-i[S_1,Q_\eta]F=\frac{i^{2}}{2\,k_m}\,\vec e_\eta F\vec e_y
=-\dfrac{1}{2\,k_m}\,\vec e_\eta F\vec e_y,
$$

where $i\cdot i=-1$ once more. Hence

$$
\vec X=\sum_\eta X_\eta\vec e_\eta,
\qquad
X_kF=Q_kF-\dfrac{1}{2\,k_m}\,\vec e_\eta F\vec e_y+\cdots .
$$

The correction is of the order of the half reduced Compton wavelength $\dfrac{1}{2\,k_m}$ — the Zitterbewegung amplitude — and the next correction is of order $1/m^2$. The exact closed form of the previous section gives the same leading term: differentiating $\theta$ and differentiating $\vec u_p$ contribute two pieces whose dependence on $\vec u_p$ cancels, so the sum is the single operator $\vec e_\eta(\cdot)\vec e_y$, and the residual against $U^\dagger\vec q\,U$ is of order $1/m^2$. The operator $\vec X$ is the **mean position** (Foldy–Wouthuysen position). Its defining property is that its Heisenberg velocity,

$$
\frac{d\vec X}{dr'_t}=\frac{i}{\hbar}[H,\vec X]=U^\dagger\Bigl(\beta\frac{\vec pc^2}{E}\Bigr)U,
$$

commutes with $H$ and therefore has no oscillatory part: in the transformed frame it is exactly the classical drift $\beta\vec pc^2/E$, and the rapid trembling of the ordinary position operator is entirely contained in the difference

$$
\vec q-\vec X=\dfrac{1}{2\,k_m}\sum_\eta\vec e_\eta(\cdot)\vec e_y+\cdots .
$$

The step in the middle is one line: $UHU^\dagger=\beta E$ makes $[H,\vec X]=U^\dagger[\beta E,\vec q]U$, and $[E(\vec p),\vec q]=-\frac{i\,\hbar\,c^{2}\,\vec p}{E}$ on a function of the momentum alone, so no derivative of the field enters. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

In the biquaternion language, the trembling is a rotation of the field between the two frames of the algebra, and the mean position is the coordinate that is blind to it. The companion article *Zitterbewegung in Biquaternionic Form* records the same conclusion from the side of the oscillation; here it appears as a property of the mean position.

The correction $\dfrac{1}{2\,k_m}\vec e_\eta(\cdot)\vec e_y$ is itself worth reading in the algebra. It is a frame-odd displacement: it anticommutes with $\beta$, as the generator does, and it is the first term in the expansion of the mean position in powers of $1/m$. It is not a measurement of the particle's size; it is the statement that the coordinate conjugate to the diagonal Hamiltonian is not the coordinate conjugate to the original field. The operator $\vec X$ does not have commuting components, and it is not Lorentz covariant in the naive sense — the Newton–Wigner operator is the covariant completion of it — a fact already visible in the biquaternion framework as the difference between a material position $\vec q$ and a configuration-space position on the module.

## The Biquaternion Reading

The transformation can now be located in the two splits of the algebra, and the location is the content of the article.

**The subscript is where the biquaternion pair lives.** The massive biquaternionic Dirac equation is the pair $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$. The mass term of the Hamiltonian is $mc^2\beta$, and $\beta$ multiplies on the right by the element $\vec e_x$, which anticommutes with the chirality's $\vec e_z$; so $\beta$ reverses the value. The kinetic operator multiplies on the right by $\vec e_z$ and keeps the value. A left multiplication by a pure unit does neither: it commutes with the chirality and therefore preserves the value, and so does a right multiplication by $\vec e_z$. Only a right multiplication by $\vec e_x$ or $\vec e_y$ reverses the value. In this form the mass reverses the value and the kinetic operator keeps it; in the gradient pair of the reference article the same mass is the central coefficient $k_m$, which multiplies on the left and keeps the value. It is one coefficient read on the two sides, and the two displays are two forms of one mass, not two masses.

**The frame split is where the FW transformation works.** Conjugation by $\beta$ separates the mass from the kinetic term: the mass term commutes with $\beta$, and $O$ anticommutes with it. The fixed $*$-unitary of the frame is $F\mapsto Fw$ with $w=\frac{1}{\sqrt2}(i\vec e_x-i\vec e_z)$; it is its own inverse, $w^2=e_t$, and it conjugates $\beta$ into $\Gamma$ and back. The FW transformation is the momentum-dependent completion of that exchange: it conjugates the field so that the mass, which reverses the value, becomes the term that commutes with the mass grading, while the kinetic term, which keeps the value, becomes the first-order perturbation. Removing the odd part is exactly the statement that the mass is the large term and the mixing is small.

**The transformation does not separate the two values.** After the transformation the Hamiltonian commutes with $\beta$, and it does not commute with the chirality. The chirality in the transformed frame is momentum-dependent:

$$
\Gamma^{\mathrm{FW}}=U\Gamma U^\dagger=\Gamma\cos\theta-C\sin\theta,
\qquad
C=\Gamma A=\sum_\eta\vec e_\eta u_\eta(\cdot)\vec e_x .
$$

$C$ is even, and on the $+1$ part of $\beta$ it is $-i\sum_\eta\vec e_\eta u_\eta$, so the even part of the chirality reads $i\sin\theta\sum_\eta\vec e_\eta u_\eta$ — the helicity, with $\sin\theta=|\vec p|c/E$: the value for a massless field, reduced by that factor for a massive one. The part that anticommutes with $\beta$ is $\Gamma\cos\theta=(mc^2/E)\Gamma$, and that is the term that exchanges the two values, of relative order $m/|\vec p|$ in the ultra-relativistic regime. The FW transformation therefore separates **positive from negative frequency**, the two values of the mass grading, and not $L$ from $R$. In the algebra, the split it diagonalises is the split by $\beta$, the reflection of *The Reflection and the Rotation in Biquaternionic Form*; the subscript is read by $\Gamma$, a different reflection, and no $*$-unitary rotation of the field can diagonalise both at once because $\beta\Gamma=-\Gamma\beta$. The two splits are complementary, and the mass is the object that measures their incompatibility.

**The generator is frame-odd.** The FW generator $S_1=-\frac{i}{2\,m\,c^{2}}\beta O$ is the kinetic operator preceded by the grading, and it anticommutes with $\beta$. Conjugation by $\beta$ therefore reverses the sign of $S_1$, and the generator does not leave the grading fixed: since $U=\exp(iS_1)$,

$$
U\beta U^{\dagger}=\beta\exp(-2iS_1).
$$

The biquaternion content it carries is not a new rotation of the frame but the identification of the odd part $O$ with the frame-odd mixing term and of the mass with the frame-even large term. This is consistent with the reflection article's finding that the frame is required to state the two values and parity: the FW transformation needs the frame for the same reason.

## The Pauli Limit and the Residual Terms

With an external electromagnetic field, $\pi_\eta=p_\eta-ϙA_\eta$, and the FW-transformed Hamiltonian acquires the standard non-relativistic terms. The kinetic term is where the spin enters, through the product of the pure units combined with the non-commutativity of the momentum components. Two pure units multiply into a scalar and a spin element,

$$
\vec e_j\vec e_\eta=-\delta_{j\eta}e_t+\epsilon_{j\eta l}\vec e_l ,
$$

and the antisymmetric part contracts with the commutator of the momenta and survives:

$$
O^2=c^2\bigl(\vec\pi^2-i\,\hbar\,ϙ\,\vec B\bigr),
\qquad
[\pi_j,\pi_\eta]=i\,\hbar\,ϙ\,\epsilon_{j\eta l}\,B_{l},
\qquad
\vec B=\sum_l B_l\vec e_l .
$$

The left multiplication by $i\vec e_l$ commutes with $\beta$, so the spin terms are frame-even, and $\frac{\beta O^2}{2mc^2}$ already contains the Zeeman coupling $-\frac{\hbar\,ϙ}{2\,m}i\vec B$ with the gyromagnetic factor $g=2$. The second transformation, with the generator $S_2$ above, adds the terms of relative order $v^2/c^2$. To this order the effective Hamiltonian on the $+1$ part of the mass grading is the Pauli Hamiltonian

$$
\boxed{\;
\begin{aligned}
H_{\mathrm{Pauli}}
&=\frac{\vec \pi^{2}}{2\,m}+ϙA_0-\frac{\hbar\,ϙ}{2\,m}\,i\vec B\\[2pt]
&\quad-\frac{\hbar\,ϙ}{4\,m^{2}\,c^{2}}\,i(\vec E\times\vec\pi)
+\frac{1}{8\,k_m^{2}}\nabla^2(ϙA_0),
\end{aligned}
\;}
$$

whose terms beyond the leading kinetic and electrostatic ones are the spin–Zeeman term, the spin–orbit coupling and the Darwin term — the coefficient $1/(4m^2c^2)$ of the spin–orbit term already contains the Thomas factor of $\frac12$ — together with the relativistic kinetic correction $-\bigl(\vec\pi^2-i\,\hbar\,ϙ\,\vec B\bigr)^2/(8m^3c^2)$, which is the field version of the free term $-\vec p^4/(8m^3c^2)$ displayed above. The square is taken of $O^2/c^2=\vec\pi^2-i\,\hbar\,ϙ\,\vec B$ rather than of $\vec\pi^2$, because the two differ by the Zeeman term and it is the operator the transformation actually produces. The companion exercise *Exercise: The Non-Relativistic Limit and the Pauli Equation* derives each in the biquaternion framework; they are quoted here as the standard content of the transformation. For the electrostatic case $\vec E=-\nabla A_0$, the Darwin term has the equivalent forms

$$
\frac{1}{8\,k_m^{2}}\nabla^2(ϙA_0)=-\frac{ϙ}{8\,k_m^{2}}\nabla\cdot\vec E .
$$

The point to record is structural: every correction is **even** under the frame grading — each is a scalar or a spin–magnetic coupling, and none exchanges the two frequency parts — which is the statement that the transformation has succeeded in removing the odd part to the stated order. The residual odd terms, suppressed by a further factor of $v^2/c^2$ relative to $O$, are removed by $S_2$.

The $-1$ part is the same Hamiltonian with the sign of the mass grading reversed: it is $-E=-mc^2-\vec\pi^2/(2m)+\cdots$, the mirror image of the $+1$ part, separated from it by the mass gap $2mc^2$. Factoring out the rest-energy phase, as the companion article does, gives the antiparticle Hamiltonian: the same kinetic and spin terms, and the opposite charge, so that the potential term is $-ϙA_0$. That sign reversal is charge conjugation, and it is what the two sectors differ by once the rest energy is removed. This is the sense in which the FW transformation separates particles from antiparticles: not by splitting the field into two pieces that never talk, which the fields do not allow, but by diagonalising the Hamiltonian so that the gap is manifest and the mixing is small.

## What Is Standard and What the Algebra Adds

The transformation, the generator $S_1$, the leading Hamiltonian $\beta mc^2+\beta O^2/(2mc^2)$, the closed free-particle form $\beta E$, the mean position operator and the Pauli limit are all standard results, transcribed here from the relativistic-quantum-physics literature and cited as such. The biquaternion contribution is not a new formula but a placing:

- The **two splits** are kept distinct. The FW transformation diagonalises the frame grading (large/small, $\beta$); the biquaternion mass pair is the subscript ($L$/$R$, read by $\Gamma$). The two anticommute, so the transformation cannot diagonalise both, and the mass is the obstruction.
- The **mass term** appears in the transformation as the large, frame-even term whose diagonal form is the non-relativistic gap; under the subscript the same mass is the term that exchanges the $L$ part and the $R$ part. The passage between the two descriptions starts from the fixed $*$-unitary $F\mapsto Fw$, $w=\frac{1}{\sqrt2}(i\vec e_x-i\vec e_z)$, that conjugates $\beta$ into $\Gamma$, and the FW transformation is its momentum-dependent completion.
- The **residual odd part** is the frame-odd mixing term $O$, and its removal order by order is the statement that positive and negative frequency decouple in the non-relativistic limit.
- The **exact free form** shows that the separation, for a free field, is exact: $UHU^\dagger=\beta\sqrt{\vec p^2c^2+m^2c^4}$ with $U=\exp\bigl(\frac{\theta}{2}A\bigr)$, $AF=i\vec u_pF\vec e_y$ and $\tan\theta=|\vec p|/(mc)$. The expansion used by the non-relativistic reduction is the expansion of this closed form in $|\vec p|/(mc)$.

The transformation was constructed here with the large term being the mass. If an external potential dominates, the same algorithm is applied with a different even large term, and the generator changes accordingly; the algebra reads this as a different choice of frame. The choice of frame is the physical input, and the rest is the rotation that aligns the odd part with it.

## Summary

The Foldy–Wouthuysen transformation is the $*$-unitary $U=\exp(iS)$ that diagonalises the Dirac Hamiltonian in the frame grading, separating the positive- and negative-frequency parts. With

$$
H=\beta mc^2+O+\mathcal{E},
\qquad
OF=c\,(\vec\pi F)\vec e_z,
$$

and $O$ odd under conjugation by the mass grading $\beta F=iF\vec e_x$, the leading generator is

$$
S_1=-\frac{i}{2\,m\,c^{2}}\beta O,
\qquad
S_1F=\frac{1}{2\,m\,c}\sum_\eta\vec e_\eta\pi_kF\vec e_y,
$$

and the transformed Hamiltonian through order $v^2/c^2$ is

$$
H_2=\beta mc^2+\mathcal{E}+\frac{\beta O^2}{2mc^2};
$$

in the free case $\mathcal{E}=0$ this is the Schrödinger Hamiltonian on the $+1$ part and its negative on the $-1$ part. For the free particle the transformation is exact:

$$
U=\cos\frac{\theta}{2}+A\sin\frac{\theta}{2},
\qquad
AF=i\vec u_pF\vec e_y,
\qquad
\tan\theta=\frac{|\vec p|}{mc},
$$

$$
\boxed{\;UHU^\dagger=\beta\sqrt{\vec p^2c^2+m^2c^4}\;},
$$

checked to machine precision by direct computation. The mean position is the operator whose image in the transformed frame is multiplication by the coordinate,

$$
\vec X=U^\dagger\vec q\,U=\sum_\eta X_\eta\vec e_\eta,
\qquad
X_kF=Q_kF-\dfrac{1}{2\,k_m}\,\vec e_\eta F\vec e_y+\cdots ,
$$

whose Heisenberg velocity commutes with the Hamiltonian and so has no trembling term; the Zitterbewegung resides in the difference $\vec q-\vec X$.

The biquaternion interpretation turns on two splits that must not be conflated. The frame grading, conjugation by $\beta$, is what the FW transformation diagonalises and in which the mass term is a multiple of the grading; the subscript, read by the chirality $\Gamma F=-iF\vec e_z$, is where the biquaternion mass pair is written and in which the mass exchanges $L$ and $R$. The two anticommute, so no single $*$-unitary diagonalises both, and the mass term is the measure of their incompatibility. The FW generator is frame-odd: it anticommutes with $\beta$, and the transformation it generates does not leave the grading fixed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ | Hermitian ($+$) and anti-Hermitian ($-$) sectors; $\mathbb{B}_{\Phi}$ is the material sector |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial R_\mu$ | Biquaternionic gradient; every derivative in the article |
| $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\partial/\partial R_\mu$ | Its conjugate, $\varepsilon=(1,-1,-1,-1)$ |
| $\Box=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\partial^2/\partial R_t^2+\Delta_Q$ | The d'Alembertian, $\Delta_Q-\partial^2/\partial {r'_t}^2$ on the material sector |
| $D_3=\sum_\eta\vec e_\eta\partial/\partial q_\eta$ | Pure part of the gradient; $D_3^A$ its minimally coupled form |
| $\beta F=iF\vec e_x$ | Mass grading, the right multiplication by $i\vec e_x$; $\beta^2=e_t$ |
| $\Gamma F=-iF\vec e_z=iF\omega$ | Chirality, the right multiplication by $-i\vec e_z$; $\omega=-\vec e_z$ is the pseudoscalar, $\omega^2=-e_t$ |
| $\beta\Gamma=-\Gamma\beta$ | The two involutions anticommute; no $*$-unitary diagonalises both |
| $OF=c(\vec\pi F)\vec e_z$ | Odd (frame-anticommuting) kinetic operator; $O=O^\dagger$ |
| $\mathcal{E}=ϙA_0$ | Even part; left multiplication by the scalar $ϙA_0$ |
| $H = \beta mc^2 + O + \mathcal{E}$ | Dirac Hamiltonian, odd/even split |
| $U = \exp(iS)$ | Foldy–Wouthuysen $*$-unitary |
| $S_1=-\frac{i}{2\,m\,c^{2}}\beta O$ | Leading FW generator; its action is $\frac{1}{2\,m\,c}\sum_\eta\vec e_\eta\pi_kF\vec e_y$ |
| $O_1 = i[S_1,\mathcal{E}]$ | Odd remainder after the first step |
| $S_2 = -\frac{i}{2\,m\,c^{2}}\beta O_1$ | Second generator; odd, like every generator |
| $H_2 = UHU^\dagger -i\,\hbar\,U\partial/\partial r'_t\,U^\dagger$ | Transformed Hamiltonian |
| $AF=i\vec u_pF\vec e_y$ | Free-particle involution, $A^2=-e_t$, $\beta A=-A\beta$ |
| $\theta = \arctan(|\vec p|/(mc))$ | Free-particle FW angle |
| $\vec q = \sum_\eta Q_\eta\vec e_\eta$ | Material position |
| $X_kF = Q_kF-\dfrac{1}{2\,k_m}\vec e_\eta F\vec e_y+\cdots$ | Mean (Foldy–Wouthuysen) position, $k$-th component |
| $w=\frac{1}{\sqrt2}(i\vec e_x-i\vec e_z)$ | Fixed $*$-unitary of the frame, the right multiplication $F\mapsto Fw$; $w^2=e_t$, and $w\beta w=\Gamma$ |

## Further Reading

- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the transformation and the mean position operator.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the generator, the block-diagonalisation, and the non-relativistic expansion.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the Pauli limit and the spin–orbit and Darwin terms.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac Hamiltonian, the Dirac algebra and the Foldy–Wouthuysen reduction.
- L. L. Foldy, "The electromagnetic properties of Dirac particles," *Physical Review* **87** (1952) 688–693, for the mean position and its electromagnetic couplings.
- M. E. Rose, *Relativistic Electron Theory* (Wiley, 1961), for the systematic $1/c$ expansion.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the detailed treatment of the Foldy–Wouthuysen transformation and its applications.
- P. Strange, *Relativistic Quantum Mechanics* (Cambridge, 1998), for the transformation in the presence of external fields.
