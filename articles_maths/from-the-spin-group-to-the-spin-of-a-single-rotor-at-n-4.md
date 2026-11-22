# __From the Spin Group to the Spin of a Single Rotor at $n=4$: the Sign after $2\pi$ and the Return after $4\pi$__

## Introduction

**The subject.** One rotor, one axis, one angle. The rotor is an element of the principal copy, it acts on the module by a diagonal matrix of phases, and after a full turn of $2\pi$ the action is minus the identity. After two turns it is the identity. The same rotor acting on the algebra by conjugation shows no sign at all.

**The order of the article.** The first section writes the rotor and its action on the module. The second reads the phases weight by weight and locates the half angle. The third computes the sign after $2\pi$ and the return after $4\pi$. The fourth explains the two signs as the two sheets of the double cover. The fifth performs the same computation on the algebra and finds the sign absent. The sixth compares with the row at order two.

**It assumes** *The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$* for the copy and the kernel, and *The Four Weights of the Module and the Half Angle at $n=4$* for the weight basis. The model at order two is *From the Spin Group to the Spin of a Single Rotor*.

**The result in one line.** $\rho(2\pi\,\text{turn})=(-1)^{2j}\mathrm I=-\mathrm I$ on the module because $2j=3$ is odd, $+I$ on the algebra because the two signs cancel, and the pair of behaviours is the double cover $SU(2)\to SO(3)$ read at one rotor.

**Boundaries.** Nothing here is about a family of rotors or about the composition of two rotations; the article treats a single one-parameter subgroup. The general theory of the double cover belongs to *The Spin Group via $4\times4$ Real Matrices*.

## The Rotor

**Definition.** Fix a unit axis and let $J_n$ be the corresponding Hermitian generator of the copy, so that $J_n$ has the eigenvalues $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ along the axis. The **rotor of angle $\theta$** is

$$
R(\theta)=\exp\bigl(i\theta J_n\bigr),
$$

the image under the principal copy of the element $\exp\bigl(i\tfrac{\theta}{2}\sigma_n\bigr)$ of $SU(2)$.

**Proposition.** $R(\theta)$ is unitary, $R(\theta)R(\theta')=R(\theta+\theta')$, and $R$ is $2\pi$-periodic up to sign: $R(\theta+2\pi)=-R(\theta)$.

*Proof.* $J_n$ is Hermitian, so $iJ_n$ is skew-Hermitian and its exponential is unitary. The addition formula is the exponential of commuting multiples of one matrix. For the last claim compute $R(\theta+2\pi)=R(\theta)R(2\pi)$ and evaluate $R(2\pi)$ in the next section.

**The axis at $z$.** With the axis along $z$ and the orthonormal weight basis, the rotor is the diagonal matrix with the four entries

$$
e^{\tfrac32 i\theta},\qquad e^{\tfrac12 i\theta},\qquad e^{-\tfrac12 i\theta},\qquad e^{-\tfrac32 i\theta}.
$$

*Proof.* The generator $J_z$ is diagonal with those four eigenvalues, so its exponential is diagonal with the exponentials of the eigenvalues.

**Corollary.** The rotor is determined by its four phases, and the four phases are the $(2m)$-th powers of the single phase $e^{i\theta/2}$.

*Proof.* The entry of weight $m$ is $e^{im\theta}=(e^{i\theta/2})^{2m}$, and $2m$ runs over $3,1,-1,-3$.

## The Phases and the Half Angle

**Proposition.** On the weight vector of weight $m$ the rotor acts by the phase $e^{im\theta}$, and the phase varies from weight to weight. The module therefore carries four distinct phases, not one.

*Proof.* The weight vector is an eigenvector of $J_z$ with eigenvalue $m$, and the exponential of a diagonal matrix multiplies each eigenvector by the exponential of its eigenvalue.

**Corollary.** The smallest positive angle after which the top weight returns to itself is $4\pi/3$, and the smallest positive angle after which every weight returns is $4\pi$.

*Proof.* The phase of weight $m$ is $1$ exactly when $m\theta$ is a multiple of $2\pi$; the four conditions are $\theta\in\tfrac{4\pi}{3}\mathbb{Z}$, $\theta\in4\pi\mathbb{Z}$, $\theta\in4\pi\mathbb{Z}$ and $\theta\in\tfrac{4\pi}{3}\mathbb{Z}$, and the common period is $4\pi$.

**The half angle.** The angle $\theta$ of the rotor enters the module only through $\theta/2$: the element of $SU(2)$ is $\exp(i\tfrac{\theta}{2}\sigma_n)$, whose entries involve $\cos\tfrac{\theta}{2}$ and $\sin\tfrac{\theta}{2}$. The module then multiplies this half angle by the weights, which are themselves half-integers, and the product is an integer multiple of $\theta$.

*Proof.* The representation of $\exp(i\tfrac{\theta}{2}\sigma_n)$ on the line of highest weight is the multiplication by $e^{i\tfrac32\theta}=(\cos\tfrac{\theta}{2}+i\sin\tfrac{\theta}{2})^{3}$ up to lower-order terms.

**Corollary.** The half angle is visible on the lowest weight as the phase $e^{i\tfrac32\theta}$, that is, the cube of $e^{i\tfrac{\theta}{2}}$, and on the weight $\tfrac12$ as the phase $e^{i\tfrac{\theta}{2}}$ itself.

*Proof.* The two phases displayed in the diagonal form of the rotor.

## The Sign after $2\pi$ and the Return after $4\pi$

**Theorem.** $R(2\pi)=-\mathrm I_4$ and $R(4\pi)=\mathrm I_4$.

*Proof.* At $\theta=2\pi$ each entry of the diagonal rotor is $e^{im\cdot2\pi}=e^{2\pi i m}$; since $m$ is a half-integer, $2m$ is an odd integer, and $e^{\pi i(2m)}=-1$. All four entries are $-1$. At $\theta=4\pi$ the exponent is $4\pi i m=2\pi i(2m)$, an even multiple of $\pi i$, and every entry is $+1$.

**Corollary.** The sign after a full turn is $(-1)^{2j}=-1$, because $2j=3$ is odd.

*Proof.* The general formula $R(2\pi)=(-1)^{2j}\mathrm I$ is the computation of the theorem with $2m$ running over the odd integers $\pm1,\pm3$.

**Corollary.** The module returns to itself after $4\pi$ and not after $2\pi$; the period of the rotor on the module is twice the period of the rotation it represents.

*Proof.* The two evaluations, and the fact that the rotation represented by the rotor has period $2\pi$.

**The sign is not a choice.** The sign is not a convention of the display: it is the evaluation of one matrix at one value of the parameter. A reader who rescales $\theta$ changes the value at which the sign occurs but not the existence of the sign, since the value $-1$ belongs to the image of the module representation and $+1$ at that point would contradict $\rho(-\mathrm I_2)=-\mathrm I_4$.

*Proof.* $\rho$ is a homomorphism and $\exp(i\pi\sigma_z)=-\mathrm I_2$.

## The Two Sheets

**Proposition.** The map $SU(2)\to SO(3)$ is two-to-one, and the two preimages of a rotation are the two signs of the rotor, $q$ and $-q$.

*Proof.* The kernel of the adjoint action is the centre $\{\pm\mathrm I_2\}$, proved in the article on the principal copy.

**Corollary.** The path $\theta\mapsto R(\theta)$ for $\theta\in[0,2\pi]$ ends at $-R(0)$, so it is not a closed path in $SU(2)$; the path for $\theta\in[0,4\pi]$ is closed.

*Proof.* The evaluation at the two endpoints.

**The reading.** The module distinguishes the two sheets, since its rotor takes different values on them; the algebra does not, since its action is the same on both. A rotor is therefore not a rotation: it is a rotation together with a choice of sheet, and the module is the object that sees the choice.

*Proof.* The values at $2\pi$ on the module and the computation of the next section on the algebra.

## The Same Rotor on the Algebra

**Proposition.** On the algebra the rotor acts by $\Phi_{R(\theta)}(X)=R(\theta)XR(\theta)^{-1}$, and at $\theta=2\pi$ this is the identity.

*Proof.* Insert $R(2\pi)=-\mathrm I_4$ and compute $(-\mathrm I)X(-\mathrm I)^{-1}=(-\mathrm I)X(-\mathrm I)=X$, since $(-\mathrm I)^{-1}=-\mathrm I$ and the two signs multiply to $+1$.

**Corollary.** The algebra action has period $2\pi$ in $\theta$, while the module action has period $4\pi$.

*Proof.* The algebra action depends on the rotor only up to sign, and the sign changes the rotor by $-1$ at $2\pi$; the module action does not.

**Corollary.** The spectrum of the generator on the algebra has integer eigenvalues, while the spectrum on the module has half-integer ones.

*Proof.* The adjoint action of $J_z$ on the algebra has the eigenvalues $m-m'$, differences of two half-integers, hence integers; on the module the eigenvalues are the weights themselves.

**The two signs compared.** The minus sign after $2\pi$ on the module and the absence of a sign on the algebra are the same fact read twice: one factor of $-1$ on each side of the conjugation cancels, and a single factor on the module does not.

*Proof.* The two computations.

## The Comparison with $n=2$

**Proposition.** At $n=2$ the module is $V_{1/2}$ and the rotor is a two-by-two diagonal matrix with the entries $e^{i\theta/2}$ and $e^{-i\theta/2}$; after $2\pi$ it is $-\mathrm I_2$, the quaternion sign.

*Proof.* The weights are $\pm\tfrac12$, so $2m=\pm1$ is odd and both entries are $-1$ at $\theta=2\pi$.

**Corollary.** The mechanism is the same at the two rows, and the only difference is the length of the weight string: two weights at $n=2$, four at $n=4$.

*Proof.* The general formula $R(2\pi)=(-1)^{2j}\mathrm I$ with $j=\tfrac12$ and $j=\tfrac32$.

**The reading.** At $n=2$ the sign after $2\pi$ is the defining property of the quaternions, where $i^{2}=j^{2}=k^{2}=-1$ and a rotation by $2\pi$ in the spinor representation is minus the identity. At $n=4$ the same sign is carried by a four-dimensional module, and the cube of the fundamental phase appears because the top weight is $\tfrac32$. Nothing new is needed: the sign is the parity of $2j$.

## Summary

The rotor $R(\theta)=\exp(i\theta J_n)$ acts on the module by the four phases $e^{im\theta}$ with $m=\pm\tfrac32,\pm\tfrac12$, all of them $(2m)$-th powers of the fundamental phase $e^{i\theta/2}$. The weights are half-integers, so $2m$ is odd, and at $\theta=2\pi$ every phase equals $-1$: the rotor is $-\mathrm I_4$. At $\theta=4\pi$ every phase equals $+1$ and the rotor is the identity.

The same rotor acting on the algebra by conjugation has no sign after $2\pi$, because one factor of $-1$ on each side cancels. The module distinguishes the two sheets of the double cover $SU(2)\to SO(3)$ and the algebra does not, and the algebra action has the integer spectrum of differences of weights.

At $n=2$ the module is two-dimensional and the same computation gives the quaternion sign after a full turn. The mechanism is the parity of $2j$, and the number of weights is $2j+1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_n$ | the Hermitian generator along the axis $n$ |
| $R(\theta)=\exp(i\theta J_n)$ | the rotor of angle $\theta$ |
| $m$ | a weight, one of $\pm\tfrac32,\pm\tfrac12$ |
| $e^{im\theta}$ | the phase on the weight $m$ |
| $\Phi_q(X)=qXq^{-1}$ | the conjugation action on the algebra |
| $2j$ | three, the parity that decides the sign |

## Further Reading

- [The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-at-n-4-the-principal-copy-and-its-kernel.html), for the copy and the two kernels.
- [The Four Weights of the Module and the Half Angle at $n=4$](the-four-weights-of-the-module-and-the-half-angle-at-n-4.html), for the weight basis and the normalisations.
- [From the Spin Group to the Spin of a Single Rotor](from-the-spin-group-to-the-spin-of-a-single-rotor.html), for the row at order two.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices.html), for the double cover.
- [The Quaternionic Structure of the Module at $n=4$](the-quaternionic-structure-of-the-module-at-n-4.html), for the anti-linear structure behind the sign.
