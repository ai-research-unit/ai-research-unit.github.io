# __The Foldy–Wouthuysen Transformation in Biquaternionic Form__

## Introduction

The Dirac equation describes particles and antiparticles on the same footing, and its four-component solutions mix the two. The Foldy–Wouthuysen (FW) transformation, introduced by Leslie Foldy and Siegfried Wouthuysen in 1950, is the $*$-unitary transformation that separates them. It block-diagonalises the Dirac Hamiltonian: the upper two components become the positive-frequency (particle) sector and the lower two the negative-frequency (antiparticle) sector. In doing so it produces the systematic expansion of the relativistic Hamiltonian in powers of $1/c$ whose leading terms are the Schrödinger and Pauli Hamiltonians. The non-relativistic reductions of this corpus are built on it, and the companion articles on the electron and on the hydrogen atom presuppose it.

The transformation is worth a biquaternion article for a structural reason. The biquaternionic Dirac equation is a **chiral pair**: the mass couples $\tilde{\Psi}_L$ to $\tilde{\Psi}_R$, and the two chiral halves are the minimal left ideal $S$ and its conjugate $S^{\mathrm{c}}$ — not the two Peirce carriers, which are two copies of $S$. The FW transformation, by contrast, separates **positive from negative frequency**, and the two pieces into which it splits the field are not the two chiralities. The article therefore keeps two gradings apart. The **chirality grading** is the one in which the mass is off-diagonal and the biquaternion pair is written. The **frame grading** is the one fixed by the timelike frame cell $iR_{\vec e_x}^{\mathrm{axf}}$, in which the FW transformation works and the mass is diagonal. Conflating the two is the standard way to misread either, and making the distinction explicit is the biquaternion content of the transformation.

**Two Dirac equations.** The corpus carries two, and they must not be read as one. The equation used here is the **one-sided** chiral pair of *Operator and Calculus Conventions*, in which the gradient acts by left multiplication and the mass is the off-diagonal pairing of $S$ and $S^{\mathrm{c}}$. The **two-sided** equation is Kravchenko's, in which the time derivative and the spatial gradient act from the left, the mass acts by right multiplication through $\vec e_z$, and a componentwise conjugation supplies the antilinear part (*The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*). The two are related by the dictionary $A$ and describe the same physics in different representations. The Hamiltonian form is read off the one-sided pair, so the transformation below is stated for that pair; the two-sided equation is the same dynamics in the representation in which the analytic machinery acts. What the transformation diagonalises in either reading is the frame grading; what it leaves alone is the chirality grading.

The scope is the transformation itself: its generator, its free-particle closed form, the mean position operator it defines, and the interpretation of all this in the algebra. The quantised field, the Fock space and the fermionic path integral belong to the companion category *Biquaternion Quantum Fields*, and the relativistic qubit and the informational interpretation to the subcategory *focus on informational aspects*. The Pauli equation itself, and the detailed non-relativistic expansion including the Darwin and spin–orbit terms, are worked through in the companion exercise *Exercise: The Non-Relativistic Limit and the Pauli Equation* and are only summarised here.

**Conventions.** The algebra, the cells and their composition, the frame cells and the metric are those of *Algebra and Element Conventions*, *Operator Family Conventions*, *Frame Conventions* and *Matrix Representations Conventions*; the gradient, the d'Alembertian and the one-sided chiral pair are those of *Operator and Calculus Conventions*, and none is redefined here. The charge is $ϙ$, the four-potential is $A_\mu=(A_0,-\vec A)$, and the cells pair with the coordinates by $\nu(t)=x$, $\nu(k)=y$. One object is this article's own, the velocity cell $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, which anticommutes with the timelike frame cell $iR_{\vec e_x}^{\mathrm{axf}}$ and squares to the identity. The equation is the one-sided pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$.

## The Dirac Hamiltonian and the Odd/Even Split

The FW transformation is best stated for the Hamiltonian form of the Dirac equation. In the $\mathbb{M}_-$ frame, where $x_0=ct'$, $Q_t=ix_0$ and the metric is $(-1,1,1,1)$, the Dirac operator is

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

In the Dirac basis the timelike frame cell is diagonal and the velocity cells are off-diagonal, with matrix images

$$
iR_{\vec e_x}^{\mathrm{axf}}\mapsto\begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix},
\qquad
L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\mapsto\begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix}.
$$

The identities used below read, in the same images,

$$
(iR_{\vec e_x}^{\mathrm{axf}})^2\mapsto I_4,
\quad
(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})^2\mapsto I_4,
\quad
\{L_{\vec e_j}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\}\mapsto2\delta_{jk}I_4,
\quad
\{iR_{\vec e_x}^{\mathrm{axf}},L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\}\mapsto0 .
$$

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

The odd part $O$ is what couples the upper and lower components, and hence what makes the positive- and negative-frequency sectors talk to each other. The FW transformation is the $*$-unitary transformation that removes $O$ order by order.

It is important to say at once which grading this is, because several $\mathbb{Z}/2$'s are in play. Conjugation by the timelike frame cell defines the **frame grading**, the large/small split of the Foldy–Wouthuysen transformation; it is a frame-dependent split and not one of the algebra's gradings. It is **not** the Clifford parity. In the Clifford reading $iR_{\vec e_x}^{\mathrm{axf}}$ is itself Clifford-odd — it is one of the five generators — while the kinetic part $O=c\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k$ is a product of two generators, hence Clifford-even and Hermitian, so as a biquaternion $O$ lies in $\mathbb{M}_+$. It is the product $(iR_{\vec e_x}^{\mathrm{axf}})O$ that is Clifford-odd and anti-Hermitian, and it is that product, not $O$, that has no representative in $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$. The parity of *The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form* is a third thing again. Nor does frame parity coincide with the $*$-grading: the spacelike frame cells $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ are frame-odd and yet Hermitian, hence in $\mathbb{M}_+$, so "odd" is not another word for "anti-Hermitian".

Nor is the frame grading the chirality. The chirality cell is $-iR_{\vec e_z}^{\mathrm{axf}}=i\,\omega$, where $\omega=-L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ is the pseudoscalar of the algebra, with $\omega^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$; the scalar $i$ of the chirality cell multiplies that cell from outside. It is the product of the four frame cells:

$$
(iR_{\vec e_x}^{\mathrm{axf}})(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=-R_{\vec e_z}^{\mathrm{axf}},
\qquad
-iR_{\vec e_z}^{\mathrm{axf}}=i\cdot\bigl(-R_{\vec e_z}^{\mathrm{axf}}\bigr),
$$

the four factors of $i$ multiplying to $i^4=1$ and leaving the real cell $-R_{\vec e_z}^{\mathrm{axf}}$; the chirality cell is that cell times the scalar $i$. The chirality cell anticommutes with all four frame cells, the timelike one included. On the Dirac module it represents the central sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ (*The Dirac Equation in Biquaternionic Form*, §*Chirality and the Central Sign*), which is an element of the complexified algebra and not a Clifford matrix. The mass term is even under the frame grading and off-diagonal between the two chiral halves under the chirality, and that is the whole of the distinction: a reader who identifies "odd" with "chirality-changing" will misread the transformation the whole way through.

### The Hamiltonian as One Frame Cell Times a Bracket

The identification of $O$ as the frame-odd part can be written directly in the algebra. In the dictionary of *Matrix Representations Conventions*, §*The 2×2 Matrix Representation*, $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, so the $2\times2$ reading of the cells gives $L_{e_t}\mapsto I_4$ and $L_{\vec e_k}\mapsto I_2\otimes(-i\sigma_k)$, its Peirce arrays,. With that reading fixed, the two parts of the kinetic operator are

$$
O=c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k,
\qquad
(iR_{\vec e_x}^{\mathrm{axf}})O=c\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k,
$$

where $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=(iR_{\vec e_x}^{\mathrm{axf}})(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})$ are the spacelike frame cells. Because $(iR_{\vec e_x}^{\mathrm{axf}})(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ and $(iR_{\vec e_x}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, the whole Hamiltonian is one factor of the timelike frame cell applied to a bracket that carries no frame index:

$$
H=c\,(iR_{\vec e_x}^{\mathrm{axf}})\Bigl(mc+\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k\Bigr).
$$

The two pieces of the bracket differ in frame parity, and that difference is what the outer cell exposes: the scalar piece becomes the mass term, the vector piece the kinetic term $c\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k$. After the transformation the Hamiltonian is the timelike frame cell times the energy alone, so the frame-odd piece is gone from it, and that is the algebraic content of the block diagonalisation.

## The Transformation and Its Generator

Let $U=\exp(iS)$, with $S=S_1+S_2+\cdots$ Hermitian so that $U$ is $*$-unitary. The letter $S$ is the FW generator here, as in the literature; the spinor ideal $S$ of the introduction appears only there, always with its conjugate or as the ideal. The transformed Hamiltonian is

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

which is **even**, and therefore does not reintroduce the large/small mixing it is meant to remove; by the same computation as for $S_1$, with $O_1$ in place of $O$, it gives $i[S_2,iR_{\vec e_x}^{\mathrm{axf}}mc^2]=-O_1$. The reason is visible in the algebra: $O_1$ carries one factor $(iR_{\vec e_x}^{\mathrm{axf}})$, so $(iR_{\vec e_x}^{\mathrm{axf}})O_1$ carries two, and the two cancel. Explicitly, $[O,\mathcal{E}]=i\hbarϙc\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}E_k$ and

$$
S_2=\frac{\hbarϙ}{4m^2c^3}\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}E_k ,
$$

an even cell combination with no $iR_{\vec e_x}^{\mathrm{axf}}$ left in it. For the free particle $O=c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}p_k$, $\mathcal{E}=0$, so $O_1=0$ and $O^2=c^2\vec p^2$; then $O^2/(2mc^2)=\vec p^2/(2m)$ and

$$
H_2=iR_{\vec e_x}^{\mathrm{axf}}\Bigl(mc^2+\frac{\vec p^2}{2m}-\frac{\vec p^4}{8m^3c^2}+\cdots\Bigr),
$$

whose first two terms are the free-particle Schrödinger Hamiltonian in the upper block and its negative in the lower block, and whose $\vec p^4$ term is the first relativistic correction to the kinetic energy. The expansion is in powers of $(\vec p/mc)^2$, i.e. in $v^2/c^2$; the residual odd terms are smaller by two powers of $v/c$.

The generator has a transparent physical meaning in the algebra. The operator $(iR_{\vec e_x}^{\mathrm{axf}})O$ is the piece of the Hamiltonian that flips the large and small components. The generator $S_1=-\frac{i}{2mc^2}(iR_{\vec e_x}^{\mathrm{axf}})O$ is proportional to it, and that product is Clifford-odd, so $S_1$ lies outside the even subalgebra $\mathrm{Cl}_{1,3}^{+}$ and the transformation cannot be read as one of the algebra's rotors. It is the rotation whose angle measures how much large/small mixing the kinetic term produces. For a slowly moving particle the angle is small and the transformation is close to the identity; in the ultra-relativistic regime the expansion breaks down, which is the signal that the non-relativistic separation is no longer meaningful.

It is worth recording why one generator is not enough. With $U=e^{iS_1}$ taken exactly, the odd remainder $O_1$ survives: the leading generator removes the leading odd term and nothing more, and the displayed $H_2$ is what remains at that order. The generator is a series, $S=S_1+S_2+\cdots$, and each term removes one order. The free particle is the exception, and the next section is about it: there the series terminates and a single closed-form exponential does the whole job at once.

### The Second Transformation and the Iteration

The odd remainder of the first step is $O_1$, of relative order $v^2/c^2$ compared with $O$. The same algorithm applied to it removes it, with the generator displayed above, and leaves a new odd remainder of relative order $v^4/c^4$; call that one $O_2$, and continue. The procedure iterates: at each stage the odd part of the next order is conjugated away by a generator proportional to it, and the new odd residual is two powers of $v/c$ smaller. The resulting expansion of the transformed Hamiltonian is the systematic $1/c$ expansion of the Dirac theory, and its convergence criterion is the physically transparent one,

$$
\frac{|\vec\pi|}{mc}\ll1 ,
$$

i.e. particle momenta small compared with $mc$. When the criterion fails the iteration still exists term by term but no longer converges to a useful separation: the notion of a particle component is momentum-dependent and becomes meaningless in the ultra-relativistic regime.

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

that is, $UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})\sqrt{\vec p^2c^2+m^2c^4}$ exactly. In this language the exact generator is $S=S_1\,\theta/\tan\theta$, since $S_1=-\tfrac{i}{2}A\tan\theta$ and $iS=\tfrac{1}{2}A\theta$; it reduces to $S_1$ as $\theta\to0$; the factor $\theta/\tan\theta\le1$ is the whole of the relativistic correction to the non-relativistic generator. The upper block is the relativistic energy $+E$, the lower block is $-E$, and the odd part has been removed to all orders. The leading expansion of the closed form reproduces the result of the previous section:

$$
(iR_{\vec e_x}^{\mathrm{axf}})E=(iR_{\vec e_x}^{\mathrm{axf}})\Bigl(mc^2+\frac{\vec p^2}{2m}-\frac{\vec p^4}{8m^3c^2}+\cdots\Bigr),
$$

the $\vec p^4$ term being the first relativistic correction to the kinetic energy. The closed form was checked numerically: with $\tan\theta=|\vec p|/(mc)$ and $U=\cos(\theta/2)+A\sin(\theta/2)$, the identity $UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})E$ holds to machine precision, at the $10^{-14}$ level for a generic three-momentum and every value of $|\vec p|/(mc)$ tested.

## The Mean Position Operator

The transformation does more than block-diagonalise the Hamiltonian: it also changes which operator plays the role of position. Write the position as the material vector $\vec q=\sum_kQ_k\vec e_k$, with $Q_k$ the operator of multiplication by the coordinate. In the transformed frame that multiplication is the coordinate, so the operator carrying it back to the original frame is obtained by conjugating with $U^\dagger$, not with $U$:

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

The correction $\frac{\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ is itself worth reading in the algebra. It is an odd, spinorial displacement: it contains the same odd cells that generate the transformation, it anticommutes with the timelike frame cell, and it is the first term in the expansion of the mean position in powers of $1/m$. It is not a measurement of the particle's size; it is the statement that the coordinate conjugate to the block-diagonal Hamiltonian is not the coordinate conjugate to the original field. The operator $\vec X$ does not have commuting components, and it is not Lorentz covariant in the naive sense — the Newton–Wigner operator is the covariant completion of it — a fact already visible in the biquaternion framework as the difference between a material position $\vec q$ and a configuration-space position on the module.

## The Biquaternion Reading

The transformation can now be located in the two gradings of the algebra, and the location is the content of the article.

**The chirality basis is where the biquaternion pair lives.** The massive biquaternionic Dirac equation is the off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$. In the chiral (Weyl) basis the timelike frame cell is off-diagonal, so the mass term of the Hamiltonian, $mc^2(iR_{\vec e_x}^{\mathrm{axf}})$, is the off-diagonal matrix

$$
mc^2\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},
$$

and all four frame cells are block off-diagonal there, so the first-order operator $\mathcal{D}$ is block off-diagonal too, while the velocity cells $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ are block diagonal. This is the basis in which the two components are the minimal left ideal $S$ and its conjugate $S^{\mathrm{c}}$, and in which the mass couples them: the mass, and the gradient, are the **off-diagonal** objects in this basis.

**The frame basis is where the FW transformation works.** In the Dirac (large/small) basis the timelike frame cell is diagonal, $iR_{\vec e_x}^{\mathrm{axf}}\mapsto\mathrm{diag}(I_2,-I_2)$, and the mass term $mc^2(iR_{\vec e_x}^{\mathrm{axf}})$ is diagonal; the kinetic term $c\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k$ is the off-diagonal odd piece. The two bases are related by the fixed $*$-unitary $\frac{1}{\sqrt2}(iR_{\vec e_x}^{\mathrm{axf}}-iR_{\vec e_z}^{\mathrm{axf}})$, which is its own inverse and exchanges $iR_{\vec e_x}^{\mathrm{axf}}$ with $-iR_{\vec e_z}^{\mathrm{axf}}$, together with the relabelling of the four components that brings the two large ones together — the unitary alone gives the diagonal $\mathrm{diag}(-1,1,-1,1)$, not $\mathrm{diag}(I_2,-I_2)$. The FW transformation is the momentum-dependent completion of that exchange: it rotates the field so that the mass — off-diagonal in chirality — becomes diagonal, while the kinetic term, which was diagonal in chirality, becomes the first-order perturbation. Removing the odd part is exactly the statement that the mass is the large term and the mixing is small.

**The transformation does not separate chirality.** After the transformation the Hamiltonian is block diagonal in the large/small basis, not in the chiral basis. The chirality cell in the transformed basis is momentum-dependent:

$$
(-iR_{\vec e_z}^{\mathrm{axf}})^{FW}=U(-iR_{\vec e_z}^{\mathrm{axf}})U^\dagger=(-iR_{\vec e_z}^{\mathrm{axf}})\exp(-A\theta).
$$

Read in the Dirac basis, its upper block is $(\boldsymbol\sigma\cdot\vec u_p)\sin\theta=(\boldsymbol\sigma\cdot\vec u_p)\,|\vec p|c/E$ — the helicity for a massless field, reduced by the factor $|\vec p|c/E$ for a massive one — and its off-block part is $\cos\theta\,I_2=(mc^2/E)I_2$, which is the chirality-mixing term and is of relative order $m/|\vec p|$ in the ultra-relativistic regime. The FW transformation therefore separates **positive from negative frequency**, the two signs of the timelike frame cell, and not left from right. In the algebra, the grading it diagonalises is the grading by $iR_{\vec e_x}^{\mathrm{axf}}$, the reflection of *The Reflection and the Rotation in Biquaternionic Form*; the chirality grading is the grading by $-iR_{\vec e_z}^{\mathrm{axf}}$, a different reflection, and no $*$-unitary rotation of the field can diagonalise both at once because the two cells anticommute. The FW basis and the chiral basis are complementary, and the mass is the object that measures their incompatibility.

**The generator lies outside the algebra's rotors.** The biquaternion rotors are the even, unit-norm elements of $\mathbb{B}$; they act on the module and generate the Lorentz group. The FW generator $S_1=\frac{1}{2mc}\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\pi_k$ is a sum of odd cells and does not belong to the even subalgebra $\mathrm{Cl}^{+}_{1,3}$. The FW transformation is therefore not one of the algebra's own rotations: it is a transformation in the full cell algebra that adjoins the odd part. The biquaternion content it carries is not a new rotor but the identification of the odd part $O$ with the frame-odd mixing term and of the diagonal mass with the frame-even large term. This is consistent with the reflection article's finding that the frame is required to state chirality and parity: the FW transformation needs the frame for the same reason.

## The Pauli Limit and the Residual Terms

With an external electromagnetic field, $\pi_k=p_k-ϙA_k$, and the FW-transformed Hamiltonian acquires the standard non-relativistic terms. The kinetic term is where the spin enters, through the algebra of the velocity cells combined with the non-commutativity of the momentum components. Two velocity cells multiply into the spin cell $iL_{\vec e_l}^{\mathrm{axf}}$,

$$
L_{\vec e_j}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\,L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=\delta_{jk}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}+i\,\epsilon_{jkl}\,(iL_{\vec e_l}^{\mathrm{axf}}),
$$

which squares to $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and, in the Dirac basis, is $\sigma_l$ in each $2\times2$ block. The symmetric part of the product gives $\vec\pi^2$; the antisymmetric part contracts with the commutator of the momenta and survives:

$$
O^2=c^2\Bigl(\vec\pi^2-ϙ\hbar\sum_l(iL_{\vec e_l}^{\mathrm{axf}})B_l\Bigr),
\qquad
[\pi_j,\pi_k]=i\hbarϙ\,\epsilon_{jkl}B_l .
$$

Since $iL_{\vec e_l}^{\mathrm{axf}}$ is block diagonal, each $2\times2$ block sees $\sigma_l$, and $\frac{(iR_{\vec e_x}^{\mathrm{axf}})O^2}{2mc^2}$ already contains the Zeeman coupling $-\frac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B$ with the gyromagnetic factor $g=2$. The second transformation, with the generator $S_2$ above, adds the terms of relative order $v^2/c^2$. To this order the upper block is the Pauli Hamiltonian

$$
\boxed{\;
\begin{aligned}
H_{\mathrm{Pauli}}
&=\frac{\vec\pi^2}{2m}+ϙA_0-\frac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B\\[2pt]
&\quad-\frac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
+\frac{\hbar^2}{8m^2c^2}\nabla^2(ϙA_0),
\end{aligned}
\;}
$$

whose terms beyond the leading kinetic and electrostatic ones are the spin–Zeeman term, the spin–orbit coupling and the Darwin term — the coefficient $1/(4m^2c^2)$ of the spin–orbit term already contains the Thomas factor of $\frac12$ — together with the relativistic kinetic correction $-\bigl(\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\pi_k\bigr)^4/(8m^3c^2)$, which in the upper block reads $-(\boldsymbol\sigma\cdot\vec\pi)^4/(8m^3c^2)$ and is the field version of the free term $-\vec p^4/(8m^3c^2)$ displayed above. The difference between that and $\vec\pi^4$ is itself of order $c^{-2}$, because $O^2/c^2$ differs from $\vec\pi^2$ by the Zeeman term, so it is the spinor form that belongs at this order. The companion exercise *Exercise: The Non-Relativistic Limit and the Pauli Equation* derives each in the biquaternion framework; they are quoted here as the standard content of the transformation. For the electrostatic case $\vec E=-\nabla A_0$, the Darwin term has the equivalent forms

$$
\frac{\hbar^2}{8m^2c^2}\nabla^2(ϙA_0)=-\frac{ϙ\hbar^2}{8m^2c^2}\nabla\cdot\vec E .
$$

The point to record is structural: every correction is **even** under the frame grading — each is a scalar or a spin–magnetic coupling, none couples the large and small blocks — which is the statement that the transformation has succeeded in removing the odd part to the stated order. The residual odd terms, suppressed by a further factor of $v^2/c^2$ relative to $O$, are removed by $S_2$.

The lower block is the same Hamiltonian with the sign of the timelike frame cell reversed: it is $-E=-mc^2-\vec\pi^2/(2m)+\cdots$, the mirror image of the upper block, separated from it by the mass gap $2mc^2$. Factoring out the rest-energy phase, as the companion article does, gives the antiparticle Hamiltonian: the same kinetic and spin terms, and the opposite charge, so that the potential term is $-ϙA_0$. That sign reversal is charge conjugation, and it is what the two sectors differ by once the rest energy is removed. This is the sense in which the FW transformation separates particles from antiparticles: not by projecting them apart, which the fields do not allow, but by diagonalising the Hamiltonian so that the gap is manifest and the mixing is small.

## What Is Standard and What the Algebra Adds

The transformation, the generator $S_1$, the leading Hamiltonian $iR_{\vec e_x}^{\mathrm{axf}}mc^2+(iR_{\vec e_x}^{\mathrm{axf}})O^2/(2mc^2)$, the closed free-particle form $(iR_{\vec e_x}^{\mathrm{axf}})E$, the mean position operator and the Pauli limit are all standard results, transcribed here from the relativistic-quantum-physics literature and cited as such. The biquaternion contribution is not a new formula but a placing:

- The **two gradings** are kept distinct. The FW transformation diagonalises the frame grading (large/small, $iR_{\vec e_x}^{\mathrm{axf}}$); the biquaternion mass pair is the chirality grading (left/right, $-iR_{\vec e_z}^{\mathrm{axf}}$). They anticommute, so the transformation cannot diagonalise both, and the mass is the obstruction.
- The **mass term** appears in the transformation as the large, frame-even term whose diagonal form is the non-relativistic gap; in the chiral basis the same mass is the off-diagonal coupling of the biquaternion pair. The passage between the two descriptions starts from the fixed $*$-unitary $\frac{1}{\sqrt2}(iR_{\vec e_x}^{\mathrm{axf}}-iR_{\vec e_z}^{\mathrm{axf}})$ that exchanges the two cells, and the FW transformation is its momentum-dependent completion.
- The **residual odd part** is the frame-odd mixing term $O$, and its removal order by order is the statement that positive and negative frequency decouple in the non-relativistic limit.
- The **exact free form** shows that the separation, for a free field, is exact: $UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})\sqrt{\vec p^2c^2+m^2c^4}$ with $U=\exp\bigl(\frac{\theta}{2}(iR_{\vec e_x}^{\mathrm{axf}})\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}u_k\bigr)$ and $\tan\theta=|\vec p|/(mc)$. The expansion used by the non-relativistic reduction is the expansion of this closed form in $|\vec p|/(mc)$.

The transformation was constructed here with the large term being the mass. If an external potential dominates, the same algorithm is applied with a different even large term, and the generator changes accordingly; the algebra reads this as a different choice of frame. The choice of frame is the physical input, and the rest is the rotation that aligns the odd part with it.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. This is the only section of the article that uses them; every other statement is written in cells.

Here $L_a$ and $R_b$ are the left and right multiplications.

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

A single product is a pure tensor, a cell of rank one; a general element is a sum of at most four of them, one for each term of the rank decomposition of its coefficient matrix in the cell basis.

In terms of the vector generators this is the standard $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ of the $(+,-,-,-)$ convention: the product $\gamma_0\gamma_1\gamma_2\gamma_3$ is the cell $-R_{\vec e_z}^{\mathrm{pau}}$ computed above, so $i\gamma_0\gamma_1\gamma_2\gamma_3=-iR_{\vec e_z}^{\mathrm{pau}}=\gamma_5$. Thus $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell itself. The central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The $\gamma$'s are a complex frame, not a real one: they generate $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$ over $\mathbb{C}$, whereas the cells with real coefficients generate the real algebra $\mathrm{Cl}_{3,1}(\mathbb{R})=M_4(\mathbb{R})$. It is the complexification that makes the scalar $i$ central, and that is why each generator is written as $i$ times a real cell.

**The identities the series uses.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$

Four contraction sums accompany them, and they are frame statements, because a cell's square is. Writing $\gamma_\mu^2=\epsilon_\mu I_4$ and $S=\sum_\mu\epsilon_\mu$, the sums over a product $\Gamma$ of $p$ distinct frame cells are

$$
\sum_\mu\gamma_\mu\Gamma\gamma_\mu=(-1)^p\Bigl(S-2\sum_{i\in\Gamma}\epsilon_i\Bigr)\Gamma ,
$$

where the second sum runs over the indices carried by $\Gamma$. The rule is checked in the $\mathbb{M}_-$ frame, $\epsilon=(+1,-1,-1,-1)$ and $S=-2$:

$$
\sum_\mu\gamma_\mu\gamma_\mu=S\,I_4=-2I_4,
\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=\bigl(2\epsilon_\alpha-S\bigr)\gamma_\alpha ,
$$

$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=\bigl(S-2\epsilon_\alpha-2\epsilon_\beta\bigr)\gamma_\alpha\gamma_\beta\quad(\alpha\ne\beta),
$$

$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu
=\bigl(2\epsilon_\alpha+2\epsilon_\beta+2\epsilon_\gamma-S\bigr)\gamma_\alpha\gamma_\beta\gamma_\gamma
\quad(\alpha,\beta,\gamma\ \text{distinct}).
$$

The second sum is $4\gamma_0$ for $\alpha=0$ and vanishes for spacelike $\alpha$; the third is $2\gamma_\alpha\gamma_\beta$ when both indices are spacelike and $-2\gamma_\alpha\gamma_\beta$ when one of them is timelike; the fourth is $-4\gamma_\alpha\gamma_\beta\gamma_\gamma$ for a spacelike triple and zero when a timelike index appears. In a Euclidean frame, where every cell squares to $+I_4$ and $S=4$, the bracket is $4-2p$ and the textbook values follow:

$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,
$$

$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=-2\,\gamma_\gamma\gamma_\beta\gamma_\alpha ,
$$

the last two with the convention that repeated indices are read separately, since $\gamma_\alpha\gamma_\alpha=\epsilon_\alpha$ and the sum then collapses to the lower grade.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Foldy–Wouthuysen transformation is the $*$-unitary $U=\exp(iS)$ that block-diagonalises the Dirac Hamiltonian in the frame grading, separating the positive- and negative-frequency sectors. With

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

in the free case $\mathcal{E}=0$ this is the Schrödinger Hamiltonian in the upper block and its negative in the lower block. For the free particle the transformation is exact:

$$
U=\cos\frac{\theta}{2}+(iR_{\vec e_x}^{\mathrm{axf}})\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}u_k\sin\frac{\theta}{2},
\qquad
\tan\theta=\frac{|\vec p|}{mc},
$$

$$
\boxed{\;UHU^\dagger=(iR_{\vec e_x}^{\mathrm{axf}})\sqrt{\vec p^2c^2+m^2c^4}\;},
$$

checked to machine precision by direct matrix computation. The mean position is the operator whose image in the transformed frame is multiplication by the coordinate,

$$
\vec X=U^\dagger\vec q\,U=\sum_kX_k\vec e_k,
\qquad
X_k=Q_k-\frac{\hbar}{2mc}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}+\cdots ,
$$

whose Heisenberg velocity commutes with the Hamiltonian and so has no trembling term; the Zitterbewegung resides in the difference $\vec q-\vec X$.

The biquaternion interpretation turns on two gradings that must not be conflated. The frame grading, conjugation by $iR_{\vec e_x}^{\mathrm{axf}}$, is what the FW transformation diagonalises and in which the mass is diagonal; the chirality grading, $-iR_{\vec e_z}^{\mathrm{axf}}$, is what the biquaternion mass pair is written in and in which the mass is off-diagonal. The two gradings anticommute, so no single $*$-unitary diagonalises both, and the mass term is the measure of their incompatibility. The FW generator is a sum of odd cells and therefore lies outside the even subalgebra $\mathrm{Cl}_{1,3}^{+}$: the transformation is not one of the algebra's Lorentz rotors but a transformation in the full cell algebra that adjoins the odd part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_\pm$ | Hermitian ($+$) and anti-Hermitian ($-$) sectors; $\mathbb{M}_-$ is the material sector |
| $L_{a}R_{b}$ | Cell, the two-sided multiplication of *Operator Family Conventions* |
| $iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | Timelike frame cell; $(iR_{\vec e_x}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Velocity cells; $(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=(iR_{\vec e_x}^{\mathrm{axf}})(L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}})$ | Spacelike frame cells; square $-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $iL_{\vec e_l}^{\mathrm{axf}}$ | Spin cell: left multiplication by $i\vec e_l$; $(iL_{\vec e_l}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, block-wise $\sigma_l$ |
| $-iR_{\vec e_z}^{\mathrm{axf}}=i\,\omega$, $\omega=(iR_{\vec e_x}^{\mathrm{axf}})(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})(iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})=-L_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell; $(-iR_{\vec e_z}^{\mathrm{axf}})^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $ϙ$ | Charge of the field; $A_\mu=(A_0,-\vec A)$ |
| $g = \mathrm{diag}(-1,+1,+1,+1)$ | Clifford metric; used only in *The Legacy Gamma Formulation* |
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
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | One-sided mass pair (chirality grading) |
| $\Box$ | Series d'Alembertian |

## Further Reading

- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the transformation and the mean position operator.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the generator, the block-diagonalisation, and the non-relativistic expansion.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the Pauli limit and the spin–orbit and Darwin terms.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac Hamiltonian, the Dirac algebra and the Foldy–Wouthuysen reduction.
- L. L. Foldy, "The electromagnetic properties of Dirac particles," *Physical Review* **87** (1952) 688–693, for the mean position and its electromagnetic couplings.
- M. E. Rose, *Relativistic Electron Theory* (Wiley, 1961), for the systematic $1/c$ expansion.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the detailed treatment of the Foldy–Wouthuysen transformation and its applications.
- P. Strange, *Relativistic Quantum Mechanics* (Cambridge, 1998), for the transformation in the presence of external fields.
