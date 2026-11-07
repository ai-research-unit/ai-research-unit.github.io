# __Angular Momentum and Spin in Biquaternionic Form__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ contains two complementary four-dimensional real subspaces, the anti-Hermitian material space $\mathbb{B}_{\Phi}$ and the Hermitian informational space $\mathbb{B}_{\Psi}$, and the companion article *Quantum Physics in Biquaternionic Form* established that $\mathbb{B}_{\Psi}$ is, algebraically, the space of Hermitian observables of a two-state quantum system, whose products generate its full operator algebra. The companion article *Spin-1/2 Quantum Physics in Biquaternionic Form* developed that identification for a single spin: the observables are the Hermitian elements of $\mathbb{B}_{\Psi}$, the pure states are its idempotents, and the Born rule is the normalised Hermitian form, read through the trace. The present article extends the identification from a single spin to the **general angular-momentum algebra**.

The scope is the angular momentum of non-relativistic quantum physics: the orbital angular momentum operator, the spin operator, the total operator, the Casimir, the ladder operators, the addition of angular momenta with the resulting Clebsch–Gordan structure, and the realisation of rotations by unit quaternions. The parent article treated the single spin-1/2 in detail; here the spin is one ingredient in a general algebraic scheme, and the genuinely new content is the algebra of angular momenta and their addition. The article closes by stating explicitly which results are standard quantum physics rewritten in biquaternion language and which are consequences of the biquaternion algebra itself.

Two conventions of the corpus are used throughout. The isomorphism $\mathsf{M}_2: \mathbb{B} \to M_2(\mathbb{C})$ is the one fixed in the companion articles,

$$
\mathsf{M}_2(e_t) = I_2, \qquad \mathsf{M}_2(\vec e_k) = -i\sigma_k, \qquad \mathsf{M}_2(i) = iI_2,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices and $i$ on the right is the complex unit of $M_2(\mathbb{C})$. It follows that

$$
\mathsf{M}_2(i \vec e_k) = \sigma_k, \qquad \mathsf{M}_2\bigl(c r_t e_t + i \sum_k h_k \vec e_k\bigr) = c r_t I_2 + \sum_k h_k \sigma_k .
$$

The scalar imaginary is $i$, the quaternion basis satisfies $e_t=1$, $\vec e_k^2=-e_t$, and $\vec e_\mu \vec e_\nu = \epsilon_{\mu\nu\lambda}\,\vec e_\lambda$ for $\mu\neq\nu$. The reduced Planck constant $\frac{m\,c}{k_m}$ is written explicitly; the algebra literature often sets $\hbar=1$, and the commutation relation quoted in the scope, $[L_{\mathrm{orb},i},L_{\mathrm{orb},j}]=i\epsilon_{ijk}L_{\mathrm{orb},k}$, is the $\hbar=1$ form of the relations below.

## The Angular-Momentum Algebra

Angular momentum in quantum physics is an abstract algebraic structure, independent of any particular realisation. A set of three Hermitian operators $S_{\mathrm{tot},1},S_{\mathrm{tot},2},S_{\mathrm{tot},3}$ on a complex Hilbert space forms an **angular-momentum algebra** if

$$
[S_{\mathrm{tot},i}, S_{\mathrm{tot},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,S_{\mathrm{tot},k}}{k_m}.
$$

The **Casimir operator**

$$
S_{\mathrm{tot}}^2 = S_{\mathrm{tot},1}^2 + S_{\mathrm{tot},2}^2 + S_{\mathrm{tot},3}^2
$$

commutes with every $S_{\mathrm{tot},k}$, since $[S_{\mathrm{tot}}^2,S_{\mathrm{tot},k}] = \sum_i [S_{\mathrm{tot},i}^2,S_{\mathrm{tot},k}] = \sum_i (S_{\mathrm{tot},i}[S_{\mathrm{tot},i},S_{\mathrm{tot},k}] + [S_{\mathrm{tot},i},S_{\mathrm{tot},k}]S_{\mathrm{tot},i})$ and each term is antisymmetric in the summed indices. The **ladder operators**

$$
S_{\mathrm{tot},\pm} = S_{\mathrm{tot},1} \pm i S_{\mathrm{tot},2}
$$

satisfy

$$
[S_{\mathrm{tot},3}, S_{\mathrm{tot},\pm}] = \pm\frac{m\,c\,S_{\mathrm{tot},\pm}}{k_m}, \qquad [S_{\mathrm{tot},+}, S_{\mathrm{tot},-}] =\frac{2\,m\,c\,S_{\mathrm{tot},3}}{k_m},
$$

$$
S_{\mathrm{tot}}^2 = S_{\mathrm{tot},\mp} S_{\mathrm{tot},\pm} + S_{\mathrm{tot},3}^2 \pm \frac{m\,c\,S_{\mathrm{tot},3}}{k_m}, \qquad S_{\mathrm{tot}}^2 = \tfrac{1}{2}\bigl(S_{\mathrm{tot},+}S_{\mathrm{tot},-} + S_{\mathrm{tot},-}S_{\mathrm{tot},+}\bigr) + S_{\mathrm{tot},3}^2 .
$$

The representation theory is standard. The simultaneous eigenvectors of $S_{\mathrm{tot}}^2$ and $S_{\mathrm{tot},3}$ are labelled $|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$ with

$$
S_{\mathrm{tot}}^2 |s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle  =\frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle, \qquad S_{\mathrm{tot},3} |s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle  =\frac{m\,c\,s_{\mathrm{tot},z}}{k_m}|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle,
$$

where $s_{\mathrm{tot}}\in\{0,\tfrac12,1,\tfrac32,\dots\}$ and $s_{\mathrm{tot},z} = -s_{\mathrm{tot}},\dots,+s_{\mathrm{tot}}$ in unit steps. The ladder operators connect neighbouring values of $s_{\mathrm{tot},z}$:

$$
S_{\mathrm{tot},\pm} |s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle  =\frac{m\,c}{k_m}\sqrt{(s_{\mathrm{tot}}\mp s_{\mathrm{tot},z})(s_{\mathrm{tot}}\pm s_{\mathrm{tot},z}+1)}\,|s_{\mathrm{tot}},s_{\mathrm{tot},z}\pm1\rangle  .
$$

None of this uses the biquaternion algebra. The question is where this structure lives inside $\mathbb{B}$, and what the algebra adds to it.

## The Rotation Group Inside the Biquaternion Algebra

The companion article on quantum physics records that the Lie algebra of the $*$-unitary group $\mathrm{U}(2)\subset\mathbb{B}$ is the anti-Hermitian subspace $\mathbb{B}_{\Phi}$, equipped with the commutator bracket. The compact subalgebra of spatial rotations is therefore generated by elements of $\mathbb{B}_{\Phi}\cap\mathbb{B}_{H}$, the space of pure real quaternions. The natural generators are

$$
g_k = -\tfrac{1}{2} \vec e_k \in \mathbb{B}_{\Phi} , \qquad k=1,2,3 .
$$

Using $[\vec e_\mu,\vec e_\nu] = 2\epsilon_{\mu\nu\lambda}\vec e_\lambda$ for $\mu\neq\nu$ — the commutator form of the quaternion multiplication rule $\vec e_\mu \vec e_\nu = \epsilon_{\mu\nu\lambda}\vec e_\lambda$ — we obtain

$$
[g_\mu,g_\nu] = \tfrac{1}{4}[\vec e_\mu,\vec e_\nu] = \tfrac{1}{2}\epsilon_{\mu\nu\lambda} \vec e_\lambda = -\epsilon_{\mu\nu\lambda} g_\lambda .
$$

This is the standard **anti-Hermitian** convention for the generators of $SU(2)$, familiar from $\mathrm{SU}(2)$ in its matrix form $g_k \leftrightarrow \tfrac{i}{2}\sigma_k$. Exponentiating a generator with the standard sign of the rotation operator gives the rotation through $\theta$ about $\vec u$:

$$
\exp\!\left(-\theta\,\sum_k \vec u_k g_k\right) = \exp\!\left(\tfrac{\theta}{2}\sum_k \vec u_k \vec e_k\right) = \cos\tfrac{\theta}{2}\,e_t + \sin\tfrac{\theta}{2}\,\sum_k \vec u_k \vec e_k ,
$$

where $\vec u$ is a unit real vector, and the adjoint action of that element turns a vector through $+\theta$ about $\vec u$ (*Quaternion Rotations and Reflections*, §*The Adjoint Action*). This is a **unit real quaternion**: it lies in $\mathbb{B}_{H}$ and has unit quaternion norm. The set of all such elements is exactly the group $SU(2)$ of unit quaternions, which is the double cover of the rotation group $SO(3)$. The exponential was computed with $\sum_k \vec u_k \vec e_k$ a pure real quaternion of square $-e_t$, so that the power series splits into the trigonometric series.

The **observables** are obtained by multiplying the generators by $-\frac{m\,c\,i}{k_m}$:

$$
\tilde S_{\Psi,k} = -\frac{m\,c\,i\,g_{k}}{k_m}=\frac{m\,c\,i}{2\,k_m} \vec e_k \quad(\text{for spin-}\tfrac12), \qquad [\tilde S_{\Psi,i},\tilde S_{\Psi,j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m}.
$$

The verification is one line: $[\tilde S_{\Psi,i},\tilde S_{\Psi,j}] = (-\frac{m\,c\,i}{k_m})^2 [g_i,g_j] = -\frac{m^{2}\,c^{2}\,(-\epsilon_{ijk}g_k)}{k_m^{2}}=\frac{m^{2}\,c^{2}\,\epsilon_{ijk}\,g_{k}}{k_m^{2}}$, while $\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m}=\frac{m\,c\,i\,\epsilon_{ijk}}{k_m}(-\frac{m\,c\,i\,g_{k}}{k_m}) =\frac{m^{2}\,c^{2}\,\epsilon_{ijk}\,g_{k}}{k_m^{2}}$. The two agree. The passage between the two pictures is the standard one: the Hermitian observables $\tilde S_{\Psi,k}$ generate the $*$-unitary rotations through $\exp(-i\theta\,\sum_k \frac{k_m\,\vec u_{k}\,\tilde{S}_{\Psi,k}}{m\,c})$, and the anti-Hermitian generators $g_k$ are the elements of the Lie algebra.

A structural remark is in order. For two Hermitian elements $\tilde Q_1 = Q_{1t} e_t + i\vec Q_1$ and $\tilde Q_2 = Q_{2t} e_t + i\vec Q_2$ of $\mathbb{B}_{\Psi}$, the companion article computes

$$
[\tilde Q_1,\tilde Q_2] = -2\,(\vec Q_1\times\vec Q_2),
$$

which is a pure real quaternion, an element of $\mathbb{B}_{\Phi}\cap\mathbb{B}_{H}$. In particular the commutator of two observables is not another observable but a **rotation generator**. The angular-momentum commutation relations are therefore a statement about the quaternion product: the right-hand side $\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m}$ is a rotation generator — $i$ times a Hermitian observable, hence anti-Hermitian.

## The Orbital Angular Momentum Operator

The orbital angular momentum is built from position and momentum. In the biquaternion framework the position of a point of the material sector is the real quaternion

$$
\vec r = r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z \in \mathbb{B}_{H},
$$

and the momentum operator is $\tilde{p} = -\frac{m\,c\,i}{k_m}\nabla$ with the vector gradient $\nabla = \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z$. For pure quaternions the product rule is $\vec q\,\vec v = -\vec q\cdot\vec v + \vec q\times\vec v$, so

$$
\vec r\,\tilde{p} = -\frac{m\,c\,i\,\vec r}{k_m}\circ\nabla  =\frac{m\,c\,i\,\vec r}{k_m}\nabla  \;-\;\frac{m\,c\,i\,\vec r}{k_m}\nabla  .
$$

The **vector part** of the quaternionic product has components

$$
L_{\mathrm{orb},k} = -\frac{m\,c\,i\,\epsilon_{klm}\,x_{l}}{k_m}\partial/\partial x_m ,
$$

which are exactly the standard orbital angular momentum operators. This is the biquaternion expression of the vector formula $\vec L = \vec r\times\vec p$: the cross product is the vector part of a quaternion product, and only the replacement $\vec p\to  -\frac{m\,c\,i}{k_m}\nabla$ is needed. The scalar part, $\frac{m\,c\,i\,\vec r}{k_m}\nabla$, is the radial (divergence) term and carries no angular information.

For the algebra of components it is convenient to use the representatives in $\mathbb{B}_{\Psi}$ that $\mathsf{M}_2$ assigns to each operator. Extending $\mathsf{M}_2$ coefficient-wise to biquaternion-valued operators, the scalar operator $L_{\mathrm{orb},k}$ corresponds to the central element $L_{\mathrm{orb},k} e_t$:

$$
\mathsf{M}_2(L_{\mathrm{orb},k} e_t) = L_{\mathrm{orb},k} \otimes I_2 .
$$

The element $L_{\mathrm{orb},k} e_t$ is Hermitian, since $L_{\mathrm{orb},k}$ is Hermitian and $e_t$ is central, so it plays the role of an observable; on the module it acts as $L_{\mathrm{orb},k}$, and the same letter serves for both. The orbital operators satisfy

$$
[L_{\mathrm{orb},i},L_{\mathrm{orb},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,L_{\mathrm{orb},k}}{k_m},
$$

and the representatives inherit the relation because $e_t$ is central.

In spherical coordinates the operators take their standard forms,

$$
L_{\mathrm{orb},z} = -\frac{m\,c\,i}{k_m}\partial/\partial\theta_{\mathrm{azm}}, \qquad
L^2 = -\frac{m^{2}\,c^{2}}{k_m^{2}}\left[\frac{1}{\sin\theta}\partial/\partial\theta\bigl(\sin\theta\,\partial/\partial\theta\bigr) + \frac{1}{\sin^2\theta}\partial^2/\partial{\theta_{\mathrm{azm}}}^2\right] ,
$$

with ladder combinations $L_\pm = L_{\mathrm{orb},1} \pm iL_{\mathrm{orb},2}$ acting on the spherical harmonics as $L_\pm Y_l^{l_z} =\frac{m\,c}{k_m}\sqrt{(l\mp l_z)(l\pm l_z+1)}\,Y_l^{l_z\pm1}$. The spectrum is the standard one,

$$
L^2\,Y_l^{l_z} =\frac{m^{2}\,c^{2}\,l\,(l+1)\,Y_{l}^{l_z}}{k_m^{2}}, \qquad L_{\mathrm{orb},z}\,Y_l^{l_z} =\frac{m\,c\,l_{z}\,Y_{l}^{l_z}}{k_m}.
$$

These are the operators that a position-space treatment of the hydrogen atom requires: the radial equation is coupled to the angular problem only through the eigenvalues $\frac{m^{2}\,c^{2}\,l\,(l+1)}{k_m^{2}}$ and the spin–orbit term defined in a later section.

Note the structural asymmetry between orbital and spin angular momentum. The orbital operators act on the argument of the wavefunction, that is on the **external** position variable, and in the biquaternion algebra they occupy the central scalar slot $e_t$. The spin operators, treated next, act on the **internal** quaternionic structure and occupy the vector slots $i\vec e_k$. The biquaternion framework thus makes an algebraic distinction between external and internal degrees of freedom that the standard formalism leaves implicit.

## The Spin Operators Under the Isomorphism

The parent article developed the single spin-1/2 in detail; we recall only what is needed for the angular-momentum algebra. Under $\mathsf{M}_2$, the spin operators $S_k =\frac{m\,c}{2\,k_m}\sigma_k$ correspond to the Hermitian elements

$$
\tilde{S}_{\Psi,k} =\frac{m\,c}{2\,k_m}\, i \vec e_k \in  \mathbb{B}_{\Psi}, \qquad \mathsf{M}_2(\tilde{S}_{\Psi,k}) =\frac{m\,c}{2\,k_m}\sigma_k = S_k .
$$

The three cases are collected in the following table, together with the ladder combinations $\tilde S_{\Psi,\pm} = \tilde S_{\Psi,1} \pm i\tilde S_{\Psi,2}$.

| Standard operator | Biquaternion element | Image under $\mathsf{M}_2$ |
|---|---|---|
| $S_1 =\frac{m\,c}{2\,k_m}\sigma_1$ | $\tilde S_{\Psi,1} =\frac{m\,c}{2\,k_m} i \vec e_x$ | $\frac{m\,c}{2\,k_m}\sigma_1$ |
| $S_2 =\frac{m\,c}{2\,k_m}\sigma_2$ | $\tilde S_{\Psi,2} =\frac{m\,c}{2\,k_m} i \vec e_y$ | $\frac{m\,c}{2\,k_m}\sigma_2$ |
| $S_3 =\frac{m\,c}{2\,k_m}\sigma_3$ | $\tilde S_{\Psi,3} =\frac{m\,c}{2\,k_m} i \vec e_z$ | $\frac{m\,c}{2\,k_m}\sigma_3$ |
| $S_+ =\frac{m\,c\,\sigma_{+}}{k_m}$ | $\tilde S_{\Psi,+} =\frac{m\,c}{2\,k_m}(i \vec e_x - \vec e_y)$ | $\frac{m\,c\,\sigma_{+}}{k_m}$ |
| $S_- =\frac{m\,c\,\sigma_{-}}{k_m}$ | $\tilde S_{\Psi,-} =\frac{m\,c}{2\,k_m}(i \vec e_x + \vec e_y)$ | $\frac{m\,c\,\sigma_{-}}{k_m}$ |

Here $\sigma_\pm = \tfrac{1}{2}(\sigma_1 \pm i\sigma_2)$ are the standard raising and lowering matrices. The elements $\tilde S_{\Psi,k}$ lie in $\mathbb{B}_{\Psi}$ and are Hermitian. The ladder operators do **not**: $\tilde S_{\Psi,\pm}^{*} = \tilde S_{\Psi,\mp}$, so they are neither Hermitian nor in $\mathbb{B}_{\Psi}$; they lie in the full algebra $\mathbb{B}$. They are also invariant, up to sign, under quaternion conjugation, $\tilde S_{\Psi}^{\natural}_\pm = -\tilde S_{\Psi,\pm}$.

The pure spin states are the idempotents $\tilde\Pi(\pm\vec u) = \tfrac{1}{2}(e_t \pm i\vec u)$ with $\vec u$ a unit pure real quaternion, and they are the eigenstates of the spin along $\vec u$:

$$
\sum_k  \vec u_k \tilde{S}_{\Psi,k}\, \tilde\Pi(\pm\vec u) = \pm\frac{m\,c}{2\,k_m}\, \tilde\Pi(\pm\vec u) .
$$

This is the content of the parent article, expressed in the notation needed below.

## Commutation Relations as Biquaternion Commutators

The spin commutation relations are computed entirely inside the algebra. From $(i\vec e_\mu)(i\vec e_\nu) = i^2 \vec e_\mu \vec e_\nu = -\vec e_\mu \vec e_\nu$ we get

$$
[i\vec e_\mu, i\vec e_\nu] = -[\vec e_\mu,\vec e_\nu] = -2\epsilon_{\mu\nu\lambda}\vec e_\lambda = 2i\,\epsilon_{\mu\nu\lambda}\,(i\vec e_\lambda),
$$

where the last step uses $\vec e_k = -i\,(i\vec e_k)$. Multiplying by $(\frac{m\,c}{2\,k_m})^2$,

$$
\boxed{\;[\tilde{S}_{\Psi,\mu},\tilde{S}_{\Psi,\nu}] =\frac{m^{2}\,c^{2}}{4\,k_m^{2}}\,[i\vec e_\mu,i\vec e_\nu] =\frac{m^{2}\,c^{2}\,i}{2\,k_m^{2}}\,\epsilon_{\mu\nu\lambda}\,(i\vec e_\lambda) =\frac{m\,c\,i\,\epsilon_{\mu\nu\lambda}\,\tilde{S}_{\Psi,\lambda}}{k_m}}.
$$

The only inputs are the multiplication rule $\vec e_\mu \vec e_\nu = \epsilon_{\mu\nu\lambda}\vec e_\lambda$, the square $\vec e_k^2 = -e_t$, and $i^2=-1$. Reading the result backwards, the angular-momentum algebra in the biquaternion setting is the statement that the Hermitian basis elements $i\vec e_k$ close under commutation with a structure constant proportional to $i$ — a fact that follows from the quaternion product and from the sign $i^2=-1$ that makes $i\vec e_k$ Hermitian.

The Casimir is likewise immediate. Since $(i\vec e_k)^2 = i^2 \vec e_k^2 = (-1)(-e_t) = +e_t$,

$$
\tilde{S}_{\Psi}^2 = \sum_{k=1}^{3}\left(\frac{m\,c}{2\,k_m} i\vec e_k\right)^2 =\frac{m^{2}\,c^{2}}{4\,k_m^{2}}\cdot  3e_t =\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}\, e_t ,
$$

a central element of the algebra, and $[\tilde S_{\Psi}^2,\tilde S_{\Psi,k}]=0$ for all $k$. This is the value $\frac{m^{2}\,c^{2}\,s\,(s+1)}{k_m^{2}}$ with $s=\tfrac12$, obtained here from $(i\vec e_k)^2=+e_t$.

The orbital and spin operators act on independent structures — the external position argument and the internal quaternionic index — so the mixed commutators vanish:

$$
[L_{\mathrm{orb},i},\tilde{S}_{\Psi,j}] = 0 .
$$

## Total Angular Momentum and Spin–Orbit Coupling

The **total angular-momentum operator** is the sum of the orbital and spin parts,

$$
\tilde S_{\Psi,\mathrm{tot},k} = L_{\mathrm{orb},k} e_t + \tilde{S}_{\Psi,k} ,
\qquad \mathsf{M}_2(\tilde S_{\Psi,\mathrm{tot},k}) = L_{\mathrm{orb},k}\,I_2 +\frac{m\,c}{2\,k_m}\sigma_k .
$$

Because the two parts commute and each satisfies the angular-momentum algebra, so does the sum:

$$
[\tilde S_{\Psi,\mathrm{tot},i},\tilde S_{\Psi,\mathrm{tot},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}.
$$

The operator $\tilde S_{\Psi,\mathrm{tot},k}$ is Hermitian, its orbital part sitting in the scalar slot and its spin part in the vector slot; the expression is the biquaternion form of $\vec S_{\mathrm{tot}} = \vec L + \vec S$ on the tensor product of the orbital and spin state spaces.

The **spin–orbit operator** is the scalar contraction of the two vector operators,

$$
\sum_k  (L_{\mathrm{orb},k} e_t)\tilde{S}_{\Psi,k} =\frac{m\,c\,i}{2\,k_m}\,\sum_k  L_{\mathrm{orb},k} \vec e_k,
\qquad \mathsf{M}_2\bigl(\sum_k  (L_{\mathrm{orb},k} e_t)\tilde{S}_{\Psi,k}\bigr) =\frac{m\,c}{2\,k_m}\,\sum_k  L_{\mathrm{orb},k}\sigma_k = L\cdot\vec S.
$$

Its eigenvalues follow from the Casimir identity $\vec L\cdot\vec S = \tfrac{1}{2}(S_{\mathrm{tot}}^2 - L^2 - S^2)$: on a state of definite $l$ and total $s_{\mathrm{tot}} = l\pm\tfrac12$,

$$
\boxed{\;\vec L\cdot\vec S \;\longrightarrow\;\frac{m^{2}\,c^{2}}{2\,k_m^{2}}\Bigl[s_{\mathrm{tot}}(s_{\mathrm{tot}}+1) - l(l+1) - \tfrac34\Bigr] =
\begin{cases} +\frac{m^{2}\,c^{2}\,l}{2\,k_m^{2}}, & s_{\mathrm{tot}} = l+\tfrac12,\\[6pt] -\frac{m^{2}\,c^{2}\,(l+1)}{2\,k_m^{2}}, & s_{\mathrm{tot}} = l-\tfrac12 .\end{cases}\;}
$$

For a given $l$ the orbital and spin operators therefore commute with $L^2$, $S^2$, $S_{\mathrm{tot}}^2$ and $S_{\mathrm{tot},z}$, and the simultaneous labels $(l,s_{\mathrm{tot}},s_{\mathrm{tot},z})$ are the ones that diagonalise the spin–orbit coupling. This is exactly the structure that the non-relativistic hydrogen treatment uses: the spin–orbit term splits each orbital level into the two values above.

## The Casimir Operator

For a general angular momentum the Casimir is $S_{\mathrm{tot}}^2=\sum_k S_{\mathrm{tot},k}^2$, and it is central in the sense that it commutes with every $S_{\mathrm{tot},k}$. In the biquaternion realisation it is

$$
\boxed{\;\tilde S_{\Psi,\mathrm{tot}}^2 = \sum_{k=1}^{3}\tilde S_{\Psi,\mathrm{tot},k}^2
= L^2 e_t + \tilde{S}_{\Psi}^2 + 2\,\sum_k  (L_{\mathrm{orb},k} e_t)\tilde{S}_{\Psi,k}
= \Bigl(L^2 +\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}\Bigr)e_t +\frac{m\,c\,i}{k_m}\sum_k  L_{\mathrm{orb},k} \vec e_k\;},
$$

where the cross terms combine to $2\sum_k  L_{\mathrm{orb},k}\tilde S_{\Psi,k} =\frac{m\,c\,i}{k_m}\sum_k  L_{\mathrm{orb},k}\vec e_k$. Unlike the pure-spin Casimir $\tilde S_{\Psi}^2=\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}e_t$, the total Casimir is **not** a multiple of $e_t$ when orbital angular momentum is present: it has a vector part proportional to the spin–orbit operator. It is nevertheless central within each irreducible multiplet, where it takes the value

$$
\tilde S_{\Psi,\mathrm{tot}}^2 \;\longrightarrow\;\frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}, \qquad s_{\mathrm{tot}} = l\pm\tfrac12 \;\;(l\ge 1), \qquad s_{\mathrm{tot}} = \tfrac12 \;\;(l=0).
$$

The distinction is worth recording: the pure-spin Casimir is a central element of the algebra $\mathbb{B}$ itself, while the total Casimir is central only in the enveloping algebra of the rotation group acting on the coupled orbital–spin space. Both facts are standard; the biquaternion setting makes the first of them manifest, since $\tilde S_{\Psi}^2=\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}e_t$ is literally a scalar multiple of the identity.

## Ladder Operators

The biquaternion ladder operators are

$$
\tilde S_{\Psi,\mathrm{tot},\pm} = \tilde S_{\Psi,\mathrm{tot},1} \pm i\tilde S_{\Psi,\mathrm{tot},2} = L_\pm e_t + \tilde{S}_{\Psi,\pm} ,
$$

with $L_\pm=L_{\mathrm{orb},1}\pm iL_{\mathrm{orb},2}$ and $\tilde S_{\Psi,\pm}$ as in the table above. They satisfy

$$
[\tilde S_{\Psi,\mathrm{tot},3},\tilde S_{\Psi,\mathrm{tot},\pm}] = \pm\frac{m\,c\,\tilde{S}_{\Psi,\mathrm{tot},\pm}}{k_m}, \qquad
[\tilde S_{\Psi,\mathrm{tot},+},\tilde S_{\Psi,\mathrm{tot},-}] =\frac{2\,m\,c\,\tilde{S}_{\Psi,\mathrm{tot},3}}{k_m}, \qquad
\{\tilde S_{\Psi,\mathrm{tot},+},\tilde S_{\Psi,\mathrm{tot},-}\} = 2\,\tilde S_{\Psi,\mathrm{tot}}^2 - 2\,\tilde S_{\Psi,\mathrm{tot},3}^2 ,
$$

and act on the coupled states as $\tilde S_{\Psi,\mathrm{tot},\pm}|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle  =\frac{m\,c}{k_m}\sqrt{(s_{\mathrm{tot}}\mp s_{\mathrm{tot},z})(s_{\mathrm{tot}}\pm s_{\mathrm{tot},z}+1)}\,|s_{\mathrm{tot}},s_{\mathrm{tot},z}\pm1\rangle$. For the spin part alone,

$$
[\tilde{S}_{\Psi,3},\tilde{S}_{\Psi,\pm}] = \pm\frac{m\,c\,\tilde{S}_{\Psi,\pm}}{k_m}, \qquad
[\tilde{S}_{\Psi,+},\tilde{S}_{\Psi,-}] =\frac{2\,m\,c\,\tilde{S}_{\Psi,3}}{k_m}, \qquad
\{\tilde{S}_{\Psi,+},\tilde{S}_{\Psi,-}\} =\frac{m^{2}\,c^{2}\,e_{t}}{k_m^{2}}.
$$

The spin ladder operators have an algebraic property that the standard matrices share but that the biquaternion algebra exhibits transparently:

$$
\tilde{S}_{\Psi,\pm}^2 = 0, \qquad \langle\tilde{S}_{\Psi,\pm}\rangle_{\natural} = \tilde{S}_{\Psi,\pm} \tilde{S}_{\Psi}^{\natural}_\pm = 0 .
$$

They are **nilpotent**, and they are **zero divisors** of $\mathbb{B}$ — indeed they lie on the biquaternion-norm cone. The raising and lowering operators are therefore elements of the same null cone that defines the light cone of the material sector and the pure states of the informational sector. This is a genuinely algebraic feature of the biquaternion realisation: the ladder operators are not merely non-Hermitian matrices, they are null elements of the algebra.

## Addition of Angular Momenta and Clebsch–Gordan Coefficients

Two independent angular momenta $\vec S^{(1)}$ and $\vec S^{(2)}$, acting on different factors of a tensor product, combine by

$$
\tilde S_{\Psi,\mathrm{tot},k} = \tilde S_{\Psi}^{(1)}_k + \tilde S_{\Psi}^{(2)}_k,
$$

with each factor satisfying its own commutation relations and cross-commutators vanishing. The total operator again satisfies $[\tilde S_{\Psi,\mathrm{tot},i},\tilde S_{\Psi,\mathrm{tot},j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}$, and the coupled states $|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$ are the eigenvectors of $\tilde S_{\Psi,\mathrm{tot}}^2$ and $\tilde S_{\Psi,\mathrm{tot},3}$.

The framework's tensor product is available for the spin factors. Two spin-1/2 degrees of freedom live in $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$, and the familiar decomposition $\tfrac12\otimes\tfrac12 = 1\oplus 0$ — a triplet and a singlet — is realised there as the symmetric and antisymmetric parts of the tensor square. This is genuinely algebraic within the framework: the composite spin-1 system is built from two fundamental spin-1/2 systems without leaving the algebra.

The case required for hydrogen is one spin-1/2 coupled to an orbital angular momentum $l$. The orbital factor is the $(2l+1)$-dimensional representation of the rotation algebra, and the coupled space has dimension $2(2l+1)$; it decomposes into $s_{\mathrm{tot}}=l+\tfrac12$ (multiplicity $2l+2$) and $s_{\mathrm{tot}}=l-\tfrac12$ (multiplicity $2l$, absent for $l=0$), the multiplicities summing to $4l+2 = 2(2l+1)$. In the basis $|l,m_l\rangle\,|\!\uparrow\rangle$, $|l,m_l\rangle\,|\!\downarrow\rangle$ the Clebsch–Gordan coefficients in the standard Condon–Shortley phase convention are

$$
\begin{aligned}
|s_{\mathrm{tot}}=l+\tfrac12,\,s_{\mathrm{tot},z}\rangle &=
\sqrt{\frac{l+s_{\mathrm{tot},z}+\tfrac12}{2l+1}}\;|l,s_{\mathrm{tot},z}-\tfrac12\rangle|\!\uparrow\rangle
+ \sqrt{\frac{l-s_{\mathrm{tot},z}+\tfrac12}{2l+1}}\;|l,s_{\mathrm{tot},z}+\tfrac12\rangle|\!\downarrow\rangle,\\[6pt]
|s_{\mathrm{tot}}=l-\tfrac12,\,s_{\mathrm{tot},z}\rangle &=
-\sqrt{\frac{l-s_{\mathrm{tot},z}+\tfrac12}{2l+1}}\;|l,s_{\mathrm{tot},z}-\tfrac12\rangle|\!\uparrow\rangle
+ \sqrt{\frac{l+s_{\mathrm{tot},z}+\tfrac12}{2l+1}}\;|l,s_{\mathrm{tot},z}+\tfrac12\rangle|\!\downarrow\rangle .
\end{aligned}
$$

For $l=1$ this gives a quartet and a doublet; the $s_{\mathrm{tot},z}=\tfrac12$ members are

$$
|s_{\mathrm{tot}}=\tfrac32, s_{\mathrm{tot},z}=\tfrac12\rangle = \sqrt{\tfrac23}\,|1,0\rangle|\!\uparrow\rangle + \sqrt{\tfrac13}\,|1,1\rangle|\!\downarrow\rangle,
$$

$$
|s_{\mathrm{tot}}=\tfrac12, s_{\mathrm{tot},z}=\tfrac12\rangle = -\sqrt{\tfrac13}\,|1,0\rangle|\!\uparrow\rangle + \sqrt{\tfrac23}\,|1,1\rangle|\!\downarrow\rangle .
$$

The coefficients are pure numbers; they do not depend on the biquaternion representation of the spin factor, which enters only through the operators $\tilde S_{\Psi,k}$ generating the suitable matrix action. In this respect the addition of angular momenta is standard quantum physics expressed in biquaternion language, with one genuinely algebraic ingredient: the spin-1/2 factor is the fundamental module of $\mathbb{B}$, so the spin operators used in the coupling are the elements $\tilde S_{\Psi,k}$ of $\mathbb{B}_{\Psi}$ constructed above.

Two structural points should be stated precisely. First, the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, so it has a **single** irreducible module, the fundamental two-dimensional one; there is no one-dimensional unital module, because a unital algebra map $M_2(\mathbb{C})\to\mathbb{C}$ would have a two-sided kernel. The algebra therefore realises, as a module, only $s=\tfrac12$. The scalar $s=0$ is present instead in the centre of the algebra, and the vector representation $s=1$ is present not as a $\mathbb{B}$-module but as the adjoint action of the $*$-unitary subgroup on the imaginary quaternions; higher $s_{\mathrm{tot}}$ require tensor products or symmetric powers. Second, the orbital representation is not a biquaternion module at all (except for $l=0$); it is the standard rotation representation carried by the position dependence of the wavefunction. The biquaternion content of the coupled system is therefore confined to the spin factor, while the orbital factor and the Clebsch–Gordan coefficients are carried over unchanged from standard quantum physics.

## The Rotor Realisation of Rotations

Rotations in the biquaternion framework are realised by **rotor conjugation**. A rotation through angle $\theta$ about the unit axis $\vec u$ is generated by the unit real quaternion

$$
\tilde u(\theta,\vec u) = \cos\tfrac{\theta}{2}\,e_t + \sin\tfrac{\theta}{2}\,\sum_k \vec u_k \vec e_k \in \mathbb{B}_{H}, \qquad \tilde u\,\tilde u^{*} = e_t ,
$$

acting on states and observables by conjugation. On the observables of the informational sector, a state $\tilde{Ϛ}_{\Psi} = \tfrac12(e_t + i\vec r)$ transforms as

$$
\tilde{Ϛ}_{\Psi} \;\longmapsto\; \tilde u\,\tilde{Ϛ}_{\Psi}\,\tilde u^{*} ,
$$

which leaves the scalar part fixed and rotates the Bloch vector $\vec r$ by angle $\theta$ about $\vec u$. On the vectors of the material sector, $\tilde R_\Phi = i c r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, the same conjugation rotates the spatial part while preserving the biquaternion norm. Both are the standard rotation of a three-dimensional vector, expressed through the double cover $SU(2)\to SO(3)$.

The rotor is generated by the total angular momentum. Writing the rotation operator as $\exp(-\frac{k_m\,i\,\theta\,\vec u_{k}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{m\,c})$ and using $\tilde S_{\Psi,\mathrm{tot},k} = L_{\mathrm{orb},k}+\tilde S_{\Psi,k}$, the orbital part acts on the position dependence while the spin part acts on the internal index. For the spin alone,

$$
\exp\!\left(-\frac{k_m\,i\,\theta}{m\,c}\,\sum_k  \vec u_k\tilde{S}_{\Psi,k}\right)
= \exp\!\left(-\frac{k_m\,i\,\theta}{m\,c}\cdot\frac{m\,c}{2\,k_m}\,i\sum_k  \vec u_k \vec e_k\right)
= \exp\!\left(\frac{\theta}{2}\sum_k  \vec u_k \vec e_k\right)
= \tilde u(\theta,\vec u) ,
$$

so the abstract spin rotation operator and the unit quaternion rotor are the same element of $\mathbb{B}$. The identification reproduces the characteristic spinorial behaviour: $\tilde u(\theta+2\pi,\vec u) = -\tilde u(\theta,\vec u)$, and the two rotors $\pm\tilde u$ produce the same rotation of $\vec r$ and of $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. The sign ambiguity is the double cover, and it is here a statement about unit real quaternions: the group of rotors is $SU(2)$, and the rotation group is its quotient by $\{\pm e_t\}$.

The rotor realisation ties the two sectors together in the way the companion articles describe: the same unit quaternion acts by conjugation on the material four-vectors of $\mathbb{B}_{\Phi}$ and on the states of the informational sector $\mathbb{B}_{\Psi}$. Angular momentum is the infinitesimal generator of that action, and its biquaternion form is the subject of this article.

## What Is Standard and What Is Algebraic

It is useful to separate the two kinds of result that the article contains.

**Standard quantum physics, rewritten.**

- The abstract angular-momentum algebra $[S_{\mathrm{tot},i},S_{\mathrm{tot},j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,S_{\mathrm{tot},k}}{k_m}$, its Casimir, its ladder operators, and its representation theory with $\frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}$ and $\frac{m\,c\,s_{\mathrm{tot},z}}{k_m}$.
- The orbital angular momentum operator $L_{\mathrm{orb},k}=-\frac{m\,c\,i\,\epsilon_{klm}\,x_{l}}{k_m}\partial/\partial x_m$, its spherical-coordinate form, and the spectra $\frac{m^{2}\,c^{2}\,l\,(l+1)}{k_m^{2}}$ and $\frac{m\,c\,l_{z}}{k_m}$.
- The total operator $\vec S_{\mathrm{tot}}=\vec L+\vec S$, the spin–orbit eigenvalues $\frac{m^{2}\,c^{2}}{2\,k_m^{2}}[s_{\mathrm{tot}}(s_{\mathrm{tot}}+1)-l(l+1)-\tfrac34]$, and the Clebsch–Gordan coefficients for $\tfrac12\otimes l$.
- The equivalence of rotor conjugation with the standard rotation operators.

**Genuinely algebraic consequences of the biquaternion setting.**

- The rotation generators sit in the Lie algebra $\mathbb{B}_{\Phi}$ of the $*$-unitary group; the compact generators are $-\tfrac12 \vec e_k$ inside the real quaternion subspace $\mathbb{B}_{H}$, and the rotation group is the group of unit real quaternions.
- The spin commutation relations $[\tilde S_{\Psi,i},\tilde S_{\Psi,j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m}$ follow from the quaternion product rule $\vec e_\mu \vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda$, the square $\vec e_k^2=-e_t$, and $i^2=-1$; the Hermiticity of $i\vec e_k$ is what places the observables in $\mathbb{B}_{\Psi}$.
- The commutator of two Hermitian observables is $-2(\vec r_\Psi\times\vec k)$, a pure real quaternion in $\mathbb{B}_{\Phi}\cap\mathbb{B}_{H}$: the commutator of observables is a rotation generator.
- The pure-spin Casimir $\tilde S_{\Psi}^2=\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}e_t$ is a central element of $\mathbb{B}$, and its value $\frac{m^{2}\,c^{2}\,s\,(s+1)}{k_m^{2}}$ with $s=\tfrac12$ follows from $(i\vec e_k)^2=+e_t$.
- The spin eigenstates are the idempotents $\tilde\Pi(\pm\vec u)=\tfrac12(e_t\pm i\vec u)$, and $\sum_k \vec u_k\tilde S_{\Psi,k}$ has eigenvalues $\pm\frac{m\,c}{2\,k_m}$ on them.
- The spin ladder operators are nilpotent and null in the biquaternion norm, $\tilde S_{\Psi,\pm}^2=0$ and $\langle\tilde S_{\Psi,\pm}\rangle_{\natural}=0$: they are zero divisors of the algebra.
- Orbital operators occupy the central scalar slot $e_t$ and spin operators the vector slots $i\vec e_k$, an algebraic distinction between external and internal degrees of freedom.
- As a module over $\mathbb{B}$, the algebra affords only $s=0$ and $s=\tfrac12$; the $s=1$ vector representation appears through the adjoint action on the imaginary quaternions, and higher spins require tensor products.

## Open Questions

**1. A biquaternion realisation of orbital angular momentum.** The orbital factor of the coupled system is not a $\mathbb{B}$-module, and its Clebsch–Gordan structure is imported from standard quantum physics. Is there a natural biquaternion construction of the $(2l+1)$-dimensional rotation representation, for instance as a symmetric power of the fundamental module, that would make the orbital factor algebraic as well?

**2. Higher spin.** The framework realises spin-1 as the adjoint (vector) representation, but a spin-1 particle with three states is not a module over the algebra. Should higher spins be constructed through tensor products $\mathbb{B}^{\otimes n}\cong M_{2^n}(\mathbb{C})$, through symmetric powers of the fundamental module, or through a larger algebra?

**3. The hydrogen degeneracy.** The non-relativistic hydrogen atom has an additional $SO(4)$ symmetry (the Runge–Lenz vector) beyond the manifest $SO(3)$. Does the biquaternion framework offer an algebraic account of this hidden symmetry, in the same way that it makes the rotation group manifest?

**4. Relativistic angular momentum.** The relativistic generalisation of the angular-momentum algebra involves the Lorentz generators and the Pauli–Lubanski vector, with spin entering the generators of the Lorentz group rather than as an independent $SU(2)$. The biquaternion Dirac equation is available; the corresponding relativistic spin algebra has not been developed here.

**5. The meaning of the two slots.** The orbital part of angular momentum occupies the scalar slot $e_t$ and the spin part the vector slots $i\vec e_k$. Is this split merely a bookkeeping convenience, or does it reflect a structural distinction between external and internal degrees of freedom within the algebra?

**6. Empirical content.** The whole construction reproduces standard angular-momentum physics. Any deviation would have to appear in the coupling between the two sectors, for example in a modification of the spin–orbit interaction; none is visible at the level developed here.

## Summary

Angular momentum in the biquaternion framework is organised by the isomorphism $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, under which the spin operators $S_k=\frac{m\,c}{2\,k_m}\sigma_k$ correspond to the Hermitian elements $\tilde S_{\Psi,k}=\frac{m\,c}{2\,k_m}i\vec e_k\in\mathbb{B}_{\Psi}$. The rotation generators lie in the Lie algebra $\mathbb{B}_{\Phi}$ and, for spatial rotations, in the real quaternion subspace $\mathbb{B}_{H}$, where they are $-\tfrac12\vec e_k$; their exponentials are the unit real quaternions, which are the group $SU(2)$.

The orbital angular momentum operator is the vector part of the quaternionic product $\vec r\tilde p$ of position and momentum, with components $L_{\mathrm{orb},k}=-\frac{m\,c\,i\,\epsilon_{klm}\,x_{l}}{k_m}\partial/\partial x_m$ and central representatives $L_{\mathrm{orb},k} e_t$. The spin operators generate the same algebra internally, and the commutation relations $[\tilde S_{\Psi,i},\tilde S_{\Psi,j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m}$ follow directly from the quaternion multiplication rule, the square $\vec e_k^2=-e_t$, and $i^2=-1$. The pure-spin Casimir is the central element $\tilde S_{\Psi}^2=\frac{3\,m^{2}\,c^{2}}{4\,k_m^{2}}e_t$; the total Casimir $\tilde S_{\Psi,\mathrm{tot}}^2$ takes the value $\frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}$ on coupled states with $s_{\mathrm{tot}}=l\pm\tfrac12$.

The spin ladder operators are nilpotent and null in the biquaternion norm, and hence zero divisors of the algebra. The addition of angular momenta follows the standard Clebsch–Gordan scheme, with the spin factor expressed through the elements $\tilde S_{\Psi,k}$; for a spin-1/2 coupled to orbital $l$ the coupled states carry $s_{\mathrm{tot}}=l\pm\tfrac12$, and the spin–orbit operator takes the eigenvalue $+\frac{m^{2}\,c^{2}\,l}{2\,k_m^{2}}$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $-\frac{m^{2}\,c^{2}\,(l+1)}{2\,k_m^{2}}$ for $s_{\mathrm{tot}}=l-\tfrac12$. Rotations are realised by rotor conjugation with unit quaternions, and the rotor $\tilde u(\theta,\vec u)$ is identical to the exponential of the spin angular momentum. The framework thus contains the complete angular-momentum algebra, with the orbital part standard and the spin part algebraic; the operators and their spectra are those that a position-space treatment of the hydrogen atom requires.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_\mu \vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda$ $(\mu\neq \nu)$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace, Lie algebra of the $*$-unitary group |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace, observables and states |
| $\mathbb{B}_{H}$ | Real quaternion subspace, home of the rotation rotors |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i\vec e_k)=\sigma_k$ | Isomorphism with $M_2(\mathbb{C})$ |
| $L_{\mathrm{orb},k}=-\frac{m\,c\,i\,\epsilon_{klm}\,x_{l}}{k_m}\partial/\partial x_m$ | Orbital angular momentum operator |
| $L_{\mathrm{orb},k} e_t$ | Biquaternion representative of $L_{\mathrm{orb},k}$ (Hermitian) |
| $\tilde{S}_{\Psi,k}=\frac{m\,c}{2\,k_m}i\vec e_k$ | Spin operators in $\mathbb{B}_{\Psi}$, $\mathsf{M}_2(\tilde S_{\Psi,k})=\frac{m\,c}{2\,k_m}\sigma_k$ |
| $\tilde S_{\Psi,\mathrm{tot},k}=L_{\mathrm{orb},k}+\tilde{S}_{\Psi,k}$ | Total angular momentum |
| $\tilde S_{\Psi,\mathrm{tot},\pm}=\tilde S_{\Psi,\mathrm{tot},1}\pm i\tilde S_{\Psi,\mathrm{tot},2}$ | Ladder operators |
| $\tilde S_{\Psi,\mathrm{tot}}^2=\sum_k\tilde S_{\Psi,\mathrm{tot},k}^2$ | Casimir operator, eigenvalue $\frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}$ |
| $[\tilde S_{\Psi,\mathrm{tot},i},\tilde S_{\Psi,\mathrm{tot},j}]=\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}$ | Angular-momentum algebra |
| $\tilde u(\theta,\vec u)=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\sum_k \vec u_k\vec e_k$ | Rotation rotor (unit real quaternion) |
| $\tilde\Pi(\pm\vec u)=\tfrac{1}{2}(e_t\pm i\vec u)$ | Spin eigenstates (idempotents) |
| $s_{\mathrm{tot}},s_{\mathrm{tot},z}$; $l,l_z$; $s,s_z$ | Total, orbital, and spin quantum numbers |
| $\langle l,l_z;\tfrac12,s_z|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$ | Clebsch–Gordan coefficients (Condon–Shortley phase) |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the operator formulation of angular momentum and spin.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard treatment of angular momentum, spin, and the addition of angular momenta.
- Albert Messiah, *Quantum Mechanics* (Dover, 1999), for the representation theory of the angular-momentum algebra.
- M. E. Rose, *Elementary Theory of Angular Momentum* (Wiley, 1957), for the Clebsch–Gordan coefficients and their phase conventions.
- A. R. Edmonds, *Angular Momentum in Quantum Mechanics* (Princeton, 1957), for the coupling of angular momenta and the $3j$ formalism.
- L. C. Biedenharn and J. D. Louck, *Angular Momentum in Quantum Physics* (Addison-Wesley, 1981), for the algebraic and group-theoretic foundations.
- R. N. Zare, *Angular Momentum* (Wiley, 1988), for the coupling of orbital and spin angular momenta in atomic physics.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the realisation of $SU(2)$ and $SO(3)$ in quaternion and Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of rotations and angular momentum.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra treatment of spin and rotations.
