# __The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral__

## Introduction

Two articles of this series already treat Maxwell's equations quaternionically: *Maxwell's Equations in the Biquaternionic Formulation* reduces the full time-dependent system to the single equation $\tilde\nabla\tilde F=-\tilde R$, and *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* diagonalises the time-harmonic system of a magnetoelectric medium into two Beltrami equations. What neither carries is the **ordinary** time-harmonic system — the one of a homogeneous isotropic medium, possibly lossy, with charges and currents — and the integral theory that belongs to it. That is the subject of this article, and the medium here has no chirality: it is the $\beta=0$ case of the chiral reduction, but with sources, and with the operator theory that the sources require.

The source is the founding paper of the series: V. V. Kravchenko and M. V. Shapiro, *Quaternionic time-harmonic Maxwell operator*, *Journal of Physics A* **28** (1995) 5017–5031. It is among the earliest peer-reviewed papers of the quaternionic-analysis programme, and it established the result that this article records: a **one-to-one correspondence between time-harmonic electromagnetic fields and pairs of mutually conjugate hyperholomorphic functions**, and with it a **Cauchy-type integral for Maxwell's equations**. The same material, in book form and with the boundary-value problem worked out, is in V. V. Kravchenko, *Applied Quaternionic Analysis* [2003], Sections 3.1–3.3, which is used here for the clean statements; where the two differ in arrangement the book's form is taken and the difference is noted.

The claim of the paper is stronger than a reformulation. Its authors introduce "a somewhat more general quaternionic object which has better algebraic and analytic properties than the 'physical' Maxwell operator and which contains the latter as a special case". The object is a $2\times2$ matrix of first-order operators, and this is what its betterness consists in: it acts on **all** pairs of complex-quaternionic functions, not only on divergence-free vector pairs, and its square is a **scalar** Helmholtz operator. The physical Maxwell operator is the awkward member of the family — defined only on a subspace, with a vector-valued square — and the strategy the authors draw from that is the strategy this literature uses throughout: **work in the general family and specialise at the end**.

The theory was announced in the same period in a short note, V. V. Kravchenko, "Quaternion-valued integral representations of the harmonic electromagnetic and spinor fields", *Doklady Mathematics* **51** (1995), no. 2, 287–289, cited here for the **unification** it states. The general system of Kravchenko and Shapiro is one parametric system with a parameter $a\in\mathbb{B}$, and the note's point is that at one value of the parameter it is the time-harmonic **Maxwell** system and at another it is the time-harmonic **Dirac** system; the Cauchy integral formula, the Sokhotski formulas and the boundary-value problems are therefore obtained for the two fields "from the common point of view", and the boundary problems are presented as the analogues, for these equations, of analytic continuation in the theory of a complex-valued function. The Maxwell half is this article; the Dirac half, with the sense in which one Cauchy theory serves both, is in *The Dirac Equation in Biquaternionic Form*.

The plan is the diagonalisation and then its consequences. The next section fixes the time-harmonic system and its Helmholtz reduction. The section after introduces the quaternionic Maxwell operator and shows what it is better for. Then the diagonalisation into the two conjugate Cauchy–Riemann equations, the correspondence it gives, and the decomposition of the Helmholtz null-set into two rotated halves. The remaining sections give the Maxwell–Cauchy kernel, the integral operators that go with it, the integral representations of the field — whose vector form is the classical Stratton–Chu formula — and the boundary-value problem that the same theory solves.

## The Time-Harmonic System in a Homogeneous Medium

The convention is $e^{-i\omega t}$, so that $\partial_t\to-i\omega$ and a monochromatic field is its complex amplitude. The medium is homogeneous and isotropic, and its response is carried by two possibly complex constants: the permittivity $\epsilon$ and the permeability $\mu$, so that the loss tangent of the dielectric and the inertia of the polarisation processes are both representable by making $\epsilon$ complex. The ohmic conduction of the medium enters separately, through the real conductivity $\sigma_*$, and the two are combined into a single **complex conductivity**

$$
\sigma:=\sigma_*-i\omega\epsilon ,
$$

which is the quantity the first Maxwell equation carries. With charges and currents present, and with the divergence equations kept explicitly as the source contains them, the time-harmonic Maxwell system is

$$
\mathrm{rot}\,\mathbf{H}=\sigma\mathbf{E}+\mathbf{j},
\qquad
\mathrm{rot}\,\mathbf{E}=i\omega\mu\mathbf{H},
\qquad
\mathrm{div}\,\mathbf{E}=\frac{\rho}{\epsilon},
\qquad
\mathrm{div}\,\mathbf{H}=0 .
\tag{1}
$$

The fourth equation is not independent: taking the divergence of the second shows $\mathrm{div}\,\mathbf{H}=0$, and taking the divergence of the first gives the time-harmonic continuity equation

$$
\mathrm{div}\,\mathbf{j}-i\omega\rho=0 ,
\tag{2}
$$

which is what fixes the sources, not the fields. Two remarks separate this system from the ones already in the series. First, no magnetoelectric coupling appears: the constitutive relations are the ordinary $\mathbf{D}=\epsilon\mathbf{E}$ and $\mathbf{B}=\mu\mathbf{H}$, and the second equation of $(1)$ has no $\mathrm{rot}\,\mathbf{H}$ term on its right. Second, the conduction is not a source but a part of the medium: absorbing $\sigma_*$ into $\sigma$ makes the medium lossy while leaving the shape of the system unchanged.

Eliminating one field in the usual way gives the **Helmholtz reduction**. Applying the curl to the second equation of $(1)$ and using the first, and then using $\mathrm{rot}\,\mathrm{rot}=\mathrm{grad}\,\mathrm{div}-\Delta$, the two complex amplitudes satisfy the homogeneous Helmholtz equations wherever the sources vanish,

$$
\Delta\mathbf{E}+\lambda\mathbf{E}=0,
\qquad
\Delta\mathbf{H}+\lambda\mathbf{H}=0,
\qquad
\lambda:=i\omega\mu\sigma_*+\omega^2\mu\epsilon ,
\tag{3}
$$

with the same constant for both. The parameter $\lambda$ is the square of the medium wavenumber:

$$
\alpha^2=\lambda,
\qquad
\operatorname{Im}\alpha\ge0 ,
$$

and it is this $\alpha$ — not $\omega\sqrt{\epsilon\mu}$ — that the function theory of the article runs on when conduction is present. In the lossless case $\sigma_*=0$ the two agree, $\lambda=\omega^2\mu\epsilon$,

$$
k=\omega\sqrt{\epsilon\mu}=\frac{\omega}{c},
\qquad
c=\frac{1}{\sqrt{\epsilon\mu}} ,
$$

and $\alpha=k$ is the ordinary medium wavenumber of *Electromagnetism in Media — The Local Complex Structure at Work*. The lossy case is therefore not a new theory but the same theory with a complex wavenumber, and every statement below is written for the complex $\alpha$ with the lossless case recovered by $\alpha\to k$.

One property of the sourceless system is worth recording because it is what makes the transcription into the function theory possible at all: the fields of a solution with $\mathbf{j}=0$ and $\rho=0$ are transverse,

$$
\mathrm{div}\,\mathbf{E}=\mathrm{div}\,\mathbf{H}=0 ,
\tag{4}
$$

so that the curl in the first two equations of $(1)$ can be replaced by the full Cauchy–Riemann operator. A remark belongs here, because the neighbouring statement is easy to make wrongly. For a single plane wave the electric and magnetic amplitudes are orthogonal as well as transverse, and orthogonality is sometimes recorded as a property of the solutions of the time-harmonic system. It is not a pointwise property of a general solution: for a superposition of two plane waves of the same wavenumber the scalar product $\langle\mathbf{E},\mathbf{H}\rangle$ is generally non-zero, because it is bilinear in the two amplitudes and vanishes only for the single-wave configurations, while $(4)$ holds for every solution. What carries the structure below is therefore the operator identity $(5)$ and the transversality $(4)$, not a pointwise relation between the two fields.

## The Quaternionic Maxwell Operator

The spatial operator is the Moisil–Theodoresco operator of the series,

$$
D_3=e_1\partial_1+e_2\partial_2+e_3\partial_3,
\qquad
D_3^2=-\Delta ,
$$

and its action on a purely vectorial biquaternion is the identity that carries the whole transcription. For a pure vector $\mathbf{f}$,

$$
D_3\mathbf{f}=-\mathrm{div}\,\mathbf{f}+\mathrm{rot}\,\mathbf{f},
\qquad\text{so}\qquad
D_3\mathbf{f}=\mathrm{rot}\,\mathbf{f}\quad\text{whenever }\mathrm{div}\,\mathbf{f}=0 .
\tag{5}
$$

The curl is therefore the restriction of the Cauchy–Riemann operator to the divergence-free vectors, and a first-order system in curls can be written as a first-order quaternionic system. This is the step that puts the time-harmonic Maxwell system inside the function theory of $D_3$.

With the fields read as purely vectorial biquaternions, define the **quaternionic Maxwell operator** as the $2\times2$ matrix of first-order operators

$$
N:=\begin{pmatrix} D_3 & -i\omega\mu \\[2pt] -\sigma & D_3 \end{pmatrix},
\qquad
N:\ \mathbb{B}^2\longrightarrow\mathbb{B}^2 .
\tag{6}
$$

Its action is transparent: on a pair $(\mathbf{E},\mathbf{H})$,

$$
N(\mathbf{E},\mathbf{H})
=\bigl(D_3\mathbf{E}-i\omega\mu\mathbf{H},\ D_3\mathbf{H}-\sigma\mathbf{E}\bigr)
=\Bigl(-\frac{\rho}{\epsilon},\ \mathbf{j}\Bigr),
\tag{7}
$$

the second equality being $(5)$ applied to each component and the system $(1)$ used in the form $D_3\mathbf{E}-\mathrm{rot}\,\mathbf{E}=-\rho/\epsilon$ and $D_3\mathbf{H}-\mathrm{rot}\,\mathbf{H}=\mathbf{j}$. On the sourceless system, therefore, the time-harmonic fields are exactly the pairs annihilated by $N$. On the pairs of **divergence-free** vectors, $D_3$ acts as the curl, and the restriction of $N$ to those pairs is the matrix of the curl system,

$$
N\big|_{\mathrm{div}=0}=\begin{pmatrix} \mathrm{rot} & -i\omega\mu \\[2pt] -\sigma & \mathrm{rot} \end{pmatrix},
$$

which is the physical time-harmonic Maxwell operator $M$ up to the ordering of the two rows, with the solenoidal pairs as its natural domain. The difference between the two is exactly what the source means by a "better" object. The domain of the physical operator is a subspace cut out by the divergence conditions, so that the system can only be posed on pairs satisfying them and the operator cannot be iterated without re-imposing them; the domain of $N$ is all pairs of complex-quaternionic functions, with no side condition at all. And the algebra improves with the domain:

$$
N N^{\dagger}=-(\Delta+\lambda)\,I_2,
\qquad
N^{\dagger}=\begin{pmatrix} D_3 & i\omega\mu \\[2pt] \sigma & D_3 \end{pmatrix},
\tag{8}
$$

as a direct computation with $D_3^2=-\Delta$, with the off-diagonal cross terms cancelling because the coefficients are scalars and commute with $D_3$. The square of the quaternionic Maxwell operator is thus a **scalar** Helmholtz operator, exactly as the square of the Dirac operator is a scalar d'Alembertian — the operator is of Dirac type, and $(8)$ is the factorisation on which the function theory rests. That factorisation is what the physical operator lacks: the vector Helmholtz operator is not the square of a first-order operator with scalar symbol, which is why no analogue of the Cauchy kernel exists for the curl system directly, and why the detour through $N$ is what makes one available.

The relation between the two operators is not merely a containment. Written in matrix-vector form, the time-harmonic system is $M(\mathbf{E},\mathbf{H})=0$ on solenoidal pairs, and $N$ restricted to those pairs has the same null-set; but the restriction of $N$ to all pairs is the object with the scalar square $(8)$, and it is by working there that the integral theory is built. This is the generalisation strategy stated in the introduction: the general operator is the tool, and the physical operator is recovered as a restriction.

## The Diagonalisation and the Two Conjugate Function Theories

The scalar square $(8)$ already says that a pair annihilated by $N$ is metaharmonic, that is, a solution of $(\Delta+\lambda)I_2$. The sharper statement is that $N$ is, by a similarity, a **direct sum of two first-order operators**, and that the two are conjugate. With $\alpha$ a square root of $\lambda$ and

$$
b:=\frac{i\omega\mu}{\alpha},
\tag{9}
$$

form the two combinations

$$
\Phi:=\mathbf{E}+b\,\mathbf{H},
\qquad
\Psi:=\mathbf{E}-b\,\mathbf{H},
\qquad
\mathbf{E}=\tfrac12(\Phi+\Psi),
\qquad
\mathbf{H}=\frac{1}{2b}(\Phi-\Psi).
\tag{10}
$$

Then the change of variables $(10)$ conjugates $N$ to a diagonal operator:

$$
C\,N\,C^{-1}
=\begin{pmatrix} D_3-\alpha & 0 \\[2pt] 0 & D_3+\alpha \end{pmatrix},
\qquad
C=\begin{pmatrix} 1 & b \\[2pt] 1 & -b \end{pmatrix},
\qquad
C^{-1}=\frac12\begin{pmatrix} 1 & 1 \\[2pt] b^{-1} & -b^{-1} \end{pmatrix}.
\tag{11}
$$

The verification is two lines. The first row of $CN$ is $\bigl(D_3-b\sigma,\ -i\omega\mu+bD_3\bigr)$, and $b\sigma=(i\omega\mu/\alpha)\sigma=i\omega\mu\sigma/\alpha=\alpha^2/\alpha=\alpha$, so that row is $\bigl(D_3-\alpha,\ b(D_3-\alpha)\bigr)$; the second row is $\bigl(D_3+\alpha,\ -b(D_3+\alpha)\bigr)$. Multiplying on the right by $C^{-1}$ cancels the off-diagonal entries, because the two contributions to each are equal and opposite, and leaves $D_3\mp\alpha$ on the diagonal, which is $(11)$. In the sourceless case the two diagonal equations are therefore

$$
\bigl(D_3-\alpha\bigr)\Phi=0,
\qquad
\bigl(D_3+\alpha\bigr)\Psi=0 ,
\tag{12}
$$

and with sources they read $(D_3-\alpha)\Phi=-\rho/\epsilon+b\,\mathbf{j}$ and $(D_3+\alpha)\Psi=-\rho/\epsilon-b\,\mathbf{j}$, the pair of scalar equations into which $(7)$ factors.

Each of equations $(12)$ is an equation of the shifted or **$\alpha$-hyperholomorphic** type — the class $\ker(D_3\mp\alpha)$ — whose function theory is the subject of *Biquaternion Regular Functions* and its physics companion. The operators $D_3-\alpha$ and $D_3+\alpha$ are the **mutually conjugate** Cauchy–Riemann operators of the paper, and their squares are the scalar Helmholtz operators of opposite sign,

$$
-(D_3-\alpha)(D_3+\alpha)=-(D_3+\alpha)(D_3-\alpha)=\Delta+\alpha^2 ,
\tag{13}
$$

which is $(8)$ seen through the diagonalisation: the two factors multiply to the Helmholtz operator, and each is a square root of it up to the conjugation. The factorisation $(\Delta+\alpha^2)=-(D_3+\alpha)(D_3-\alpha)$ is the three-dimensional case of $\Box=\tilde\nabla\bar{\tilde\nabla}$, and it is the exact computation that makes the time-harmonic Maxwell system a pair of hyperholomorphic problems.

This gives the paper's central theorem. Because $(11)$ is invertible, the pairs annihilated by $N$ are in bijection with the pairs annihilated by the diagonal operator, that is, with the pairs $(\Phi,\Psi)$ whose first component is $\alpha$-hyperholomorphic and whose second is $\alpha$-hyperholomorphic for the conjugate operator:

$$
\ker N
\;\cong\;
\ker(D_3-\alpha)\times\ker(D_3+\alpha) .
\tag{14}
$$

The correspondence is **one-to-one**, and it is this, not the mere rewriting of the curl equations, that the article records: a time-harmonic electromagnetic field in a homogeneous medium is the same object as a pair of mutually conjugate hyperholomorphic functions, and the map between the two descriptions is the explicit matrix $C$ of $(11)$. Every property of the pair — the Cauchy integral formula, the mean value property, the removable singularities — is then a property of the field, and every operation on the field has a reading in the function theory. The value of the quaternionic formulation is exactly this transfer, and it is why the source insists that the general operator is worth more than the physical one.

The lossless normalised variables of the chiral article are the special case $\sigma_*=0$, and they are worth spelling out because they connect the present article to the rest of the series. With $\tilde{\mathbf{E}}=\mathbf{E}/\sqrt{\mu}$ and $\tilde{\mathbf{H}}=\mathbf{H}/\sqrt{\epsilon}$ and $\sigma_*=0$ one has $\alpha=k$, the coherence factor $(9)$ is $b=i\sqrt{\mu/\epsilon}=iZ$, the impedance, and $(10)$ becomes, up to the common factor $\sqrt{\mu}$,

$$
\Phi\propto\tilde{\mathbf{E}}+i\tilde{\mathbf{H}},
\qquad
\Psi\propto\tilde{\mathbf{E}}-i\tilde{\mathbf{H}},
$$

which are precisely the two circularly polarised combinations $\Phi,\Psi$ of the chiral reduction at $\beta=0$. The Beltrami vector form follows from $(5)$: on a pure vector, $(D_3\mp\alpha)\mathbf{f}=0$ is $\mathrm{rot}\,\mathbf{f}=\pm\alpha\mathbf{f}$ together with the divergence condition, so $(12)$ is the pair of Beltrami equations of the ordinary medium, and the classical vector form is recovered from the quaternionic one. The reformulation is thus the $\beta=0$ case of the chiral reduction of the series, with the function theory attached, and it is the function theory — not the vector form — that is new.

## The Helmholtz Null-Set as Two Rotated Copies of the Maxwell Null-Set

There is a second structural theorem, which the source states for the Helmholtz null-set. Let

$$
\mathcal{R}_\lambda:=\ker\bigl((\Delta+\lambda)I_2\bigr)
$$

be the space of pair-valued metaharmonic functions, that is, of pairs whose two components are solutions of the Helmholtz equation with the same $\lambda$. The factorisation $(8)$ shows at once that $\ker N$ sits inside it, since $(\Delta+\lambda)f=-N N^{\dagger}f$, but the sharper statement is that $\mathcal{R}_\lambda$ is the **direct sum of two rotated copies of $\ker N$**. The two rotations are the two orientations of the conjugating matrix, and the two summands are the images of two complementary projections

$$
Q_1+Q_2=I,
\qquad
Q_i^2=Q_i,
\qquad
Q_1Q_2=Q_2Q_1=0 ,
\tag{15}
$$

built from the matrices $A_i,B_i$ that realise the similarity $(11)$ in each of its two orientations; the projections are the two halves into which the diagonalisation splits the metaharmonic pairs. With $\mathcal{X}_{1,\lambda}:=Q_1(\mathcal{R}_\lambda)$ and $\mathcal{X}_{2,\lambda}:=Q_2(\mathcal{R}_\lambda)$ the theorem reads

$$
\mathcal{R}_\lambda
=\mathcal{X}_{1,\lambda}\oplus\mathcal{X}_{2,\lambda}
=B_1^{-1}\bigl(\ker N\bigr)\oplus B_2^{-1}\bigl(\ker N\bigr),
\tag{16}
$$

so that the general solution of the Helmholtz system is the sum of two **rotated** solutions of the Maxwell system, one for each of the two conjugate Cauchy–Riemann operators. This is a statement about the operator family rather than about a particular field: it says that the Helmholtz null-set, which is the natural ambient space of any one of the classical reductions, is assembled from the Maxwell null-set by the two rotations, and hence that the integral theory of the Maxwell operator is available to every metaharmonic pair.

The time-dependent version of the same decomposition is stated in the book and makes the shape of $(16)$ clear:

$$
\ker\Bigl(\frac{1}{c^2}\partial_t^2-\Delta\Bigr)
=\ker\Bigl(\frac{1}{c}\partial_t+iD_3\Bigr)\oplus\ker\Bigl(\frac{1}{c}\partial_t-iD_3\Bigr),
\tag{17}
$$

with the biquaternionic Maxwell operator $(1/c)\partial_t+iD_3$ of the time-dependent reduction. Every solution of the wave equation is the sum of a solution of the first-order operator and a solution of its conjugate, and the two summands are the two halves of the same diagonalisation. Equation $(16)$ is the time-harmonic analogue with $\alpha$ in place of the frequency and the rotated null-set of the generalised operator $N$ in place of the two first-order factors; in the lossless case, where the two chiral wavenumbers coincide, it is the statement that the Helmholtz field splits into the two circular polarisations.

## The Maxwell–Cauchy Kernel and the Integral Operators

The integral theory begins with the kernel of the first-order operators. Let $\Theta_\alpha$ be the outgoing fundamental solution of the Helmholtz operator,

$$
\Theta_\alpha(x)=-\frac{e^{\,i\alpha\lvert x\rvert}}{4\pi\lvert x\rvert},
\qquad
(\Delta+\alpha^2)\Theta_\alpha=\delta ,
\qquad
\operatorname{Im}\alpha\ge0 ,
\tag{18}
$$

the kernel already used by the chiral article, with the branch fixed by the radiation condition. The fundamental solutions of the two conjugate Cauchy–Riemann operators are then obtained from it by one application of the operator itself:

$$
\mathcal{K}_{\pm\alpha}=-(D_3\mp\alpha)\Theta_\alpha ,
\qquad
(D_3\pm\alpha)\mathcal{K}_{\pm\alpha}=\delta ,
\tag{19}
$$

the identity following from $(13)$, since $(D_3\pm\alpha)\mathcal{K}_{\pm\alpha}=-(D_3\pm\alpha)(D_3\mp\alpha)\Theta_\alpha=(\Delta+\alpha^2)\Theta_\alpha=\delta$. The sign is the one verified in the sibling articles; the choice $\operatorname{Im}\alpha\ge0$ makes the kernel outgoing, and at $\alpha=0$ it degenerates to the classical spatial Cauchy kernel $-\mathbf{x}/(4\pi\lvert\mathbf{x}\rvert^3)$ of the unshifted $D_3$.

The kernel of the Maxwell operator is the same object carried through the rotation $(11)$. Conjugating the diagonal kernel by $C$,

$$
K_N:=C^{-1}\begin{pmatrix} \mathcal{K}_{-\alpha} & 0 \\[2pt] 0 & \mathcal{K}_{\alpha}\end{pmatrix}C ,
\qquad
N\,K_N=\delta\, I_2 ,
\tag{20}
$$

which is the fundamental solution of the quaternionic Maxwell operator recorded by the source, expressed here in the book's arrangement: it is built from the hyperholomorphic Cauchy kernels by the two rotations $A_i,B_i$ of $(15)$, and — because all the factors except $N$ are scalar — the same kernel serves the left and the right theories. From it the two integral operators of the Maxwell theory are formed in the usual way,

$$
\mathcal{K}_N[f](x)=-\int_\Gamma K_N(x-y)\,\mathbf{n}(y)\,f(y)\,d\Gamma_y ,
\qquad
\mathcal{T}_N[f](x)=\int_\Omega K_N(x-y)\,f(y)\,dy ,
\tag{21}
$$

the **Cauchy-type** and **Teodorescu-type** operators associated with Maxwell's equations; the defining difference from the operators $\mathcal{K}_\alpha,\mathcal{T}_\alpha$ of the hyperholomorphic theory of the sibling articles is only the replacement of the kernel $\mathcal K_\alpha$ by the Maxwell kernel $K_N$, and the boundary integrals are taken over the Liapunov boundary $\Gamma=\partial\Omega$ of a bounded domain with outward normal $\mathbf{n}$. Three theorems then hold, the analogues of the three of the hyperholomorphic theory and proved from them by the same rotation.

**Theorem (Borel–Pompeiu for the Maxwell operator).** For a pair $f\in C^1(\Omega;\mathbb{B}^2)\cap C(\bar\Omega;\mathbb{B}^2)$,

$$
f=\mathcal{K}_N[f]+\mathcal{T}_N\,N[f]
\qquad\text{in }\Omega .
\tag{22}
$$

**Theorem (right inverse).** For a pair $f$ that is Hölder-continuous and compactly supported in $\Omega$, $N\,\mathcal{T}_N[f]=f$ in $\Omega$.

**Theorem (Cauchy integral formula).** If in addition $N[f]=0$ in $\Omega$, then

$$
f=\mathcal{K}_N[f]
\qquad\text{in }\Omega ,
\tag{23}
$$

so the boundary values determine a quaternionic monochromatic function, and the operator $\mathcal{K}_N$ reproduces it. The Plemelj–Sokhotski formulas, the Morera theorem and the boundary-value criterion of the hyperholomorphic theory pass to the Maxwell theory by the same rotation, and the two-sidedness of $K_N$ makes the left and the right versions coincide.

## The Integral Representations of the Field

Translated back to the fields, the Cauchy formula $(23)$ becomes an integral representation, and its vector form is a classical one. The Cauchy-type operator is the boundary integral of the field and the normal against the Maxwell kernel, and the Teodorescu term is the volume integral of the current; written out in vectors and separated into the electric and magnetic parts, the boundary part of the representation is

$$
\mathbf{E}(x)=\int_\Gamma\Bigl\{\langle\mathrm{grad}_x\Theta_\alpha(x-y),\mathbf{n}(y)\rangle\tilde{\mathbf{E}}(y)
+\bigl[[\mathrm{grad}_x\Theta_\alpha(x-y),\mathbf{n}(y)],\tilde{\mathbf{E}}(y)\bigr]
+i\omega\,\Theta_\alpha(x-y)[\mathbf{n}(y),\tilde{\mathbf{H}}(y)]\Bigr\}d\Gamma_y
+\text{source terms},
\tag{24}
$$

and the corresponding formula for $\mathbf{H}$, which is the **Stratton–Chu formula** of classical electromagnetic theory. The reading is the point of the reformulation: the Stratton–Chu formula is the Cauchy integral formula for the electromagnetic field, its kernel is the fundamental solution of the first-order quaternionic operator, and the "source terms" are the Teodorescu transform of the current. The survey of the programme states the reading in exactly these words — the Stratton–Chu integrals "in their biquaternionic representation" are "a convolution of a biquaternionic fundamental solution of the Maxwell operator with the electromagnetic field", and their meaning "as a Cauchy integral formula for the electromagnetic field becomes transparent". What the vector form does not show, and what the quaternionic form makes explicit, is that the kernel is a single function rather than a matrix and that the boundary combination is the boundary value of a holomorphic object in a four-component algebra.

The same theory solves the boundary-value problem, and it is worth recording because it is where both components of the quaternionic function are used. For the Dirichlet problem — find the pair $(\mathbf{E},\mathbf{H})$ satisfying $(1)$ in the sourceless case inside $\Omega$ and $\mathbf{E}|_\Gamma=\tilde{\mathbf{e}}$, $\mathbf{H}|_\Gamma=\tilde{\mathbf{h}}$ with Hölder data — the diagonalised problem is the pair of Dirichlet problems for the two shifted operators $D_3\mp\alpha$, one for each of the combinations $(10)$. Each is solvable exactly when its Plemelj condition holds, with the projectors $P_{\pm\alpha}=\frac12(I+S_{\pm\alpha})$ of the twin articles, and when both hold the solution is the integral representation $(24)$ with the fields replaced by their boundary values. For the sourceless problem, with the diagonalised boundary data $\Phi|_\Gamma=\tilde{\mathbf{e}}+b\,\tilde{\mathbf{h}}$ and $\Psi|_\Gamma=\tilde{\mathbf{e}}-b\,\tilde{\mathbf{h}}$, the two conditions are

$$
Q_{-\alpha}\bigl(\tilde{\mathbf{e}}+b\,\tilde{\mathbf{h}}\bigr)=0,
\qquad
Q_{\alpha}\bigl(\tilde{\mathbf{e}}-b\,\tilde{\mathbf{h}}\bigr)=0
\qquad\text{on }\Gamma ,
\qquad
Q_{\pm\alpha}=I-P_{\pm\alpha},
\tag{25}
$$

and with sources the right-hand sides are the Teodorescu transforms of the current, in the form the source writes at its equations $(3.3.7)$–$(3.3.8)$. The point of the quaternionic form is that each condition is a condition on a boundary function of **four** components, not three: the classical vector formulation separates only the vector part of the same quaternionic identity, and the scalar component it drops is the one that the second of the two conditions pins down.

The note states the same criterion in its announced form — the boundary data are admissible exactly when they reproduce themselves under the two Cauchy-type integrals, its equations $(7)$ and $(8)$ — and records where its version differs from the vector conditions already obtained in the theory of geophysical fields: those conditions involve the divergence of the tangential field and therefore require, in addition, the differentiability of the tangential components of $\mathbf{E}$ and $\mathbf{H}$ on $\Gamma$, an extra hypothesis that the scalar components of the quaternionic identity avoid.

For the exterior problem the same representation is closed by the **Silver–Müller radiation condition**,

$$
\mathbf{E}\wedge\frac{\mathbf{x}}{\lvert\mathbf{x}\rvert}+W\,\mathbf{H}=o\!\left(\frac{1}{\lvert\mathbf{x}\rvert}\right),
\qquad
\lvert\mathbf{x}\rvert\to\infty ,
\qquad
W=\sqrt{\frac{\mu}{\epsilon}} ,
\tag{26}
$$

the intrinsic impedance being the $W$ of the chiral article, and the sign convention that of the source; on a charged interface between two media the same kernel gives the familiar jump conditions, with the normal components of $\epsilon\mathbf{E}$ and $\mu\mathbf{H}$ jumping by the surface charge and the tangential components of $\mathbf{H}$ by the surface current.

## What Is Not Claimed

Four boundaries are worth stating, because the reformulation invites more than it delivers.

The first is a matter of fidelity. The source's Section 3 realises the similarity $(11)$ through two pairs of matrices $A_i,B_i$, and states the projections $(15)$ and the decomposition $(16)$ in that form. The present article uses the book's equivalent arrangement — the conjugating matrix $C$ of $(11)$, whose entries follow from the diagonalisation itself — and the identity $(11)$ and the factorisations $(8)$ and $(13)$ have been recomputed symbol by symbol, one Fourier mode at a time, for the lossy and the lossless case alike. The source's own matrices are not reproduced, because the available copy of the paper is a scan whose text layer is degraded in the formulas; a reader who needs the exact matrices should consult the paper rather than this article.

The second is that the "better algebraic and analytic properties" of the general operator are, in the source, a qualitative claim. What is verifiable, and what is used here, is the precise part of it: $N$ is defined on all pairs where the physical operator is defined only on solenoidal pairs, and the square of $N$ is **scalar**, $-(\Delta+\lambda)I_2$, while the square of the vector operator is not. The rest of the claim — the explicitness of the kernels, the behaviour under the projections $(15)$ — is used, not re-proved, and belongs to the source.

The third is the scope of $(14)$. The correspondence $\ker N\cong\ker(D_3-\alpha)\times\ker(D_3+\alpha)$ is stated for the sourceless system, on a domain on which the decomposition $(16)$ exists; with sources the two equations $(12)$ acquire the right-hand sides of $(7)$ and the correspondence becomes an inhomogeneous one. The decomposition $(16)$ itself is a statement about the **constant-coefficient** theory: a variable coefficient breaks the simple similarity, and it is exactly the failure recorded in the articles on inhomogeneous media, where the recoverable shift is the gradient coefficient $\mathrm{grad}\,\phi/\phi$ rather than a constant and the operator does not factor as a pair of conjugates of the same type.

The fourth is physical. Nothing here is a new prediction. The article records a reformulation, a correspondence and a family of integral representations; the observables are those of the classical time-harmonic system, and the content is that the time-harmonic field has the structure of a pair of hyperholomorphic functions — which is what makes the boundary-value problems and the numerical methods of the programme possible. The chiral case $\beta\neq0$, where the two wavenumbers separate and the optical activity appears, is the subject of *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*, and is not repeated here.

## Summary

The ordinary time-harmonic Maxwell system in a homogeneous isotropic medium, possibly lossy, is the system $(1)$, with the conduction absorbed into the complex conductivity $\sigma=\sigma_*-i\omega\epsilon$ and the Helmholtz reduction carried by the single complex parameter $\lambda=i\omega\mu\sigma_*+\omega^2\mu\epsilon$, whose square root $\alpha$ is the medium wavenumber. The quaternionic Maxwell operator is the $2\times2$ matrix $N$ of $(6)$; it acts on all pairs of complex-quaternionic functions, its restriction to solenoidal pairs is the physical Maxwell operator, and its square is the scalar Helmholtz operator, $NN^{\dagger}=-(\Delta+\lambda)I_2$. That scalar square is what the physical operator lacks and what makes the function theory available.

The diagonalisation $(11)$ by the matrix $C$, with the coherence factor $b=i\omega\mu/\alpha$, turns $N$ into the direct sum of the two mutually conjugate Cauchy–Riemann operators $D_3\mp\alpha$, whose squares are the scalar Helmholtz operators of $(13)$. Consequently the time-harmonic fields are in one-to-one correspondence with pairs of mutually conjugate hyperholomorphic functions, $\ker N\cong\ker(D_3-\alpha)\times\ker(D_3+\alpha)$; in the lossless normalised variables the two combinations are the circularly polarised $\tilde{\mathbf{E}}\pm i\tilde{\mathbf{H}}$ of the chiral reduction at $\beta=0$; and the Helmholtz null-set itself is the direct sum of the two rotated copies of $\ker N$ of $(16)$, which is the time-harmonic analogue of the splitting of the wave operator into its two first-order factors.

The kernel of the theory is the outgoing Helmholtz kernel $\Theta_\alpha$ of $(18)$ and its two Cauchy–Riemann descendants $\mathcal{K}_{\pm\alpha}=-(D_3\mp\alpha)\Theta_\alpha$; the Maxwell kernel $K_N$ of $(20)$ is the same object carried through the diagonalising rotation, and the Cauchy-type and Teodorescu-type operators built from it satisfy the Borel–Pompeiu formula, the right-inverse formula and the Cauchy integral formula $(22,23)$. Translated back to the fields, the Cauchy formula is the integral representation $(24)$, whose vector form is the classical **Stratton–Chu formula**: the Stratton–Chu kernel is the fundamental solution of the first-order quaternionic Maxwell operator, and the Stratton–Chu representation is a Cauchy integral formula for the electromagnetic field. The Dirichlet problem is solved by the same theory, its solvability governed by the two Plemelj conditions $(25)$, whose quaternionic form carries the scalar component that the vector formulation drops, and the exterior problem is closed by the Silver–Müller condition $(26)$. The parametric system of the source is not specific to the electromagnetic field: at another value of its parameter it is the time-harmonic **Dirac** system, and the same Cauchy integral formula, the same Plemelj–Sokhotski formulas and the same boundary-value criterion then hold for the harmonic spinor field. That statement of the source's announcement, and the spinor half of the theory, are recorded in *The Dirac Equation in Biquaternionic Form*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, basis $e_0=1,e_1,e_2,e_3$, scalar imaginary $i$ |
| $D_3=e_1\partial_1+e_2\partial_2+e_3\partial_3$ | Spatial Moisil–Theodoresco operator; $D_3^2=-\Delta$ |
| $\Delta$ | Spatial Laplacian $\partial_1^2+\partial_2^2+\partial_3^2$ |
| $\epsilon,\mu$ | Permittivity and permeability; possibly complex |
| $\sigma_*$ | Real ohmic conductivity of the medium |
| $\sigma=\sigma_*-i\omega\epsilon$ | Complex conductivity carried by the first Maxwell equation |
| $\lambda=i\omega\mu\sigma_*+\omega^2\mu\epsilon$ | Helmholtz parameter of the reduction |
| $\alpha^2=\lambda$, $\operatorname{Im}\alpha\ge0$ | Medium wavenumber; $\alpha=k=\omega\sqrt{\epsilon\mu}$ when $\sigma_*=0$ |
| $k=\omega\sqrt{\epsilon\mu}=\omega/c$ | Lossless medium wavenumber |
| $N$ | Quaternionic Maxwell operator $(6)$; $NN^{\dagger}=-(\Delta+\lambda)I_2$ |
| $M$ | Physical time-harmonic Maxwell operator, defined on solenoidal pairs |
| $b=i\omega\mu/\alpha$ | Coherence factor of the diagonalisation; $b=iZ$ when $\sigma_*=0$ |
| $C$ | Diagonalising matrix $(11)$; $CNC^{-1}=\mathrm{diag}(D_3-\alpha,D_3+\alpha)$ |
| $\Phi,\Psi$ | Diagonalising combinations $\mathbf{E}\pm b\mathbf{H}$; conjugate Cauchy–Riemann solutions |
| $\mathcal{R}_\lambda$ | Metaharmonic pairs $\ker((\Delta+\lambda)I_2)$ |
| $Q_i=\tfrac{1}{2\alpha}A_iNB_i$ | The two complementary projections, $Q_1+Q_2=I$ |
| $\Theta_\alpha=-e^{\,i\alpha\lvert x\rvert}/(4\pi\lvert x\rvert)$ | Outgoing Helmholtz fundamental solution |
| $\mathcal{K}_{\pm\alpha}=-(D_3\mp\alpha)\Theta_\alpha$ | Fundamental solution of $D_3\pm\alpha$ |
| $K_N$ | Maxwell–Cauchy kernel, the rotation of $\mathrm{diag}(\mathcal{K}_\alpha,\mathcal{K}_{-\alpha})$ |
| $\mathcal{K}_N,\mathcal{T}_N$ | Cauchy-type and Teodorescu-type operators of the Maxwell theory |
| $P_\alpha=\tfrac12(I+S_\alpha)$, $Q_\alpha=I-P_\alpha$ | Plemelj projectors of the shifted theory |
| $\Omega,\Gamma=\partial\Omega$ | Bounded domain and its Liapunov boundary; $\mathbf{n}$ the outward normal |
| $\tilde{\mathbf{e}},\tilde{\mathbf{h}}$ | Dirichlet boundary data of the field |
| $W=\sqrt{\mu/\epsilon}$ | Intrinsic impedance of the medium |

## Further Reading

- V. V. Kravchenko and M. V. Shapiro, "Quaternionic time-harmonic Maxwell operator", *Journal of Physics A: Mathematical and General* **28** (1995) 5017–5031, the paper this article records: the quaternionic Maxwell operator, the one-to-one correspondence with pairs of mutually conjugate hyperholomorphic functions, the decomposition of the Helmholtz null-set into two rotated copies of the Maxwell null-set, the Maxwell–Cauchy kernel and the associated Borel–Pompeiu, right-inverse and Cauchy formulas. It is among the earliest peer-reviewed papers of the programme, and the reference for the exact matrices $A_i,B_i$ that this article quotes in the book's equivalent form.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Research and Exposition in Mathematics 28, Heldermann, 2003), Sections 3.1–3.3, for the same theory in book form: the quaternionic Maxwell operator of the time-dependent reduction, the diagonalisation and the two decoupled equations, the integral representations of the field in their Stratton–Chu form, the Dirichlet problem for the Maxwell equations with its solvability conditions, the charged interface and the Silver–Müller condition. The clean statements of this article are taken from it.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics* (Pitman Research Notes in Mathematics 351, Addison-Wesley Longman, 1996), for the Borel–Pompeiu formula, the Cauchy integral formula and the Plemelj–Sokhotski formulas of the hyperholomorphic theory on which the Maxwell theory is built.
- V. V. Kravchenko, "Quaternion-valued integral representations of the harmonic electromagnetic and spinor fields", *Doklady Mathematics* **51** (1995), no. 2, 287–289 (translated from *Doklady Akademii Nauk* **341** (1995), no. 5, 603–605), the short announcement of the theory of this article: for the unifying statement that one parametric system is the time-harmonic Maxwell system at one value of its parameter and the time-harmonic Dirac system at another; for the announced form of the boundary-value criterion (its equations $(7)$ and $(8)$) and the comparison with the vector conditions of the geophysical integral theory, which require in addition the differentiability of the tangential components on $\Gamma$; and for the spinor half — the dictionary, the helicity reading of the two projectors, and the Cauchy integral formula, Plemelj–Sokhotski formulas and boundary-value criterion for the harmonic spinor field, recorded in *The Dirac Equation in Biquaternionic Form*. The predecessor of the general system is V. V. Kravchenko and M. V. Shapiro, *Doklady Akademii Nauk* **329** (1993), no. 5, 547–549, which the note cites as its reference $[1]$ for the system, the Cauchy-type integral and the three theorems of the parametric theory.
- K. V. Khmelnytskaya and V. V. Kravchenko, "Biquaternions for analytic and numerical solution of equations of electrodynamics", arXiv:0902.3490v1 [math-ph] (2009), for the survey of the programme and for the reading of the Stratton–Chu formulas as a Cauchy integral formula for the electromagnetic field quoted in the section *The Integral Representations of the Field*.
- V. V. Kravchenko and H. Oviedo, "On a quaternionic reformulation of Maxwell's equations for chiral media and its applications", *Zeitschrift für Analysis und ihre Anwendungen* **22** (2003) 569–589, for the chiral extension $\beta\neq0$ of the diagonalisation, the two wavenumbers and the optical activity, recorded in *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*.
- M. V. Shapiro and N. L. Vasilevski, "Quaternionic $\psi$-hyperholomorphic functions, singular integral operators and boundary value problems I. $\psi$-hyperholomorphic function theory", *Complex Variables* **27** (1995) 17–46, for the $\alpha$-hyperholomorphic function theory, its Cauchy kernel, its singular integral operators and the boundary-value problems in the general parameter.
- D. Colton and R. Kress, *Inverse Acoustic and Electromagnetic Scattering Theory* (Applied Mathematical Sciences 93, Springer, 1992), for the Stratton–Chu formulas and the boundary integral equations of electromagnetic scattering in their classical vector form.
