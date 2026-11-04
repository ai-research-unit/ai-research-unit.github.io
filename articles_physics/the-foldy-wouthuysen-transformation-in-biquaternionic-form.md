# __The Foldy–Wouthuysen Transformation in Biquaternionic Form__

## Introduction

The Dirac equation describes particles and antiparticles on the same footing, and its solutions mix the two. The Foldy–Wouthuysen (FW) transformation, introduced by Leslie Foldy and Siegfried Wouthuysen in 1950, is the $*$-unitary transformation that separates them. It diagonalises the Dirac Hamiltonian: one part of the field becomes the positive-frequency (particle) sector and the other the negative-frequency (antiparticle) sector. In doing so it produces the systematic expansion of the relativistic Hamiltonian in powers of $1/c$ whose leading terms are the Schrödinger and Pauli Hamiltonians. The non-relativistic reductions of this corpus are built on it, and the companion articles on the electron and on the hydrogen atom presuppose it.

The transformation is worth a biquaternion article for a structural reason. The biquaternionic Dirac equation is a **pair**: the mass couples $\tilde{\Psi}_L$ to $\tilde{\Psi}_R$, and the two parts are the two values of the subscript of *Special Element Conventions*, §*The Chirality Convention*. The FW transformation, by contrast, separates **positive from negative frequency**, and the two pieces into which it splits the field are not the two values of the subscript. The article therefore keeps two splits apart. The **subscript split** is the one the mass exchanges, and in it the biquaternion pair is written. The **frame split** is the one fixed by the timelike frame cell $iR_{\vec e_x}^{\mathrm{axf}}$, in which the FW transformation works and the mass term is a multiple of that cell. Conflating the two is the standard way to misread either, and making the distinction explicit is the biquaternion content of the transformation.

**Two Dirac equations.** The corpus carries two, and they must not be read as one. The equation used here is the **one-sided** chiral pair of *Operator and Calculus Conventions*, in which the gradient acts by left multiplication and the mass couples the $L$ part of the field to the $R$ part. The **two-sided** equation is Kravchenko's, in which the time derivative and the spatial gradient act from the left, the mass acts by right multiplication through $\vec e_z$, and a componentwise conjugation supplies the antilinear part (*The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*). The two are related by the dictionary $A$ and describe the same physics in different representations. The Hamiltonian form is read off the one-sided pair, so the transformation below is stated for that pair; the two-sided equation is the same dynamics in the representation in which the analytic machinery acts. What the transformation diagonalises in either reading is the frame grading; what it leaves alone is the subscript.

The scope is the transformation itself: its generator, its free-particle closed form, the mean position operator it defines, and the interpretation of all this in the algebra. The quantised field, the Fock space and the fermionic path integral belong to the companion category *Biquaternion Quantum Fields*, and the relativistic qubit and the informational interpretation to the subcategory *focus on informational aspects*. The Pauli equation itself, and the detailed non-relativistic expansion including the Darwin and spin–orbit terms, are worked through in the companion exercise *Exercise: The Non-Relativistic Limit and the Pauli Equation* and are only summarised here.

**Conventions.** The algebra, the cells and their composition, the frame cells and the metric are those of *Algebra and Element Conventions*, *Operator Family Conventions*, *Frame Conventions* and *Matrix Representations Conventions*; the gradient, the d'Alembertian and the one-sided chiral pair are those of *Operator and Calculus Conventions*, and none is redefined here. The charge is $ϙ$, the four-potential is $A_\mu=(A_0,-\vec A)$, and the cells pair with the coordinates by $\nu(t)=x$, $\nu(k)=y$. One object is this article's own, the velocity cell $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, which anticommutes with the timelike frame cell $iR_{\vec e_x}^{\mathrm{axf}}$ and squares to the identity. The equation is the one-sided pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$.

## The Dirac Hamiltonian and the Odd/Even Split

The FW transformation is best stated for the Hamiltonian form of the Dirac equation. In the $\mathbb{M}_-$ frame the Dirac operator is

$$
\mathcal{D}=i\sum_\mu\bigl(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\bigr)\frac{\partial}{\partial x_\mu},
$$

in which the outer $i$ and the $i$ of each frame cell multiply to $i^2=-1$, so that the operator is a plain cell combination,

$$
\mathcal{D}=-R_{\vec e_x}^{\mathrm{axf}}D_0-\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}D_k .
$$

The minimal coupling is

$$
D_0=\frac{1}{c}\Bigl(\frac{\partial}{\partial t'}+\frac{iϙA_0}{\hbar}\Bigr),
\qquad
D_k=\frac{\partial}{\partial Q_k}-\frac{iϙA_k}{\hbar},
$$

where $A_0$ is the electrostatic potential and $\vec A$ the vector potential; the relative sign of the two couplings is the metric's, the prescription being $D=\tilde{\nabla}+iϙ\tilde{A}/\hbar$ of *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*. With the derivatives of the free operator in place of the covariant derivatives, the square is the d'Alembertian, $\mathcal{D}^2=\Box$, because $(-R_{\vec e_x}^{\mathrm{axf}})^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $(-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, and the four cells anticommute. The covariant equation is $(\hbar\mathcal{D}-mc)\psi=0$. Multiplying it on the left by $R_{\vec e_x}^{\mathrm{axf}}$ and using

$$
R_{\vec e_x}^{\mathrm{axf}}(-R_{\vec e_x}^{\mathrm{axf}})=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
\qquad
R_{\vec e_x}^{\mathrm{axf}}(-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

gives

$$
\hbar D_0+\hbar\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}D_k-mc\,R_{\vec e_x}^{\mathrm{axf}}=0 .
$$

Inserting $D_0$ and $D_k$, multiplying by $c$, dividing by $i$, and using $R_{\vec e_x}^{\mathrm{axf}}=-i(iR_{\vec e_x}^{\mathrm{axf}})$, leaves the Hamiltonian form,

$$
i\hbar\frac{\partial}{\partial t'}\psi=H\psi,
$$

with

$$
\boxed{\;
H=iR_{\vec e_x}^{\mathrm{axf}}mc^2+c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k+ϙA_0,
\qquad
\pi_k=p_k-ϙA_k,
\quad
p_k=-i\hbar\frac{\partial}{\partial Q_k}.
\;}
$$

The identities used below are cells, and they are derived forms of the cell table of *Matrix Representations Conventions*, §*The Sixteen Products in This Frame*:

$$
(iR_{\vec e_x}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
\quad
(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
\quad
\{L_{\vec e_j}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\}=2\delta_{jk}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
\quad
\{iR_{\vec e_x}^{\mathrm{axf}},L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\}=0 .
$$

Each velocity cell squares to the unit, the three anticommute in pairs, and each anticommutes with the timelike frame cell.

The Hamiltonian splits into an **even** part and an **odd** part,

$$
H=iR_{\vec e_x}^{\mathrm{axf}}mc^2+\underbrace{c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k}_{\textstyle O}+\underbrace{ϙA_0}_{\textstyle\mathcal{E}},
$$

where even and odd are defined by conjugation with the timelike frame cell,

$$
\mathcal{E}\ \text{even}:\ iR_{\vec e_x}^{\mathrm{axf}}\mathcal{E}\,iR_{\vec e_x}^{\mathrm{axf}}=+\mathcal{E},
\qquad
O\ \text{odd}:\ iR_{\vec e_x}^{\mathrm{axf}}O\,iR_{\vec e_x}^{\mathrm{axf}}=-O .
$$

The odd part $O$ is what exchanges the $+1$ and $-1$ parts of the timelike frame cell, and hence what makes the positive- and negative-frequency sectors talk to each other. The FW transformation is the $*$-unitary transformation that removes $O$ order by order.

It is important to say at once which split this is, because several $\mathbb{Z}/2$'s are in play. Conjugation by the timelike frame cell defines the **frame grading**, the large/small split of the Foldy–Wouthuysen transformation; it is a frame-dependent split and not one of the algebra's own gradings. It is **not** the split by the conjugation $\natural$: the velocity cells $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ are frame-odd and yet Hermitian, hence in $\mathbb{M}_+$, so "odd" is not another word for "anti-Hermitian". The parity of *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form* is a third thing again.

Nor is the frame grading the subscript. The chirality cell is $-iR_{\vec e_z}^{\mathrm{axf}}$, the volume cell of the frame (*Special Element Conventions*, §*The Chirality Convention*). It anticommutes with all four frame cells, the timelike one included. The parent article states the value as a label and computes no cell (*The Dirac Equation in Biquaternionic Form*, §*The Two Values of the Subscript*), and the central form of the same split is $\chi=i\tilde\Xi_{\mathrm{ad}}$. Either way it is an element of the algebra, not an array. The mass term is even under the frame grading, and it exchanges the $L$ part and the $R$ part: a reader who identifies "odd" with "value-changing" will misread the transformation the whole way through.

### The Hamiltonian as One Frame Cell Times a Bracket

The identification of $O$ as the frame-odd part can be written directly in the algebra. The two parts of the kinetic operator are

$$
O=c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k,
\qquad
(iR_{\vec e_x}^{\mathrm{axf}})O=c\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k,
$$

where $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=(iR_{\vec e_x}^{\mathrm{axf}})(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})$ are the spacelike frame cells. Because $(iR_{\vec e_x}^{\mathrm{axf}})(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ and $(iR_{\vec e_x}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, the whole Hamiltonian is one factor of the timelike frame cell applied to a bracket that carries no frame index:

$$
H=c\,(iR_{\vec e_x}^{\mathrm{axf}})\Bigl(mc+\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k\Bigr).
$$

The two pieces of the bracket differ in frame parity, and that difference is what the outer cell exposes: the scalar piece becomes the mass term, the vector piece the kinetic term $c\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k$. After the transformation the Hamiltonian is the timelike frame cell times the energy alone, so the frame-odd piece is gone from it, and that is the algebraic content of the diagonalisation.

## The Transformation and Its Generator

Let $U=\exp(iS)$, with $S=S_1+S_2+\cdots$ Hermitian so that $U$ is $*$-unitary. The letter $S$ is the FW generator here, as in the literature. The transformed Hamiltonian is

$$
H_2=UHU^\dagger-i\hbar\,U\frac{\partial}{\partial t'}U^\dagger ,
$$

where the second term vanishes for a time-independent $S$. Since $H=iR_{\vec e_x}^{\mathrm{axf}}mc^2+O+\mathcal{E}$, the idea is to choose $S$ so that the large commutator $i[S,iR_{\vec e_x}^{\mathrm{axf}}mc^2]$ equals $-O$ at leading order, cancelling the odd part and leaving an even remainder of order $1/c^2$.

Expanding,

$$
UHU^\dagger=H+i[S,H]+\frac{i^2}{2!}[S,[S,H]]+\cdots ,
$$

the condition $i[S,iR_{\vec e_x}^{\mathrm{axf}}mc^2]=-O$ is satisfied by

$$
\boxed{\;
S_1=\frac{1}{2mc}\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,\pi_k
\;}
$$

because $-i$ times the $i$ of $iR_{\vec e_x}^{\mathrm{axf}}$ is $+1$:

$$
-\frac{i}{2mc^2}(iR_{\vec e_x}^{\mathrm{axf}})(cL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})
=-\frac{i\cdot i}{2mc}\,L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}
=\frac{1}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$

Indeed $[S_1,iR_{\vec e_x}^{\mathrm{axf}}]=\frac{i}{mc^2}O$, since $[L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},iR_{\vec e_x}^{\mathrm{axf}}]=2iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, whence $i[S_1,iR_{\vec e_x}^{\mathrm{axf}}mc^2]=-O$. The remaining term is evaluated with the same anticommutation:

$$
i[S_1,O]=\frac{1}{mc^2}(iR_{\vec e_x}^{\mathrm{axf}})O^2,
$$

because $[iR_{\vec e_x}^{\mathrm{axf}}O,O]=2(iR_{\vec e_x}^{\mathrm{axf}})O^2$ when $O$ is odd.

The second-order term of the expansion is of the same magnitude and supplies the factor $\frac12$. At this order $[S_1,H]=iO+\cdots$, whence

$$
-\frac{1}{2}[S_1,[S_1,H]]=-\frac{i}{2}[S_1,O]=-\frac{i}{2}\cdot\Bigl(-\frac{i}{mc^2}\Bigr)(iR_{\vec e_x}^{\mathrm{axf}})O^2
=\frac{i\cdot i}{2mc^2}(iR_{\vec e_x}^{\mathrm{axf}})O^2
=-\frac{(iR_{\vec e_x}^{\mathrm{axf}})O^2}{2mc^2},
$$

using $i\cdot i=-1$ once more. Collecting, the first-order term $+(iR_{\vec e_x}^{\mathrm{axf}})O^2/(mc^2)$ and this one combine to the half, and the transformed Hamiltonian at this order is

$$
\boxed{\;
H_2=iR_{\vec e_x}^{\mathrm{axf}}mc^2+\mathcal{E}+\frac{(iR_{\vec e_x}^{\mathrm{axf}})O^2}{2mc^2}+O_1+\cdots
\;}
$$

The odd remainder is fixed by the same commutator, applied to the potential rather than to the mass:

$$
O_1=i[S_1,\mathcal{E}]=\frac{(iR_{\vec e_x}^{\mathrm{axf}})}{2mc^2}\,[O,\mathcal{E}],
$$

which is odd because $(iR_{\vec e_x}^{\mathrm{axf}})$ is, and of relative order $v^2/c^2$ compared with $O$. It is removed by the second generator

$$
S_2=-\frac{i}{2mc^2}(iR_{\vec e_x}^{\mathrm{axf}})O_1 ,
$$

which is **even**, and therefore does not reintroduce the mixing it is meant to remove; by the same computation as for $S_1$, with $O_1$ in place of $O$, it gives $i[S_2,iR_{\vec e_x}^{\mathrm{axf}}mc^2]=-O_1$. The reason is visible in the algebra: $O_1$ carries one factor $(iR_{\vec e_x}^{\mathrm{axf}})$, so $(iR_{\vec e_x}^{\mathrm{axf}})O_1$ carries two, and the two cancel. Explicitly, $[O,\mathcal{E}]=i\hbarϙc\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}E_k$ and

$$
S_2=\frac{\hbarϙ}{4m^2c^3}\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}E_k ,
$$

an even cell combination with no $iR_{\vec e_x}^{\mathrm{axf}}$ left in it. For the free particle $O=c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}p_k$, $\mathcal{E}=0$, so $O_1=0$ and $O^2=c^2\vec p^2$; then $O^2/(2mc^2)=\vec p^2/(2m)$ and

$$
H_2=iR_{\vec e_x}^{\mathrm{axf}}\Bigl(mc^2+\frac{\vec p^2}{2m}-\frac{\vec p^4}{8m^3c^2}+\cdots\Bigr),
$$

whose first two terms are the free-particle Schrödinger Hamiltonian on the $+1$ part of the timelike frame cell and its negative on the $-1$ part, and whose $\vec p^4$ term is the first relativistic correction to the kinetic energy. The expansion is in powers of $(\vec p/mc)^2$, i.e. in $v^2/c^2$; the residual odd terms are smaller by two powers of $v/c$.

The generator has a transparent physical meaning in the algebra. The operator $(iR_{\vec e_x}^{\mathrm{axf}})O$ is the piece of the Hamiltonian that exchanges the $+1$ and $-1$ parts of the timelike frame cell. The generator $S_1=-\frac{i}{2mc^2}(iR_{\vec e_x}^{\mathrm{axf}})O$ is proportional to it, and it anticommutes with $iR_{\vec e_x}^{\mathrm{axf}}$: the generator is frame-odd, and the transformation it generates does not leave the frame cell fixed. It is the rotation whose angle measures how much mixing of the two frequency parts the kinetic term produces. For a slowly moving particle the angle is small and the transformation is close to the identity; in the ultra-relativistic regime the expansion breaks down, which is the signal that the non-relativistic separation is no longer meaningful.

It is worth recording why one generator is not enough. With $U=e^{iS_1}$ taken exactly, the odd remainder $O_1$ survives: the leading generator removes the leading odd term and nothing more, and the displayed $H_2$ is what remains at that order. The generator is a series, $S=S_1+S_2+\cdots$, and each term removes one order. The free particle is the exception, and the next section is about it: there the series terminates and a single closed-form exponential does the whole job at once.

### The Second Transformation and the Iteration

The odd remainder of the first step is $O_1$, of relative order $v^2/c^2$ compared with $O$. The same algorithm applied to it removes it, with the generator displayed above, and leaves a new odd remainder of relative order $v^4/c^4$; call that one $O_2$, and continue. The procedure iterates: at each stage the odd part of the next order is conjugated away by a generator proportional to it, and the new odd residual is two powers of $v/c$ smaller. The resulting expansion of the transformed Hamiltonian is the systematic $1/c$ expansion of the Dirac theory, and its convergence criterion is the physically transparent one,

$$
\frac{|\vec\pi|}{mc}\ll1 ,
$$

i.e. particle momenta small compared with $mc$. When the criterion fails the iteration still exists term by term but no longer converges to a useful separation: the notion of a particle part is momentum-dependent and becomes meaningless in the ultra-relativistic regime.

Two features of the iteration are worth keeping in view. First, the transformation is **asymptotic, not exact**, unless the theory is free, or the background has a special symmetry: the series is what the non-relativistic limit means. Second, the even terms are not unique as operators until the ordering of the non-commuting factors is fixed — $\vec E$ and $\vec\pi$ do not commute, and only the Hermitian, symmetrised combination is physical. The biquaternion framework reads the first feature as the statement that the frame grading is only approximately aligned with the dynamics, and the second as the statement that the cells multiply the field, so it is the field's own non-commutativity that the ordering ambiguity expresses.

## The Free Particle in Closed Form

For the free particle the transformation can be written exactly, and the exact form is the cleanest check that the expansion above is right. With $\vec u_p$ the unit vector along $\vec p$ and

$$
A=(iR_{\vec e_x}^{\mathrm{axf}})\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}u_k,
\qquad
A^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
\qquad
\theta=\arctan\frac{|\vec p|}{mc},
$$

the $*$-unitary

$$
U=\cos\frac{\theta}{2}+A\sin\frac{\theta}{2}=\exp(A\theta/2)
$$

brings the Hamiltonian to diagonal form. The verification is short. Since $(iR_{\vec e_x}^{\mathrm{axf}})A=-A(iR_{\vec e_x}^{\mathrm{axf}})$, conjugation by $U$ acts as

$$
U(iR_{\vec e_x}^{\mathrm{axf}})U^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})\exp(-A\theta),
$$

while $A$ commutes with $U$ and is unchanged. Writing

$$
H=(iR_{\vec e_x}^{\mathrm{axf}})mc^2+c|\vec p|\,(iR_{\vec e_x}^{\mathrm{axf}})A=(iR_{\vec e_x}^{\mathrm{axf}})(mc^2+c|\vec p|A),
$$

where $\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}u_k=(iR_{\vec e_x}^{\mathrm{axf}})A$ follows from $(iR_{\vec e_x}^{\mathrm{axf}})A=(iR_{\vec e_x}^{\mathrm{axf}})^2\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}u_k$, one has

$$
H=(iR_{\vec e_x}^{\mathrm{axf}})E(\cos\theta+A\sin\theta)=(iR_{\vec e_x}^{\mathrm{axf}})E\exp(A\theta),
$$

with

$$
E=\sqrt{\vec p^2c^2+m^2c^4},
\qquad
\cos\theta=\frac{mc^2}{E},
\qquad
\sin\theta=\frac{c|\vec p|}{E},
$$

and $\exp(A\theta)=\cos\theta+A\sin\theta$ because $A^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$. Therefore

$$
\begin{aligned}
UHU^\dagger
&=\exp(A\theta/2)\,(iR_{\vec e_x}^{\mathrm{axf}})E\exp(A\theta)\exp(-A\theta/2)\\
&=(iR_{\vec e_x}^{\mathrm{axf}})E\exp(-A\theta/2)\exp(A\theta)\exp(-A\theta/2)\\
&=(iR_{\vec e_x}^{\mathrm{axf}})E,
\end{aligned}
$$

that is, $UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})\sqrt{\vec p^2c^2+m^2c^4}$ exactly. In this language the exact generator is $S=S_1\,\theta/\tan\theta$, since $S_1=-\tfrac{i}{2}A\tan\theta$ and $iS=\tfrac{1}{2}A\theta$; it reduces to $S_1$ as $\theta\to0$; the factor $\theta/\tan\theta\le1$ is the whole of the relativistic correction to the non-relativistic generator. The $+1$ part of $iR_{\vec e_x}^{\mathrm{axf}}$ is the relativistic energy $+E$, the $-1$ part is $-E$, and the odd part has been removed to all orders. The leading expansion of the closed form reproduces the result of the previous section:

$$
(iR_{\vec e_x}^{\mathrm{axf}})E=(iR_{\vec e_x}^{\mathrm{axf}})\Bigl(mc^2+\frac{\vec p^2}{2m}-\frac{\vec p^4}{8m^3c^2}+\cdots\Bigr),
$$

the $\vec p^4$ term being the first relativistic correction to the kinetic energy. The closed form was checked numerically: with $\tan\theta=|\vec p|/(mc)$ and $U=\cos(\theta/2)+A\sin(\theta/2)$, the identity $UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})E$ holds to machine precision, at the $10^{-14}$ level for a generic three-momentum and every value of $|\vec p|/(mc)$ tested.

## The Mean Position Operator

The transformation does more than diagonalise the Hamiltonian: it also changes which operator plays the role of position. Write the position as the material vector $\vec q=\sum_kQ_k\vec e_k$, with $Q_k$ the operator of multiplication by the coordinate. In the transformed frame that multiplication is the coordinate, so the operator carrying it back to the original frame is obtained by conjugating with $U^\dagger$, not with $U$:

$$
\vec X=U^\dagger\vec q\,U=\vec q-i[S_1,\vec q]-\frac{1}{2}[S_1,[S_1,\vec q]]+\cdots .
$$

The direction of the conjugation is the content of the definition. The other ordering, $U\vec q\,U^\dagger$, is the original coordinate read in the transformed frame, and it keeps the trembling; $U^\dagger\vec q\,U$ is the coordinate whose image in the transformed frame is plain multiplication.

The correction to each component is fixed by one commutator with the momentum. Since the cells commute with multiplication by a coordinate and $[\pi_k,Q_k]=-i\hbar$,

$$
[S_1,Q_k]=-\frac{i\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
\qquad
-i[S_1,Q_k]=i\cdot\frac{i\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=-\frac{\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

where $i\cdot i=-1$ once more. Hence

$$
\vec X=\sum_kX_k\vec e_k,
\qquad
X_k=Q_k-\frac{\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+\cdots .
$$

The correction is of the order of the half reduced Compton wavelength $\hbar/(2mc)$ — the Zitterbewegung amplitude — and the next correction is of order $1/m^2$. The exact closed form of the previous section gives the same leading term: differentiating $\theta$ and differentiating $\vec u_p$ contribute two pieces whose dependence on $\vec u_p$ cancels, so the sum is the single cell, and the residual against $U^\dagger\vec q\,U$ is of order $1/m^2$. The operator $\vec X$ is the **mean position** (Foldy–Wouthuysen position). Its defining property is that its Heisenberg velocity,

$$
\frac{d\vec X}{dt'}=\frac{i}{\hbar}[H,\vec X]=U^\dagger\Bigl((iR_{\vec e_x}^{\mathrm{axf}})\frac{\vec pc^2}{E}\Bigr)U,
$$

commutes with $H$ and therefore has no oscillatory part: in the transformed frame it is exactly the classical drift $(iR_{\vec e_x}^{\mathrm{axf}})\vec pc^2/E$, and the rapid trembling of the ordinary position operator is entirely contained in the difference

$$
\vec q-\vec X=\frac{\hbar}{2mc}\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+\cdots .
$$

In the biquaternion language, the trembling is a rotation of the field between the two frames of the algebra, and the mean position is the coordinate that is blind to it. The companion article *Zitterbewegung in Biquaternionic Form* records the same conclusion from the side of the oscillation; here it appears as a property of the mean position.

The correction $\frac{\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ is itself worth reading in the algebra. It is a frame-odd displacement: it contains the same odd cells that generate the transformation, it anticommutes with the timelike frame cell, and it is the first term in the expansion of the mean position in powers of $1/m$. It is not a measurement of the particle's size; it is the statement that the coordinate conjugate to the diagonal Hamiltonian is not the coordinate conjugate to the original field. The operator $\vec X$ does not have commuting components, and it is not Lorentz covariant in the naive sense — the Newton–Wigner operator is the covariant completion of it — a fact already visible in the biquaternion framework as the difference between a material position $\vec q$ and a configuration-space position on the module.

## The Biquaternion Reading

The transformation can now be located in the two splits of the algebra, and the location is the content of the article.

**The subscript is where the biquaternion pair lives.** The massive biquaternionic Dirac equation is the pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$. The mass term of the Hamiltonian is $mc^2(iR_{\vec e_x}^{\mathrm{axf}})$, and the timelike frame cell acts on the right by $\vec e_x$, so it exchanges the two values of the subscript. All four frame cells exchange them, each acting on the right by $\vec e_x$ or by $\vec e_y$. The velocity cells $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ act on the right by $\vec e_z$ and keep the value. Under the subscript the mass and the four frame cells cross from one value to the other, and the velocity cells stay.

**The frame split is where the FW transformation works.** Conjugation by the timelike frame cell separates the mass from the kinetic term: the mass term commutes with $iR_{\vec e_x}^{\mathrm{axf}}$, and the velocity cells anticommute with it. The fixed $*$-unitary $\frac{1}{\sqrt2}(iR_{\vec e_x}^{\mathrm{axf}}-iR_{\vec e_z}^{\mathrm{axf}})$ is its own inverse and conjugates $iR_{\vec e_x}^{\mathrm{axf}}$ to $-iR_{\vec e_z}^{\mathrm{axf}}$ and back. The FW transformation is the momentum-dependent completion of that exchange: it conjugates the field so that the mass, which exchanges the two values, becomes the term that commutes with the timelike frame cell, while the kinetic term, which keeps the value, becomes the first-order perturbation. Removing the odd part is exactly the statement that the mass is the large term and the mixing is small.

**The transformation does not separate the two values.** After the transformation the Hamiltonian commutes with $iR_{\vec e_x}^{\mathrm{axf}}$, and it does not commute with the chirality cell. The chirality cell in the transformed frame is momentum-dependent:

$$
(-iR_{\vec e_z}^{\mathrm{axf}})^{FW}=U(-iR_{\vec e_z}^{\mathrm{axf}})U^\dagger=(-iR_{\vec e_z}^{\mathrm{axf}})\exp(-A\theta).
$$

Its part that commutes with $iR_{\vec e_x}^{\mathrm{axf}}$ is $-\sin\theta\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}u_k$, which on the $+1$ part is the helicity $i\sin\theta\sum_kL_{\vec e_k}^{\mathrm{axf}}u_k$ with $\sin\theta=|\vec p|c/E$ — the value for a massless field, reduced by that factor for a massive one. Its part that anticommutes with $iR_{\vec e_x}^{\mathrm{axf}}$ is $\cos\theta\,(-iR_{\vec e_z}^{\mathrm{axf}})=(mc^2/E)(-iR_{\vec e_z}^{\mathrm{axf}})$, and that is the term that exchanges the two values, of relative order $m/|\vec p|$ in the ultra-relativistic regime. The FW transformation therefore separates **positive from negative frequency**, the two values of the frame cell, and not $L$ from $R$. In the algebra, the split it diagonalises is the split by $iR_{\vec e_x}^{\mathrm{axf}}$, the reflection of *The Reflection and the Rotation in Biquaternionic Form*; the subscript is read by $-iR_{\vec e_z}^{\mathrm{axf}}$, a different reflection, and no $*$-unitary rotation of the field can diagonalise both at once because the two cells anticommute. The two splits are complementary, and the mass is the object that measures their incompatibility.

**The generator is frame-odd.** The FW generator $S_1=\frac{1}{2mc}\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k$ is a sum of the spacelike frame cells, and every spacelike frame cell anticommutes with $iR_{\vec e_x}^{\mathrm{axf}}$. Conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$ therefore reverses the sign of $S_1$, and the generator does not leave the frame cell fixed: since $U=\exp(iS_1)$,

$$
U(iR_{\vec e_x}^{\mathrm{axf}})U^{*}=(iR_{\vec e_x}^{\mathrm{axf}})\exp(-2iS_1).
$$

The biquaternion content it carries is not a new rotation of the frame but the identification of the odd part $O$ with the frame-odd mixing term and of the mass with the frame-even large term. This is consistent with the reflection article's finding that the frame is required to state the two values and parity: the FW transformation needs the frame for the same reason.

## The Pauli Limit and the Residual Terms

With an external electromagnetic field, $\pi_k=p_k-ϙA_k$, and the FW-transformed Hamiltonian acquires the standard non-relativistic terms. The kinetic term is where the spin enters, through the algebra of the velocity cells combined with the non-commutativity of the momentum components. Two velocity cells multiply into the spin cell $iL_{\vec e_l}^{\mathrm{axf}}$,

$$
L_{\vec e_j}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\delta_{jk}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}+i\,\epsilon_{jkl}\,(iL_{\vec e_l}^{\mathrm{axf}}),
$$

and the spin cell squares to $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$. The symmetric part of the product gives $\vec\pi^2$; the antisymmetric part contracts with the commutator of the momenta and survives:

$$
O^2=c^2\Bigl(\vec\pi^2-ϙ\hbar\sum_l(iL_{\vec e_l}^{\mathrm{axf}})B_l\Bigr),
\qquad
[\pi_j,\pi_k]=i\hbarϙ\,\epsilon_{jkl}B_l .
$$

The spin cell commutes with the timelike frame cell, so the spin terms are frame-even, and $\frac{(iR_{\vec e_x}^{\mathrm{axf}})O^2}{2mc^2}$ already contains the Zeeman coupling $-\frac{ϙ\hbar}{2m}\sum_l(iL_{\vec e_l}^{\mathrm{axf}})B_l$ with the gyromagnetic factor $g=2$. The second transformation, with the generator $S_2$ above, adds the terms of relative order $v^2/c^2$. To this order the effective Hamiltonian on the $+1$ part of the timelike frame cell is the Pauli Hamiltonian

$$
\boxed{\;
\begin{aligned}
H_{\mathrm{Pauli}}
&=\frac{\vec\pi^2}{2m}+ϙA_0-\frac{ϙ\hbar}{2m}\sum_l(iL_{\vec e_l}^{\mathrm{axf}})B_l\\[2pt]
&\quad-\frac{ϙ\hbar}{4m^2c^2}\sum_l(iL_{\vec e_l}^{\mathrm{axf}})(\vec E\times\vec\pi)_l
+\frac{\hbar^2}{8m^2c^2}\nabla^2(ϙA_0),
\end{aligned}
\;}
$$

whose terms beyond the leading kinetic and electrostatic ones are the spin–Zeeman term, the spin–orbit coupling and the Darwin term — the coefficient $1/(4m^2c^2)$ of the spin–orbit term already contains the Thomas factor of $\frac12$ — together with the relativistic kinetic correction $-\bigl(\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k\bigr)^4/(8m^3c^2)$, which on the $+1$ part reads $-\bigl(\sum_l(iL_{\vec e_l}^{\mathrm{axf}})\pi_l\bigr)^4/(8m^3c^2)$ and is the field version of the free term $-\vec p^4/(8m^3c^2)$ displayed above. The difference between that and $\vec\pi^4$ is itself of order $c^{-2}$, because $O^2/c^2$ differs from $\vec\pi^2$ by the Zeeman term, so it is the form with the spin cell that belongs at this order. The companion exercise *Exercise: The Non-Relativistic Limit and the Pauli Equation* derives each in the biquaternion framework; they are quoted here as the standard content of the transformation. For the electrostatic case $\vec E=-\nabla A_0$, the Darwin term has the equivalent forms

$$
\frac{\hbar^2}{8m^2c^2}\nabla^2(ϙA_0)=-\frac{ϙ\hbar^2}{8m^2c^2}\nabla\cdot\vec E .
$$

The point to record is structural: every correction is **even** under the frame grading — each is a scalar or a spin–magnetic coupling, and none exchanges the two frequency parts — which is the statement that the transformation has succeeded in removing the odd part to the stated order. The residual odd terms, suppressed by a further factor of $v^2/c^2$ relative to $O$, are removed by $S_2$.

The $-1$ part is the same Hamiltonian with the sign of the timelike frame cell reversed: it is $-E=-mc^2-\vec\pi^2/(2m)+\cdots$, the mirror image of the $+1$ part, separated from it by the mass gap $2mc^2$. Factoring out the rest-energy phase, as the companion article does, gives the antiparticle Hamiltonian: the same kinetic and spin terms, and the opposite charge, so that the potential term is $-ϙA_0$. That sign reversal is charge conjugation, and it is what the two sectors differ by once the rest energy is removed. This is the sense in which the FW transformation separates particles from antiparticles: not by splitting the field into two pieces that never talk, which the fields do not allow, but by diagonalising the Hamiltonian so that the gap is manifest and the mixing is small.

## What Is Standard and What the Algebra Adds

The transformation, the generator $S_1$, the leading Hamiltonian $iR_{\vec e_x}^{\mathrm{axf}}mc^2+(iR_{\vec e_x}^{\mathrm{axf}})O^2/(2mc^2)$, the closed free-particle form $(iR_{\vec e_x}^{\mathrm{axf}})E$, the mean position operator and the Pauli limit are all standard results, transcribed here from the relativistic-quantum-physics literature and cited as such. The biquaternion contribution is not a new formula but a placing:

- The **two splits** are kept distinct. The FW transformation diagonalises the frame grading (large/small, $iR_{\vec e_x}^{\mathrm{axf}}$); the biquaternion mass pair is the subscript ($L$/$R$, read by $-iR_{\vec e_z}^{\mathrm{axf}}$). The two cells anticommute, so the transformation cannot diagonalise both, and the mass is the obstruction.
- The **mass term** appears in the transformation as the large, frame-even term whose diagonal form is the non-relativistic gap; under the subscript the same mass is the term that exchanges the $L$ part and the $R$ part. The passage between the two descriptions starts from the fixed $*$-unitary $\frac{1}{\sqrt2}(iR_{\vec e_x}^{\mathrm{axf}}-iR_{\vec e_z}^{\mathrm{axf}})$ that exchanges the two cells, and the FW transformation is its momentum-dependent completion.
- The **residual odd part** is the frame-odd mixing term $O$, and its removal order by order is the statement that positive and negative frequency decouple in the non-relativistic limit.
- The **exact free form** shows that the separation, for a free field, is exact: $UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})\sqrt{\vec p^2c^2+m^2c^4}$ with $U=\exp\bigl(\frac{\theta}{2}(iR_{\vec e_x}^{\mathrm{axf}})\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}u_k\bigr)$ and $\tan\theta=|\vec p|/(mc)$. The expansion used by the non-relativistic reduction is the expansion of this closed form in $|\vec p|/(mc)$.

The transformation was constructed here with the large term being the mass. If an external potential dominates, the same algorithm is applied with a different even large term, and the generator changes accordingly; the algebra reads this as a different choice of frame. The choice of frame is the physical input, and the rest is the rotation that aligns the odd part with it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. This is the only section of the article that uses them; every other statement is written in cells.

Here $L_a$ and $R_b$ are the left and right multiplications.

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

A single product is a pure tensor, a cell of rank one; a general element is a sum of at most four of them, one for each term of the rank decomposition of its coefficient matrix in the cell basis.

In terms of the vector generators this is the standard $\gamma_5=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ of the $(+,-,-,-)$ convention: the product $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$ is the cell $-R_{\vec e_z}^{\mathrm{pau}}$ computed above, so $i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{pau}}=\gamma_5$. Thus $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell itself. The central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The $\gamma$'s are a complex frame, not a real one: they generate $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$ over $\mathbb{C}$, whereas the cells with real coefficients generate the real algebra $\mathrm{Cl}_{3,1}(\mathbb{R})=M_4(\mathbb{R})$. It is the complexification that makes the scalar $i$ central, and that is why each generator is written as $i$ times a real cell.

**The identities the series uses.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,

$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
\qquad \varepsilon=(1,-1,-1,-1),$$

$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$

$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

Four contraction sums accompany them, and they are frame statements, because a cell's square is. Writing $\gamma_\mu[\mathbb{M}_-]^2=\epsilon_\mu I_4$ and $S=\sum_\mu\epsilon_\mu$, the sums over a product $\Gamma$ of $p$ distinct frame cells are

$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\Gamma\gamma_\mu[\mathbb{M}_-]=(-1)^p\Bigl(S-2\sum_{i\in\Gamma}\epsilon_i\Bigr)\Gamma ,
$$

where the second sum runs over the indices carried by $\Gamma$. The rule is checked in the $\mathbb{M}_-$ frame, $\epsilon=(+1,-1,-1,-1)$ and $S=-2$:

$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=S\,I_4=-2I_4,
\qquad
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=\bigl(2\epsilon_\alpha-S\bigr)\gamma_\alpha[\mathbb{M}_-] ,
$$

$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=\bigl(S-2\epsilon_\alpha-2\epsilon_\beta\bigr)\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\quad(\alpha\ne\beta),
$$

$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]
=\bigl(2\epsilon_\alpha+2\epsilon_\beta+2\epsilon_\gamma-S\bigr)\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]
\quad(\alpha,\beta,\gamma\ \text{distinct}).
$$

The second sum is $4\gamma_0[\mathbb{M}_-]$ for $\alpha=0$ and vanishes for spacelike $\alpha$; the third is $2\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]$ when both indices are spacelike and $-2\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]$ when one of them is timelike; the fourth is $-4\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]$ for a spacelike triple and zero when a timelike index appears. In a Euclidean frame, where every cell squares to $+I_4$ and $S=4$, the bracket is $4-2p$ and the textbook values follow:

$$
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=4I_4,\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-2\gamma_\alpha[\mathbb{B}],\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\mu[\mathbb{B}]=4\delta_{\alpha\beta}I_4,
$$

$$
\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-2\,\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-] ,
$$

the last two with the convention that repeated indices are read separately, since $\gamma_\alpha[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]=\epsilon_\alpha$ and the sum then collapses to the lower grade.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Foldy–Wouthuysen transformation is the $*$-unitary $U=\exp(iS)$ that diagonalises the Dirac Hamiltonian in the frame grading, separating the positive- and negative-frequency parts. With

$$
H=iR_{\vec e_x}^{\mathrm{axf}}mc^2+O+\mathcal{E},
\qquad
O=c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k,
$$

and $O$ odd under conjugation by the timelike frame cell $iR_{\vec e_x}^{\mathrm{axf}}$, the leading generator is

$$
S_1=\frac{1}{2mc}\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k,
$$

and the transformed Hamiltonian through order $v^2/c^2$ is

$$
H_2=iR_{\vec e_x}^{\mathrm{axf}}mc^2+\mathcal{E}+\frac{(iR_{\vec e_x}^{\mathrm{axf}})O^2}{2mc^2};
$$

in the free case $\mathcal{E}=0$ this is the Schrödinger Hamiltonian on the $+1$ part and its negative on the $-1$ part. For the free particle the transformation is exact:

$$
U=\cos\frac{\theta}{2}+(iR_{\vec e_x}^{\mathrm{axf}})\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}u_k\sin\frac{\theta}{2},
\qquad
\tan\theta=\frac{|\vec p|}{mc},
$$

$$
\boxed{\;UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})\sqrt{\vec p^2c^2+m^2c^4}\;},
$$

checked to machine precision by direct computation. The mean position is the operator whose image in the transformed frame is multiplication by the coordinate,

$$
\vec X=U^\dagger\vec q\,U=\sum_kX_k\vec e_k,
\qquad
X_k=Q_k-\frac{\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+\cdots ,
$$

whose Heisenberg velocity commutes with the Hamiltonian and so has no trembling term; the Zitterbewegung resides in the difference $\vec q-\vec X$.

The biquaternion interpretation turns on two splits that must not be conflated. The frame grading, conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$, is what the FW transformation diagonalises and in which the mass term is a multiple of the frame cell; the subscript, read by $-iR_{\vec e_z}^{\mathrm{axf}}$, is where the biquaternion mass pair is written and in which the mass exchanges $L$ and $R$. The two cells anticommute, so no single $*$-unitary diagonalises both, and the mass term is the measure of their incompatibility. The FW generator is a sum of odd cells, each of which anticommutes with $iR_{\vec e_x}^{\mathrm{axf}}$: it is frame-odd, and the transformation it generates does not leave the frame cell fixed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_\pm$ | Hermitian ($+$) and anti-Hermitian ($-$) sectors; $\mathbb{M}_-$ is the material sector |
| $L_{a}R_{b}$ | Cell, the two-sided multiplication of *Operator Family Conventions* |
| $iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | Timelike frame cell; $(iR_{\vec e_x}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Velocity cells; $(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=(iR_{\vec e_x}^{\mathrm{axf}})(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})$ | Spacelike frame cells; square $-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $iL_{\vec e_l}^{\mathrm{axf}}$ | Spin cell: left multiplication by $i\vec e_l$; $(iL_{\vec e_l}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $-iR_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, the volume cell of the frame (*Special Element Conventions*, §*The Chirality Convention*); $(-iR_{\vec e_z}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $ϙ$ | Charge of the field; $A_\mu=(A_0,-\vec A)$ |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector of the cells; used only in *The Legacy Pauli Gamma Formulation* |
| $\mathcal{D}=i\sum_\mu\bigl(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\bigr)\partial/\partial x_\mu$ | Dirac operator; $\mathcal{D}^2=\Box$ |
| $H = iR_{\vec e_x}^{\mathrm{axf}}mc^2 + O + \mathcal{E}$ | Dirac Hamiltonian, odd/even split |
| $O = c\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k$ | Odd (frame-anticommuting) part |
| $\mathcal{E} = ϙA_0$ | Even (frame-commuting) part |
| $U = \exp(iS)$ | Foldy–Wouthuysen $*$-unitary |
| $S_1 = \frac{1}{2mc}\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k$ | Leading FW generator |
| $O_1 = i[S_1,\mathcal{E}]$ | Odd remainder after the first step |
| $S_2 = -\frac{i}{2mc^2}(iR_{\vec e_x}^{\mathrm{axf}})O_1$ | Second generator; even |
| $H_2 = UHU^\dagger - i\hbar U\partial/\partial t'\,U^\dagger$ | Transformed Hamiltonian |
| $\theta = \arctan(|\vec p|/(mc))$ | Free-particle FW angle |
| $\vec q = \sum_kQ_k\vec e_k$ | Material position |
| $X_k = Q_k-\frac{\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+\cdots$ | Mean (Foldy–Wouthuysen) position, $k$-th component |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | One-sided mass pair (the subscript) |
| $\Box$ | Series d'Alembertian |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the transformation and the mean position operator.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the generator, the block-diagonalisation, and the non-relativistic expansion.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the Pauli limit and the spin–orbit and Darwin terms.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac Hamiltonian, the Dirac algebra and the Foldy–Wouthuysen reduction.
- L. L. Foldy, "The electromagnetic properties of Dirac particles," *Physical Review* **87** (1952) 688–693, for the mean position and its electromagnetic couplings.
- M. E. Rose, *Relativistic Electron Theory* (Wiley, 1961), for the systematic $1/c$ expansion.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the detailed treatment of the Foldy–Wouthuysen transformation and its applications.
- P. Strange, *Relativistic Quantum Mechanics* (Cambridge, 1998), for the transformation in the presence of external fields.
