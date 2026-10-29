# __Biquaternion Rotations and Lorentz Transformations__

## Introduction

The biquaternion norm fixes what a motion is: the isometries of the form are the transformations that preserve $\langle\cdot,\cdot\rangle_{\natural}$, and they are the rotations, the Lorentz transformations and the reflections. This article reads those motions, the double covers that carry them, and the dagger sandwich as the action of the units on the algebra. The operator theory of the sandwich is *The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion*; its action on the six remarkable subspaces, including the elements whose sandwich preserves all of them, is *The Polar Decomposition and Remarkable Subspaces*; and the one-sided reading is *The One-Sided Operators of a N-Regular, Spectrally Regular Biquaternion*. The article then reads the representations of the same groups: the group of units, the finite-dimensional representations of the Lorentz group, the Weyl and Dirac spinors, the Clebsch–Gordan rule and the principal series. Nothing of the cited articles is reproved here.

The article is the Geometry slot of the Lie-theoretic block, extended with the representation theory of the groups it describes: the algebra is *Symmetric and Antisymmetric Decomposition of the Four General Products*, the group and its exponential are *Biquaternion Lie Group and Exponential Structure*, and the topology of the group is *The Biquaternion Unit Group as a Topological Group*. The reflections and the Cartan–Dieudonné theorem are stated generally in *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and their biquaternion case is worked here; the Clifford reading of the algebra is *Biquaternion Versors and the Orthogonal Group*; the transformation group in full is in *Biquaternion Automorphisms and Derivations*; and the finite groups of units, together with the figures they determine, are *Quaternion Orders and Finite Groups of Units*.

## The Double Covers and the Lorentz Group

The unit quaternions are the unit sphere $Sp(1)$, and they carry the motions of the definite form, with the double cover $SU(2)\to SO(3)$; their complexification $\mathbb{B}^\times_1\cong SL(2,\mathbb{C})$ carries the motions of the indefinite one. The centre $\{\pm e_t\}$ of $\mathbb{B}^\times_1$ is discrete, so the quotient is a Lie group, and

$$
\mathbb{B}^\times_1/\{\pm e_t\} \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $\mathbb{B}^\times_1$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
\boxed{\;\mathbb{B}^\times_1 \cong \mathrm{Spin}(1,3), \qquad \mathrm{B}_0 \cong \mathrm{so}(1,3)\;}.
$$

The parameter count explains why the complexification is needed and what it costs. A Lorentz transformation has six real parameters, three of rotation and three of boost, and the quaternion algebra $\mathbb{H}_{\mathbb{B}}$ has real dimension four; there is no smooth embedding of $SO^+(1,3)$ into $\mathbb{H}_{\mathbb{B}}$, since the differential at any point would inject a six-dimensional tangent space into a four-dimensional one. The group manifold is the object that does not fit, while the action does: $SO^+(1,3)$ acts on the four-dimensional $\mathbb{M}_+$ without being contained in it. The quaternions contain the three-dimensional $S^3$, the double cover of the rotations, and even there the rotation group is the quotient $S^3/\{\pm e_t\}$ rather than a subset.

Complexifying doubles the ambient dimension to eight and turns the norm from a real into a complex function. Over $\mathbb{R}$ the condition $N=1$ is one real equation in four real dimensions and leaves three; over $\mathbb{C}$ it is two real equations in eight and leaves six. The complexification adds four real dimensions, the condition removes one more real dimension than before, and the net gain is three. At the identity the tangent space of the level set is the trace-free part $\mathrm{B}_0$, spanned over $\mathbb{R}$ by $\vec e_x,\vec e_y,\vec e_z$ and $i\vec e_x,i\vec e_y,i\vec e_z$; the first three are the rotations and the last three the boosts. The algebra therefore contains the double cover $\mathbb{B}^\times_1\cong SL(2,\mathbb{C})$, while the Lorentz group itself is the quotient $\mathbb{B}^\times_1/\{\pm e_t\}$ and is not a submanifold of the algebra.

The group itself, not only its double cover, sits in the projective space. The classes of the units form the complement of the null quadric in $\mathbb{P}(\mathbb{B})\cong\mathbb{P}^3$, and that complement is $PGL(2,\mathbb{C})=PSL(2,\mathbb{C})\cong SO^+(1,3)$.

The Lorentz action is rotor conjugation, $\tilde{Q} \mapsto \tilde{U}\tilde{Q}\tilde{U}^{*}$ for $\tilde{U} \in \mathbb{B}^\times_1$, which preserves $\mathbb{M}_-$ and $\langle\tilde{Q}\rangle_{\natural}$; its compact part is the rotation family and its non-compact part the hyperbolic rotations, with closed forms in *Biquaternion Elementary Functions*, §*The Exponential in the Two Real Directions*.

## The Rotor and the Sandwich Action

A rotation is performed by conjugation, and the conjugating element is read as a **rotor**. A unit quaternion $\tilde u$, an element of the unit sphere $Sp(1)$ of the quaternion layer, acts on a biquaternion by the sandwich
$$
\tilde{Q}\mapsto \tilde u\,\tilde{Q}\,\tilde u^{-1},
$$
and on the imaginary part this is the rotation of $\mathbb{R}^3$ through the angle $\theta$ when $\tilde u=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\vec u$. Two features are visible in the formula. The angle appears **halved** in the rotor, since the rotation is applied once for the left factor and once for the right, and a full turn of the rotor, $\tilde u\mapsto-\tilde u$, is the identity rotation: the map $Sp(1)\to SO(3)$ is two-to-one, which is the double cover $SU(2)\to SO(3)$ of the double covers above. The unit quaternions carry the rotations of the definite form, and their complexification carries the motions of the indefinite one; the construction, with the versor and the sandwich action, is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* of Part II.

## The Dagger Sandwich

The rotor of the previous section conjugates by a real quaternion, $\tilde Q\mapsto\tilde u\tilde Q\tilde u^{-1}$, with $\tilde u^{-1}=\tilde u^{\natural}$ on the unit sphere. The Lorentz action on the whole algebra uses the Hermitian adjoint instead, $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$, and admits any unit $\tilde U$. The two operators agree only on the $*$-unitary slice, where $\tilde U^{*}=\tilde U^{-1}$:

$$
\mathrm{H}_{\tilde{Q}}:\ \mathbb{B}\longrightarrow\mathbb{B},\qquad \mathrm{H}_{\tilde{Q}}(\tilde Q_3)=\tilde{Q}\,\tilde Q_3\,\tilde{Q}^{*},
$$

the **dagger sandwich**. Its carrier is the algebra as a real vector space of dimension eight, with basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$, and its group is the group of units. It is a linear action of that group on the algebra, and a central factor acts by its squared modulus, so a central phase does not change the operator; the two laws and their proofs are *The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion*, §*The Sandwich of the Word*.

**Why the dagger.** The involution ${}^{*}$ splits the algebra into the Hermitian sector $\mathbb{M}_+$ and the anti-Hermitian sector $\mathbb{M}_-$. Among the two-sided maps $\tilde Q_3\mapsto A\tilde Q_3B$ with $A,B$ invertible, those that carry the fixed space of ${}^{*}$ into itself are exactly those with $B=\lambda A^{*}$ for a real $\lambda$, and the dagger sandwich is the normalised case $\lambda=1$. A sandwich built from the inverse instead carries $\mathbb{M}_+$ into a different fixed space: the automorphism $\tilde Q_3\mapsto\tilde{Q}\tilde Q_3\tilde{Q}^{-1}$ preserves the fixed spaces of the involution ${}^{*}$ conjugated by the image of the identity, $A\mapsto\tilde{Q}\tilde{Q}^{*}\bar{A}(\tilde{Q}\tilde{Q}^{*})^{-1}$, which is a different involution as soon as $\tilde{Q}$ is not $*$-unitary. Since the halves and the sectors are the fixed spaces of the involutions, the subspaces a sandwich preserves are the ones its own involution defines.

The sandwich preserves both Hermitian sectors, scales the biquaternion norm by $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$ and is an isometry on the unit-norm slice. The proofs, the factor-by-factor reading, the kernel $\mathrm{U}(1)$, the image $CO^{+}(1,3)$, the boost matrices and the infinitesimal form are *The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion* and *The Polar Decomposition and Remarkable Subspaces*.

## Orbits and the Invariants

The sandwich preserves the rank of the matrix image $\mathsf{M}_2(\tilde Q_3)$ (*$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*) and scales the biquaternion norm by $\lvert \langle\tilde{Q}\rangle_{\natural}\rvert^{2}$, the scaling being one on the unit-norm slice. The rank is unchanged because a congruence by an invertible matrix does not change it, and the biquaternion norm is the determinant. The two invariants cut the algebra as follows.

| invariant | value | meaning |
|---|---|---|
| $\operatorname{rank}\mathsf{M}_2(\tilde Q_3)=2$ | $\langle\tilde Q_3\rangle_{\natural}\neq0$ | $\tilde Q_3$ is $\natural$-regular, hence a unit |
| $\operatorname{rank}\mathsf{M}_2(\tilde Q_3)=1$ | $\langle\tilde Q_3\rangle_{\natural}=0$, $\tilde Q_3\neq0$ | $\tilde Q_3$ is $\natural$-degenerate, a zero divisor of rank one |
| $\operatorname{rank}\mathsf{M}_2(\tilde Q_3)=0$ | $\tilde Q_3=0$ | the origin, $\natural$-degenerate |

Off the unit-norm slice every orbit is rescaled by the same positive factor, so it is enough to classify the orbits on the slice. There the two sectors carry the classification the four-vector calculus uses: on $\mathbb{M}_+$ the Hermitian forms are classified by their signature, and on $\mathbb{M}_-$ the four-vectors split into the timelike, the null and the spacelike classes, with the proper orthochronous component, so that the two time directions are not mixed. The non-zero $\natural$-degenerate elements are the null cone, and on the slice they form a single orbit, which is the sense in which the null cone is one geometric object rather than a union of the cones of individual four-vectors.

The infinitesimal form contains the two symmetries of the algebra in one expression: along the anti-Hermitian directions the operator is the commutator, the infinitesimal rotation, and along the Hermitian ones the anticommutator, the infinitesimal boost. The formula and the split into the two summands of the Cartan decomposition are *The Polar Decomposition and Remarkable Subspaces*, §*The Infinitesimal Split*; the adjoint maps are in *Symmetric and Antisymmetric Decomposition of the Four General Products* and the exponential in *Biquaternion Lie Group and Exponential Structure*.

## Reflections

The sandwich also realises the **reflections**, on the subspaces where the multiplication is Clifford. Let $v\in\mathbb{B}$ with $\langle v\rangle_{\natural}=1$; the reflection in the hyperplane $v^{\perp}$ is the linear map
$$
\rho_v(\tilde Q_3)=-v\,\tilde Q_3\,v^{\natural},
$$
the right factor being the quaternion conjugate. On the norm-one slice $v\,v^{\natural}=\langle v\rangle_{\natural}=e_t$, so $v^{\natural}$ is the inverse there, and the formula needs no operator inverse.

On the vector subspace the conjugate is minus the element, $v^{\natural}=-v$, so the same map is
$$
\rho_v(\tilde Q_3)=v\,\tilde Q_3\,v,
$$
the minus sign carried by $v^{2}=-e_t$. On the real form, where $v^{*}=v$, this is the dagger sandwich $\rho_v(\tilde Q_3)=v\,\tilde Q_3\,v^{*}=\mathrm{H}_v(\tilde Q_3)$.

**Theorem.** For $v$ with $\langle v\rangle_{\natural}=1$ the map $\rho_v$ preserves the biquaternion norm and its polar form, satisfies $\rho_v(v)=-v$, and fixes pointwise every element that anticommutes with $v$; its square is the conjugation $\rho_v^2(\tilde Q_3)=v^2\tilde Q_3(v^2)^{\natural}$.

**Proof.** The map is linear and invertible, with inverse $\rho_{v^{\natural}}$, but it is not an algebra automorphism: on a product it gives $\rho_v(\tilde Q\tilde R)=-\rho_v(\tilde Q)\rho_v(\tilde R)$. The norm is multiplicative, so $\langle\rho_v(\tilde Q_3)\rangle_{\natural}=\langle v\rangle_{\natural}\langle\tilde Q_3\rangle_{\natural}\langle v^{\natural}\rangle_{\natural}=\langle\tilde Q_3\rangle_{\natural}$, whence the polar form is preserved too; the statement $\rho_v(v)=-v\,v\,v^{\natural}=-v$ is immediate. If $\tilde Q_3$ anticommutes with $v$, then $-v\tilde Q_3v^{\natural}=\tilde Q_3v\,v^{\natural}=\tilde Q_3$, so $\tilde Q_3$ is fixed. The square is $\rho_v(\rho_v(\tilde Q_3))=v(v\tilde Q_3v^{\natural})v^{\natural}=v^2\tilde Q_3(v^2)^{\natural}$, a conjugation by $v^2$, and it is the identity exactly when $v^2$ is a scalar.

**Remark (which subspaces carry the reflections).** For the formula to be a genuine reflection, orthogonality and anticommutation must coincide on the ambient subspace. This happens when the multiplication is Clifford there: on the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\}$ and its real form $\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ one has
$$
v\tilde Q_3+\tilde Q_3v=-2\langle v,\tilde Q_3\rangle\,e_t,
$$
so the hyperplane $v^{\perp}$ is exactly the set of elements anticommuting with $v$, and $\rho_v$ fixes $v^{\perp}$ pointwise, negates $v$, and has complex-linear determinant $-1$. Here $v^2=-\bigl(\sum_k v_k^2\bigr)e_t$ is a scalar, so $\rho_v$ is an involution. On the quaternion and Hermitian subspaces the elements do not anticommute, and a norm-one element acts there by conjugation as a rotation rather than as a reflection. On the algebra as a whole, likewise, $\rho_v$ has determinant $+1$ for every $v$ with $\langle v\rangle_{\natural}=1$, so the maps attached to the finite groups of units are rotations and not reflections; and on $\mathbb{H}_{\mathbb{B}}$ the norm-one element $e_t$ is central, so $\rho_{e_t}=-\mathrm{id}$ and nothing is fixed.

**Theorem (Cartan–Dieudonné in the biquaternion algebra).** On the complex three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$ and on its real form $\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, every isometry is a product of at most three reflections $\rho_v$ with $\langle v\rangle_{\natural}=1$.

**Proof.** On these subspaces $\langle v\rangle_{\natural}=v_1^2+v_2^2+v_3^2$ is a non-degenerate form, and by the theorem above the maps $\rho_v$ with $\langle v\rangle_{\natural}=1$ are its reflections in the hyperplanes $v^{\perp}$; the Cartan–Dieudonné theorem, stated for a general vector space in *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, then gives generation by at most $\dim W=3$ reflections.

**Remark.** The reflections of this section are attached to the odd part $\mathrm{Vect}(\mathbb{B})$; the Lorentz reflections are not of the shape $\rho_v$ and live in the Clifford layer, not in $\mathbb{B}$.

## Rotations, Boosts and the Two-Sided Action

Over the reals the trace-free subalgebra splits into the compact rotation directions $\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and the hyperbolic directions $\mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ (*Symmetric and Antisymmetric Decomposition of the Four General Products*). A **rotation** is the motion generated by the first, an element of the compact group $Sp(1)$ of the rotation family; a **boost**, or hyperbolic rotation, is the motion generated by the second, an isometry of the indefinite form that fixes a timelike direction and leaves the null cone invariant. Both are boosts or rotations of the form the algebra carries, and together they generate the Lorentz group $SO^+(1,3)$ of the double covers above; the rotations are the isometries of the definite form, the boosts those of the indefinite one, and the closed forms of their exponentials are in *Biquaternion Elementary Functions*.

A **two-sided** action, $\tilde{Q}\mapsto \tilde u_1\,\tilde{Q}\,\tilde u_2$ with $\tilde u_1,\tilde u_2\in Sp(1)$ independent, is a four-dimensional rotation: the pair $(\tilde u_1,\tilde u_2)$ acts on $\mathbb{B}\cong\mathbb{R}^8$ preserving the Euclidean form, with kernel $\{\pm(e_t,e_t)\}$, so the two-sided action realises
$$
(Sp(1)\times Sp(1))/\{\pm e_t\}\cong SO(4)
$$
on the algebra. The one-sided action is its diagonal restriction, and the Lorentzian motions are obtained from the complexification instead.

## The Group of Units

The group of units is the $\natural$-regular set, $\mathbb{B}^{\times} = \{\tilde{Q} : \langle\tilde{Q}\rangle_{\natural} \neq 0\}$, which under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ is the group of invertible matrices, since the biquaternion norm is the determinant (*$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*):

$$
\mathbb{B}^{\times} \cong GL_2(\mathbb{C}),
$$

a connected non-compact complex Lie group of complex dimension $4$ and real dimension $8$, with centre $\mathbb{C}^{\times}$. The unit-norm subgroup is $\mathbb{B}^{\times}_1 \cong SL(2,\mathbb{C})$, of complex dimension $3$ and real dimension $6$, the double cover of the proper orthochronous Lorentz group (§*The Double Covers and the Lorentz Group* of this article). The $*$-unitary biquaternions $\tilde{Q}^{*}\tilde{Q} = e_t$ form $\mathrm{U}(2)$, the maximal compact subgroup of $\mathbb{B}^{\times}$ (*The Unitary Group of the Biquaternion Algebra*), and the unit quaternions form $SU(2) = \mathbb{B}^{\times}_1 \cap \mathrm{U}(2)$, the maximal compact subgroup of $SL(2,\mathbb{C})$ and the double cover of $SO(3)$.

## Representations of the Group of Units

As a reductive group, $GL_2(\mathbb{C})$ has finite-dimensional algebraic (rational) representations parameterised by highest weights $(\lambda_1, \lambda_2) \in \mathbb{Z}^2$ with $\lambda_1 \geq \lambda_2$; the irreducible one is $\operatorname{Sym}^{\lambda_1 - \lambda_2}(\mathbb{C}^2) \otimes (\det)^{\lambda_2}$, of dimension $\lambda_1 - \lambda_2 + 1$, with central character $A \mapsto A^{\lambda_1 + \lambda_2}$. Restriction to $SL(2,\mathbb{C})$ forgets the determinant twist, leaving the highest weight $2j = \lambda_1 - \lambda_2 \geq 0$, that is, the irreducible $V_j$ below with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$.

## Finite-Dimensional Representations of the Lorentz Group

Let $G = SL(2,\mathbb{C})$, with real Lie algebra the traceless $2\times2$ complex matrices (*Symmetric and Antisymmetric Decomposition of the Four General Products*). Its complexification is a sum of two copies of the special linear algebra, the complexified Lorentz algebra:

$$
\mathrm{so}(1,3)\otimes_{\mathbb{R}}\mathbb{C} \cong \mathrm{sl}(2,\mathbb{C}) \oplus \mathrm{sl}(2,\mathbb{C}),
$$

the two summands corresponding to the self-dual and anti-self-dual parts. Every finite-dimensional smooth complex representation of $G$ is completely reducible, and its irreducible summands are the outer tensor products $(m,n) = V_m \boxtimes V_n$ with $m, n \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, where $V_j$ denotes the irreducible $\mathrm{SU}(2)$-module of dimension $2j+1$, equivalently the $\mathrm{SL}(2,\mathbb{C})$-module $\operatorname{Sym}^{2j}(\mathbb{C}^2)$ of highest weight $2j$; thus $\dim_{\mathbb{C}}(m,n) = (2m+1)(2n+1)$. The defining representation is $(\tfrac{1}{2}, 0)$ and its complex conjugate is $(0, \tfrac{1}{2})$.

**Polynomial representations.** Relative to a Cartan subalgebra spanned by $h = \operatorname{diag}(1,-1)$, the irreducible $SL(2,\mathbb{C})$-modules are the symmetric powers $V_j \cong \operatorname{Sym}^{2j}(\mathbb{C}^2)$, with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, highest weight $2j$ and dimension $2j+1$. These are exactly the **polynomial** (equivalently holomorphic, equivalently algebraic) finite-dimensional representations of the complex group $G$: their matrix entries are polynomial functions of the entries of $g \in G$, and every finite-dimensional holomorphic representation of $G$ is a direct sum of the $V_j$, hence is parameterised by its highest weight $2j$, that is, by its spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. Not every continuous finite-dimensional representation is polynomial: the complex conjugates of the $V_j$ are antiholomorphic and belong to the $(0, j)$ family.

**The $*$-unitary trick.** Restriction to the maximal compact subgroup $SU(2)$ is an equivalence of categories

$$
\left\{\text{f.d. polynomial representations of } SL(2,\mathbb{C})\right\} \simeq \left\{\text{f.d. }{}^{*}\text{-unitary representations of } SU(2)\right\},
$$

so the finite-dimensional polynomial representations of $SL(2,\mathbb{C})$ are obtained from those of $SU(2)$ by complexifying the Lie algebra and exponentiating, and both are parameterised by the same highest weights $2j$, $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. What complexification does not preserve is unitarity, a point taken up in §*$*$-Unitary Representations*.

## The Defining Representation and the Weyl Spinors

The defining representation of $SL(2,\mathbb{C})$ is $V_{1/2} = \mathbb{C}^2$, the polynomial representation of highest weight $1$. It is the same space that appears in *The Category of Modules* as the unique simple module of the algebra $\mathbb{B}$, and the isomorphism $\mathbb{B} \cong \operatorname{End}_{\mathbb{C}}(V_{1/2})$ is the content of the matrix realization (*$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*): choosing a basis of $V_{1/2}$ writes each element of the algebra as a $2 \times 2$ matrix, and the choice of basis is the only freedom in doing so. Under the Lorentz group the defining representation and its conjugate are the two **Weyl spinors**: $V_{1/2} = (\tfrac{1}{2}, 0)$ is the left-handed one and $\overline{V_{1/2}} = (0, \tfrac{1}{2})$ is the right-handed one; they are not isomorphic as complex representations, and parity exchanges them. In the algebra each is a Peirce column on which the one-sided operator acts, the realization in *The One-Sided Operators of a N-Regular, Spectrally Regular Biquaternion*, §*The Eigenbasis and the Two Spinor Spaces*. Their direct sum is the **Dirac spinor**

$$
\Delta = V_{1/2} \oplus \overline{V_{1/2}} = (\tfrac{1}{2},0) \oplus (0,\tfrac{1}{2}), \qquad \dim_{\mathbb{C}} \Delta = 4,
$$

and their tensor product is the **vector representation** $(\tfrac{1}{2}, \tfrac{1}{2}) = V_{1/2} \otimes \overline{V_{1/2}}$, of complex dimension $4$, whose real form is the Lorentz action on the four-dimensional vector space. The adjoint representation of the Lorentz algebra is $(1,0) \oplus (0,1)$, of dimension $3 + 3$.

Two dualities must be distinguished. The defining module is **self-dual** as a representation of $SL(2,\mathbb{C})$: since $\det = 1$, the alternating form $\varepsilon(u,v) = u_x v_2 - u_y v_1$ is invariant and identifies $V_{1/2}^{*}$ with $V_{1/2}$, so $V_{1/2}^{*} \cong V_{1/2}$. The **conjugate** $\overline{V_{1/2}}$, by contrast, is not isomorphic to $V_{1/2}$; it is the other chirality. Finally, since $-e_t$ acts as $-1$ on $V_{1/2}$, the defining representation, and every $(m,n)$ with $m+n$ half-integral, does not descend to $SO^+(1,3)$. This is the representation-theoretic form of the statement that the Lorentz group itself has no two-dimensional spin representation: the spin representation is a representation of its double cover. The Clifford module that carries the same two spinors is *Spin Representations and Clifford Modules with Inner Conjugation*.

**Remark (the conformal group is not a group of multiplications).** The algebra has complex dimension four, so its underlying vector space is also the twistor module $\mathbb{C}^4$, on which the conformal group $SU(2,2)\cong\mathrm{Spin}(4,2)$ acts. On the Lorentz subgroup the twistor is the Dirac spinor $\Delta$ above. No multiplication of the algebra restricts to $\Delta$: left multiplication and right multiplication give two copies of $(\tfrac12,0)$, and the sandwich gives $(\tfrac12,\tfrac12)$. The conformal action is therefore not a multiplication, and $SU(2,2)$ is not a subgroup of $\mathbb{B}^{\times}$: its translations and special conformal transformations are the off-diagonal blocks that mix the two chiralities.

## Tensor Products and the Clebsch–Gordan Rule

Group representations tensor with the diagonal action $g \cdot (v \otimes w) = (gv) \otimes (gw)$. For the polynomial representations of $SL(2,\mathbb{C})$ the Clebsch–Gordan rule is

$$ V_j \otimes V_k \cong \bigoplus_{l=|j-k|}^{j+k} V_l, \qquad j, k \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}. $$

The tensor square of the spinor is the simplest nontrivial case:

$$
V_{1/2} \otimes V_{1/2} \cong \operatorname{Sym}^2 V_{1/2} \oplus \Lambda^2 V_{1/2} \cong V_1 \oplus V_0, \qquad \dim_{\mathbb{C}} V_1 = 3, \quad \dim_{\mathbb{C}} V_0 = 1.
$$

The summand $V_1$ is the symmetric square and is the adjoint representation of the special linear algebra, that is, the complexification of the adjoint representation of the compact algebra $\mathrm{su}(2) \cong \mathrm{so}(3)$; the summand $V_0 = \Lambda^2 V_{1/2} \cong \mathbb{C}$ is the **scalar**, spanned by the invariant alternating form $\varepsilon$. Thus the tensor square of the spinor splits as the complexified adjoint representation plus a scalar. This is the three-dimensional rotation algebra; the adjoint representation of the six-dimensional Lorentz algebra is instead $(1,0) \oplus (0,1)$.

For the two-parameter family the rule applies to each factor:

$$
\boxed{\;(m,n) \otimes (m',n') \cong \bigoplus_{k=0}^{\min(m,m')} \bigoplus_{k'=0}^{\min(n,n')} (m+m'-2k,\ n+n'-2k')\;}.
$$

For example, $(\tfrac{1}{2},\tfrac{1}{2}) \otimes (\tfrac{1}{2},\tfrac{1}{2}) \cong (0,0) \oplus (1,0) \oplus (0,1) \oplus (1,1)$, of dimension $1 + 3 + 3 + 9 = 16 = 4 \times 4$.

**Tensor powers of the defining representation.** Iterating the rule gives the complete decomposition of the $N$-fold tensor power of the spinor,

$$
V_{1/2}^{\otimes N} \cong \bigoplus_{k=0}^{\lfloor N/2 \rfloor} \left[ \binom{N}{k} - \binom{N}{k-1} \right] V_{N/2-k}, \qquad \binom{N}{-1} = 0,
$$

the multiplicity of $V_{N/2-k}$ being the ballot (Catalan-triangle) number $\binom{N}{k} - \binom{N}{k-1}$. For example $V_{1/2}^{\otimes 2} \cong V_1 \oplus V_0$ and $V_{1/2}^{\otimes 3} \cong V_{3/2} \oplus 2V_{1/2}$. Since every finite-dimensional polynomial representation is completely reducible, the composition factors of a tensor power are exactly its direct summands, with these multiplicities.

## $*$-Unitary Representations

A representation $\rho$ on $W$ is **$*$-unitary** if $W$ carries an invariant positive-definite Hermitian form $\langle \cdot, \cdot \rangle$. On $V_{1/2} = \mathbb{C}^2$ the standard form $\langle u,v \rangle = u_x^{*}v_1 + u_y^{*}v_2$ is invariant under $SU(2)$, so $V_{1/2}$ is $*$-unitary for the compact form $SU(2)$. It is **not** $*$-unitary for $SL(2,\mathbb{C})$: the non-compact one-parameter subgroups of hyperbolic rotations do not preserve it. More generally a non-compact simple Lie group has no nontrivial finite-dimensional $*$-unitary representation, since the image would lie in a compact group; hence only the trivial representation is finite-dimensional and $*$-unitary for $SL(2,\mathbb{C})$, and the defining representation is not unitarisable for the complex group. Unitarity of the compact form $SU(2)$, not of $SL(2,\mathbb{C})$, is what complexification preserves.

**The principal series.** The infinite-dimensional $*$-unitary representations are built by induction (*Induced Representations of Locally Compact Groups*). Let $P$ be the Borel subgroup of upper triangular matrices, with $P = MAN$,

$$
M = \{\operatorname{diag}(u,u^{-1}) : |u| = 1\} \cong \mathrm{U}(1), \qquad A = \{\operatorname{diag}(\exp(t/2), \exp(-t/2)) : t \in \mathbb{R}\},
$$

and $N$ the upper unitriangular matrices. For $m \in \mathbb{Z}$ and $\nu \in \mathbb{R}$ define a character of $P$ by $\chi_{m,\nu}(man) = u^{m} \exp((i\nu+\tfrac12)t)$; the factor $\exp(t/2)$ is the square root of the modulus of $P$, and the **principal series** representation is the unitarily induced representation

$$
\pi_{m,\nu} = \operatorname{Ind}_{P}^{G}(\chi_{m,\nu}),
$$

realised on $L^2(G/P) = L^2(S^2)$ in the case $m = 0$, where $G/P \cong SU(2)/\mathrm{U}(1) \cong S^2$, and on the sections of the associated line bundle in general. Each $\pi_{m,\nu}$ is $*$-unitary by construction; it is irreducible for generic parameters, and for $\nu \in \mathbb{R}$ it is tempered. The parameter $m$ is discrete and $\nu$ is continuous. The principal series is not the whole $*$-unitary dual: there are also the **complementary series**, for which the continuous parameter is purely imaginary and bounded rather than real, and the trivial representation. The finite-dimensional polynomial representations are not $*$-unitary for $SL(2,\mathbb{C})$, except for the trivial representation $V_0$; only their restrictions to $SU(2)$ are $*$-unitary.

**The $*$-unitary dual is not the complexification of the compact one.** The $*$-unitary dual of the maximal compact subgroup $SU(2)$ is discrete, the family $\{V_j\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$. Passing to $SL(2,\mathbb{C})$ replaces the discrete highest-weight parameter by a continuous one; the $*$-unitary representations are the principal series, with parameter on the $*$-unitary axis, together with the complementary series and the trivial representation. The polynomial representations of $SU(2)$ complexify to representations of $SL(2,\mathbb{C})$ that are not $*$-unitary except for the trivial one, and the $*$-unitary dual of $SL(2,\mathbb{C})$ is continuous rather than the complexification of the discrete dual of $SU(2)$.

## Summary

The motions of the biquaternion algebra are the isometries of its biquaternion norm, and they are the rotations and the Lorentz transformations. The unit quaternions $Sp(1)$ carry the rotations of the definite form by the sandwich $\tilde{Q}\mapsto \tilde u\tilde{Q}\tilde u^{-1}$, in which the angle is halved and $\pm\tilde u$ gives the same rotation: the map $Sp(1)\to SO(3)$ is the double cover $SU(2)\to SO(3)$. Complexifying, the norm-one group $\mathbb{B}^\times_1$ carries the rotations of the indefinite form, and $\mathbb{B}^\times_1/\{\pm e_t\}\cong SO^+(1,3)$ with $\mathbb{B}^\times_1\cong Spin(1,3)$, so that the double cover of the proper orthochronous Lorentz group is realised inside the algebra; the group has six real parameters and the quaternions four, so the algebra contains the double cover and the group itself sits in the projective complement of the null quadric; the trace-free subalgebra splits into the compact rotation directions and the hyperbolic directions, and it is the boosts generated by the latter that are the isometries of the indefinite form.

The action that carries these motions on the whole algebra is the dagger sandwich $\mathrm{H}_{\tilde{Q}}(\tilde Q_3)=\tilde{Q}\tilde Q_3\tilde{Q}^{*}$. It is a linear action of the group of units whose kernel is the central circle $\mathrm{U}(1)$, reducing to $\{\pm e_t\}$ on the unit-norm slice, and whose image on the slice is $SO^+(1,3)$. Its operator theory, its factor-by-factor reading, the image $CO^{+}(1,3)$ on the full group of units, and the action on the six remarkable subspaces with the elements that preserve all of them, are *The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion* and *The Polar Decomposition and Remarkable Subspaces*; the one-sided reading, in which the one-sided operator is the spinor action, is *The One-Sided Operators of a N-Regular, Spectrally Regular Biquaternion*.

The two-sided action $\tilde{Q}\mapsto \tilde u_1\tilde{Q}\tilde u_2$ with independent unit quaternions preserves the Euclidean form and gives $(Sp(1)\times Sp(1))/\{\pm e_t\}\cong SO(4)$; the one-sided action is its diagonal restriction. The reflections are the maps $\rho_v(\tilde Q_3)=-v\tilde Q_3v^{\natural}=v\tilde Q_3v$ with $\langle v\rangle_{\natural}=1$, defined on the Clifford vector subspace $\mathrm{Vect}(\mathbb{B})$ and its real form, where orthogonality and anticommutation coincide; on that subspace every isometry is a product of at most three of them, by Cartan–Dieudonné. The construction is that of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* of Part II, and the full symmetry group of the algebra, wider than its isometries, is in *Biquaternion Automorphisms and Derivations*. The representation theory of these groups — the group of units, the finite-dimensional representations of the Lorentz group, the Weyl and Dirac spinors, the Clebsch–Gordan rule and the principal series — is §*The Group of Units* to §*$*$-Unitary Representations* of this article.

The group of units is $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$, of real dimension $8$, with unit-norm subgroup $SL(2,\mathbb{C})$, maximal compact subgroups $U(2)$ and $SU(2)$ respectively, and finite-dimensional algebraic representations of $GL_2(\mathbb{C})$ parameterised by the highest weights $(\lambda_1,\lambda_2)$. The finite-dimensional representations of the Lorentz group are the outer products $(m,n)=V_m\boxtimes V_n$ of dimension $(2m+1)(2n+1)$; the polynomial ones are the symmetric powers $V_j$, which the $*$-unitary trick recovers from $SU(2)$; and $V_{1/2}=\mathbb{C}^2$ is the defining representation and the unique simple module of $M_2(\mathbb{C})$. Its conjugate is the other Weyl spinor, their sum is the Dirac spinor, their tensor product is the four-vector representation $(\tfrac12,\tfrac12)$, and the adjoint representation of the Lorentz algebra is $(1,0)\oplus(0,1)$. Tensor products obey the Clebsch–Gordan rule, with the ballot numbers counting the composition factors of the tensor powers of the spinor. The only finite-dimensional $*$-unitary representation of $SL(2,\mathbb{C})$ is the trivial one; the infinite-dimensional $*$-unitary representations are the principal series, induced from characters of the Borel subgroup, together with the complementary series.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde{Q}\rangle_{\natural}$ | Biquaternion norm; the invariant of the motions |
| $Sp(1)$ | Unit quaternions; rotors of the definite form |
| $\tilde u\tilde{Q}\tilde u^{-1}$ | Sandwich action; rotor conjugation |
| $\rho_v(\tilde Q_3)=-v\tilde Q_3v^{\natural}=v\tilde Q_3v$ | Reflection in $v^{\perp}$ on $\mathrm{Vect}(\mathbb{B})$, $\langle v\rangle_{\natural}=1$ |
| $v\tilde Q_3+\tilde Q_3v=-2\langle v,\tilde Q_3\rangle e_t$ | Anticommutation as orthogonality on $\mathrm{Vect}(\mathbb{B})$; then $v^{\perp}=\{\tilde Q_3:\tilde Q_3v=-v\tilde Q_3\}$ |
| Cartan–Dieudonné | Every isometry of $\mathrm{Vect}(\mathbb{B})$ is at most three reflections $\rho_v$ |
| $Sp(1)\to SO(3)$ | Double cover $SU(2)\to SO(3)$; $\pm\tilde u$ give the same rotation |
| $\mathbb{B}^\times_1\cong Spin(1,3)$ | Norm-one group as the spin group; double cover of $SO^+(1,3)$ |
| $\mathbb{B}^\times_1/\{\pm e_t\}\cong SO^+(1,3)$ | Proper orthochronous Lorentz group |
| $\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | Rotation directions; compact |
| $\mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ | Hyperbolic (boost) directions |
| $\tilde u_1\tilde{Q}\tilde u_2$ | Two-sided action; preserves the Euclidean form |
| $(Sp(1)\times Sp(1))/\{\pm e_t\}\cong SO(4)$ | Two-sided action as four-dimensional rotations |
| $\mathrm{H}_{\tilde{Q}}(\tilde Q_3)=\tilde{Q}\tilde Q_3\tilde{Q}^{*}$ | The dagger sandwich; the action of a unit on the algebra |
| $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ | Group of units; real dimension $8$ |
| $\mathrm{U}(2)$ | $*$-Unitary biquaternions; maximal compact subgroup of $\mathbb{B}^{\times}$ |
| $(\lambda_1,\lambda_2)$ | Highest weight of an algebraic representation of $GL_2(\mathbb{C})$ |
| $\operatorname{Sym}^{\lambda_1-\lambda_2}(\mathbb{C}^2)\otimes(\det)^{\lambda_2}$ | The irreducible representation of $GL_2(\mathbb{C})$ of highest weight $(\lambda_1,\lambda_2)$ |
| $V_j$ | Irreducible representation of spin $j$, highest weight $2j$, dimension $2j+1$ |
| $(m,n)=V_m\boxtimes V_n$ | Finite-dimensional irreducible representation of the Lorentz group |
| $(\tfrac12,0)$, $(0,\tfrac12)$ | Left- and right-handed Weyl spinors |
| $(\tfrac12,\tfrac12)$ | Four-vector representation, $V_{1/2}\otimes\overline{V_{1/2}}$ |
| $V_{1/2}^{\otimes N}$ | Ballot-number decomposition of the tensor powers of the spinor |
| $\operatorname{Ind}_P^G(\chi_{m,\nu})$ | Principal series of $SL(2,\mathbb{C})$; $P=MAN$ the Borel subgroup |

## Further Reading

- [The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion](two-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the operator theory of the dagger sandwich: composition, factorisation through the polar word, spectra, kernel $U(1)$, image $CO^{+}(1,3)$ and the scaling of the norm.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the action on the six remarkable subspaces, the operators that preserve all of them, and the infinitesimal split.
- [The One-Sided Operators of a N-Regular, Spectrally Regular Biquaternion](one-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the one-sided reading and the half-spin.
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples* (Princeton University Press, 1986).
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed., 2015).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
